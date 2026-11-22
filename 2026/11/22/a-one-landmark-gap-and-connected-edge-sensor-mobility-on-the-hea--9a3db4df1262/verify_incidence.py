#!/usr/bin/env python3
"""Exact exhaustive certificate for Fano incidence edge sensing and reconfiguration.
Only Python standard library; use `python3 verify_incidence.py`.
"""
from collections import Counter, deque
from itertools import combinations, permutations

N = 14
D = {0, 1, 3}
lines = [frozenset(i for i in range(7) if (i - j) % 7 in D) for j in range(7)]
assert len(set(lines)) == 7 and all(len(x) == 3 for x in lines)
edges = sorted((i, 7 + j) for j, L in enumerate(lines) for i in L)
assert len(edges) == 21
nbr = [set() for _ in range(N)]
for a, b in edges:
    nbr[a].add(b)
    nbr[b].add(a)
assert all(len(x) == 3 for x in nbr)

# Standard BFS definition of graph distance, without projective-plane distance formulas.
d = []
for s in range(N):
    dd = {s: 0}
    queue = deque([s])
    while queue:
        v = queue.popleft()
        for w in nbr[v]:
            if w not in dd:
                dd[w] = dd[v] + 1
                queue.append(w)
    assert len(dd) == N
    d.append(dd)
P = [[min(d[v][a], d[v][b]) for a, b in edges] for v in range(N)]
ve = [sum(1 << j for j, val in enumerate(P[v]) if val <= 1) for v in range(N)]
all_e = (1 << len(edges)) - 1

# Edge-resolving: all pairwise codes are distinct (not just edges incident to S).
def resolves(S):
    return len({tuple(P[v][e] for v in S) for e in range(len(edges))}) == len(edges)

def ve_dominates(S):
    seen = 0
    for v in S:
        seen |= ve[v]
    return seen == all_e

edge_count = Counter()
qualified_count = Counter()
five = []
six = []
for k in range(7):
    for S in combinations(range(N), k):
        if resolves(S):
            edge_count[k] += 1
            if k == 5:
                five.append(frozenset(S))
            if ve_dominates(S):
                qualified_count[k] += 1
                if k == 6:
                    six.append(frozenset(S))
assert [edge_count[k] for k in range(7)] == [0, 0, 0, 0, 0, 168, 1890]
assert [qualified_count[k] for k in range(7)] == [0, 0, 0, 0, 0, 0, 1386]

# Every five-landmark edge-metric basis has exactly one edge outside distance 1.
assert all((all_e ^ __import__('functools').reduce(int.__or__, (ve[v] for v in S), 0)).bit_count() == 1 for S in five)
five_set = set(five)
contained_five_bases = Counter(sum(frozenset(S - {v}) in five_set for v in S) for S in six)
assert contained_five_bases == {0: 574, 1: 672, 2: 84, 3: 56}

states = set(six)
TJ = {S: set() for S in six}
TS = {S: set() for S in six}
for S in six:
    for u in S:
        for v in range(N):
            if v in S:
                continue
            T = (S - {u}) | {v}
            if T not in states:
                continue
            TJ[S].add(T)
            if v in nbr[u]:
                TS[S].add(T)

# Exhaustive all-pairs BFS (also proves connectivity and both sharp diameters).
def signature(adj):
    assert all(S in adj[T] for T, vals in adj.items() for S in vals)
    dist = Counter()
    ecc = Counter()
    for S in adj:
        seen = {S: 0}
        Q = deque([S])
        while Q:
            U = Q.popleft()
            for V in adj[U]:
                if V not in seen:
                    seen[V] = seen[U] + 1
                    Q.append(V)
        assert len(seen) == len(adj)
        ecc[max(seen.values())] += 1
        dist.update(seen.values())
    return (sum(map(len, adj.values())) // 2, Counter(map(len, adj.values())),
            ecc, {i: (x if i == 0 else x // 2) for i, x in sorted(dist.items())})

j = signature(TJ)
s = signature(TS)
assert j == (17514, Counter({12: 28, 21: 336, 24: 168, 26: 504, 30: 350}),
             Counter({6: 1386}),
             {0: 1386, 1: 17514, 2: 133308, 3: 356608, 4: 332066, 5: 109620, 6: 10689})
assert s == (5040, Counter({4: 168, 6: 532, 7: 168, 9: 224, 10: 252, 12: 42}),
             Counter({7: 210, 8: 812, 9: 364}),
             {0: 1386, 1: 5040, 2: 23940, 3: 81256, 4: 194460, 5: 296464, 6: 247891, 7: 97104, 8: 13314, 9: 336})

# Derive the 336 Fano automorphisms, including the point-line duality.
line_index = {x: j for j, x in enumerate(lines)}
aut = []
for perm in permutations(range(7)):
    if not all(frozenset(perm[i] for i in L) in line_index for L in lines):
        continue
    lp = [line_index[frozenset(perm[i] for i in L)] for L in lines]
    aut.append(tuple(perm) + tuple(7 + x for x in lp))
assert len(aut) == 168
polarity = tuple(7 + (-i) % 7 for i in range(7)) + tuple((-j) % 7 for j in range(7))
full_aut = aut + [tuple(polarity[v] for v in perm) for perm in aut]
assert len(set(full_aut)) == 336
assert all({tuple(sorted((p[a], p[b]))) for a, b in edges} == set(edges) for p in full_aut)
seen = set()
orbits = []
for S in six:
    if S in seen:
        continue
    orbit = {frozenset(p[v] for v in S) for p in full_aut}
    assert orbit <= states and not orbit & seen
    seen |= orbit
    orbits.append(len(orbit))
assert sorted(orbits) == [14, 28, 28, 56, 84, 168, 168, 168, 168, 168, 336]
assert seen == states

print('model=Fano cyclic incidence; vertices=14 edges=21')
print('edge_resolvers_at_5=168; each_misses_exactly_one_ve_edge=TRUE')
print('minimum_vertex_edge_dominant_edge_metric_size=6')
print('minimum_qualifying_6_sets=1386; other_edge_resolving_6_sets=504')
print('five_basis_containment', sorted(contained_five_bases.items()))
print('TJ edges=17514; connected=TRUE; radius=6 diameter=6')
print('TS edges=5040; connected=TRUE; radius=7 diameter=9')
print('orbit_sizes', sorted(orbits))
print('TJ_distance_counts', j[3])
print('TS_distance_counts', s[3])
print('PASS')
