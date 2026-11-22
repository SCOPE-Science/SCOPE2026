#!/usr/bin/env python3
"""Cross-check independently computed exact exhaustive frequency tables."""
from pathlib import Path
from collections import defaultdict
import csv
import re
import sys

def table_from_line(text, name):
    match = re.search(r'^' + re.escape(name) + r' (.*)$',text,re.M)
    assert match is not None, f'missing {name}'
    return {int(k):int(v) for k,v in re.findall(r'(\d+):(\d+)',match.group(1))}

assert len(sys.argv)==3, 'Usage: python3 verify_tables.py reverse_output.txt forward_output.txt'
reverse=Path(sys.argv[1]).read_text(encoding='utf-8')
forward=Path(sys.argv[2]).read_text(encoding='utf-8')
expected='TOTAL 141120 NON 1856 MAX 37 EXTREMA 1'
assert reverse.splitlines()[0]==expected
assert forward.splitlines()[0]==expected
h1=table_from_line(reverse,'TRIPLE_HIST')
h2=table_from_line(forward,'TRIPLE_HIST')
assert h1==h2
with Path('triple_spectrum.csv').open(newline='') as f:
    triples=list(csv.DictReader(f))
assert len(triples)==len(h1)+1
assert triples[0]=={'worst_prescribed_triple_length':'unmergeable','rotation_classes':'1856'}
assert {int(x['worst_prescribed_triple_length']):int(x['rotation_classes']) for x in triples[1:]}==h1
assert len(h1)==23 and sum(h1.values())==139264
joint={}
for t,r,c in re.findall(r'^J (\d+) (\d+) (\d+)$',reverse,re.M):
    assert (int(t),int(r)) not in joint
    joint[(int(t),int(r))]=int(c)
with Path('joint_spectrum.csv').open(newline='') as f:
    csvjoint={(int(x['worst_prescribed_triple_length']),int(x['full_reset_length'])):int(x['rotation_classes']) for x in csv.DictReader(f)}
assert joint==csvjoint and len(joint)==205
for t,n in h1.items():assert sum(c for (j,r),c in joint.items() if j==t)==n
reset=table_from_line(reverse,'RESET_HIST')
for t,n in reset.items():assert sum(c for (j,r),c in joint.items() if r==t)==n
assert len(reset)==31 and sum(reset.values())==139264
assert re.search(r'^EXAMPLES\n11234567$',reverse,re.M)
print('TABLES_OK maps=141120 nonsynchronizing=1856 synchronizing=139264 triple_bins=23 joint_bins=205')
