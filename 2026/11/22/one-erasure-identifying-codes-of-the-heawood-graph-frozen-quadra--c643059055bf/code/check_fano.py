#!/usr/bin/env python3
"""Exhaustive certificate for redundant identifying codes of the Fano incidence graph.
No external dependencies. Uses bitsets for exact finite inequalities.
"""
from collections import Counter, deque
from itertools import combinations

N = 14
ALL = (1 << N) - 1
# Points 0..6; lines 7..13, with line j containing points j,j-1,j-3 mod 7.
neighbors = [0] * N
for p in range(7):
    for d in (0, 1, 3):
        ell = 7 + ((p + d) % 7)
        neighbors[p] |= 1 << ell
        neighbors[ell] |= 1 << p
closed = [(1 << i) | neighbors[i] for i in range(N)]
diffs = [closed[u] ^ closed[v] for u in range(N) for v in range(u+1, N)]

# A redundant identifying code survives removal of any one chosen detector
# exactly when every closed-neighborhood signature has >=2 detectors,
# and every pair of distinct signatures differs at >=2 detector positions.
def valid(mask):
    return all((mask & s).bit_count() >= 2 for s in closed) and \
           all((mask & s).bit_count() >= 2 for s in diffs)

codes = [m for m in range(1 << N) if valid(m)]
weight_counts = dict(sorted(Counter(m.bit_count() for m in codes).items()))
min_w = min(weight_counts)
optima = sorted(m for m in codes if m.bit_count() == min_w)
assert (min_w, len(optima)) == (10, 98)
assert weight_counts == {10: 98, 11: 224, 12: 91, 13: 14, 14: 1}

# Structural catalogue: complements of a point quadrangle/line quadrangle,
# or the endpoints of an induced matching of two distinct edges.
quad = set()
for shore in (range(7), range(7,14)):
    for vertices in combinations(shore, 4):
        om = sum(1 << v for v in vertices)
        # A quadrangle has no triple on any projective line or its dual pencil.
        if all(((om & neighbors[v]).bit_count() <= 2) for v in range(N)):
            quad.add(ALL ^ om)
matching = set()
edges = [(i, j) for i in range(7) for j in range(7, 14)
         if neighbors[i] >> j & 1]
for e, f in combinations(edges, 2):
    endpoints = set(e + f)
    if len(endpoints) != 4:
        continue
    # Exactly two incidence edges inside the four endpoints.
    if sum((neighbors[v] >> w) & 1 for v, w in combinations(sorted(endpoints), 2)) == 2:
        matching.add(ALL ^ sum(1 << v for v in endpoints))
assert len(quad) == 14 and len(matching) == 84
assert quad.isdisjoint(matching)
assert set(optima) == quad | matching

# Exhaustiveness of the lower bound: no five omitted sensors can be feasible.
assert sum(valid(ALL ^ sum(1 << v for v in ss)) for ss in combinations(range(N),5)) == 0


def analyze_exchange(replacements):
    adj = [set() for _ in optima]
    for i, x in enumerate(optima):
        for j in range(i+1,len(optima)):
            if (x ^ optima[j]).bit_count() == 2 * replacements:
                adj[i].add(j)
                adj[j].add(i)
    components=[]
    visited=set()
    ecc=Counter()
    shells=Counter()
    for i in range(len(optima)):
        if i not in visited:
            queue=[i];visited.add(i)
            for u in queue:
                for v in adj[u]:
                    if v not in visited:
                        visited.add(v);queue.append(v)
            components.append(len(queue))
    for src in range(len(optima)):
        dist={src:0};queue=deque([src])
        while queue:
            u=queue.popleft()
            for v in adj[u]:
                if v not in dist:
                    dist[v]=dist[u]+1;queue.append(v)
        if len(dist)>1:
            ecc[max(dist.values())]+=1
            shells[tuple(Counter(dist.values())[i] for i in range(max(dist.values())+1))]+=1
    return dict(
        edges=sum(map(len,adj))//2,
        degree_hist=dict(sorted(Counter(map(len,adj)).items())),
        components=dict(sorted(Counter(components).items())),
        eccentricity_hist=dict(sorted(ecc.items())),
        shell_hist={','.join(map(str,k)):v for k,v in sorted(shells.items())},
    )

one=analyze_exchange(1)
two=analyze_exchange(2)
assert one=={
    'edges':168,'degree_hist':{0:14,4:84},'components':{1:14,84:1},
    'eccentricity_hist':{5:84},'shell_hist':{'1,4,10,22,39,8':84}}
assert two=={
    'edges':1134,'degree_hist':{22:84,30:14},'components':{98:1},
    'eccentricity_hist':{2:98},
    'shell_hist':{'1,22,75':84,'1,30,67':14}}

import json
print(json.dumps({'graph':'Heawood/Fano incidence','minimum':min_w,
    'size_distribution':weight_counts,'optima':len(optima),
    'omitted_quadrangles':len(quad),'omitted_induced_two_edge_matchings':len(matching),
    'one_replacement':one,'exactly_two_replacements':two},sort_keys=True))
