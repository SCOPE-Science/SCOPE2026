"""Exact semitotal-domination reconfiguration calculation for Pappus's graph.

Standalone Python 3: no third-party packages are required.
"""
from collections import Counter, deque
from itertools import combinations
import json

N = 18
SHIFTS = (5, 7, -7, 7, -7, -5) * 3
adj = [0] * N
for i in range(N):
    for j in ((i+1) % N, (i-1) % N, (i+SHIFTS[i]) % N):
        adj[i] |= 1 << j
        adj[j] |= 1 << i
assert all(m.bit_count() == 3 for m in adj)
assert sum(x.bit_count() for x in adj) == 54
FULL = (1 << N) - 1
closed = [adj[i] | (1 << i) for i in range(N)]
near = [0] * N
for i in range(N):
    near[i] = adj[i]
    for j in range(N):
        if adj[i] & (1 << j):
            near[i] |= adj[j]
    near[i] &= ~(1 << i)

def semitotal(mask):
    cover = 0
    for i in range(N):
        if (mask >> i) & 1:
            cover |= closed[i]
            if not (near[i] & mask):
                return False
    return cover == FULL

sets = [sum(1 << j for j in c) for c in combinations(range(N), 6)
        if semitotal(sum(1 << j for j in c))]
assert len(sets) == 297
masks = set(sets)
# 2014 delta-bound: 2*n/(2*Delta+1)=36/7 > 5.
assert N * 2 > 5 * (2 * 3 + 1)
efficient = {s for s in sets if all((adj[i] & s).bit_count() == 1 for i in range(N))}
assert len(efficient) == 9

def analyze(slide):
    neigh = {s: set() for s in sets}
    for s in sets:
        for v in range(N):
            if not (s >> v) & 1:
                continue
            allowed = (adj[v] if slide else FULL) & ~s
            for w in range(N):
                if not (allowed >> w) & 1:
                    continue
                t = (s ^ (1 << v)) | (1 << w)
                if t in masks:
                    neigh[s].add(t)
    assert all(s in neigh[t] for s in sets for t in neigh[s])
    edges = sum(map(len,neigh.values())) // 2
    comps = []
    unseen = set(sets)
    while unseen:
        root = min(unseen)
        dist = {root: 0}
        queue = deque([root])
        while queue:
            x = queue.popleft()
            for y in neigh[x]:
                if y not in dist:
                    dist[y] = dist[x] + 1
                    queue.append(y)
        cs = set(dist)
        unseen -= cs
        comps.append(cs)
    big = max(comps, key=len)
    ecc = []
    for root in big:
        dist = {root: 0}
        q = deque([root])
        while q:
            x = q.popleft()
            for y in neigh[x]:
                if y not in dist:
                    dist[y] = dist[x] + 1
                    q.append(y)
        assert len(dist) == len(big)
        ecc.append(max(dist.values()))
    return {
        "states": len(sets), "edges": edges,
        "component_size_multiplicities": sorted(Counter(map(len,comps)).items()),
        "degree_multiplicities": sorted(Counter(map(len,neigh.values())).items()),
        "largest_component_radius": min(ecc),
        "largest_component_diameter": max(ecc),
        "largest_component_eccentricities": sorted(Counter(ecc).items()),
        "isolated_equal_efficient": {next(iter(c)) for c in comps if len(c)==1} == efficient,
    }

out = {"graph": "Pappus graph from LCF [5,7,-7,7,-7,-5]^3",
       "semitotal_domination_minimum": 6,
       "minimum_states": len(sets), "efficient_open_dominating_minima": len(efficient),
       "jump": analyze(False), "slide": analyze(True)}
assert out['jump']['edges'] == 1026
assert out['slide']['edges'] == 432
assert out['jump']['component_size_multiplicities'] == [(1,9),(288,1)]
assert out['slide']['component_size_multiplicities'] == [(1,9),(288,1)]
assert out['jump']['largest_component_radius'] == out['jump']['largest_component_diameter'] == 6
assert out['slide']['largest_component_radius'] == 8
assert out['slide']['largest_component_diameter'] == 10
assert out['jump']['isolated_equal_efficient'] and out['slide']['isolated_equal_efficient']
print(json.dumps(out, sort_keys=True, indent=2))
print('VERIFY_OK')
