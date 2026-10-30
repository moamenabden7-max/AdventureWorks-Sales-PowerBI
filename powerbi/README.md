# Power BI report files

[← Project home](../README.md)

## Choose your version

| Version | File | What to expect |
| --- | --- | --- |
| **Original report** | **[Download PBIX](https://github.com/moamenabden7-max/AdventureWorks-Sales-PowerBI/raw/refs/heads/main/powerbi/legacy/adventure.pbix)** | One report file to open in Power BI Desktop. Does not include the revised source changes. |
| **Revised source** | [AdventureWorks.pbip](AdventureWorks.pbip) | Updated report/model definitions. Requires matching local data and Desktop validation. |

## Open the revised source

Download the **whole repository**, extract it, then open `powerbi/AdventureWorks.pbip`. Keep `AdventureWorks.Report` and `AdventureWorks.SemanticModel` next to it.

Set **DataFolder** to your matching local snapshots, apply changes and refresh. Data snapshots are not included on GitHub.

[Opening checklist](../docs/DESKTOP_FINISH.md) · [Model & DAX](../docs/MODEL.md) · [Change notes](../docs/QUALITY_REVIEW.md)

The `legacy/` folder preserves the original PBIX. Report and model folders are components of the revised project, not additional reports.
