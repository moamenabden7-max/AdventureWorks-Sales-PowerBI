"""Read a PBIX locally and export aggregate evidence, never customer-level data.

Usage: python tools/audit_model.py "adventure.pbix" --output audit-results.json
Dependencies: pbixray, pandas. This script does not modify the PBIX or run DAX.
"""
import argparse
import hashlib
import json
from pathlib import Path

import pandas as pd
from pbixray import PBIXRay


def audit(path):
    m = PBIXRay(str(path))
    adventure = "sales" in m.tables
    fact, product, customer, returns, calendar = (
        ("sales", "Product Lookup", "Customer Lookup", "Returns Data", "Calendar Lookup")
        if adventure else ("Transection", "Products", "Customers", "Returns_1997-1998", "Calendar")
    )
    pk, ck, qty, price, cost, date, cd, rq, label = (
        ("ProductKey", "CustomerKey", "OrderQuantity", "ProductPrice", "ProductCost", "OrderDate", "Date", "ReturnQuantity", "ProductName")
        if adventure else ("product_id", "customer_id", "quantity", "Discount_Price", "product_cost", "transaction_date", "date", "quantity", "product_brand")
    )
    f, p, c, r, cal = [m.get_table(t) for t in (fact, product, customer, returns, calendar)]
    joined = f.merge(p[[pk, price, cost, label]], on=pk, how="left", validate="many_to_one", indicator=True)
    assert len(joined) == len(f), "Product join multiplied fact rows"
    assert joined['_merge'].eq('both').all(), "Product keys missing; totals would be incomplete"
    assert joined[[qty, price, cost]].notna().all().all(), "Missing quantity, price or cost"
    joined["revenue"] = joined[qty].astype(float) * joined[price].astype(float)
    joined["cost"] = joined[qty].astype(float) * joined[cost].astype(float)
    joined["month"] = pd.to_datetime(joined[date]).dt.strftime("%Y-%m")
    revenue = float(joined.revenue.sum())
    costs = float(joined.cost.sum())
    units, returned = float(f[qty].sum()), float(r[rq].sum())
    calendar_dates = pd.to_datetime(cal[cd]).dropna()
    expected_dates = pd.date_range(calendar_dates.min(), calendar_dates.max())
    result = {
        "source_sha256": hashlib.sha256(Path(path).read_bytes()).hexdigest(),
        "scope": "All imported fact rows; Python recomputation, not DAX engine output. No report filters applied.",
        "date_from": str(f[date].min().date()), "date_to": str(f[date].max().date()),
        "fact_rows": len(f), "quantity_sold": units, "quantity_returned": returned,
        "return_rows": len(r), "revenue": revenue, "cost": costs, "profit": revenue-costs,
        "profit_margin": (revenue-costs)/revenue if revenue else None,
        "unit_return_rate": returned/units if units else None,
        "distinct_orders": int(f.OrderNumber.nunique()) if adventure else None,
        "active_customer_keys": int(f[ck].nunique()),
        "customer_rows": len(c), "customer_null_keys": int(c[ck].isna().sum()),
        "customer_duplicate_nonnull_keys": int(c[ck].dropna().duplicated().sum()),
        "fact_rows_missing_customer_key": int((~f[ck].isin(c[ck].dropna())).sum()),
        "calendar_null_dates": int(cal[cd].isna().sum()),
        "calendar_duplicate_dates": int(cal[cd].duplicated().sum()),
        "calendar_missing_days": int(len(expected_dates.difference(calendar_dates))),
        "fact_rows_outside_calendar": int((~f[date].isin(cal[cd])).sum()),
        "monthly_revenue": {str(k):float(v) for k,v in joined.groupby('month').revenue.sum().items()},
        "top_revenue_groups": {str(k):float(v) for k,v in joined.groupby(label).revenue.sum().nlargest(5).items()},
    }
    assert abs(sum(result['monthly_revenue'].values())-revenue) < 0.01
    assert abs(result['profit']+costs-revenue) < 0.01
    m.close()
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pbix', type=Path)
    parser.add_argument('--output', type=Path, default=Path('audit-results.json'))
    args = parser.parse_args()
    args.output.write_text(json.dumps(audit(args.pbix), indent=2)+'\n', encoding='utf-8')
    print(f'Aggregate audit saved to {args.output}')
