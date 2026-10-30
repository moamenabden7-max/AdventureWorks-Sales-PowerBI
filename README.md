<p align="center"><img src="assets/project-cover.svg" alt="AdventureWorks — Sales and Customer Analytics by Moamen Taha Abuzied" width="100%"></p>

<p align="center">
<strong><a href="https://github.com/moamenabden7-max/AdventureWorks-Sales-PowerBI/raw/refs/heads/main/powerbi/legacy/adventure.pbix">Download original report (.pbix)</a></strong>
&nbsp; · &nbsp;
<a href="powerbi/">Browse revised project</a>
&nbsp; · &nbsp;
<a href="docs/MODEL.md">Explore DAX &amp; model</a>
</p>

# AdventureWorks · Sales & Customer Analytics

A Power BI portfolio project exploring sales performance, product profitability and customer activity, with price and quantity scenarios.

## Start here

| What would you like to do? | Open this |
| --- | --- |
| **View the original report in Power BI Desktop** | **[Download original PBIX](https://github.com/moamenabden7-max/AdventureWorks-Sales-PowerBI/raw/refs/heads/main/powerbi/legacy/adventure.pbix)** — one file |
| **Review the revised report and model source** | **[Revised Power BI project](powerbi/)** — project files and opening guide |
| **Understand the calculations and relationships** | **[Model & DAX reference](docs/MODEL.md)** |

**Two versions, clearly separated:** the PBIX download is the original report. The revised PBIP contains the source changes and requires matching local data; Desktop validation is still pending.

## What the report explores

| View | Business questions |
| --- | --- |
| **Sales Overview** | How are revenue, gross profit and orders changing across time and locations? |
| **Product Performance** | Which products drive performance, how do they compare with targets, and how do price/quantity assumptions affect profit? |
| **Customer Insights** | How do customer sales, activity and gross margin compare? |

## Open the original report

1. **[Download the PBIX](https://github.com/moamenabden7-max/AdventureWorks-Sales-PowerBI/raw/refs/heads/main/powerbi/legacy/adventure.pbix)**.
2. Open it in **Power BI Desktop**.

Refreshing the original report may require its original source files and updated local paths. It does not include the revised project changes.

<details>
<summary><strong>Working with the revised source project?</strong></summary>

Download the whole repository with **Code → Download ZIP**, then extract it. Open `powerbi/AdventureWorks.pbip` and keep the adjacent `.Report` and `.SemanticModel` folders together.

Set **DataFolder** to the matching local data folder, then apply and refresh. The revised queries expect compressed snapshots of the imported tables. These data files are not included on GitHub; compatible data or adapted source queries are required.

The revised definitions include corrected division and scenario references, customer relationship settings, gauge bindings and customer/margin visuals. [See the change notes](docs/QUALITY_REVIEW.md). Source structure was checked; opening, refreshing, DAX execution and visual inspection in Desktop remain pending.

</details>

## Find your way around

| Location | Purpose |
| --- | --- |
| [powerbi/](powerbi/) | Report files and the guide to choosing a version |
| [docs/](docs/) | Model reference, change notes and verification guidance |
| [assets/](assets/) | Portfolio visuals |
| [docs/maintenance/](docs/maintenance/) | Optional audit tools and historical proposals |

---

**Moamen Taha Abuzied** · Data Analytics & Business Intelligence  
[LinkedIn](https://www.linkedin.com/in/moamen-taha-data-analyst/) · [Maven Market project](https://github.com/moamenabden7-max/Maven-Market-PowerBI)
