# Revised project changes

Applied to the PBIP definitions:

- Corrected sibling project/report/model paths.
- Replaced machine-specific sources with a DataFolder parameter and queries expecting matching private imported-table snapshots.
- Filtered null customer keys on refresh and configured single-direction customer-to-sales filtering through a one-to-many relationship.
- Corrected return-rate and margin division, prior-month profit dates, and the undefined quantity adjustment reference.
- Preserved referenced placeholder measures as BLANK().
- Connected a quantity selector to scenario measures.
- Corrected target and maximum roles on product gauges.
- Replaced the gender margin donut with bars and removed customer return rate from the customer matrix.
- Standardized page names, retained navigation identities, and replaced the oversized automatic narrative with a compact guide.

The source definitions have structural checks. Power Query evaluation, relationship processing, DAX execution, layout and interaction testing still require Power BI Desktop.

Private data snapshots and derived verification files are not included in this public update. Historical audit files describe the earlier input and are not validation of the current project.

Project files are grouped under powerbi/; supporting tools and historical proposals are under docs/maintenance/.
