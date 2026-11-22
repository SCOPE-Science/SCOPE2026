#!/usr/bin/env python3
"""Independent sign-vote, trajectory-by-trajectory enumeration; Python 3 standard library."""
from pathlib import Path
from collections import Counter
import csv

# Edges are indexed as in Sage's named graph constructor.
EDGES = [
(0,1),(0,3),(0,4),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,10),
(2,3),(2,7),(3,4),(3,7),(3,8),(3,9),(3,10),(4,5),(4,9),(4,10),
(5,10),(6,7),(6,10),(7,8),(7,10),(8,10),(9,10)]
assert len(EDGES) == 27
nbs = [set() for _ in range(11)]
for a,b in EDGES:
    assert a<b
    nbs[a].add(b)
    nbs[b].add(a)

def majority(x):
    old = [1 if x & (1<<i) else -1 for i in range(11)]
    new = []
    for i in range(11):
        margin = sum(old[j] for j in nbs[i])
        new.append(old[i] if margin == 0 else (1 if margin > 0 else -1))
    return sum(1<<i for i in range(11) if new[i]>0)

basins=Counter();entry=Counter();cycles=set();periods=Counter();basin_by_period=Counter();sharp=[]
for state in range(2048):
    seen={};t=state;path=[]
    while t not in seen:
        seen[t]=len(path)
        path.append(t)
        t=majority(t)
        assert len(path)<=2048
    mu=seen[t]; cyclic=path[mu:]
    assert len(cyclic) in [1,2]
    key=tuple(sorted(cyclic))
    cycles.add(key);basins[key]+=1;entry[mu]+=1;periods[len(key)]+=1;basin_by_period[len(key)]+=1
    if mu==4:sharp.append(state)
assert entry=={0:96,1:742,2:850,3:324,4:36}
assert len(cycles)==49 and sum(len(c)==1 for c in cycles)==2
assert Counter(basins[k] for k in basins if len(k)==1)=={935:2}
assert Counter(basins[k] for k in basins if len(k)==2)=={2:27,6:18,8:2}
assert basin_by_period=={1:1870,2:178}
assert len(sharp)==36 and sharp[0]==179
rows=sorted((k[0],k[-1],len(k),v) for k,v in basins.items())
with open(Path(__file__).with_name('basin_catalog.csv'),newline='',encoding='utf8') as f:
    got=list(csv.DictReader(f))
assert [tuple(map(int,(r['phase0'],r['phase1'],r['period'],r['basin_size']))) for r in got]==rows
print('PASS trajectories: independently verified 2048 labelled states and 49 orbit basins')
print('depth-4 witness =',sharp[0]);print('period basin populations:',dict(basin_by_period))
