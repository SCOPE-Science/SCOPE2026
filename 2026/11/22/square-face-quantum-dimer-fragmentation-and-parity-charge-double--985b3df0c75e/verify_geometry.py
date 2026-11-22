"""Exact square-face quantum dimer dynamics on the 24-vertex rhombicuboctahedron.

Python 3 standard library only. Exhaustively constructs matchings from a
three-coordinate signed-axis model and independently checks face flips.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations, product

VERTICES = [(s, i) for s in range(8) for i in range(3)]
POS = {v: p for p, v in enumerate(VERTICES)}
EDGES = set()
for s in range(8):
    for i, j in combinations(range(3), 2):
        EDGES.add(tuple(sorted((POS[s, i], POS[s, j]))))
    for i in range(3):
        for j in range(3):
            if j != i:
                EDGES.add(tuple(sorted((POS[s, i], POS[s ^ (1 << j), i]))))
assert len(EDGES) == 48
ADJ = [[] for _ in VERTICES]
for a, b in EDGES:
    ADJ[a].append(b)
    ADJ[b].append(a)
assert all(len(row) == 4 for row in ADJ)
FACES = []
for i in range(3):
    for bit in range(2):
        vs = [POS[s, i] for s in range(8) if (s >> i) & 1 == bit]
        FACES.append(frozenset(e for e in EDGES if e[0] in vs and e[1] in vs))
for i, j in combinations(range(3), 2):
    k = next(z for z in range(3) if z not in (i, j))
    for a, b in product(range(2), repeat=2):
        s = (a << i) | (b << j)
        vs = {POS[s, i], POS[s, j], POS[s ^ (1 << k), i], POS[s ^ (1 << k), j]}
        FACES.append(frozenset(e for e in EDGES if e[0] in vs and e[1] in vs))
assert len(FACES) == len(set(FACES)) == 18 and all(len(f) == 4 for f in FACES)

@lru_cache(None)
def matchings(mask):
    if mask == 0:
        return ((),)
    x = (mask & -mask).bit_length() - 1
    remainder = mask ^ (1 << x)
    return tuple(((min(x, y), max(x, y)),) + m
                 for y in ADJ[x] if remainder & (1 << y)
                 for m in matchings(remainder ^ (1 << y)))

MATCHINGS = matchings((1 << 24) - 1)
assert len(MATCHINGS) == 1088
INDEX = {frozenset(m): i for i, m in enumerate(MATCHINGS)}
assert len(INDEX) == len(MATCHINGS)
NEIGHBORS = [set() for _ in MATCHINGS]
face_of_edge = {}
for i, m in enumerate(MATCHINGS):
    s = set(m)
    for fi, f in enumerate(FACES):
        occ = s & f
        if len(occ) == 2:
            other = f - occ
            if len(other) == 2:
                m2 = frozenset((s - occ) | other)
                if m2 in INDEX:
                    j = INDEX[m2]
                    NEIGHBORS[i].add(j)
                    face_of_edge[tuple(sorted((i, j)))] = fi
assert all(i in NEIGHBORS[j] for i, ns in enumerate(NEIGHBORS) for j in ns)
assert sum(map(len, NEIGHBORS)) // 2 == 2616

component_of = [-1] * len(MATCHINGS)
components = []
for start in range(len(MATCHINGS)):
    if component_of[start] >= 0:
        continue
    k = len(components)
    q = deque([start]); component_of[start] = k; members = []
    while q:
        a = q.popleft(); members.append(a)
        for b in NEIGHBORS[a]:
            if component_of[b] < 0:
                component_of[b] = k; q.append(b)
    components.append(members)
expected = {594: 1, 16: 6, 14: 24, 2: 24, 1: 14}
assert dict(Counter(map(len, components))) == expected
assert len(components) == 69

# All 48 Euclidean symmetry operations: arbitrary signed coordinate permutations.
actions = []
for p in permutations(range(3)):
    for sign_bits in range(8):
        vperm = []
        for s, i in VERTICES:
            newbits = sum(((((s >> p[j]) & 1) ^ ((sign_bits >> j) & 1)) << j) for j in range(3))
            newaxis = p.index(i)
            vperm.append(POS[newbits, newaxis])
        actions.append(tuple(vperm))
assert len(set(actions)) == 48
for p in actions:
    assert {tuple(sorted((p[a], p[b]))) for a, b in EDGES} == EDGES

seen = set(); orbit_counts = Counter()
for i, comp in enumerate(components):
    if i in seen:
        continue
    sample = MATCHINGS[comp[0]]
    orbit = {component_of[INDEX[frozenset(tuple(sorted((p[u], p[v]))) for u, v in sample)]]
             for p in actions}
    assert all(len(components[j]) == len(comp) for j in orbit)
    seen.update(orbit)
    orbit_counts[len(comp), len(orbit)] += 1
assert dict(orbit_counts) == {(594, 1): 1, (16, 6): 1, (14, 24): 1, (2, 24): 1,
                              (1, 6): 1, (1, 8): 1}

# Linear conservation charges: quotient of matching edge-incidence vectors by
# the span of the 18 square-face boundaries over F_2.
eids = {e: j for j, e in enumerate(sorted(EDGES))}
def bits(es):
    return sum(1 << eids[e] for e in es)
basis = {}
for f in FACES:
    x = bits(f)
    for j in sorted(basis, reverse=True):
        if (x >> j) & 1:
            x ^= basis[j]
    assert x != 0
    basis[x.bit_length() - 1] = x
assert len(basis) == 18

def syndrome(m):
    x = bits(m)
    for j in sorted(basis, reverse=True):
        if (x >> j) & 1:
            x ^= basis[j]
    return x
classes = defaultdict(list)
for i, m in enumerate(MATCHINGS):
    classes[syndrome(m)].append(i)
assert len(classes) == 35
assert dict(Counter(map(len, classes.values()))) == {594: 1, 32: 3, 28: 12, 4: 12, 2: 7}
for ids in classes.values():
    by_component = Counter(component_of[i] for i in ids)
    if len(ids) == 594:
        assert len(by_component) == 1 and list(by_component.values()) == [594]
    else:
        assert len(by_component) == 2 and set(by_component.values()) == {len(ids) // 2}

print('vertices=24 edges=48 triangle_faces=8 square_faces=18')
print('perfect_matchings=1088 flip_edges=2616')
print('component_size_counts=', dict(sorted(expected.items())))
print('component_symmetry_orbits=', dict(sorted(orbit_counts.items())))
print('square_face_boundary_rank=18 syndrome_classes=35')
print('syndrome_sizes=', dict(sorted(Counter(map(len, classes.values())).items())))
print('one 594-state class; all 34 other classes split into equal twin components')
print('PASS: exact geometry, flips, components, symmetry and linear-charge partition')
