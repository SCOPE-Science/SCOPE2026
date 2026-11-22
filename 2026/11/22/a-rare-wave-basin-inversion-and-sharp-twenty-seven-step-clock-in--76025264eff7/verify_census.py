"""Exact structural consistency checks for independently enumerated finite-state censuses.

This checks output agreement and arithmetic invariants; the two C++ programs
are the exhaustive generators and must be run to reproduce the certificate.
"""
from pathlib import Path
import csv
from collections import Counter

def read_report(path):
    text=Path(path).read_text(encoding='utf8').splitlines()
    sections={}
    current=None
    for line in text:
        if line in ('ORBITCOUNTS','MAX_STATES','BASIN_SIZES_BY_PERIOD','HIST'):
            current=line
            sections[current]=[]
        elif current and line not in ('BY_PERIOD',) and not line.startswith(('MAX_WITNESS','N ')):
            sections[current].append(line)
        elif line=='BY_PERIOD':
            current=None
    return sections

a,b=(read_report(f) for f in ('frucht4_a.out','frucht4_b.out'))
for section in ('ORBITCOUNTS','MAX_STATES','BASIN_SIZES_BY_PERIOD','HIST'):
    assert a[section] == b[section],f'Independent programs disagree at {section}'
orbits=dict(map(lambda s:tuple(map(int,s.split())),a['ORBITCOUNTS']))
assert orbits=={1:1,4:1024,5:10,6:2}
assert sum(orbits.values())==1037
assert sum(p*c for p,c in orbits.items())==4159
hist={(int(t),int(p)):int(n) for t,p,n in (s.split() for s in a['HIST'])}
assert len(hist)==72
assert sum(hist.values())==4**12
assert max(t for t,p in hist)==27
assert {p:n for (t,p),n in hist.items() if t==27}=={4:18}
byperiod=Counter()
for (t,p),n in hist.items(): byperiod[p]+=n
assert dict(byperiod)=={1:6520408,4:3302146,5:5168039,6:1786623}
lines=a['BASIN_SIZES_BY_PERIOD']
bs={}
for line in lines:
    if line.startswith('VALUES'):
        bs[last]['values']=list(map(int,line.split()[1:]))
    else:
        p,*stats=line.split(); last=int(p)
        bs[last]={key:int(value) for token in stats for key,value in [token.split('=')]}
assert bs[4]['count']==1024 and bs[4]['max']==373631
assert bs[5]['count']==10 and bs[5]['min']==385193 and bs[5]['max']==673112
assert bs[6]['count']==2 and bs[6]['min']==880674 and bs[6]['max']==905949
assert bs[5]['min']>bs[4]['max']
assert len(bs[5]['values'])==10 and sum(bs[5]['values'])==bs[5]['sum']
assert len(bs[6]['values'])==2 and sum(bs[6]['values'])==bs[6]['sum']
assert {p:bs[p]['sum'] for p in (1,4,5,6)}==dict(byperiod)
with Path('joint_census.csv').open(encoding='utf8',newline='') as f:
    r=csv.DictReader(f)
    csvhist={(int(x['first_periodic_entry_time']),int(x['eventual_least_period'])):int(x['initial_configuration_count']) for x in r}
assert csvhist==hist
print('CENSUS_OK 16777216 states, 72 cells, 1037 cycles, 27-entry cutoff, basin inversion')
