"""Exact acyclic matching and integral Morse-boundary certificate for the
perfect-matching complex of the four-by-five Cartesian grid.
Run with Python 3; uses only its standard library.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
from random import Random

ROWS, COLS = 4, 5
N = ROWS * COLS
EDGES = []
for r in range(ROWS):
    for c in range(COLS):
        v = r * COLS + c
        if r + 1 < ROWS:
            EDGES.append((v, v + COLS))
        if c + 1 < COLS:
            EDGES.append((v, v + 1))
assert len(EDGES) == 31
ADJ = [[] for _ in range(N)]
for k, (a, b) in enumerate(EDGES):
    ADJ[a].append((b, k))
    ADJ[b].append((a, k))


def all_perfect_matchings():
    def rec(remaining, chosen):
        if not remaining:
            yield tuple(sorted(chosen))
            return
        v = (remaining & -remaining).bit_length() - 1
        for w, edge_index in ADJ[v]:
            if remaining & (1 << w):
                yield from rec(remaining ^ (1 << v) ^ (1 << w),
                               chosen + (edge_index,))
    return list(rec((1 << N) - 1, ()))

FACETS = all_perfect_matchings()
assert len(FACETS) == 95
assert all(len(f) == 10 for f in FACETS)
BY_SIZE = defaultdict(set)
for facet in FACETS:
    for k in range(1, 11):
        BY_SIZE[k].update(combinations(facet, k))
FACES = set()
for k, tuples in BY_SIZE.items():
    for sub in tuples:
        FACES.add(sum(1 << i for i in sub))
FV = Counter(x.bit_count() for x in FACES)
assert [FV[i] for i in range(1, 11)] == [31,383,2229,6891,12427,13815,9592,4049,950,95]
assert len(FACES) == 50462

COFAC = defaultdict(set)
for upper in FACES:
    bits = upper
    while bits:
        bit = bits & -bits
        bits ^= bit
        lower = upper ^ bit
        if lower in FACES:
            COFAC[lower].add(upper)

active = set(FACES)
random = Random(0)
free = [face for face in active if len(COFAC[face]) == 1]
random.shuffle(free)
pairs = []
critical = []


def remove(face):
    assert face in active
    active.remove(face)
    bits = face
    while bits:
        bit = bits & -bits
        bits ^= bit
        lower = face ^ bit
        if lower in active:
            COFAC[lower].remove(face)
            if len(COFAC[lower]) == 1:
                free.append(lower)


def collapse_free_pairs():
    while free:
        lower = free.pop()
        if lower not in active or len(COFAC[lower]) != 1:
            continue
        upper = next(iter(COFAC[lower]))
        assert upper in active and upper.bit_count() == lower.bit_count() + 1
        pairs.append((lower, upper))
        remove(lower)
        remove(upper)


collapse_free_pairs()
while active:
    maximal = [f for f in active if not COFAC[f]]
    assert maximal
    # Prefer top-dimensional maximal cells that unlock the most free pairs.
    # Seeded tie-breaking makes the finite certificate reproducible.
    best, selected = None, None
    for f in maximal:
        count_two = sum(len(COFAC[f ^ (1 << i)]) == 2
                        for i in range(len(EDGES)) if (f >> i) & 1)
        score = (f.bit_count(), count_two, random.random())
        if best is None or score > best:
            best, selected = score, f
    assert not COFAC[selected]
    critical.append(selected)
    remove(selected)
    collapse_free_pairs()
assert not active
assert len(pairs) == 25227
assert len(critical) == 8
assert Counter(f.bit_count() - 1 for f in critical) == {0: 1, 2: 1, 3: 6}
assert len(set(critical).union(x for p in pairs for x in p)) == len(FACES)

# Independent full directed-graph acyclicity test. Every Hasse incidence
# is oriented upward exactly when matched, downward otherwise.
matched = set(pairs)
indeg = {face: 0 for face in FACES}
out = defaultdict(list)
incidences = 0
for upper in FACES:
    bits = upper
    while bits:
        bit = bits & -bits
        bits ^= bit
        lower = upper ^ bit
        if lower not in FACES:
            continue
        incidences += 1
        start, finish = ((lower, upper) if (lower, upper) in matched
                         else (upper, lower))
        out[start].append(finish)
        indeg[finish] += 1
q = deque(f for f, d in indeg.items() if d == 0)
visited = 0
while q:
    x = q.popleft()
    visited += 1
    for y in out[x]:
        indeg[y] -= 1
        if indeg[y] == 0:
            q.append(y)
assert visited == len(FACES), (visited, len(FACES))

# Exact algebraic Morse boundary from the six critical 3-cells to the
# unique critical 2-cell. Descending signed faces use increasing edge index.
up = {a: b for a, b in pairs if a.bit_count() == 3 and b.bit_count() == 4}
down = {b: a for a, b in pairs if a.bit_count() == 2 and b.bit_count() == 3}
target = next(f for f in critical if f.bit_count() == 3)
top = [f for f in critical if f.bit_count() == 4]


def signed_boundary(face):
    bs = [1 << i for i in range(len(EDGES)) if (face >> i) & 1]
    return [(face ^ bit, (-1) ** j) for j, bit in enumerate(bs)]


@lru_cache(None)
def reduce_two_face(face):
    if face == target:
        return 1
    if face in down:
        return 0
    assert face in up, face
    upper = up[face]
    coeff = next(c for other, c in signed_boundary(upper) if other == face)
    return -coeff * sum(c * reduce_two_face(other)
                        for other, c in signed_boundary(upper) if other != face)

boundary = tuple(sum(c * reduce_two_face(g) for g, c in signed_boundary(x))
                 for x in top)
assert boundary == (1, 0, -1, -1, 0, 0), boundary
assert sum(abs(c) for c in boundary) > 0 and 1 in boundary
assert 2 * len(pairs) + len(critical) == len(FACES)
print('GRID_4X5_PERFECT_MATCHING_OK')
print('facets', len(FACETS), 'nonempty_faces', len(FACES))
print('face_sizes', [FV[k] for k in range(1, 11)])
print('gradient_pairs', len(pairs), 'critical_cells',
      dict(Counter(f.bit_count() - 1 for f in critical)))
print('acyclic_Hasse_nodes', visited, 'incidences', incidences)
print('integral_Morse_boundary', boundary)
print('homotopy', 'wedge_of_five_3_spheres')
