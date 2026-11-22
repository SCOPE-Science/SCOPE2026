"""Independent exhaustive check of the Shrikhande power-domination classification.
Run with Python 3. Uses simultaneous propagation and bit masks.
"""
from collections import Counter
from itertools import combinations

V = [(i, j) for i in range(4) for j in range(4)]
INDEX = {p: k for k, p in enumerate(V)}
DELTA = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}
K = {(0, 0), (0, 2), (2, 0), (2, 2)}
DIRECTIONS = [(1, 0), (0, 1), (1, 1)]
FULL = (1 << 16) - 1

def add(a, b):
    return ((a[0] + b[0]) % 4, (a[1] + b[1]) % 4)

def is_edge(p, q):
    return ((q[0] - p[0]) % 4, (q[1] - p[1]) % 4) in DELTA

def mask(points):
    return sum(1 << INDEX[p] for p in points)

NEIGH = [mask(q for q in V if is_edge(p, q)) for p in V]

def close(seed):
    seen = seed
    for i in range(16):
        if seed >> i & 1:
            seen |= NEIGH[i]
    while True:
        add_mask = 0
        for i in range(16):
            if seen >> i & 1:
                white = NEIGH[i] & (FULL ^ seen)
                if white and white & (white - 1) == 0:
                    add_mask |= white
        if not add_mask:
            return seen
        seen |= add_mask

triangles = {
    mask((V[i], V[j], V[k]))
    for i, j, k in combinations(range(16), 3)
    if is_edge(V[i], V[j]) and is_edge(V[i], V[k]) and is_edge(V[j], V[k])
}
lines = {
    mask(add(p, (a * d[0], a * d[1])) for a in range(4))
    for p in V for d in DIRECTIONS
}
assert len(triangles) == 32 and len(lines) == 12
# Explicit independent check of the critical nine-difference lemma.
B = DELTA | (K - {(0, 0)})
assert len(B) == 9
local_edges = lambda u,v: (u != v and ((v[0]-u[0]) % 4, (v[1]-u[1]) % 4) in B)
assert all(sum(local_edges(u,v) for v in B) == 4 for u in B)
local_triangles = {frozenset(c) for c in combinations(sorted(B),3)
                   if all(local_edges(u,v) for u,v in combinations(c,2))}
expected_local_triangles = {frozenset(t) for t in [
    [(0,1),(0,2),(0,3)], [(1,0),(2,0),(3,0)],
    [(1,1),(2,2),(3,3)], [(0,2),(2,0),(2,2)]]}
assert local_triangles == expected_local_triangles
assert not any(all(local_edges(u,v) for u,v in combinations(c,2))
               for c in combinations(sorted(B),4))
facets = triangles | lines

def predicted_failure(s):
    return any((s & f) == s for f in facets)

counts = Counter()
failures = set()
for s in range(1 << 16):
    actual_failure = close(s) != FULL
    assert actual_failure == predicted_failure(s), (s, actual_failure)
    if actual_failure:
        failures.add(s)
        counts[s.bit_count()] += 1
assert [counts[i] for i in range(5)] == [1, 16, 72, 80, 12]
assert len(failures) == 181
min_success = [s for s in range(1 << 16) if s not in failures and
               all((s ^ (1 << i)) in failures for i in range(16) if s >> i & 1)]
minimal = Counter(s.bit_count() for s in min_success)
assert minimal == Counter({2: 48, 3: 16}), minimal
K_cosets = {
    mask(add(p, q) for q in K) for p in V
}
assert len(K_cosets) == 4
expected_triples = {x ^ (1 << i) for x in K_cosets for i in range(16) if x >> i & 1}
D = {(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)}
expected_pairs = {
    (1 << i) | (1 << j) for i,j in combinations(range(16),2)
    if ((V[j][0]-V[i][0]) %4, (V[j][1]-V[i][1]) %4) in D
}
assert set(min_success) == expected_triples | expected_pairs
max_failed = {s for s in failures if all((s | 1<<i) not in failures for i in range(16) if not (s >> i & 1))}
assert max_failed == facets
# Every subset of size >=5 power dominates; all failures are listed here.
assert all(s.bit_count() <= 4 for s in failures)
print('PASS Python: all 65536 subsets match 32 triangles/12 cycles; failures 1,16,72,80,12; minimal PDS 48 pairs + 16 triples')
