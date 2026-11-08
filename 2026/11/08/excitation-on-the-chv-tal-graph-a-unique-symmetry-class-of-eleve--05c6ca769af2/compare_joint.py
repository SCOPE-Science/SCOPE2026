#!/usr/bin/env python3
"""Check exact agreement of the two independently generated temporal tables."""
import csv
from pathlib import Path

rows = list(csv.DictReader(Path('chvatal_joint_census.csv').open(encoding='utf-8', newline='')))
p = {(int(r['first_entry_time']),int(r['least_period'])):int(r['configurations']) for r in rows}
assert len(p)==len(rows)==52
c = {}
cycles={}
for line in Path('chvatal_census.txt').read_text(encoding='utf-8').splitlines():
    a=line.split()
    if a[0]=='J': c[int(a[1]),int(a[2])]=int(a[3])
    if a[0]=='C': cycles[int(a[1])]=int(a[2])
assert p==c,('disagreement', set(p.items())^set(c.items()))
assert sum(p.values())==3**12
assert cycles=={1:1,3:4768,4:294,7:1012,10:504,11:8}
assert {(t,per):num for (t,per),num in p.items() if t==10}=={(10,3):32,(10,11):32}
assert sum(cycles.values())==6587
assert sum(per*k for per,k in cycles.items())==27693
print('JOINT_CENSUS_AGREEMENT_OK 52 classes 531441 states')
