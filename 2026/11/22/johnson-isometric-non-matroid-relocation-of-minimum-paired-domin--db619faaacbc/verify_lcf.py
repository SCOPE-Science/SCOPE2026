#!/usr/bin/env python3
"""Exhaustive standalone integer certificate for a paired-domination exchange metric.

Run: python3 verify_lcf.py. All tests use exact finite loops and the Python standard library.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations, permutations
import json

N = 12
FULL = (1 << N) - 1
# Franklin graph: the Hamiltonian cycle and the six undirected chords [5,-5]^6.
adj = [0] * N
for u in range(N):
    for v in ((u + 1) % N, (u - 1) % N, (u + (5 if u % 2 == 0 else -5)) % N):
        adj[u] |= 1 << v
assert all(adj[u].bit_count() == 3 for u in range(N))
assert all(bool(adj[u] & (1 << v)) == bool(adj[v] & (1 << u)) for u in range(N) for v in range(N))
assert sum(a.bit_count() for a in adj) == 36
assert all(not (adj[u] & (1 << v)) for u in range(0, 12, 2) for v in range(0, 12, 2))

closed = [a | (1 << i) for i, a in enumerate(adj)]
def dominate(s):
    covered = 0
    for v in range(N):
        if s & (1 << v):
            covered |= closed[v]
    return covered == FULL

@lru_cache(maxsize=None)
def perfect(s):
    if s == 0:
        return True
    v = (s & -s).bit_length() - 1
    possible = adj[v] & (s ^ (1 << v))
    while possible:
        w_bit = possible & -possible
        if perfect(s ^ (1 << v) ^ w_bit):
            return True
        possible ^= w_bit
    return False

def masks(k):
    return [sum(1 << i for i in c) for c in combinations(range(N), k)]

assert all(not (dominate(s) and perfect(s)) for k in (2, 4) for s in masks(k))
sets = [s for s in masks(6) if dominate(s) and perfect(s)]
assert len(sets) == 184
index = {s: i for i, s in enumerate(sets)}
links = [set() for _ in sets]
for i, s in enumerate(sets):
    for v in range(N):
        if not s & (1 << v):
            continue
        for w in range(N):
            t = (s ^ (1 << v)) | (1 << w)
            if not s & (1 << w) and t in index:
                links[i].add(index[t])
assert all(i in links[j] for i, li in enumerate(links) for j in li)
assert sum(len(li) for li in links) == 1968
assert Counter(map(len, links)) == {10: 120, 12: 64}

pairs = Counter()
ecc = Counter()
for i, s in enumerate(sets):
    dist = {i: 0}
    q = deque([i])
    while q:
        u = q.popleft()
        for v in links[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    assert len(dist) == len(sets)
    ecc[max(dist.values())] += 1
    for j in range(i + 1, len(sets)):
        jdist = (s ^ sets[j]).bit_count() // 2
        assert dist[j] == jdist, (i, j, dist[j], jdist)
        pairs[dist[j]] += 1
assert pairs == {1: 984, 2: 3900, 3: 6640, 4: 4512, 5: 768, 6: 32}
assert ecc == {4: 24, 5: 96, 6: 64}

# Constructive target-improving exchange certificate for every ordered pair:
# from S != T some legal exchange removes an element outside T and adds one in T.
# Induction on |S\T| gives a length-|S\T| exchange path.
greedy_counts = Counter()
for S in sets:
    for T in sets:
        if S == T:
            continue
        missing = [u for u in range(N) if S & (1 << u) and not T & (1 << u)]
        wanted = [v for v in range(N) if T & (1 << v) and not S & (1 << v)]
        choices = sum(((S ^ (1 << u)) | (1 << v)) in index for u in missing for v in wanted)
        assert choices >= 1
        greedy_counts[choices] += 1
assert sum(greedy_counts.values()) == 184 * 183
assert sum(pairs.values()) == 184 * 183 // 2

# Entire automorphism group by the bipartition. The image of the six even
# vertices determines images of all six odd vertices by their neighbor sets.
shores = (tuple(range(0, N, 2)), tuple(range(1, N, 2)))
automorphisms = []
for target_even, target_odd in (shores, shores[::-1]):
    odd_signatures = {frozenset(v for v in target_even if adj[w] & (1 << v)): w for w in target_odd}
    assert len(odd_signatures) == 6
    for p in permutations(target_even):
        mapping = dict(zip(shores[0], p))
        for old_odd in shores[1]:
            sig = frozenset(mapping[v] for v in shores[0] if adj[old_odd] & (1 << v))
            if sig not in odd_signatures:
                break
            mapping[old_odd] = odd_signatures[sig]
        if len(mapping) != N or len(set(mapping.values())) != N:
            continue
        if all(bool(adj[u] & (1 << v)) == bool(adj[mapping[u]] & (1 << mapping[v])) for u in range(N) for v in range(N)):
            automorphisms.append(mapping)
assert len(automorphisms) == 48
unassigned = set(sets)
orbits = []
while unassigned:
    s = min(unassigned)
    o = {sum(1 << p[u] for u in range(N) if s & (1 << u)) for p in automorphisms}
    assert o <= unassigned
    orbits.append(o)
    unassigned -= o
assert Counter(map(len, orbits)) == {8: 2, 12: 2, 24: 2, 48: 2}

# Not a matroid-base family, despite metric isometry in a Johnson graph.
A = sum(1 << u for u in (0, 2, 3, 9, 10, 11))
B = sum(1 << u for u in (0, 1, 6, 9, 10, 11))
assert A in index and B in index
assert all(((A ^ (1 << 2)) | (1 << v)) not in index for v in (1, 6))

# Each original-graph edge joins different shores, so no balanced size-six
# paired-dominating set can undergo a token slide and remain paired dominating.
slide_count = 0
for s in sets:
    for u in range(N):
        if not s & (1 << u):
            continue
        for v in range(N):
            if adj[u] & (1 << v) and not s & (1 << v) and ((s ^ (1 << u)) | (1 << v)) in index:
                slide_count += 1
assert slide_count == 0
print(json.dumps({
    'graph_order': 12, 'graph_edges': 18, 'minimum_paired_domination': 6,
    'minimum_sets': len(sets), 'jump_edges': 984,
    'jump_degree_histogram': dict(sorted(Counter(map(len, links)).items())),
    'jump_distance_histogram_unordered': dict(sorted(pairs.items())),
    'radius': min(ecc), 'diameter': max(ecc),
    'eccentricity_histogram': dict(sorted(ecc.items())),
    'automorphisms': len(automorphisms),
    'automorphism_orbit_sizes': sorted(map(len, orbits)),
    'johnson_isometry': True, 'greedy_exchange_histogram_ordered': dict(sorted(greedy_counts.items())),
    'matroid_basis_exchange': False,
    'exchange_failure': {'from': [0, 2, 3, 9, 10, 11],
                         'to': [0, 1, 6, 9, 10, 11],
                         'remove': 2, 'possible_insertions': [1, 6]},
    'slide_edges': 0,
    'status': 'ALL CHECKS PASSED'
}, sort_keys=True))
