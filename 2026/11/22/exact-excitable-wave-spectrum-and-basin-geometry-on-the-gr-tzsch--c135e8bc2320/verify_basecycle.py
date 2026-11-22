#!/usr/bin/env python3
"""Five-cycle baseline for the 11-vertex Mycielski graph comparison."""
from collections import Counter

n=5
p=[3**i for i in range(n)]
q=3**n

def shift(x):
    a=[(x//w)%3 for w in p]
    out=[]
    for i,v in enumerate(a):
        out.append((v+1)%3 if v else int(a[(i-1)%5]==1 or a[(i+1)%5]==1))
    return sum(z*p[i] for i,z in enumerate(out))

period=Counter();basin=Counter();maxdepth=0
cycles={}
for s in range(q):
    route=[];position={};t=s
    while t not in position:
        position[t]=len(route)
        route.append(t)
        t=shift(t)
    mu=position[t]
    cyc=route[mu:]
    key=min(cyc)
    period[len(cyc)]+=1
    basin[key]+=1
    maxdepth=max(maxdepth,mu)
    cycles[key]=len(cyc)
assert Counter(cycles.values())=={1:1,5:2}
assert sorted(basin.values())==[45,45,153]
assert maxdepth==4
print('PASS 5-cycle baseline: 1 fixed, 2 primitive five-cycles, basins 153/45/45, sharp entry 4')
