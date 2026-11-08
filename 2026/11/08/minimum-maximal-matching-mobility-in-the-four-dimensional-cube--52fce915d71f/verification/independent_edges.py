#!/usr/bin/env python3
"""Independent certificate: enumerate edge k-subsets, check matchability/coverage,
then compute full cube automorphism orbits and exchange-graph connectivity.
"""
from itertools import combinations,permutations
from collections import Counter,deque
import json

E=tuple((i,i^(1<<j)) for i in range(16) for j in range(4) if i<(i^(1<<j)))
assert len(E)==32
edge_masks=tuple((1<<u)|(1<<v) for u,v in E)
all_mask=(1<<16)-1

# Any matching with <=5 edges is nonmaximal, and all 6-edge maximal
# matchings are enumerated independently of a matching generator.
opt=[]
for size in (5,6):
    for subset in combinations(range(32),size):
        occupied=0
        valid=True
        for edge_index in subset:
            bitset=edge_masks[edge_index]
            if occupied&bitset:
                valid=False;break
            occupied|=bitset
        if not valid:continue
        free=all_mask^occupied
        if any((free&bit)==bit for bit in edge_masks):continue
        assert size==6
        opt.append(frozenset(E[t] for t in subset))
assert len(opt)==192
S=set(opt)

def permute(v,p):
    return sum(((v>>j)&1)<<p[j] for j in range(4))

def image_matching(m,p,t):
    return frozenset(tuple(sorted((permute(u,p)^t,permute(v,p)^t))) for u,v in m)

orbit_map={};orbits=[]
for seed in opt:
    if seed in orbit_map:continue
    orbit={image_matching(seed,p,t) for p in permutations(range(4)) for t in range(16)}
    assert orbit<=S
    for m in orbit:orbit_map[m]=len(orbits)
    orbits.append(orbit)
assert sorted(map(len,orbits))==[96,96]

index={m:i for i,m in enumerate(opt)}
links=[set() for _ in opt]
edge_types=Counter()
for i in range(192):
    for j in range(i+1,192):
        lost=len(opt[i]-opt[j])
        assert lost>1
        if lost==2:
            links[i].add(j);links[j].add(i)
            pair=tuple(sorted((orbit_map[opt[i]],orbit_map[opt[j]])))
            edge_types[pair]+=1
assert sum(map(len,links))//2==528
assert sorted(edge_types.values())==[48,96,384],edge_types

# Recompute connectivity/diameter with independent queue traversal.
ecc=[]
for src in range(192):
    levels=[-1]*192
    levels[src]=0
    q=deque([src])
    while q:
        a=q.popleft()
        for b in links[a]:
            if levels[b]<0:
                levels[b]=levels[a]+1;q.append(b)
    assert all(x>=0 for x in levels)
    ecc.append(max(levels))
assert Counter(ecc)=={5:96,6:96}

print(json.dumps({
    "graph":"Q4","independent_edge_candidate_k5_checked":201376,
    "independent_edge_candidate_k6_checked":906192,
    "minimum_maximal_matching_count":len(opt),
    "minimum_maximal_matching_size":6,
    "hyperoctahedral_automorphism_orbit_sizes":sorted(map(len,orbits)),
    "two_edge_exchange_edges":sum(map(len,links))//2,
    "orbit_pair_edge_count_values":sorted(edge_types.values()),
    "two_edge_exchange_connected":True,
    "two_edge_radius":min(ecc),"two_edge_diameter":max(ecc)
},sort_keys=True))
