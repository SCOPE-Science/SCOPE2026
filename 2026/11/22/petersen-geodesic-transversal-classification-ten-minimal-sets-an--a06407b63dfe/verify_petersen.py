#!/usr/bin/env python3
"""Independent finite verification of geodesic transversals of KG(5,2).

Run: python3 verify_petersen.py
All computations use only the Python standard library.
"""
from itertools import combinations, permutations
from collections import Counter, deque
from math import comb

BASE = range(5)
vertices = tuple(combinations(BASE, 2))
N = len(vertices)
assert N == 10
adj = tuple(tuple(a != b and set(a).isdisjoint(b) for b in vertices)
            for a in vertices)

# Derive distances from the graph itself and construct all shortest paths.
dist = []
for start in range(N):
    d = [-1] * N
    d[start] = 0
    q = deque([start])
    while q:
        x = q.popleft()
        for y in range(N):
            if adj[x][y] and d[y] == -1:
                d[y] = d[x] + 1
                q.append(y)
    dist.append(d)
assert set(v for row in dist for v in row) == {0, 1, 2}

geodesics = set()
for i in range(N):
    for j in range(i + 1, N):
        if dist[i][j] == 2:
            for m in range(N):
                if adj[i][m] and adj[m][j]:
                    geodesics.add((1 << i) | (1 << m) | (1 << j))
assert len(geodesics) == 30

# Direct path-hitting condition: every maximal length-two geodesic is hit.
direct = {s for s in range(1 << N) if all(s & path for path in geodesics)}

# Distinct characterization: unselected edges of K5 either have an isolated
# ground vertex or are exactly the four edges incident with one ground vertex.
star = []
for v in BASE:
    star.append(sum(1 << i for i, e in enumerate(vertices) if v in e))
all_edges = (1 << N) - 1
structural = {
    s for s in range(1 << N)
    if any(s & t == t for t in star)
    or any(s & (all_edges ^ t) == (all_edges ^ t) for t in star)
}
assert direct == structural
poly = Counter(s.bit_count() for s in direct)
assert dict(poly) == {4: 5, 5: 30, 6: 80, 7: 90, 8: 45, 9: 10, 10: 1}

# Inclusion-minimal transversals and symmetry classes.
minimal = {s for s in direct if all(s ^ (1 << i) not in direct for i in range(N) if s >> i & 1)}
expected_minimal = set(star) | {all_edges ^ t for t in star}
assert minimal == expected_minimal and Counter(s.bit_count() for s in minimal) == {4: 5, 6: 5}

# Direct S5 action: each distinguished five-set is a symmetry orbit.
perms = list(permutations(BASE))
for s in list(minimal):
    orbit = set()
    for p in perms:
        image = tuple(vertices.index(tuple(sorted((p[a], p[b])))) for a, b in vertices)
        orbit.add(sum(1 << image[i] for i in range(N) if s >> i & 1))
    assert orbit == (set(star) if s.bit_count() == 4 else {all_edges ^ t for t in star})

# Explicit single-vertex add/delete reconfiguration, truncated at each budget.
components = {}
for budget in range(4, 8):
    states = {s for s in direct if s.bit_count() <= budget}
    unseen = set(states)
    sizes = []
    while unseen:
        start = unseen.pop()
        queue = deque([start])
        size = 0
        while queue:
            s = queue.popleft()
            size += 1
            for i in range(N):
                t = s ^ (1 << i)
                if t in unseen:
                    unseen.remove(t)
                    queue.append(t)
        sizes.append(size)
    components[budget] = sorted(sizes)
assert components == {4: [1] * 5, 5: [7] * 5,
                      6: [1] * 5 + [22] * 5, 7: [205]}

# Exactly six add/delete moves separate any two distinct four-vertex minima.
minima = list(star)
states = {s for s in direct if s.bit_count() <= 7}
for start in minima:
    q = deque([start])
    d = {start: 0}
    while q:
        s = q.popleft()
        for i in range(N):
            t = s ^ (1 << i)
            if t in states and t not in d:
                d[t] = d[s] + 1
                q.append(t)
    assert all(d[t] == 6 for t in minima if t != start)

# Inclusion-exclusion formula for the polynomial (without the brute-force path test).
formula = Counter()
for j in range(1, 6):
    remaining = comb(5-j, 2)
    fixed = 10 - remaining
    factor = (-1)**(j+1) * comb(5, j)
    for k in range(remaining+1):
        formula[fixed+k] += factor*comb(remaining, k)
formula[6] += 5
assert {k:v for k,v in formula.items() if v} == dict(poly)
print('PETERSEN_GEODESIC_VERIFY_OK')
print('maximal_geodesics=30; all_sets=261; polynomial=', sorted(poly.items()))
print('minimal_polynomial=5z^4+5z^6; budget_components=', components)
print('distinct_minimum_distance_at_budget7=6; symmetry_orbits=5+5')
