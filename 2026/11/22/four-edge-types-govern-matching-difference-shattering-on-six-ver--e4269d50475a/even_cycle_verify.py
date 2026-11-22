"""Independent finite verifier for six-vertex matching-difference shattering.

Python >= 3.9, standard library only. Invoke: python3 even_cycle_verify.py
Uses recursive support growth (not the C++ program's direct 2^15 census).
"""
import itertools
import json
import pathlib
from collections import Counter

EDGES = list(itertools.combinations(range(6), 2))
EINDEX = {e: i for i, e in enumerate(EDGES)}


def matchings(vertices):
    if not vertices:
        yield 0
        return
    x, *rest = vertices
    for y in rest:
        for m in matchings([z for z in rest if z != y]):
            yield (1 << EINDEX[x, y]) | m


MATCH = sorted(matchings(list(range(6))))
CONCEPTS = sorted({a ^ b for a, b in itertools.combinations(MATCH, 2)})
assert len(MATCH) == 15 and len(CONCEPTS) == 105
assert Counter(c.bit_count() for c in CONCEPTS) == {4: 45, 6: 60}


def label(concept, support_indices):
    return sum(((concept >> e) & 1) << pos for pos, e in enumerate(support_indices))


def shattered(s):
    indices = [i for i in range(15) if (s >> i) & 1]
    return len({label(c, indices) for c in CONCEPTS}) == 1 << len(indices)


FACES = {0}
FACE_BY_SIZE = {0: [0]}
for k in range(1, 11):
    nxt = set()
    for s in FACE_BY_SIZE[k - 1]:
        start = s.bit_length()
        for e in range(start, 15):
            candidate = s | (1 << e)
            if shattered(candidate):
                nxt.add(candidate)
    FACE_BY_SIZE[k] = sorted(nxt)
    FACES |= nxt
    if not nxt:
        break
EXPECTED = [1, 15, 105, 375, 675]
assert [len(FACE_BY_SIZE[k]) for k in range(5)] == EXPECTED
assert not FACE_BY_SIZE[5]

# All positive patterns must lie in one even cycle. Conversely, every
# subset of at most four edges of an even cycle is shattered.
positive_possible = {0}
for c in CONCEPTS:
    sub = c
    while sub:
        if sub.bit_count() <= 4:
            positive_possible.add(sub)
        sub = (sub - 1) & c
assert positive_possible == FACES

facets = [s for s in FACES if not any(s | (1 << i) in FACES for i in range(15) if not ((s >> i) & 1))]
assert len(facets) == 675 and all(s.bit_count() == 4 for s in facets)


def shape(s):
    E = [EDGES[i] for i in range(15) if (s >> i) & 1]
    degree = Counter(v for e in E for v in e)
    active = set(degree)
    components = []
    while active:
        root = active.pop()
        comp = {root}
        while True:
            new = {v for a,b in E for v in ((b,) if a in comp else ((a,) if b in comp else ())) }
            if new <= comp:
                break
            comp |= new
        active -= comp
        components.append(len(comp))
    if sorted(degree.values()) == [2,2,2,2]:
        return 'four_cycle'
    if sorted(degree.values()) == [1,1,2,2,2]:
        return 'five_vertex_path'
    if sorted(components) == [2,4]:
        return 'path_three_plus_edge'
    if sorted(components) == [3,3]:
        return 'two_three_vertex_paths'
    raise AssertionError(E)

counts = Counter(shape(s) for s in facets)
assert counts == {'four_cycle': 45, 'five_vertex_path': 360,
                  'path_three_plus_edge': 180, 'two_three_vertex_paths': 90}

# Finite trace certificates for one representative of each symmetry type.
certificate = json.loads(pathlib.Path(__file__).with_name('witnesses.json').read_text())
assert len(certificate['cases']) == 4
for case in certificate['cases']:
    support = [EINDEX[tuple(sorted(map(int, edge)))] for edge in case['support_edges']]
    assert len(support) == 4
    for pattern, cycle in enumerate(case['witness_cycles_by_pattern']):
        mask = sum(1 << EINDEX[tuple(sorted(map(int, edge)))] for edge in cycle)
        assert mask in CONCEPTS and label(mask, support) == pattern
    assert shape(sum(1 << i for i in support)) == case['type']


def rank_mod2(cols):
    basis = {}
    for x in cols:
        while x:
            pivot = x.bit_length()-1
            if pivot not in basis:
                basis[pivot] = x
                break
            x ^= basis[pivot]
    return len(basis)

ranks = [0]
for k in range(1, 5):
    previous = {s: i for i, s in enumerate(FACE_BY_SIZE[k - 1])}
    boundaries = []
    for face in FACE_BY_SIZE[k]:
        boundary = 0
        for e in range(15):
            if (face >> e) & 1:
                boundary ^= 1 << previous[face & ~(1 << e)]
        boundaries.append(boundary)
    ranks.append(rank_mod2(boundaries))
assert ranks == [0, 1, 14, 91, 284]
reduced_betti = [len(FACE_BY_SIZE[k])-ranks[k]-(ranks[k+1] if k<4 else 0)
                 for k in range(1, 5)]
assert reduced_betti == [0,0,0,391]
print('PASS: 15 matchings, 105 cycles (45 four-cycles, 60 six-cycles)')
print('PASS: shattered-support f-vector', EXPECTED)
print('PASS: four facet orbits', dict(counts))
print('PASS: rank boundaries', ranks[1:], 'reduced betti', reduced_betti)
print('PASS: 64 explicit trace witnesses, positive-support characterization')
