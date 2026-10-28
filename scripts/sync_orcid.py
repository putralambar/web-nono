#!/usr/bin/env python3
"""Fetch public ORCID works, deduplicate by DOI or ORCID work ID."""
import json, os, re, urllib.request
from pathlib import Path
ORCID = os.environ.get('ORCID_ID', '').strip()
DEST = Path(__file__).resolve().parents[1] / '_data' / 'publications.json'
if not re.fullmatch(r'\d{4}-\d{4}-\d{4}-[\dX]{4}', ORCID):
    raise SystemExit('Set a valid ORCID_ID in GitHub repository variables.')
def get(url):
    req = urllib.request.Request(url, headers={'Accept':'application/json','User-Agent':'NonoAcademicSite/1.0'})
    with urllib.request.urlopen(req, timeout=25) as res:
        return json.load(res)
base=f'https://pub.orcid.org/v3.0/{ORCID}'
works=get(base+'/works').get('group',[])
rows=[];seen=set()
for group in works:
    summaries=group.get('work-summary',[])
    if not summaries: continue
    w=summaries[0]
    title=((w.get('title') or {}).get('title') or {}).get('value') or 'Untitled'
    year=(((w.get('publication-date') or {}).get('year') or {}).get('value') or '')
    venue=((w.get('journal-title') or {}).get('value') or ''
    doi=''
    for external in ((w.get('external-ids') or {}).get('external-id') or []):
        if (external.get('external-id-type') or '').lower()=='doi':
            doi=(external.get('external-id-value') or '').strip().replace('https://doi.org/','')
            break
    key=('doi:'+doi.lower()) if doi else 'orcid:'+str(w.get('put-code'))
    if key in seen: continue
    seen.add(key)
    rows.append({'title':title,'year':year,'venue':venue,'authors':'','doi':doi,'url':('https://doi.org/'+doi if doi else (w.get('url') or {}).get('value') or '')})
rows.sort(key=lambda x: x['year'],reverse=True)
DEST.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Synchronized {len(rows)} ORCID publication records.')
