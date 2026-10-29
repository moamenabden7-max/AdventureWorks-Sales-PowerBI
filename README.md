# AdventureWorks | Power BI Analytics

Sales, products, customers and scenario analysis by **Moamen Taha Abuzied**.

[Project](AdventureWorks.pbip) · [Model & DAX](docs/MODEL.md) · [Change notes](docs/QUALITY_REVIEW.md)

## Open the revised project

Download the whole repository and open `AdventureWorks.pbip` in Power BI Desktop. Keep its Report and SemanticModel folders together.

The revised queries expect a local folder of matching compressed imported-table snapshots. Those data files are supplied privately to the owner and are excluded from GitHub. Set the **DataFolder** parameter to that local folder, apply changes and refresh. Other users must provide compatible local snapshots or adapt the source queries.

## Report pages

- Sales Overview: sales measures, trends and geography.
- Product Performance: drillthrough, target gauges and price/quantity scenarios.
- Customer Insights: customer sales and gross margin comparison.
- Report Tooltip: supporting tooltip.

## Changes

The revised PBIP source corrects safe division, the quantity scenario reference, the prior-month profit date reference, customer relationship direction and cardinality, and gauge actual/target/maximum roles. The customer matrix excludes return rate, and gross margin by gender uses bars. An oversized automatic narrative was replaced with a short scenario guide.

The project definitions were checked structurally. **Desktop opening, refresh, DAX execution and visual verification remain pending.**

`adventure.pbix` is the unchanged legacy report and does not include these PBIP changes. Existing historical audit materials describe the original report.

[Maven Market](https://github.com/moamenabden7-max/Maven-Market-PowerBI) · [LinkedIn](https://www.linkedin.com/in/moamen-taha-data-analyst/)
