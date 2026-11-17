#!/usr/bin/env python3
"""Exact finite verification of the rational cube-matching homology character.

Uses only the Python standard library; all faces and signed group actions are
constructed from the defining graph, without stored boundary/character tables.
"""
from collections import defaultdict
from itertools import combinations, permutations

VERTICES = range(8)
EDGES = tuple(sorted({tuple(sorted((v, v ^ (1 << j))))
                      for v in VERTICES for j in range(3)}))
INDEX = {edge: i for i, edge in enumerate(EDGES)}
FACES = {r: tuple(face for face in combinations(range(len(EDGES)), r)
                        if len({v for e in face for v in EDGES[e]}) == 2 * r)
         for r in range(1, 5)}
assert [len(FACES[r]) for r in range(1, 5)] == [12, 42, 44, 9]

# Over F_2 each boundary column is a bit vector indexed by lower faces.
def boundary_rank(upper, lower):
    lower_index = {face: j for j, face in enumerate(lower)}
    pivots = {}
    for face in upper:
        vector = sum(1 << lower_index[face[:j] + face[j + 1:]]
                     for j in range(len(face)))
        while vector:
            j = vector.bit_length() - 1
            if j in pivots:
                vector ^= pivots[j]
            else:
                pivots[j] = vector
                break
    return len(pivots)

RANKS = (boundary_rank(FACES[2], FACES[1]),
         boundary_rank(FACES[3], FACES[2]),
         boundary_rank(FACES[4], FACES[3]))
assert RANKS == (11, 31, 9), RANKS
# Rational boundary ranks are at least the mod-2 ranks. The first rank is
# at most 11, the last at most 9, and d1*d2=0 bounds rank(d2) by 42-11.
# Hence those are exactly the rational ranks, giving reduced beta_2=4.
assert (44 - RANKS[1] - RANKS[2]) == 4


def perm_sign(seq):
    return -1 if sum(seq[i] > seq[j]
                     for i in range(len(seq)) for j in range(i + 1, len(seq))) % 2 else 1


def vertex_action(sigma, b):
    return tuple(b ^ sum(((v >> i) & 1) << sigma[i] for i in range(3))
                 for v in VERTICES)


def signed_cycles(sigma, b):
    """B_3 conjugacy key: positive-cycle and negative-cycle length lists."""
    seen = set()
    pos, neg = [], []
    for i in range(3):
        if i in seen:
            continue
        orbit = []
        j = i
        while j not in seen:
            seen.add(j)
            orbit.append(j)
            j = sigma[j]
        parity = sum((b >> j) & 1 for j in orbit) % 2
        (neg if parity else pos).append(len(orbit))
    return tuple(sorted(pos)), tuple(sorted(neg))


GROUP = []
CLASS_DATA = defaultdict(list)
for sigma in permutations(range(3)):
    for b in range(8):
        vertices = vertex_action(sigma, b)
        edge_action = tuple(INDEX[tuple(sorted((vertices[u], vertices[v])))]
                            for u, v in EDGES)
        assert len(set(edge_action)) == 12
        # Reduced Lefschetz number: the empty face contributes -1.
        trace = -1
        for r, faces in FACES.items():
            for face in faces:
                moved = tuple(edge_action[e] for e in face)
                if set(moved) == set(face):
                    trace += (-1)**(r - 1) * perm_sign(moved)
        parity = (-1)**(b.bit_count() % 2)
        orientation = parity * perm_sign(sigma)
        geometric_trace = sum((-1)**((b >> j) & 1)
                              for j in range(3) if sigma[j] == j)
        predicted = parity + orientation * geometric_trace
        assert trace == predicted, (sigma, b, trace, predicted)
        row = (sigma, b, trace, predicted)
        GROUP.append(row)
        CLASS_DATA[signed_cycles(sigma, b)].append(row)

assert len(GROUP) == 48
assert len(CLASS_DATA) == 10
assert sorted(len(rows) for rows in CLASS_DATA.values()) == [1, 1, 3, 3, 6, 6, 6, 6, 8, 8], sorted(len(rows) for rows in CLASS_DATA.values())

# Character norms and constituent orthogonality.
chi = [g[2] for g in GROUP]
epsilon = [(-1)**(b.bit_count() % 2) for _, b, _, _ in GROUP]
three = [a - e for a, e in zip(chi, epsilon)]
assert sum(a * a for a in chi) == 2 * len(GROUP)
assert sum(a * e for a, e in zip(chi, epsilon)) == len(GROUP)
assert sum(a * t for a, t in zip(chi, three)) == len(GROUP)
assert sum(t * t for t in three) == len(GROUP)
assert sum(e * t for e, t in zip(epsilon, three)) == 0

# Dimensions of invariant homology for natural symmetry subgroups.
def invdim(predicate):
    selected = [c for sigma, b, c, _ in GROUP if predicate(sigma, b)]
    assert selected and sum(selected) % len(selected) == 0
    return len(selected), sum(selected)//len(selected)

INV = {
    'full': invdim(lambda s, b: True),
    'translations': invdim(lambda s, b: s == (0, 1, 2)),
    'coordinate_permutations': invdim(lambda s, b: b == 0),
    'central_inversion': invdim(lambda s, b: s == (0, 1, 2) and b in (0, 7)),
    'even_translations': invdim(lambda s, b: s == (0, 1, 2) and b.bit_count() % 2 == 0),
}
assert INV == {
    'full': (48, 0), 'translations': (8, 0),
    'coordinate_permutations': (6, 1),
    'central_inversion': (2, 3), 'even_translations': (4, 1),
}, INV
print('face_counts_by_dimension:', [len(FACES[r]) for r in range(1, 5)])
print('boundary_ranks_mod_2:', RANKS)
print('rational_reduced_betti:', (0, 0, 4, 0))
print('automorphism_count:', len(GROUP))
print('character_classes: (positive_cycle_lengths, negative_cycle_lengths, size, trace)')
for key, rows in sorted(CLASS_DATA.items()):
    assert len(set(x[2] for x in rows)) == 1
    print(' ', key[0], key[1], len(rows), rows[0][2])
print('invariant_dimensions:', INV)
print('Q3_MATCHING_EQUIVARIANT_PASS')
