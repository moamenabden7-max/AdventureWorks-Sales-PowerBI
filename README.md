# AdventureWorks | Power BI Analytics

Sales, product performance, customer insights and price/quantity scenarios.

**Moamen Taha Abuzied** · Power BI · DAX · Power Query

[Revised project](powerbi/AdventureWorks.pbip) · [Original PBIX](powerbi/legacy/adventure.pbix) · [Model & DAX](docs/MODEL.md)

## Project files

| Folder | Contents |
| --- | --- |
| [powerbi/](powerbi/) | Revised Power BI project and the original report under legacy/ |
| [docs/](docs/) | Model reference, change notes and supporting tools |
| [assets/](assets/) | Supporting portfolio graphic |

## Open the revised report

1. Download the whole repository and extract it.
2. Open `powerbi/AdventureWorks.pbip` in Power BI Desktop.
3. Set **DataFolder** to the matching local data folder, apply changes and refresh.

The revised source queries expect matching compressed snapshots of the imported tables. Those snapshots were supplied privately to the owner and are not included on GitHub. Other users must supply compatible data or adapt the queries.

The original `powerbi/legacy/adventure.pbix` is retained for reference and does not include the project changes.

## Report pages

- **Sales Overview** — revenue, gross profit, orders, trends and geography.
- **Product Performance** — product drillthrough, targets and price/quantity scenarios.
- **Customer Insights** — customer sales and gross margin comparison.
- **Report Tooltip** — supporting tooltip.

## Changes and validation

The PBIP definitions include corrected division and scenario measures, customer relationship settings, target gauges and customer/margin visuals. [Change notes](docs/QUALITY_REVIEW.md).

Source definitions were checked structurally. **Opening, refreshing, executing DAX and reviewing the visuals in Power BI Desktop remain pending.**

Optional audit utilities and historical proposals are under [docs/maintenance/](docs/maintenance/). Run the original PBIX audit from the repository root:

```bash
python -m pip install -r docs/maintenance/requirements.txt
python docs/maintenance/tools/audit_model.py "powerbi/legacy/adventure.pbix" --output audit-results.json
```

[Maven Market](https://github.com/moamenabden7-max/Maven-Market-PowerBI) · [LinkedIn](https://www.linkedin.com/in/moamen-taha-data-analyst/)
