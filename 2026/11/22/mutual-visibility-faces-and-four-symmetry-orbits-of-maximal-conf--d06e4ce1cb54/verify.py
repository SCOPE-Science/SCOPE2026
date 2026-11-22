"""Exact finite verification of mutual visibility in the Fano incidence graph.

Run with Python 3.10 or newer: python verify.py
No third-party packages or input files are required.
"""
from collections import Counter
from itertools import combinations, permutations

N = 7
VERTICES = 2 * N
LINES = tuple(frozenset(((j + d) % N for d in (0, 1, 3))) for j in range(N))
INCIDENT = {(p, j) for j, line in enumerate(LINES) for p in line}
ADJ = [set() for _ in range(VERTICES)]
for p, j in INCIDENT:
    ADJ[p].add(N + j)
    ADJ[N + j].add(p)
assert all(len(s) == 3 for s in ADJ)
assert len(set(LINES)) == N
assert all(sum({p, q} <= line for line in LINES) == 1
           for p, q in combinations(range(N), 2))
assert all(len(LINES[i] & LINES[j]) == 1
           for i, j in combinations(range(N), 2))

# Test A: generic graph search and all shortest-path internal masks.
def distances(source):
    result = [-1] * VERTICES
    result[source] = 0
    queue = [source]
    for x in queue:
        for y in sorted(ADJ[x]):
            if result[y] == -1:
                result[y] = result[x] + 1
                queue.append(y)
    assert -1 not in result
    return tuple(result)

D = tuple(distances(u) for u in range(VERTICES))
assert max(max(row) for row in D) == 3
PATH_MASKS = {}
for u, v in combinations(range(VERTICES), 2):
    def extend(x, interior):
        if x == v:
            return [interior]
        result = []
        for y in sorted(ADJ[x]):
            if D[u][y] == D[u][x] + 1 and D[y][v] == D[x][v] - 1:
                result.extend(extend(y, interior if y == v else interior | (1 << y)))
        return result
    paths = extend(u, 0)
    assert len(paths) == (1 if D[u][v] in (1, 2) else 3)
    PATH_MASKS[(u, v)] = tuple(paths)

def test_graph(mask):
    points = [v for v in range(VERTICES) if mask & (1 << v)]
    return all(any((mask & internal) == 0 for internal in PATH_MASKS[(u, v)])
               for u, v in combinations(points, 2))

# Test B: independent Fano-geometric criterion, with no distance search.
JOIN = {(p, q): next(j for j in range(N) if {p, q} <= LINES[j])
        for p, q in combinations(range(N), 2)}
INTERSECTION = {(j, k): next(iter(LINES[j] & LINES[k]))
                for j, k in combinations(range(N), 2)}

def test_geometry(mask):
    pset = {p for p in range(N) if mask & (1 << p)}
    lset = {j for j in range(N) if mask & (1 << (N + j))}
    for p, q in combinations(sorted(pset), 2):
        if JOIN[(p, q)] in lset:
            return False
    for j, k in combinations(sorted(lset), 2):
        if INTERSECTION[(j, k)] in pset:
            return False
    for p in pset:
        for j in lset:
            if (p, j) in INCIDENT:
                continue
            if not any(a not in lset and next(iter(LINES[a] & LINES[j])) not in pset
                       for a in range(N) if p in LINES[a]):
                return False
    return True

FACES = set()
face_poly = Counter()
bidegrees = Counter()
for mask in range(1 << VERTICES):
    a = test_graph(mask)
    b = test_geometry(mask)
    assert a == b, (mask, a, b)
    if a:
        FACES.add(mask)
        face_poly[mask.bit_count()] += 1
        bidegrees[((mask & 127).bit_count(), (mask >> 7).bit_count())] += 1
assert len(FACES) == 2257
assert [face_poly[k] for k in range(8)] == [1, 14, 91, 322, 651, 728, 392, 58]
assert not any(face_poly[k] for k in range(8, 15))
FACETS = {mask for mask in FACES if all((mask | (1 << v)) not in FACES
          for v in range(VERTICES) if not (mask & (1 << v)))}
facet_poly = Counter(mask.bit_count() for mask in FACETS)
assert dict(facet_poly) == {6: 70, 7: 58}

# Verify that point permutations preserving Fano lines give all 168 collineations.
line_dict = {line: j for j, line in enumerate(LINES)}
COLLINEATIONS = []
for pi in permutations(range(N)):
    images = [line_dict.get(frozenset(pi[i] for i in line)) for line in LINES]
    if all(j is not None for j in images):
        COLLINEATIONS.append(tuple(pi) + tuple(N + j for j in images))
assert len(COLLINEATIONS) == 168
# This polarity exchanges point p with line -p (indices modulo 7).
POLARITY = tuple(N + (-i) % N for i in range(N)) + tuple((-i) % N for i in range(N))
AUTOMORPHISMS = set(COLLINEATIONS)
AUTOMORPHISMS.update(tuple(POLARITY[p[i]] for i in range(VERTICES))
                     for p in COLLINEATIONS)
assert len(AUTOMORPHISMS) == 336
for p in AUTOMORPHISMS:
    assert all(((v in ADJ[u]) == (p[v] in ADJ[p[u]]))
               for u in range(VERTICES) for v in range(VERTICES))

def transform(mask, permutation):
    return sum(1 << permutation[i] for i in range(VERTICES) if mask & (1 << i))

unseen = set(FACETS)
orbits = []
while unseen:
    representative = min(unseen)
    orbit = {transform(representative, pi) for pi in AUTOMORPHISMS}
    assert orbit <= FACETS
    unseen -= orbit
    orbits.append((representative.bit_count(), len(orbit), representative,
                   Counter(((x & 127).bit_count(), (x >> 7).bit_count())
                           for x in orbit)))
assert sorted((d, size) for d, size, _, _ in orbits) == [(6, 28), (6, 42), (7, 2), (7, 56)]
assert sum(size for _, size, _, _ in orbits) == 128
print('FANO_GEODESIC_CRITERION_OK')
print('FACES', [face_poly[i] for i in range(8)], 'TOTAL', len(FACES))
print('FACETS', dict(sorted(facet_poly.items())))
for degree, size, rep, parts in sorted(orbits):
    print('ORBIT', degree, size, 'REP', [i for i in range(14) if rep & (1 << i)],
          'BIDEGREES', sorted(parts.items()))
print('AUTOMORPHISMS', len(AUTOMORPHISMS))
print('VERIFY_OK')
