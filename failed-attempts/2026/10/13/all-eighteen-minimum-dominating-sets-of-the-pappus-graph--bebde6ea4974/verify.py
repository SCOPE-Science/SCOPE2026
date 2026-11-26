#!/usr/bin/env python3
"""Standalone finite checks for Pappus-graph minimum dominating sets.

Requires only Python 3 standard library. Defines the incidence graph of
TD(3,3) and compares it with an independently constructed LCF graph.
"""

from collections import Counter, deque
from itertools import combinations

N = 18
V = range(N)
POINTS = range(9)
LINES = range(9, 18)


def P(i, a):
    return 3 * i + (a % 3)


def L(x, y):
    return 9 + 3 * (x % 3) + (y % 3)


adj = [set() for _ in V]
for x in range(3):
    for y in range(3):
        ell = L(x, y)
        for p in (P(0, x), P(1, y), P(2, x + y)):
            adj[ell].add(p)
            adj[p].add(ell)
assert all(len(adj[v]) == 3 for v in V)
assert sum(map(len, adj)) // 2 == 27

# Distinct graph presentation: Frucht LCF [5,7,-7,7,-7,-5]^3.
lcf_steps = [5, 7, -7, 7, -7, -5] * 3
lcf_edges = {
    frozenset((i, (i + 1) % N)) for i in V
} | {
    frozenset((i, (i + lcf_steps[i]) % N)) for i in V
}
assert len(lcf_edges) == 27
# Fixed incidence-to-LCF isomorphism (each edge is directly checked).
lcf_label = (0, 10, 14, 2, 6, 16, 8, 4, 12, 1, 5, 17, 3, 11, 9, 13, 7, 15)
assert sorted(lcf_label) == list(V)
assert {frozenset((lcf_label[u], lcf_label[v])) for u in V
        for v in adj[u]} == lcf_edges


# Exact distances, including the two opposite-partner vertices at distance 4.
dist = []
for v in V:
    d = [-1] * N
    d[v] = 0
    todo = deque((v,))
    while todo:
        u = todo.popleft()
        for w in adj[u]:
            if d[w] == -1:
                d[w] = d[u] + 1
                todo.append(w)
    assert Counter(d) == {0: 1, 1: 3, 2: 6, 3: 6, 4: 2}
    dist.append(d)


# Completely independent exhaustive test: all 2^18 labeled subsets.
closed = [sum(1 << u for u in (adj[v] | {v})) for v in V]
full_mask = (1 << N) - 1
levels = Counter()
opt = set()
min_size = N + 1
for mask in range(1 << N):
    covered = 0
    for v in V:
        if mask & (1 << v):
            covered |= closed[v]
    if covered == full_mask:
        k = mask.bit_count()
        levels[k] += 1
        if k < min_size:
            min_size = k
            opt.clear()
        if k == min_size:
            opt.add(mask)
assert min_size == 5
assert len(opt) == 18

# The structural construction is a priori independent of the preceding census.
canonical = {}
for v in V:
    s = adj[v] | {w for w in V if dist[v][w] == 4}
    assert len(s) == 5
    bitset = sum(1 << u for u in s)
    assert bitset not in canonical.values()
    canonical[v] = bitset
assert set(canonical.values()) == opt

# Exactly one closed-neighborhood incidence triple, the unique omitted center.
for center, mask in canonical.items():
    multiplicity = [sum(bool(mask & (1 << u)) for u in (adj[w] | {w}))
                    for w in V]
    assert multiplicity[center] == 3
    assert all(multiplicity[w] == 1 for w in V if w != center)
    assert sum(1 for v in POINTS if mask >> v & 1) in (2, 3)

# In the chosen labeling, verify all three noncollinearity / parallel classes.
noncol = [set() for _ in POINTS]
for u in POINTS:
    for v in POINTS:
        if u != v and not (adj[u] & adj[v]):
            noncol[u].add(v)
assert all(noncol[u] == {v for v in range(3 * (u // 3), 3 * (u // 3) + 3)
                             if v != u} for u in POINTS)

nonmeet = {u: set() for u in LINES}
for u in LINES:
    for v in LINES:
        if u != v and not (adj[u] & adj[v]):
            nonmeet[u].add(v)
assert all(nonmeet[L(x, y)] ==
           {L(xx, yy) for xx in range(3) for yy in range(3)
            if (yy - xx) % 3 == (y - x) % 3 and (xx, yy) != (x, y)}
           for x in range(3) for y in range(3))

# Explicit graph automorphisms, including a point-line duality.
def translation(a, b):
    f = [None] * N
    for x in range(3):
        f[P(0, x)] = P(0, x + a)
        f[P(1, x)] = P(1, x + b)
        f[P(2, x)] = P(2, x + a + b)
    for x in range(3):
        for y in range(3):
            f[L(x, y)] = L(x + a, y + b)
    return tuple(f)

cyclic = [None] * N
for a in range(3):
    cyclic[P(0, a)] = P(1, -a)
    cyclic[P(1, a)] = P(2, a)
    cyclic[P(2, a)] = P(0, a)
for x in range(3):
    for y in range(3):
        cyclic[L(x, y)] = L(x + y, -x)
cyclic = tuple(cyclic)

dual = (9, 13, 17, 10, 14, 15, 11, 16, 12, 0, 6, 3, 4, 1, 8, 7, 5, 2)
generators = [translation(1, 0), translation(0, 1), cyclic, dual]
for perm in generators:
    assert sorted(perm) == list(V)
    assert {frozenset((perm[u], perm[v])) for u in V for v in adj[u]} == \
           {frozenset((u, v)) for u in V for v in adj[u]}
identity = tuple(V)
auto_group = {identity}
todo = deque((identity,))
while todo:
    p = todo.popleft()
    for g in generators:
        q = tuple(g[p[u]] for u in V)
        if q not in auto_group:
            auto_group.add(q)
            todo.append(q)
assert len(auto_group) == 216
assert {g[0] for g in auto_group} == set(V)
assert {sum(1 << g[u] for u in V if canonical[0] >> u & 1)
        for g in auto_group} == opt

print("VERIFY_OK graph=TD(3,3)=Pappus LCF_iso=18 vertices=18 edges=27")
print("VERIFY_OK all_masks=262144 gamma=5 optimum_sets=18 point_split=9+9")
print("VERIFY_OK unique_triple_coverage=18 canonical_centers=18 distance4_two_each")
print("VERIFY_OK automorphism_group=216 one_optimum_orbit=18")
