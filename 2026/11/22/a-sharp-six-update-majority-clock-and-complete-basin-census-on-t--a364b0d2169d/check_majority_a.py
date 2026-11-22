#!/usr/bin/env python3
"""Exhaustive certificate for majority on the labelled Bidiakis cube.
Pure Python 3, no third-party dependencies. Run: python3 check_majority_a.py.
State bit i is the binary opinion of vertex i.
"""
from collections import Counter, deque
from itertools import permutations

N = 12
LCF = (-6, 4, -4) * 4
edges = set()
for i in range(N):
    edges.add(tuple(sorted((i, (i+1)%N))))
    edges.add(tuple(sorted((i, (i+LCF[i])%N))))
assert len(edges) == 18
nb = [0] * N
for a, b in edges:
    nb[a] |= 1 << b
    nb[b] |= 1 << a
assert set(map(int.bit_count, nb)) == {3}

# All 2^12 successor entries; the strict majority is precisely >=2 neighbors.
F = [sum(1 << i for i in range(N) if (s & nb[i]).bit_count() >= 2)
     for s in range(1 << N)]
indeg = [0] * len(F)
for y in F:
    indeg[y] += 1
pending = deque(s for s in range(len(F)) if indeg[s] == 0)
removed = []
while pending:
    u = pending.popleft()
    removed.append(u)
    v = F[u]
    indeg[v] -= 1
    if indeg[v] == 0:
        pending.append(v)
recurrent = {s for s in range(len(F)) if indeg[s] > 0}
assert len(removed) + len(recurrent) == 4096

cycle_of = [-1] * len(F)
depth = [-1] * len(F)
cycles = []
for s in sorted(recurrent):
    if cycle_of[s] >= 0:
        continue
    c = []
    x = s
    while cycle_of[x] < 0:
        assert x in recurrent
        cycle_of[x] = len(cycles)
        depth[x] = 0
        c.append(x)
        x = F[x]
    assert x == s
    cycles.append(tuple(c))
for s in reversed(removed):
    cycle_of[s] = cycle_of[F[s]]
    depth[s] = depth[F[s]] + 1
assert all(a >= 0 for a in cycle_of) and all(a >= 0 for a in depth)

lengths = Counter(map(len, cycles))
entry = dict(sorted(Counter(depth).items()))
weights = Counter(len([u for u in range(12) if s >> u & 1])
                  for c in cycles if len(c) == 1 for s in c)
basin_size = Counter(cycle_of)
basin_spectrum = {p: dict(sorted(Counter(basin_size[i]
                            for i, c in enumerate(cycles) if len(c) == p).items()))
                  for p in (1, 2)}
assert lengths == {1: 20, 2: 103}, lengths
assert entry == {0:226,1:1226,2:1364,3:608,4:408,5:216,6:48},entry
assert dict(sorted(weights.items())) == {0:1,4:4,5:4,6:2,7:4,8:4,12:1}
assert basin_spectrum[1] == {1:8, 3:2, 6:8, 392:2},basin_spectrum[1]
assert basin_spectrum[2] == {2:27,4:8,6:28,7:8,13:8,18:2,26:8,138:8,192:4,360:2},basin_spectrum[2]
assert basin_size[cycle_of[0]] == basin_size[cycle_of[4095]] == 392
assert len(recurrent) == 226
assert all(F[F[F[F[F[F[F[F[s]]]]]]]] == F[F[F[F[F[F[s]]]]]] for s in range(4096))
assert depth[59] == 6

# Independently enumerated graph symmetries via adjacency-respecting bijections.
adj = [{j for j in range(N) if nb[i] >> j & 1} for i in range(N)]
perms = []
def visit(partial):
    if len(partial) == N:
        perms.append(tuple(partial[i] for i in range(N)))
        return
    unassigned = [i for i in range(N) if i not in partial]
    u = max(unassigned, key=lambda t: (len(adj[t] & partial.keys()), -t))
    for w in range(N):
        if w in partial.values():
            continue
        if all(((v in adj[u]) == (partial[v] in adj[w])) for v in partial):
            partial[u] = w
            visit(partial)
            del partial[u]
visit({})
assert len(perms) == 8, len(perms)

def image_state(s, perm):
    return sum(1 << perm[v] for v in range(N) if s >> v & 1)
cycle_index = {tuple(sorted(c)): k for k,c in enumerate(cycles)}
remaining = set(range(len(cycles)))
class_spectrum = {1:Counter(), 2:Counter()}
while remaining:
    i = min(remaining)
    orbit = {cycle_index[tuple(sorted(image_state(x, p) for x in cycles[i]))]
             for p in perms}
    assert orbit <= remaining
    assert all(len(cycles[j]) == len(cycles[i]) for j in orbit)
    class_spectrum[len(cycles[i])][len(orbit)] += 1
    remaining -= orbit
assert dict(class_spectrum[1]) == {1:2,2:1,4:4}
assert dict(class_spectrum[2]) == {1:3,2:6,4:18,8:2}
print('PASS A: 4096 states; 20 fixed, 103 two-orbits; max depth 6')
print('entry', entry)
print('basin_spectrum',basin_spectrum)
print('8 graph symmetries; 7 fixed and 29 two-orbit spatial classes')
