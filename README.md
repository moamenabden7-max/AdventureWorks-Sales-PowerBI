# AdventureWorks Sales & Business Performance Analysis

**Power BI portfolio project · Sales & customer analytics**

[Download the Power BI report](./adventure.pbix) · [View Maven Market Retail Analysis](https://github.com/moamenabden7-max/Maven-Market-PowerBI)

An interactive Power BI report using the AdventureWorks dataset to explore revenue, profit, orders, returns, products, and customer segments.

## Business questions

- How do revenue, profit, orders, and returns change over time?
- Which product categories and individual products drive sales?
- How do customer segments and territories contribute to performance?
- How do adjusted price and quantity assumptions affect revenue, cost, and profit?

## Report pages

- **Overview:** revenue, profit, orders, and return rate cards; monthly trends and comparisons with the prior month; category and product breakdowns; year and continent filters.
- **Products:** target gauges for revenue and profit, return-rate trends, adjusted profit, and product selection.
- **Customers:** customer trends and segment breakdowns, including gender and country, plus a customer-level matrix.
- **Supporting pages:** a KPI collection, a scenario gap view, and a report tooltip.

## Model and measures

The report references calendar, product, category, customer, and territory lookup tables. DAX measures used in the visuals include total revenue, cost, profit, orders, returns, return rate, profit margin, quantities sold, prior-month values, and target or adjusted values. The scenario page compares original and adjusted revenue, cost, and profit.

## How to open

1. Open the [Power BI report file](./adventure.pbix) and select **Download raw file** on GitHub.
2. Open the downloaded `.pbix` file with **Power BI Desktop**.
3. Explore the report pages and their filters.

The report contains an embedded data model. Refreshing may require updated source settings and access to the original data files; those source files are not included in this repository.

## Tools

Power BI · DAX

## Repository contents

- `README.md` — project summary and report guide.
- `adventure.pbix` — Power BI report and embedded model.

## Validation scope

The existing project documentation records a check of report layout and field references. Numerical findings and data refresh have not been independently validated.

## Author

Moamen Taha Abuzied · [LinkedIn](https://www.linkedin.com/in/moamen-taha-data-analyst/)
