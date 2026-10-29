# Quality review

Status: findings verified from the current model and report metadata; proposed Desktop changes are not yet applied.

## Findings requiring Desktop changes

| Priority | Finding | Proposed action |
| --- | --- | --- |
| High | `Customer Lookup` contains 6 null customer keys; all nonnull keys are unique. The sales/customer relationship is active many-to-many with both-direction filtering. | Quarantine the 6 null-key records in Power Query, verify unmatched fact keys remain zero, then use Customers (1) → Sales (*) with single-direction filtering. Preserve rejected records for investigation. |
| High | `adjudst average quantity sold` contains `[Average Quantity Sold] * (1+qu)`. No model column/measure named `qu` was found. | Replace the undefined name with the quantity scenario measure, as proposed in the DAX fixes. |
| High | Returns are recorded by date, product and territory, with no customer key. | Do not present customer-level return rate as attributable to an individual customer. Remove it from the customer matrix or label it explicitly as a broader-context metric. |
| Medium | Return rate and profit margin use `/`. | Use `DIVIDE` to handle zero or blank denominators. |
| Medium | `LM Profit` uses the automatic Date hierarchy, unlike the other prior-month measures. | Use the explicit Calendar Lookup[Date] column, after confirming the date table configuration. |
| Medium | The orders gauge uses `Gap orders` as its maximum. | Bind Target Orders to the target marker; use a positive maximum based on actual and target values. |
| Medium | A donut chart encodes profit margin by gender. | Use clustered bars; margins are comparisons, not additive parts of a whole. |
| Medium | Saved report opens on Customers; page names are inconsistent. | Start on Sales Overview; order business pages before Scenario Analysis and helper pages. |
| Low | `Measure 2` and `Measure 3` have empty expressions; several names contain typos. | Check dependencies before removal. Rename in Desktop so dependencies update together. |

`Total Returns` counts **1,809 return rows**, whereas `Quatity Returns` sums **1,828 returned units**. Keep the two concepts separate; unit return rate uses returned units / sold units. Product price × quantity minus product cost is gross profit, not net profit.

## Checks performed

- PBIX archive and JSON report definitions could be read.
- Product joins preserved the fact-row count; every fact product key matched.
- No fact rows had an unmatched customer key.
- Calendar dates were unique, nonblank and continuous, and covered every fact date.
- Recomputed monthly revenue reconciled to the all-row revenue total within 0.01.

These checks do not execute DAX, render report visuals, refresh source files or validate every filter interaction.
