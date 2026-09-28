# AdventureWorks Sales & Business Performance Analysis

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

Download `adventure.pbix` and open it with Power BI Desktop. The report contains an embedded data model; refreshing it may require access to the original data source or updated source settings.

## Tools

Power BI · SQL · DAX

## Repository contents

- `adventure.pbix` — Power BI report and embedded model.

Dashboard screenshots can be added once exported from Power BI Desktop.

The visual layout and field references were checked from the report file. Numerical findings and refresh behavior have not been independently verified here.

## Author

Moamen Taha Abuzied · [LinkedIn](https://www.linkedin.com/in/moamen-taha-data-analyst/)
