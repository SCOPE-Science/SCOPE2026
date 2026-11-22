#!/usr/bin/env python3
"""Compare full independent exact census summaries and check population identities."""
import json
import re
import sys
from pathlib import Path

def parse_cpp(data):
    chunks = [c.strip() for c in data.strip().split('p=') if c.strip()]
    out = {}
    for part in chunks:
        lines=part.splitlines()
        vals={'p': int(lines[0].split()[0])}
        for k,v in re.findall(r'([a-z_]+)=(\d+)', lines[0]):
            vals[k]=int(v)
        vals['entry_histogram'] = [[int(a),int(b)] for a,b in re.findall(r'(\d+):(\d+)',lines[1])]
        vals['basin_histogram'] = [[int(a),int(b),int(c)] for a,b,c in re.findall(r'\((\d+),(\d+)\):(\d+)',lines[2])]
        vals['nonuniform_fixed_by_weight'] = [[int(a),int(b)] for a,b in re.findall(r'(\d+):(\d+)',lines[3])]
        out[vals['p']]=vals
    return out

p_data = {v['p']:v for v in (json.loads(s) for s in Path(sys.argv[1]).read_text().splitlines())}
c_data = parse_cpp(Path(sys.argv[2]).read_text())
assert set(p_data)==set(c_data)=={13,17}
for p in sorted(p_data):
    a,b=p_data[p],c_data[p]
    for key,val in b.items():
        assert a[key] == val,(p,key,a[key],val)
    assert sum(num for _,num in a['entry_histogram'])==1<<p
    assert sum(n*mult for _,n,mult in a['basin_histogram'])==1<<p
    assert sum(mult for k,n,mult in a['basin_histogram'] if k==1)==a['fixed']
    assert sum(mult for k,n,mult in a['basin_histogram'] if k==2)==a['two_cycles']
    assert a['consensus_total']+a['nonconsensus_fixed_basin']+a['two_cycle_basin']==1<<p
    assert a['entry_histogram'][-1][0]==6
print('PASS: Both independently generated graph, update, and orbit algorithms agree at every published statistic on both Paley graphs; exact mass and sharp-depth identities hold.')
