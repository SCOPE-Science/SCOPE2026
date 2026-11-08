#!/usr/bin/env python3
"""Exact finite verification of the symmetry module on Coxeter independence homology.

Python standard library only. No external data files required.
Run: python3 verify_coxeter_st.py
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations, product
from array import array
from math import lcm
import json

POINTS = range(1, 8)
VERTICES = list(t for t in combinations(POINTS, 3) if t[0] ^ t[1] ^ t[2])
assert len(VERTICES) == 28
VERTEX_INDEX = {v: i for i, v in enumerate(VERTICES)}
EDGES = [(i, j) for i, a in enumerate(VERTICES) for j, b in enumerate(VERTICES)
         if i < j and not set(a).intersection(b)]
assert len(EDGES) == 42
NEIGHBORS = [0] * 28
for u, v in EDGES:
    NEIGHBORS[u] |= 1 << v
    NEIGHBORS[v] |= 1 << u
assert all(m.bit_count() == 3 for m in NEIGHBORS)

# A Fano collineation sends each triple to its image under a linear bijection.
def apply_matrix(columns, x):
    y = 0
    for k in range(3):
        if x & (1 << k):
            y ^= columns[k]
    return y

INNER = set()
for columns in product(range(1, 8), repeat=3):
    if len({apply_matrix(columns, x) for x in POINTS}) != 7:
        continue
    INNER.add(tuple(VERTEX_INDEX[tuple(sorted(apply_matrix(columns, a) for a in t))]
                    for t in VERTICES))
assert len(INNER) == 168
OUTER = (0, 1, 4, 5, 2, 3, 7, 6, 12, 14, 15, 13, 8, 11,
         9, 10, 16, 24, 25, 20, 19, 26, 27, 23, 17, 18, 21, 22)
IDENTITY = tuple(range(28))
def compose(a, b):
    return tuple(a[b[k]] for k in range(28))
assert compose(OUTER, OUTER) == IDENTITY
GROUP = sorted(INNER | {compose(OUTER, x) for x in INNER})
GROUP_SET = set(GROUP)
assert len(GROUP) == 336
INDEX = {p: i for i, p in enumerate(GROUP)}
INNER_INDICES = {INDEX[p] for p in INNER}
for p in GROUP:
    assert len(set(p)) == 28
    for u, v in EDGES:
        assert NEIGHBORS[p[u]] & (1 << p[v])
# Closure, inverse, and normal index-two subgroup checks.
for p in GROUP:
    inv = tuple(p.index(i) for i in range(28))
    assert inv in GROUP_SET
    for q in GROUP:
        assert compose(p, q) in GROUP_SET

# Exhaustively compute all simplices of the independence complex.
FACES = []
FVECTOR = Counter()
def enumerate_faces(face, options):
    FACES.append(face)
    FVECTOR[face.bit_count()] += 1
    while options:
        bit = options & -options
        options ^= bit
        i = bit.bit_length() - 1
        enumerate_faces(face | bit, options & ~NEIGHBORS[i])
enumerate_faces(0, (1 << 28) - 1)
assert len(FACES) == len(set(FACES)) == 196009
assert [FVECTOR[k] for k in range(13)] == [1, 28, 336, 2268, 9506,
                25788, 45836, 52928, 38556, 16660, 3752, 336, 14]
assert sum((-1)**k * FVECTOR[k] for k in range(13)) == -7

# A complete acyclic matching supplies the integral homotopy premise.
remaining = set(FACES)
matched = {}
batches = []
while True:
    counts = [0] * 28
    for face in remaining:
        available = ((1 << 28) - 1) ^ face
        while available:
            bit = available & -available
            available ^= bit
            i = bit.bit_length() - 1
            if (face | bit) in remaining:
                counts[i] += 1
    best = max(counts)
    if best == 0:
        break
    i = max(i for i, c in enumerate(counts) if c == best)
    bit = 1 << i
    removed = []
    for face in remaining:
        if not (face & bit) and face | bit in remaining:
            matched[face] = face | bit
            removed.extend((face, face | bit))
    assert len(removed) == 2 * best
    remaining.difference_update(removed)
    batches.append((i, best))
assert len(matched) == 98001
assert 0 in matched
critical_vertex = matched.pop(0)
remaining.add(critical_vertex)
assert len(matched) == 98000
assert len(remaining) == 8
assert sum(face.bit_count() == 1 for face in remaining) == 1
assert sum(face.bit_count() == 7 for face in remaining) == 7

nonempty = [f for f in FACES if f]
face_index = {f: i for i, f in enumerate(nonempty)}
indegree = array('i', [0]) * len(nonempty)
outneighbors = [[] for _ in nonempty]
incidences = 0
for upper in nonempty:
    u = face_index[upper]
    options = upper
    while options:
        bit = options & -options
        options ^= bit
        lower = upper ^ bit
        if not lower:
            continue
        l = face_index[lower]
        if matched.get(lower) == upper:
            outneighbors[u].append(l)
            indegree[l] += 1
        else:
            outneighbors[l].append(u)
            indegree[u] += 1
        incidences += 1
assert incidences == 1319724
queue = deque(i for i, deg in enumerate(indegree) if deg == 0)
visited = traversed = 0
while queue:
    i = queue.popleft()
    visited += 1
    for j in outneighbors[i]:
        traversed += 1
        indegree[j] -= 1
        if indegree[j] == 0:
            queue.append(j)
assert visited == len(nonempty) == 196008
assert traversed == incidences
# Forman's acyclic matching theorem now proves a wedge of seven 6-spheres.

# For a permutation g, an invariant independent set is a union of its
# vertex cycles. Such a union is allowed when its selected cycles are
# independent inside and pairwise nonadjacent. Signed simplex trace
# reduces to minus the independence polynomial of that orbit graph at -1.
def order_and_cycles(p):
    seen = set()
    cyc = []
    for v in range(28):
        if v in seen:
            continue
        w = v
        orbit = []
        while w not in seen:
            seen.add(w)
            orbit.append(w)
            w = p[w]
        cyc.append(orbit)
    order = 1
    for orbit in cyc:
        order = lcm(order, len(orbit))
    return order, cyc

def homology_trace(p):
    _, cycles = order_and_cycles(p)
    legal = []
    for cyc in cycles:
        bits = sum(1 << k for k in cyc)
        if not any(NEIGHBORS[k] & bits for k in cyc):
            legal.append(bits)
    n = len(legal)
    adj = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            if any(NEIGHBORS[v] & legal[j] for v in range(28) if legal[i] >> v & 1):
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    @lru_cache(None)
    def polynomial(mask):
        if not mask:
            return 1
        bit = mask & -mask
        i = bit.bit_length() - 1
        rest = mask ^ bit
        return polynomial(rest) - polynomial(rest & ~adj[i])
    return -polynomial((1 << n) - 1)

HOMOLOGY_CHARACTER = [homology_trace(p) for p in GROUP]
assert HOMOLOGY_CHARACTER[INDEX[IDENTITY]] == 7
assert sum(HOMOLOGY_CHARACTER) == 0
assert sum(c*c for c in HOMOLOGY_CHARACTER) == 336

# Eight Sylow-seven subgroups of the 168-element Fano collineation group.
order = [order_and_cycles(p)[0] for p in GROUP]
sylows = set()
for i in INNER_INDICES:
    if order[i] != 7:
        continue
    p = GROUP[i]
    power = IDENTITY
    subgroup = []
    for j in range(6):
        power = compose(power, p)
        subgroup.append(INDEX[power])
    sylows.add(tuple(sorted(subgroup)))
assert len(sylows) == 8
SYLOWS = [frozenset(s) for s in sorted(sylows)]

def fixed_sylows(p):
    inv = tuple(p.index(v) for v in range(28))
    count = 0
    for sylow in SYLOWS:
        conjugate = {INDEX[compose(compose(p, GROUP[i]), inv)] for i in sylow}
        if conjugate == sylow:
            count += 1
    return count

SYLOW_FIXED = [fixed_sylows(p) for p in GROUP]
for i in range(336):
    epsilon = 1 if i in INNER_INDICES else -1
    assert HOMOLOGY_CHARACTER[i] == epsilon * (SYLOW_FIXED[i] - 1)
assert sum(SYLOW_FIXED) == 336
assert sum(f*f for f in SYLOW_FIXED) == 672  # two orbits on ordered pairs

# Enumerate ALL conjugacy classes of 336 group elements, not only cycle types.
classes = []
remaining_group = set(range(336))
while remaining_group:
    k = min(remaining_group)
    p = GROUP[k]
    conjugates = set()
    for a in GROUP:
        inva = tuple(a.index(v) for v in range(28))
        conjugates.add(INDEX[compose(compose(a, p), inva)])
    assert conjugates <= remaining_group
    remaining_group -= conjugates
    assert len({HOMOLOGY_CHARACTER[i] for i in conjugates}) == 1
    assert len({SYLOW_FIXED[i] for i in conjugates}) == 1
    r = min(conjugates)
    o, cycles = order_and_cycles(GROUP[r])
    classes.append({'order': o, 'class_size': len(conjugates),
                    'vertex_cycle_type': sorted([[a,b] for a,b in Counter(map(len, cycles)).items()]),
                    'sign': 1 if r in INNER_INDICES else -1,
                    'sylow_fixed': SYLOW_FIXED[r], 'homology_trace': HOMOLOGY_CHARACTER[r],
                    'representative': list(GROUP[r])})
classes.sort(key=lambda x: (x['order'],x['class_size'],x['homology_trace']))
assert len(classes) == 9
assert sum(x['class_size'] for x in classes) == 336
assert sum(x['class_size']*x['homology_trace'] for x in classes) == 0

print('graph=28 vertices, 42 edges; automorphisms=336; Fano collineations=168')
print('simplex_count_nonempty=196008; incidences=1319724')
print('Morse_pairs=98000; critical_0=1; critical_6=7; acyclic=yes')
print('reduced_homology: H_6=Z^7; others=0')
print('Sylow_seven_subgroups=8; two_transitive=yes')
print('nine_conjugacy_classes: order size sign fixed trace')
for c in classes:
    print(c['order'],c['class_size'],c['sign'],c['sylow_fixed'],c['homology_trace'])
print('character_inner_product=1; invariant_dimension=0')
print('COXETER_SIGN_TWISTED_STEINBERG_PASS')

if __name__ == '__main__':
    import sys
    if '--write-classes' in sys.argv:
        with open('character_classes.json', 'w', encoding='utf-8') as output:
            json.dump({'graph_vertices': VERTICES, 'graph_edges': EDGES,
                       'class_representatives_and_character': classes},
                      output, ensure_ascii=False, indent=2)
            output.write('\n')
