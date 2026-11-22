#!/usr/bin/env python3
"""Exact exhaustive graph-orbit and type-number collision certificate (stdlib only)."""
from collections import defaultdict
from itertools import permutations

def edges_of_order(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]

def transform(mask, E, idx, perm):
    result=0
    for k,(u,v) in enumerate(E):
        if mask & (1<<k):
            a,b=sorted((perm[u],perm[v]))
            result |= 1<<idx[(a,b)]
    return result

def connected(n,mask,E):
    reached={0}
    while True:
        new=reached.copy()
        for k,(u,v) in enumerate(E):
            if mask & (1<<k):
                if u in reached: new.add(v)
                if v in reached: new.add(u)
        if new==reached: return len(new)==n
        reached=new

def type_number_and_histogram(n,mask,E):
    hist=defaultdict(int)
    for subset in range(1<<n):
        edge_count=sum(bool(mask & (1<<k)) and bool(subset&(1<<u)) and bool(subset&(1<<v)) for k,(u,v) in enumerate(E))
        hist[edge_count]+=1
    return sum(count*(1<<e) for e,count in hist.items()),dict(sorted(hist.items()))

def degree_multiset(n,mask,E):
    ds=[0]*n
    for k,(u,v) in enumerate(E):
        if mask&(1<<k): ds[u]+=1;ds[v]+=1
    return sorted(ds)

EXPECTED_ALL={1:1,2:2,3:4,4:11,5:34,6:156}
EXPECTED_CONNECTED={1:1,2:1,3:2,4:6,5:21,6:112}
EXPECTED_SIX={256:2,376:2,832:2}
for n in range(1,7):
    E=edges_of_order(n);idx={pair:i for i,pair in enumerate(E)}
    seen=bytearray(1<<len(E));perm=list(permutations(range(n)))
    value_fibres=defaultdict(list);n_classes=0;n_connected=0
    for mask in range(len(seen)):
        if seen[mask]:continue
        orbit={transform(mask,E,idx,p) for p in perm}
        for other in orbit:seen[other]=1
        n_classes+=1
        c=connected(n,mask,E)
        if c: n_connected+=1
        val,hist=type_number_and_histogram(n,mask,E)
        value_fibres[val].append((mask,c,degree_multiset(n,mask,E),hist))
    assert all(seen)
    assert n_classes==EXPECTED_ALL[n],(n,n_classes)
    assert n_connected==EXPECTED_CONNECTED[n],(n,n_connected)
    collisions={z:items for z,items in value_fibres.items() if len(items)>1}
    assert ({z:len(items) for z,items in collisions.items()}==EXPECTED_SIX if n==6 else not collisions)
    print(f'n={n} all_isomorphism_classes={n_classes} connected_classes={n_connected} collision_fibres={len(collisions)}')
    if n==6:
        assert sum(sum(c for _,c,_,_ in items)==2 for items in collisions.values())==1
        for z in sorted(collisions):
            for mask,c,degrees,hist in collisions[z]:
                edges=[pair for k,pair in enumerate(E) if mask&(1<<k)]
                print('  ',z,'connected='+str(c),'mask='+str(mask),'edges='+str(edges),'degrees='+str(degrees),'histogram='+str(hist))
                assert sum(hist.values())==(1<<n)
                assert sum(count*(1<<e) for e,count in hist.items())==z
print('EXHAUSTIVE_COLLISION_CHECK_OK')
