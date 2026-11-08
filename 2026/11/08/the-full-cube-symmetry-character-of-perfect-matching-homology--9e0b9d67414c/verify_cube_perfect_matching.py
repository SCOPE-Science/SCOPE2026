#!/usr/bin/env python3
"""Exact finite verification of cube perfect-matching-complex homology character.
Only the Python standard library is required.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product

VERTICES = tuple(range(8))
EDGES = tuple((u, v) for u in VERTICES for v in VERTICES
              if u < v and (u ^ v).bit_count() == 1)
EDGE_SET = set(EDGES)


def enumerate_perfect_matchings(remaining, chosen=()):
    if not remaining:
        yield frozenset(chosen)
        return
    u = min(remaining)
    for v in sorted(remaining - {u}):
        if (u, v) in EDGE_SET:
            yield from enumerate_perfect_matchings(
                remaining - {u, v}, chosen + ((u, v),))


MATCHINGS = tuple(sorted(enumerate_perfect_matchings(set(VERTICES)),
                         key=lambda m: tuple(sorted(m))))
MATCHING_INDEX = {m: i for i, m in enumerate(MATCHINGS)}
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}


def all_faces(facets):
    faces = {()}
    for facet in facets:
        ordered = tuple(sorted(facet))
        for size in range(1, len(ordered) + 1):
            faces.update(combinations(ordered, size))
    return faces


ORIGINAL = all_faces([{EDGE_INDEX[e] for e in m} for m in MATCHINGS])
INCIDENCE = {e: tuple(i for i, m in enumerate(MATCHINGS) if e in m)
             for e in EDGES}
NERVE = all_faces(INCIDENCE.values())
assert len(VERTICES) == 8 and len(EDGES) == 12
assert len(MATCHINGS) == 9
assert Counter(len(inc) for inc in INCIDENCE.values()) == {3: 12}
assert Counter(len(f) for f in ORIGINAL) == {0: 1, 1: 12, 2: 42, 3: 36, 4: 9}
assert Counter(len(f) for f in NERVE) == {0: 1, 1: 9, 2: 24, 3: 12}
assert len({inc for inc in INCIDENCE.values()}) == 12

# Each pair (triangle, edge) is a genuine elementary free-face collapse.
remaining_triangles = {f for f in NERVE if len(f) == 3}
remaining_edges = {f for f in NERVE if len(f) == 2}
collapses = []
while remaining_triangles:
    free = None
    for triangle in sorted(remaining_triangles):
        for edge in combinations(triangle, 2):
            if sum(set(edge).issubset(t) for t in remaining_triangles) == 1:
                free = (triangle, edge)
                break
        if free:
            break
    if free is None:
        raise AssertionError('The claimed collapse sequence did not finish')
    triangle, edge = free
    assert edge in remaining_edges and triangle in remaining_triangles
    remaining_triangles.remove(triangle)
    remaining_edges.remove(edge)
    collapses.append(free)
assert len(collapses) == 12 and len(remaining_edges) == 12
# Connectivity of the remaining graph.
visited = {0}
while True:
    new = visited | {v for u, v in remaining_edges if u in visited} | \
          {u for u, v in remaining_edges if v in visited}
    if new == visited:
        break
    visited = new
assert visited == set(range(9))
assert len(remaining_edges) - 9 + 1 == 4


def permutation_sign(seq):
    return -1 if sum(seq[i] > seq[j] for i in range(len(seq))
                     for j in range(i+1, len(seq))) % 2 else 1


def signed_lefschetz(faces, perm):
    total = 0
    for face in faces:
        if not face:
            continue
        image = tuple(perm[i] for i in face)
        if tuple(sorted(image)) == face:
            total += (-1) ** (len(face) - 1) * permutation_sign(image)
    return total


def map_vertex(u, sigma, flips):
    return sum((((u >> sigma[j]) & 1) ^ flips[j]) << j for j in range(3))


def transform_edge(edge, sigma, flips):
    return tuple(sorted(map_vertex(v, sigma, flips) for v in edge))


def signed_type(sigma, flips):
    seen = set()
    positive, negative = [], []
    for i in range(3):
        if i in seen:
            continue
        cycle = []
        j = i
        while j not in seen:
            seen.add(j)
            cycle.append(j)
            j = sigma[j]
        (negative if sum(flips[j] for j in cycle) % 2 else positive).append(len(cycle))
    return (tuple(sorted(positive, reverse=True)),
            tuple(sorted(negative, reverse=True)))


class_values = defaultdict(list)
character = []
automorphisms = set()
for flips in product((0, 1), repeat=3):
    for sigma in permutations(range(3)):
        ep = tuple(EDGE_INDEX[transform_edge(e, sigma, flips)] for e in EDGES)
        mp = tuple(MATCHING_INDEX[frozenset(transform_edge(e, sigma, flips) for e in m)]
                   for m in MATCHINGS)
        assert len(set(ep)) == 12 and len(set(mp)) == 9
        automorphisms.add(tuple(map_vertex(v, sigma, flips) for v in VERTICES))
        chi_original = 1 - signed_lefschetz(ORIGINAL, ep)
        chi_nerve = 1 - signed_lefschetz(NERVE, mp)
        sign = permutation_sign(sigma)
        vector_trace = sum((-1) ** flips[j] for j in range(3) if sigma[j] == j)
        formula = sign + vector_trace
        assert chi_original == chi_nerve == formula, (flips, sigma,
                                                     chi_original, chi_nerve, formula)
        character.append((chi_original, sign, vector_trace))
        class_values[signed_type(sigma, flips)].append(chi_original)
assert len(automorphisms) == len(character) == 48
assert len(class_values) == 10
assert sum(chi * chi for chi, _, _ in character) == 2 * 48
assert sum(chi * sign for chi, sign, _ in character) == 48
assert sum(chi * vec for chi, _, vec in character) == 48
assert sum(sign * vec for _, sign, vec in character) == 0
assert sum(sign for _, sign, _ in character) == 0
assert sum(vec for _, _, vec in character) == 0

# Independent mod-p rank check directly on original edge-subset chains.
def mod_p_rank(columns, p):
    pivots = {}
    for col in columns:
        v = dict(col)
        while v:
            row = max(v)
            if row not in pivots:
                inv = pow(v[row], -1, p)
                pivots[row] = {k: (z*inv) % p for k,z in v.items()}
                break
            factor = v[row]
            v = {k: q for k in set(v) | set(pivots[row])
                 if (q := (v.get(k, 0) - factor*pivots[row].get(k,0)) % p)}
    return len(pivots)


def reduced_betti(p):
    by_size = {k: sorted(f for f in ORIGINAL if len(f) == k) for k in range(5)}
    ranks = [0]
    for k in range(1, 5):
        target_index = {f: i for i, f in enumerate(by_size[k-1])}
        columns = []
        for face in by_size[k]:
            columns.append({target_index[face[:i] + face[i+1:]]: (-1)**i % p
                            for i in range(k)})
        ranks.append(mod_p_rank(columns, p))
    assert ranks[1] == 1
    return tuple(len(by_size[k]) - ranks[k] - (ranks[k+1] if k < 4 else 0)
                 for k in range(5))

for p in (2, 3, 5, 7):
    assert reduced_betti(p) == (0, 0, 4, 0, 0), (p, reduced_betti(p))

print('Cube: 8 vertices, 12 edges, 9 perfect matchings.')
print('Original complex f-vector (including empty): 1,12,42,36,9.')
print('Nerve f-vector (including empty): 1,9,24,12.')
print('Nerve: 12 certified free-face collapses; graph 9 vertices/12 edges/1 component; four circles.')
print('Character by signed cycle type (positive,negative): size,trace')
for kind, vals in sorted(class_values.items()):
    assert len(set(vals)) == 1
    print(f'  {kind}: {len(vals)}, {vals[0]}')
print('All 48 cube automorphisms: original-chain Lefschetz = nerve Lefschetz = sign(sigma)+signed-coordinate trace.')
print('Rational irreducible multiplicities: coordinate-permutation sign 1, signed-coordinate module 1.')
print('Direct reduced mod-p Betti vector (empty,vertex,edge,triangle,tetrahedron) = (0,0,4,0,0), p=2,3,5,7.')
print('PASS')
