#!/usr/bin/env python3
"""Exact finite verification for the cuboctahedral three-clique-free complex.

All faces are bitmasks of the twelve edges of the three-dimensional cube.
No packages beyond the Python standard library are used.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations

EDGES = [(a, b) for a in range(8) for b in range(a + 1, 8)
         if (a ^ b).bit_count() == 1]
assert len(EDGES) == 12
STARS = [sum(1 << i for i, e in enumerate(EDGES) if v in e)
         for v in range(8)]
assert len(set(STARS)) == 8 and all(t.bit_count() == 3 for t in STARS)

# The triangles of the line graph are exactly the eight cube stars.
triangles = []
for ids in combinations(range(12), 3):
    if all(set(EDGES[i]) & set(EDGES[j]) for i, j in combinations(ids, 2)):
        triangles.append(sum(1 << i for i in ids))
assert set(triangles) == set(STARS)

FACES = {s for s in range(1 << 12) if all(s & t != t for t in STARS)}
assert len(FACES) == 1699
F_VECTOR = Counter(s.bit_count() - 1 for s in FACES)
assert [F_VECTOR[d] for d in range(-1, 8)] == [1, 12, 66, 212, 423, 516, 352, 108, 9]
facets = [s for s in FACES
          if not any(s | (1 << i) in FACES for i in range(12)
                     if not (s >> i & 1))]
assert len(facets) == 49
assert Counter(s.bit_count() - 1 for s in facets) == {5: 4, 6: 36, 7: 9}

def boundary(s):
    result = []
    i = 0
    v = s
    while v:
        bit = v & -v
        v -= bit
        result.append((s ^ bit, (-1) ** i))
        i += 1
    return result

# Sequential element matching on the augmented simplicial face poset.
remaining = set(FACES)
LOWER, UPPER = {}, {}
pairs = []
for i in range(12):
    for s in sorted(remaining):
        t = s | (1 << i)
        if t != s and t in remaining:
            LOWER[s] = t
            UPPER[t] = s
            pairs.append((s, t))
            remaining.remove(s)
            remaining.remove(t)
CRITICAL = sorted(remaining)
assert len(pairs) == 847
assert CRITICAL == [598, 888, 1446, 2710, 3158]
assert Counter(s.bit_count() - 1 for s in CRITICAL) == {4: 1, 5: 4}

# Complete directed Hasse graph: unmatched incidences down, matched up.
in_degree = {s: 0 for s in FACES}
arrows = defaultdict(list)
for s in FACES:
    for t, _ in boundary(s):
        a, b = (t, s) if LOWER.get(t) == s else (s, t)
        arrows[a].append(b)
        in_degree[b] += 1
queue = deque(s for s, deg in in_degree.items() if deg == 0)
visited = 0
while queue:
    s = queue.popleft()
    visited += 1
    for t in arrows[s]:
        in_degree[t] -= 1
        if in_degree[t] == 0:
            queue.append(t)
assert visited == len(FACES)

# Integral Morse complex via oriented elimination of matched face pairs.
@lru_cache(None)
def reduce_face(s):
    if s in remaining:
        return {s: 1}
    if s in UPPER:
        return {}
    assert s in LOWER
    t = LOWER[s]
    eps = dict(boundary(t))[s]
    out = defaultdict(int)
    for a, coeff in boundary(t):
        if a != s:
            for k, v in reduce_face(a).items():
                out[k] -= eps * coeff * v
    return {k: v for k, v in out.items() if v}

critical_differentials = {}
for s in CRITICAL:
    if s.bit_count() != 6:
        continue
    out = defaultdict(int)
    for t, coeff in boundary(s):
        for k, v in reduce_face(t).items():
            out[k] += coeff * v
    critical_differentials[s] = dict(out)
coefficients = [critical_differentials[s].get(598, 0) for s in CRITICAL[1:]]
assert coefficients == [-1, 1, -1, -1]
assert all(set(d) == {598} for d in critical_differentials.values())
# One unit attaching degree kills the only four-cell, leaving three five-spheres.

# Direct simplicial homology computation over F_2, independent of matching.
faces_by_dim = defaultdict(list)
for s in FACES:
    faces_by_dim[s.bit_count() - 1].append(s)
ranks = {}
for d in range(8):
    row_no = {s: i for i, s in enumerate(faces_by_dim[d - 1])}
    pivots = {}
    for s in faces_by_dim[d]:
        column = 0
        for t, _ in boundary(s):
            column ^= 1 << row_no[t]
        while column:
            k = column.bit_length() - 1
            if k in pivots:
                column ^= pivots[k]
            else:
                pivots[k] = column
                break
    ranks[d] = len(pivots)
mod_two_betti = {d: len(faces_by_dim[d]) - ranks.get(d, 0)
                 - ranks.get(d + 1, 0) for d in range(8)}
assert mod_two_betti == {0: 0, 1: 0, 2: 0, 3: 0,
                         4: 0, 5: 3, 6: 0, 7: 0}

# Signed Lefschetz trace on the simplicial chain complex for all 48 cube symmetries.
def permutation_sign(seq):
    parity = sum(seq[i] > seq[j] for i in range(len(seq))
                 for j in range(i + 1, len(seq)))
    return (-1) ** parity

character_values = []
for p in permutations(range(3)):
    for flips in range(8):
        def transform_vertex(x):
            return (sum(((x >> i) & 1) << p[i] for i in range(3)) ^ flips)
        edge_map = [EDGES.index(tuple(sorted((transform_vertex(a),
                                              transform_vertex(b)))))
                    for a, b in EDGES]
        assert len(set(edge_map)) == 12
        trace = 0
        for s in FACES:
            support = [i for i in range(12) if s >> i & 1]
            image = [edge_map[i] for i in support]
            if sorted(image) == support:
                trace += (-1) ** len(support) * permutation_sign(image)
        expected = permutation_sign(p) * sum((-1) ** ((flips >> i) & 1)
                   for i in range(3) if p[i] == i)
        assert trace == expected, (p, flips, trace, expected)
        character_values.append(trace)
assert Counter(character_values) == {0: 16, 1: 15, -1: 15, 3: 1, -3: 1}
assert sum(character_values) == 0  # no invariant line

print('edges:', EDGES)
print('triangles in line graph:', len(triangles))
print('face count (augmented):', len(FACES))
print('f-vector (-1 through 7):', [F_VECTOR[d] for d in range(-1, 8)])
print('facets by dimension:', dict(sorted(Counter(s.bit_count()-1 for s in facets).items())))
print('Morse pairs:', len(pairs), 'critical masks:', CRITICAL)
print('directed Hasse acyclic:', visited, 'of', len(FACES), 'vertices')
print('integral Morse differential:', coefficients)
print('simplicial mod-2 Betti:', mod_two_betti)
print('B3 automorphisms:', len(character_values))
print('rational H5 character distribution:', dict(sorted(Counter(character_values).items())))
print('signed-coordinate twist character equality: PASS')
print('all exact tests: PASS')
