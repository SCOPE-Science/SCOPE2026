#!/usr/bin/env python3
"""Exact combinatorial checks for the total four-cut complex of the Franklin graph.

Requires Python 3.9+ standard library only. Run: python verify_franklin_four_cut.py.
"""
from collections import Counter, deque
from itertools import combinations

N = 12
# The Hamiltonian representation [5,-5]^6 of the Franklin graph.
EDGES = {tuple(sorted((v, (v + 1) % N))) for v in range(N)}
EDGES |= {tuple(sorted((v, (v + (5 if v % 2 == 0 else -5)) % N))) for v in range(N)}
NEIGH = [set() for _ in range(N)]
for u, v in EDGES:
    NEIGH[u].add(v)
    NEIGH[v].add(u)
assert len(EDGES) == 18 and all(len(a) == 3 for a in NEIGH)
INDEPENDENT_FOURS = [sum(1 << v for v in t)
                     for t in combinations(range(N), 4)
                     if all(v not in NEIGH[u] for u, v in combinations(t, 2))]
# Every face is contained in the complement of an independent four-set.
FACES = {mask for mask in range(1 << N)
         if any(mask & independent == 0 for independent in INDEPENDENT_FOURS)}
assert len(INDEPENDENT_FOURS) == 45 and len(FACES) == 2533
FVECTOR = tuple(sum(mask.bit_count() == dim + 1 for mask in FACES)
                for dim in range(8))
assert FVECTOR == (12, 66, 220, 495, 792, 638, 264, 45)
assert all(any(mask & independent == 0 for independent in INDEPENDENT_FOURS)
           for mask in FACES)
assert all((mask & (mask - 1)) in FACES for mask in FACES if mask)

# Successive element matchings, in a fixed reproducible vertex order.
ORDER = (7, 9, 11, 2, 4, 5, 1, 8, 0, 3, 10, 6)
remaining = set(FACES)
PAIRS = []
for v in ORDER:
    bit = 1 << v
    new_pairs = [(lo, lo | bit) for lo in sorted(remaining)
                 if not lo & bit and lo | bit in remaining]
    for lo, hi in new_pairs:
        assert lo in remaining and hi in remaining
        remaining.remove(lo)
        remaining.remove(hi)
    PAIRS.extend(new_pairs)
assert len(PAIRS) == 1245 and len(remaining) == 43
assert all(mask.bit_count() == 5 for mask in remaining)
assert len(set(x for pair in PAIRS for x in pair)) == 2490
MATCHED = set(PAIRS)
assert (0, 1 << ORDER[0]) in MATCHED

# Independently verify the full matched face-poset digraph is acyclic.
indeg = {mask: 0 for mask in FACES}
out = {mask: [] for mask in FACES}
incidences = 0
for upper in FACES:
    for v in range(N):
        if upper & (1 << v):
            lower = upper ^ (1 << v)
            assert lower in FACES
            incidences += 1
            a, b = (upper, lower) if (lower, upper) in MATCHED else (lower, upper)
            out[a].append(b)
            indeg[b] += 1
queue = deque(mask for mask in FACES if indeg[mask] == 0)
visited = 0
while queue:
    mask = queue.popleft()
    visited += 1
    for nb in out[mask]:
        indeg[nb] -= 1
        if indeg[nb] == 0:
            queue.append(nb)
assert visited == len(FACES), "matched Hasse diagram contains a directed cycle"
assert incidences == 12780
# Unmatching the empty-face pair leaves the empty face as a directed source.
# Verify directly that the ordinary non-augmented matching is acyclic.
ordinary_pairs = MATCHED - {(0, 1 << ORDER[0])}
assert len(ordinary_pairs) == 1244
ordinary_faces = FACES - {0}
indeg = {mask: 0 for mask in ordinary_faces}
out = {mask: [] for mask in ordinary_faces}
for upper in ordinary_faces:
    for v in range(N):
        if upper & (1 << v):
            lower = upper ^ (1 << v)
            if lower == 0:
                continue
            a, b = (upper, lower) if (lower, upper) in ordinary_pairs else (lower, upper)
            out[a].append(b)
            indeg[b] += 1
queue = deque(mask for mask in ordinary_faces if indeg[mask] == 0)
visited = 0
while queue:
    mask = queue.popleft()
    visited += 1
    for nb in out[mask]:
        indeg[nb] -= 1
        if indeg[nb] == 0:
            queue.append(nb)
assert visited == len(ordinary_faces)

# Independently enumerate graph automorphisms, without external libraries.
def all_automorphisms():
    assigned = {}
    used = set()
    result = []
    def recurse():
        if len(assigned) == N:
            result.append(tuple(assigned[i] for i in range(N)))
            return
        v = max((i for i in range(N) if i not in assigned),
                key=lambda i: (sum(a in assigned for a in NEIGH[i]), -i))
        for w in range(N):
            if w in used:
                continue
            if any(((u in NEIGH[v]) != (assigned[u] in NEIGH[w]))
                   for u in assigned):
                continue
            assigned[v] = w
            used.add(w)
            recurse()
            used.remove(w)
            del assigned[v]
    recurse()
    return sorted(result)

AUTOS = all_automorphisms()
assert len(AUTOS) == 48 and len(set(AUTOS)) == 48

def cycle_type(perm):
    visited = set()
    sizes = []
    for i in range(N):
        if i not in visited:
            j = i
            count = 0
            while j not in visited:
                visited.add(j)
                j = perm[j]
                count += 1
            sizes.append(count)
    return tuple(sorted(sizes, reverse=True))

def homology_trace(perm):
    """Reduced Lefschetz trace; homology only occurs in even degree 4."""
    trace = -1  # augmented empty face has dimension -1
    for face in FACES:
        if face == 0:
            continue
        labels = [v for v in range(N) if face & (1 << v)]
        image = [perm[v] for v in labels]
        if any(not (face & (1 << v)) for v in image):
            continue
        inversions = sum(image[i] > image[j] for i in range(len(image))
                         for j in range(i + 1, len(image)))
        trace += (-1) ** (len(labels) - 1 + inversions)
    return trace

def compose(x, y):
    return tuple(x[y[i]] for i in range(N))

def inverse(p):
    result = [0] * N
    for i, j in enumerate(p):
        result[j] = i
    return tuple(result)

unclassified = set(AUTOS)
classes = []
while unclassified:
    rep = min(unclassified)
    conjugates = {compose(compose(h, rep), inverse(h)) for h in AUTOS}
    assert conjugates <= unclassified
    assert all(homology_trace(g) == homology_trace(rep) for g in conjugates)
    classes.append((len(conjugates), cycle_type(rep), homology_trace(rep)))
    unclassified -= conjugates
classes.sort(key=lambda x: (x[1], x[2], x[0]))
assert len(classes) == 10
assert classes == [
    (1, (1,)*12, 43),
    (3, (2,2,1,1,1,1,1,1,1,1), 5),
    (3, (2,2,2,2,1,1,1,1), -1),
    (6, (2,2,2,2,2,2), -7),
    (6, (2,2,2,2,2,2), -5),
    (1, (2,2,2,2,2,2), 1),
    (8, (3,3,3,3), 1),
    (6, (4,4,2,2), -1),
    (6, (4,4,2,2), 1),
    (8, (6,6), 1),
]
assert sum(size * trace for size, _, trace in classes) == 0
print('VERTICES', N, 'EDGES', len(EDGES), 'INDEPENDENT_FOURS', len(INDEPENDENT_FOURS))
print('F_VECTOR', FVECTOR, 'AUGMENTED_FACES', len(FACES))
print('ELEMENT_MATCHING_ORDER', ORDER)
print('MATCHED_PAIRS', len(PAIRS), 'CRITICAL_FOUR_FACES', len(remaining))
print('HASSE_INCIDENCES', incidences, 'AUGMENTED_DAG', len(FACES))
print('ORDINARY_DAG', len(ordinary_faces), 'CRITICAL_VERTEX', ORDER[0])
print('GRAPH_AUTOMORPHISMS', len(AUTOS), 'CONJUGACY_CLASSES', len(classes))
for size, ctype, trace in classes:
    print('CLASS', size, ','.join(str(x) for x in ctype), trace)
print('INVARIANT_RATIONAL_H4_DIM', sum(s * t for s, _, t in classes) // len(AUTOS))
print('ALL_VERIFY_OK')
