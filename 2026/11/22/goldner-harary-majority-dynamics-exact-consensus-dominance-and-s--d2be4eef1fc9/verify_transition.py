#!/usr/bin/env python3
"""Exact finite-state proof by functional-graph peeling; Python 3 standard library."""
from collections import Counter, deque
from pathlib import Path
import csv

# Sage Math's GoldnerHararyGraph edge dictionary, undirected edges listed once.
EDGE_ROWS = {
    0: (1, 3, 4),
    1: (2, 3, 4, 5, 6, 7, 10),
    2: (3, 7),
    3: (7, 8, 9, 10),
    4: (3, 5, 9, 10),
    5: (10,),
    6: (7, 10),
    7: (8, 10),
    8: (10,),
    9: (10,),
}
N = 11
MASK = (1 << N) - 1
adj = [0] * N
for u, js in EDGE_ROWS.items():
    for v in js:
        assert u != v and 0 <= v < N
        adj[u] |= 1 << v
        adj[v] |= 1 << u
assert sum(a.bit_count() for a in adj) == 54
assert sorted(a.bit_count() for a in adj) == [3]*6 + [6]*2 + [8]*3

def transition(x):
    y = 0
    for v, neighbors in enumerate(adj):
        s = (x & neighbors).bit_count()
        d = neighbors.bit_count()
        if 2*s > d or (2*s == d and ((x >> v) & 1)):
            y |= (1 << v)
    return y

NEXT = [transition(x) for x in range(MASK + 1)]
ind = [0] * (MASK+1)
for t in NEXT:
    ind[t] += 1
queue = deque(x for x in range(MASK+1) if ind[x] == 0)
removed = []
while queue:
    x = queue.popleft(); removed.append(x)
    y = NEXT[x]; ind[y] -= 1
    if ind[y] == 0:
        queue.append(y)
cycle_id = [-1] * (MASK+1)
depth = [0] * (MASK+1)
cycles = []
for start in range(MASK+1):
    if ind[start] and cycle_id[start] < 0:
        orbit = []
        y = start
        while cycle_id[y] < 0:
            cycle_id[y] = len(cycles)
            orbit.append(y)
            y = NEXT[y]
        assert y == start
        cycles.append(tuple(orbit))
for x in reversed(removed):
    cycle_id[x] = cycle_id[NEXT[x]]
    depth[x] = depth[NEXT[x]] + 1
assert all(i >= 0 for i in cycle_id)
assert all(len(c) in (1, 2) for c in cycles)
assert Counter(map(len, cycles)) == {1: 2, 2: 47}
assert Counter(depth) == {0: 96, 1: 742, 2: 850, 3: 324, 4: 36}
basins = Counter(cycle_id)
assert Counter(basins[i] for i,c in enumerate(cycles) if len(c)==1) == {935:2}
assert Counter(basins[i] for i,c in enumerate(cycles) if len(c)==2) == {2:27, 6:18, 8:2}
assert sum(basins.values()) == MASK+1
assert {c[0] for c in cycles if len(c)==1} == {0,MASK}
assert all(NEXT[NEXT[NEXT[NEXT[NEXT[NEXT[x]]]]]]==NEXT[NEXT[NEXT[NEXT[x]]]] for x in range(MASK+1))
assert any(NEXT[NEXT[NEXT[NEXT[NEXT[x]]]]]!=NEXT[NEXT[NEXT[x]]] for x in range(MASK+1))
rows = sorted((min(c), max(c), len(c), basins[i]) for i,c in enumerate(cycles))
assert len(rows)==49
with open(Path(__file__).with_name('basin_catalog.csv'), newline='',encoding='utf-8') as h:
    rd = list(csv.reader(h))
    expected = [['phase0','phase1','period','basin_size']] + [[str(a),str(b),str(c),str(d)] for a,b,c,d in rows]
    assert rd == expected
print('PASS transition: 2048 states, 2 fixed, 47 primitive two-cycles, max entry 4')
print('entry:',sorted(Counter(depth).items()))
print('basin:', sorted(Counter(basins.values()).items()))
print('consensus probability: 1870/2048 = 935/1024')
