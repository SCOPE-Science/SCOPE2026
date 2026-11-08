#!/usr/bin/env python3
"""Exact, standalone certificate for the eleven-point biplane block complex.

Requires Python 3.9 or later. Only the Python standard library is used.
"""
from collections import Counter, deque
from itertools import combinations

P = 11
Q = {pow(a, 2, P) for a in range(1, P)}
BLOCKS = frozenset(frozenset((i + q) % P for q in Q) for i in range(P))
assert Q == {1, 3, 4, 5, 9} and len(BLOCKS) == 11

# A face is nonempty and contained in one of the eleven design blocks.
faces = set()
for block in BLOCKS:
    ordered = sorted(block)
    for size in range(1, len(block) + 1):
        faces.update(combinations(ordered, size))
assert len(faces) == 242
fvector = tuple(sum(len(f) == d for f in faces) for d in range(1, 6))
assert fvector == (11, 55, 110, 55, 11)
assert all(sum({a, b} <= block for block in BLOCKS) == 2
           for a, b in combinations(range(P), 2))
assert all(len(a & b) == 2 for a, b in combinations(BLOCKS, 2))

# Independently form all simplices from the out-neighborhoods of the
# quadratic-residue tournament, and check equality of the two constructions.
outface = set()
for i in range(P):
    neigh = sorted(j for j in range(P) if j != i and (j - i) % P in Q)
    for size in range(1, len(neigh) + 1):
        outface.update(combinations(neigh, size))
assert faces == outface

# A lexicographic element matching: process pivots 0,...,10, pairing
# every still-available face not containing pivot with its coface
# obtained by adding the pivot, whenever both are still available.
# The complete Hasse orientation below proves acyclicity; ordering
# alone is not used as an unverified substitute for the DAG check.
unmatched = set(faces)
matching = []
for pivot in range(P):
    for small in sorted(unmatched, key=lambda x: (len(x), x)):
        if small not in unmatched or pivot in small:
            continue
        large = tuple(sorted(small + (pivot,)))
        if large in unmatched:
            unmatched.remove(small)
            unmatched.remove(large)
            matching.append((small, large))
assert len(matching) == 110
assert len(unmatched) == 22
assert Counter(len(face) - 1 for face in unmatched) == {0: 1, 2: 21}
assert len({f for ab in matching for f in ab}) == 220
pair_up = set(matching)
assert len(pair_up) == 110

# Full directed Hasse diagram: matched arrows are directed up;
# every other covering incidence is directed down.
indeg = {face: 0 for face in faces}
out = {face: [] for face in faces}
cover_count = 0
for large in faces:
    if len(large) == 1:
        continue
    for pos in range(len(large)):
        small = large[:pos] + large[pos + 1:]
        assert small in faces
        if (small, large) in pair_up:
            source, target = small, large
        else:
            source, target = large, small
        out[source].append(target)
        indeg[target] += 1
        cover_count += 1
assert cover_count == 715
queue = deque(face for face, degree in indeg.items() if degree == 0)
visited = 0
while queue:
    current = queue.popleft()
    visited += 1
    for target in out[current]:
        indeg[target] -= 1
        if indeg[target] == 0:
            queue.append(target)
assert visited == len(faces)

# Independent mod-2 boundary elimination, not using the matching.
edges = list(combinations(range(P), 2))
edge_index = {edge: i for i, edge in enumerate(edges)}
basis = {}
for tri in (face for face in faces if len(face) == 3):
    column = 0
    for edge in combinations(tri, 2):
        column ^= 1 << edge_index[edge]
    while column:
        top = column.bit_length() - 1
        if top in basis:
            column ^= basis[top]
        else:
            basis[top] = column
            break
assert len(basis) == 45
assert len(edges) - (P - 1) - len(basis) == 0

# Permutation composition: result[i] = left[right[i]].
identity = tuple(range(P))
translation = tuple((i + 1) % P for i in range(P))
multiplier = tuple((3 * i) % P for i in range(P))
extra = (0, 1, 10, 7, 4, 6, 5, 3, 9, 8, 2)
for g in (translation, multiplier, extra):
    assert {frozenset(g[x] for x in b) for b in BLOCKS} == BLOCKS

generators = (translation, multiplier, extra)
seen = {identity}
front = deque([identity])
while front:
    g = front.popleft()
    for h in generators:
        new = tuple(g[h[i]] for i in range(P))
        if new not in seen:
            seen.add(new)
            front.append(new)
assert len(seen) == 660


def order(g):
    seen_vertices = set()
    sizes = []
    for i in range(P):
        if i in seen_vertices:
            continue
        length = 0
        x = i
        while x not in seen_vertices:
            seen_vertices.add(x)
            x = g[x]
            length += 1
        sizes.append(length)
    from math import lcm
    result = 1
    for length in sizes:
        result = lcm(result, length)
    return result


def sign_of_order(images):
    n_inversions = sum(images[i] > images[j]
                       for i in range(len(images))
                       for j in range(i + 1, len(images)))
    return -1 if n_inversions % 2 else 1


def homology_character(g):
    # Signed simplicial Lefschetz trace L(g); H_0 is the trivial module.
    trace = 0
    for face in faces:
        image = tuple(g[i] for i in face)
        if set(image) == set(face):
            trace += (-1 if len(face) % 2 == 0 else 1) * sign_of_order(image)
    return trace - 1

order_char = Counter((order(g), homology_character(g)) for g in seen)
expected = {(1, 21): 1, (2, -3): 55, (3, 0): 110,
            (6, 0): 110, (5, 1): 264, (11, -1): 120}
assert dict(order_char) == expected, (order_char, expected)
assert sum(c * val for (_, val), c in order_char.items()) == 0

# Published irreducible characters of PSL(2,11), for classes with
# element orders 1,2,3,6,5,11 respectively. The 10-dimensional
# constituent is the one with trace -2 at involutions.
chi_10 = {1: 10, 2: -2, 3: 1, 6: 1, 5: 0, 11: -1}
chi_11 = {1: 11, 2: -1, 3: -1, 6: -1, 5: 1, 11: 0}
assert all(c == chi_10[o] + chi_11[o]
           for o, c in order_char)

# Frobenius subgroup generated by translation and multiplication.
small_group = {identity}
front = deque([identity])
while front:
    g = front.popleft()
    for h in (translation, multiplier):
        z = tuple(g[h[i]] for i in range(P))
        if z not in small_group:
            small_group.add(z)
            front.append(z)
assert len(small_group) == 55
assert sum(homology_character(g) for g in small_group) == 55
print('Q=', sorted(Q))
print('f_vector=', fvector, 'total_faces=', len(faces))
print('acyclic_pairs=', len(matching), 'critical_cells=', dict(sorted(Counter(len(f)-1 for f in unmatched).items())))
print('hasse_coverings=', cover_count, 'topologically_sorted=', visited)
print('independent_boundary_rank_F2=', len(basis))
print('full_automorphism_group_size=', len(seen))
print('character_by_element_order_and_trace=', sorted((o,c,n) for (o,c),n in order_char.items()))
print('rational_irreducibles=', (10, 11), 'full_group_invariants=', 0, 'affine_invariants=', 1)
print('ALL_CHECKS_PASS')
