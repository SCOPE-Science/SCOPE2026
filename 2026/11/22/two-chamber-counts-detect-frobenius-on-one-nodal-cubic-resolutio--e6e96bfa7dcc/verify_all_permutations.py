#!/usr/bin/env python3
"""Independent full S6-class check of the arithmetic Zariski-chamber table.

The algorithm uses the star/triangle description of sets of pairwise
intersecting secant edges and independently classifies the root extensions.
"""
from itertools import combinations,permutations
from collections import Counter
from pathlib import Path
import json
n=6
pairs=list(combinations(range(n),2))
# An admissible negative-one support comprises a chosen set E of exceptional
# curves and an intersecting family of secant edges disjoint from E.
def edge_families(remaining):
    rem=tuple(sorted(remaining))
    yield frozenset() # no secants
    for ij in combinations(rem,2):yield frozenset((ij,))
    for center in rem:
        neighbors=tuple(i for i in rem if i!=center)
        for size in range(2,len(neighbors)+1):
            for sub in combinations(neighbors,size):
                yield frozenset(tuple(sorted((center,j))) for j in sub)
    for triple in combinations(rem,3):
        yield frozenset(tuple(sorted(e)) for e in combinations(triple,2))

# Generate canonical pairs of exceptional-label subset and intersecting
# family of secant-edge labels, with or without root Q.
supports=set()
for k in range(7):
    for exceptions in combinations(range(n),k):
        E=frozenset(exceptions)
        for edges in edge_families(set(range(n))-E):
            supports.add((E,edges,False))
            if len(E)<=1:supports.add((E,edges,True))
assert len(supports)==1898
assert sum(root for _,_,root in supports)==648
source=json.loads(Path(__file__).with_name('chamber_table.json').read_text())
expected={tuple(item['cycle_partition']):(item['fixed_chambers'],item['fixed_chambers_with_conic']) for item in source['entries']}

def part(p):
    seen=set();cycles=[]
    for i in range(6):
        if i in seen:continue
        j=i;k=0
        while j not in seen:
            seen.add(j);k+=1;j=p[j]
        cycles.append(k)
    return tuple(sorted(cycles,reverse=True))

for p in permutations(range(6)):
    count=0;rootcount=0
    for E,P,root in supports:
        if {p[i] for i in E}!=set(E):continue
        if {tuple(sorted((p[i],p[j]))) for i,j in P}!=set(P):continue
        count+=1
        rootcount+=root
    assert (count,rootcount)==expected[part(p)],(p,count,rootcount)
print('ALL_720_FROBENIUS_ACTIONS_OK')
