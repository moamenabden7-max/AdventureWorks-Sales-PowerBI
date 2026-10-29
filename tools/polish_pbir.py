"""Polish a Power BI Desktop-exported PBIR report folder, with a backup.

Usage: python tools/polish_pbir.py /path/to/Project.Report
Save the PBIX as a PBIP in Desktop first. Legacy report.json is not edited.
This changes page labels/order and the profit-margin visual, not the model.
"""
import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

NAMES = {
    'overview': 'Sales Overview', 'products': 'Product Performance',
    'customers': 'Customer Insights', 'gap': 'Scenario Analysis',
    'kpis': 'KPI Reference', 'tooltip': 'Report Tooltip', 'page 1': 'Retail Overview',
}
ORDER = ['Sales Overview', 'Product Performance', 'Customer Insights',
         'Scenario Analysis', 'KPI Reference', 'Report Tooltip', 'Retail Overview']


def polish(report):
    definition = report / 'definition'
    metadata_path = definition / 'pages/pages.json'
    if not metadata_path.exists():
        raise ValueError('Expected a Desktop-exported PBIR definition/pages/pages.json. Save as PBIP with PBIR first.')
    metadata = json.loads(metadata_path.read_text(encoding='utf-8-sig'))
    changes, page_labels = {}, {}
    for path in (definition/'pages').glob('*/page.json'):
        page = json.loads(path.read_text(encoding='utf-8-sig'))
        page['displayName'] = NAMES.get(page['displayName'].strip().lower(), page['displayName'])
        page_labels[page['name']] = page['displayName']
        changes[path] = page
    if not set(metadata['pageOrder']).issubset(page_labels):
        raise ValueError('Some ordered pages are missing. Nothing has been changed.')
    metadata['pageOrder'] = sorted(metadata['pageOrder'], key=lambda x: ORDER.index(page_labels[x]) if page_labels[x] in ORDER else 999)
    overview = next((p for p in metadata['pageOrder'] if page_labels[p] in ['Sales Overview','Retail Overview']), None)
    if overview:
        metadata['activePageName'] = overview
    changes[metadata_path] = metadata
    for path in (definition/'pages').glob('*/visuals/*/visual.json'):
        data = json.loads(path.read_text(encoding='utf-8-sig'))
        visual = data.get('visual', {})
        state = visual.get('query', {}).get('queryState', {})
        projections = state.get('Y', {}).get('projections', [])
        is_margin = any(p.get('queryRef', '').lower() == 'all data.profit margin' for p in projections)
        if visual.get('visualType') == 'donutChart' and is_margin:
            visual['visualType'] = 'clusteredBarChart'
            # Both visuals use Category/Y roles. Keep query fields and filters intact.
            changes[path] = data
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    backup = report.parent / (report.name + '.backup-' + stamp)
    shutil.copytree(report, backup)
    for path, data in changes.items():
        tmp = path.with_suffix('.tmp')
        tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
        tmp.replace(path)
    return backup, len(changes)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('report_folder', type=Path)
    a = p.parse_args()
    backup, count = polish(a.report_folder)
    print(f'Updated {count} JSON files. Full backup: {backup}')
    print('Open/apply changes in Power BI Desktop and inspect every page before saving a release PBIX.')
