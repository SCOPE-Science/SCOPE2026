#!/usr/bin/env python3
"""Independent exact check from a six-by-six bipartite incidence representation.

Run: python3 verify_bipartite.py (Python standard library only).
"""
from collections import Counter, deque
from itertools import combinations, permutations
import json

rows = ((0,1,3),(0,2,3),(1,2,4),(0,4,5),(1,2,5),(3,4,5))
# The canonical matrix's rows specify the three neighbors of each x_i.
N = 12
adj = [set() for _ in range(N)]
for x, rr in enumerate(rows):
    for y in rr:
        adj[x].add(6 + y)
        adj[6 + y].add(x)
assert sorted(map(len, adj)) == [3] * N
# Explicit labelled graph isomorphism to the independent LCF representation:
phi = {0:0,11:6,6:1,10:3,1:7,2:2,8:4,7:8,5:9,4:5,3:10,9:11}
assert set(phi) == set(phi.values()) == set(range(N))
base_edges = {tuple(sorted((u,v))) for u in range(N) for v in adj[u]}
lcf_edges = {tuple(sorted((u, (u + 1) % N))) for u in range(N)}
lcf_edges.update(tuple(sorted((u, (u+(5 if u % 2 == 0 else -5)) % N))) for u in range(N))
assert {tuple(sorted((phi[u],phi[v]))) for u,v in lcf_edges} == base_edges

def dominates(s):
    for v in range(N):
        if v not in s and not (adj[v] & s):
            return False
    return True

def has_matching(s):
    if len(s) & 1: return False
    X = sorted(s & set(range(6)))
    Y = sorted(s & set(range(6,12)))
    if len(X) != len(Y): return False
    return any(all(yy in adj[xx] for xx, yy in zip(X, yp)) for yp in permutations(Y))

for k in (2, 4):
    assert not any(dominates(set(s)) and has_matching(set(s)) for s in combinations(range(N),k))

candidates = [set(a) | set(b) for a in combinations(range(6),3) for b in combinations(range(6,12),3)]
sets = [frozenset(s) for s in candidates if dominates(s) and has_matching(s)]
assert len(candidates) == 400 and len(sets) == 184
idx = {s:i for i,s in enumerate(sets)}
g = [[] for _ in sets]
for i,s in enumerate(sets):
    for x in s:
        for y in set(range(N))-s:
            t = frozenset((s-{x})|{y})
            if t in idx:g[i].append(idx[t])
assert sum(map(len, g))//2 == 984
assert Counter(map(len, g)) == {10:120,12:64}
all_distances = Counter();ecc=Counter()
for i,s in enumerate(sets):
    d=[-1]*len(sets);d[i]=0;qu=deque([i])
    while qu:
        u=qu.popleft()
        for v in g[u]:
            if d[v]<0:d[v]=d[u]+1;qu.append(v)
    assert all(t>=0 for t in d)
    ecc[max(d)]+=1
    for j in range(i+1,len(sets)):
        assert d[j] == 6-len(s & sets[j])
        all_distances[d[j]]+=1
assert all_distances == {1:984,2:3900,3:6640,4:4512,5:768,6:32}
assert ecc == {4:24,5:96,6:64}
# Separately check the local constructive form, without using the BFS distances.
for s in sets:
    for t in sets:
        if s == t: continue
        assert any(frozenset((s-{u})|{v}) in idx for u in s-t for v in t-s)
# Independent failure witness mapped to canonical bipartite labels.
A=frozenset(phi[v] for v in (0,2,3,9,10,11))
B=frozenset(phi[v] for v in (0,1,6,9,10,11))
assert A in idx and B in idx
x=phi[2]
assert all(frozenset((A-{x})|{y}) not in idx for y in B-A)
print(json.dumps({
    'representation': 'six_by_six_bipartite', 'size_two_or_four': 0,
    'balanced_candidates': len(candidates), 'minimum_sets': len(sets),
    'jump_edges': 984, 'distance_histogram': dict(sorted(all_distances.items())),
    'eccentricity_histogram': dict(sorted(ecc.items())),
    'johnson_isometry': True, 'greedy_exchange': True, 'matroid_basis_exchange': False,
    'status': 'ALL CHECKS PASSED'
}, sort_keys=True))
