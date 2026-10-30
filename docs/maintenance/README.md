# Optional maintenance tools

[← Documentation](../README.md) · [Find the report](../../powerbi/README.md)

These files are for development and auditing. They are not needed to open a report.

| Item | Purpose |
| --- | --- |
| `tools/audit_model.py` | Read-only aggregate audit of a locally supplied PBIX |
| `requirements.txt` | Python dependencies for the audit |
| `proposals/` | Historical DAX and theme proposals; revised definitions live in the project |

After saving a verified PBIX from Desktop, optionally audit that local file. Run from the repository root:

```bash
python -m pip install -r docs/maintenance/requirements.txt
python docs/maintenance/tools/audit_model.py "/path/to/verified-report.pbix" --output audit-results.json
```

This audit recomputes data aggregates in Python. It does not execute DAX, render visuals or verify the revised PBIP.
