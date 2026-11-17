#!/usr/bin/env python3
"""Exact 3-local equivariant chain computation for the Paley-17 neighborhood complex.

Requires Python >=3.9; no third-party packages. Integer and finite-field arithmetic only.
"""
from collections import Counter
from itertools import combinations

P = 17
Q = tuple(sorted({(a * a) % P for a in range(1, P)}))
assert Q == (1, 2, 4, 8, 9, 13, 15, 16)
GROUP = [(a, q) for a in range(P) for q in Q]
NEIGHBORS = [tuple(sorted((a + q) % P for q in Q)) for a in range(P)]
FACETS = set(NEIGHBORS)
FACES = {
    tuple(subset)
    for facet in NEIGHBORS
    for count in range(1, len(facet) + 1)
    for subset in combinations(facet, count)
}
BY_SIZE = {k: sorted(face for face in FACES if len(face) == k) for k in range(1, 9)}
assert len(GROUP) == 136
assert [len(BY_SIZE[k]) for k in range(1, 9)] == [17, 136, 612, 1122, 952, 476, 136, 17]
for a, q in GROUP:
    assert {tuple(sorted((a + q * x) % P for x in N)) for N in FACETS} == FACETS


def orientation_sign(values):
    return -1 if sum(values[i] > values[j] for i in range(len(values)) for j in range(i + 1, len(values))) % 2 else 1


def orbit_data(k):
    """In Z_(3), a simplex orbit with orientation-reversing stabilizer is zero."""
    reps, lookup, removed = [], {}, []
    for face in BY_SIZE[k]:
        if face in lookup:
            continue
        signs = {}
        for a, q in GROUP:
            ordered = tuple((a + q * x) % P for x in face)
            image = tuple(sorted(ordered))
            signs.setdefault(image, set()).add(orientation_sign(ordered))
        if any(len(values) == 2 for values in signs.values()):
            removed.append(face)
            lookup.update({image: (None, 0) for image in signs})
        else:
            index = len(reps)
            reps.append(face)
            lookup.update({image: (index, next(iter(values))) for image, values in signs.items()})
    assert len(lookup) == len(BY_SIZE[k])
    return reps, lookup, removed

REPS, LOOKUP, REMOVED = {}, {}, {}
for k in range(1, 9):
    REPS[k], LOOKUP[k], REMOVED[k] = orbit_data(k)
assert [len(REPS[k]) for k in range(1, 9)] == [1, 0, 4, 9, 7, 3, 1, 0]
assert [len(REMOVED[k]) for k in range(1, 9)] == [0, 2, 1, 1, 0, 1, 0, 1]


def boundary(k):
    # B_k: simplices of size k -> simplices of size k-1
    result = [[0 for _ in REPS[k]] for _ in REPS[k-1]]
    for col, simplex in enumerate(REPS[k]):
        for i in range(k):
            subface = simplex[:i] + simplex[i+1:]
            row, orientation = LOOKUP[k-1][subface]
            if row is not None:
                result[row][col] += ((-1) ** i) * orientation
    return result

BOUNDARIES = {k: boundary(k) for k in range(2, 9)}


def product(A, B):
    # Shape-safe composition; empty domain or codomain gives zero.
    if not A or not B:
        return []
    assert len(A[0]) == len(B)
    return [[sum(A[i][t]*B[t][j] for t in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

for k in range(3, 9):
    prod = product(BOUNDARIES[k-1], BOUNDARIES[k])
    assert all(all(x == 0 for x in row) for row in prod)


def rank_mod_p(matrix, p):
    if not matrix:
        return 0
    A = [[x % p for x in row] for row in matrix]
    nrow, ncol, rank = len(A), len(A[0]), 0
    for col in range(ncol):
        pivot = next((i for i in range(rank, nrow) if A[i][col] != 0), None)
        if pivot is None:
            continue
        A[pivot], A[rank] = A[rank], A[pivot]
        inv = pow(A[rank][col], -1, p)
        for i in range(rank + 1, nrow):
            if A[i][col]:
                factor = A[i][col] * inv % p
                A[i] = [(x - factor*y) % p for x,y in zip(A[i], A[rank])]
        rank += 1
        if rank == nrow:
            break
    return rank


def determinant(matrix):
    """Exact Leibniz determinant; only used on a 4-by-4 integer minor."""
    from itertools import permutations
    n=len(matrix)
    assert n==4 and all(len(r)==n for r in matrix)
    return sum(orientation_sign(p)*__import__('math').prod(matrix[i][p[i]] for i in range(n)) for p in permutations(range(n)))

# B_4 is the degree-three to degree-two differential, a 4-by-9 matrix.
B4 = BOUNDARIES[4]
assert len(B4) == 4 and all(len(row)==9 for row in B4)
assert B4 == [
    [-2, -1, 0, -2, -1, -1, -2, 0, 0],
    [2, 0, 0, -1, 1, -1, 0, -1, 0],
    [0, 1, 1, 0, -1, -1, 0, 0, -1],
    [0, -1, 1, 0, -1, 1, 2, -2, -1]
]
minor = [[row[j] for j in (0, 1, 2, 3)] for row in B4]
assert determinant(minor) == 12
rank3 = {k: rank_mod_p(BOUNDARIES[k], 3) for k in range(2, 9)}
assert [rank3[k] for k in range(2, 9)] == [0, 0, 3, 5, 2, 1, 0]
# The full-rank rational boundary B4 has exactly one 3-divisible invariant
# factor, to exactly 3-adic valuation one (rank_F3=3 and a minor is 12).
# All other boundaries have full rational rank already modulo three, using
# exactness rank bounds from B_(k-1) B_k = 0 and the chain dimensions.

# Independent signed simplicial Lefschetz trace, using the actual faces.
def fixed_simplex_trace(a, q):
    reduced_lefschetz = -1
    for k in range(1,9):
        signed_fixed = 0
        for face in BY_SIZE[k]:
            im = [(a + q*x)%P for x in face]
            if tuple(sorted(im)) == face:
                signed_fixed += orientation_sign(im)
        reduced_lefschetz += (-1)**(k-1)*signed_fixed
    # Prior nonequivariant homology is in degree 3 rationally;
    # thus this sign converts reduced Lefschetz to degree-three trace.
    return -reduced_lefschetz

assert fixed_simplex_trace(0,1) == 35
assert {fixed_simplex_trace(a,1) for a in range(1,17)} == {1}
assert {fixed_simplex_trace(a,q) for q in Q if q not in (1,16) for a in range(17)} == {-1}
assert {fixed_simplex_trace(a,16) for a in range(17)} == {3}
assert sum(fixed_simplex_trace(a,q) for a,q in GROUP) == 0

print('PALEY17_AFFINE_3LOCAL_QUOTIENT_PASS')
print('faces_by_dimension', [len(BY_SIZE[k]) for k in range(1,9)])
print('group_order', len(GROUP), 'quadratic_residues', list(Q))
print('surviving_oriented_orbits_by_dimension', [len(REPS[k]) for k in range(1,9)])
print('orientation_reversing_orbits_by_dimension', [len(REMOVED[k]) for k in range(1,9)])
print('boundary_ranks_mod3_by_source_simplex_size_2_to_8', [rank3[k] for k in range(2,9)])
print('degree3_to_degree2_boundary_4x9', B4)
print('4x4_minor_columns_0_1_2_3_determinant', determinant(minor))
print('quotient_reduced_Z_localized_at_3_homology', 'H2=Z/3; all other degrees=0')
print('rational_H3_traces', {'identity':35,'nonzero_translations':1,'nontrivial_multipliers_except_minus1':-1,'minus1':3})
print('full_affine_quotient_reduced_rational_homology', 'zero')
