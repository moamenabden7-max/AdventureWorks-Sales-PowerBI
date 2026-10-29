# Report implementation and verification

Status: outstanding work for the current `adventure.pbix`. Documentation changes do not apply fixes to the report.

## Prepare an editable copy

Open `adventure.pbix` in Power BI Desktop and save a working copy. Record baseline totals and active filters.

To edit the project outside Desktop, save as Power BI Project (.pbip), using the PBIR report format. Keep the .pbip entry point and its .Report and .SemanticModel folders together. When sharing the project, ZIP these three items with their folder structure intact.

## Apply fixes

1. Review [MODEL.md](MODEL.md) and [QUALITY_REVIEW.md](QUALITY_REVIEW.md).
2. Quarantine the six null customer-key records in Power Query, retaining rejected records for investigation. Check nonnull customer keys are unique and all sales customer keys still match. Then configure Customers (1) to Sales (*) with single-direction filtering.
3. Replace the existing measures one at a time using [measure-fixes.dax](../improvements/measure-fixes.dax). Confirm the quantity parameter used by the scenario slicer before replacing the undefined `qu` reference.
4. Remove customer-level return rate from the customer matrix: the returns fact has no customer key.
5. Set Target Orders as the orders gauge target marker and Orders Gauge Maximum as its maximum.
6. Replace the profit-margin-by-gender donut with a comparison bar chart, preserving its fields and filters.
7. Use consistent page labels, open on Sales Overview, and preserve navigation/tooltip references when ordering or hiding helper pages. The [theme](../improvements/portfolio-theme.json) is optional.

## Verify before replacing the download

- Open every page and check slicers, navigation, tooltips and empty selections.
- Check prior-month measures against explicit month selections.
- At zero price and quantity adjustments, adjusted values must equal baseline values and gaps must be zero.
- At a quantity adjustment of -100%, adjusted quantity, revenue and cost must be zero.
- Compare unfiltered aggregates with [audit-results.json](audit-results.json), allowing for numeric rounding. The audit is Python recomputation, not DAX validation.
- Test refresh with the original source files and configured local paths.
- Reopen the saved PBIX before replacing the repository download. Export real report screenshots to assets/ after verification.

Original source files are not included. The current summary graphic is not a Desktop export.
