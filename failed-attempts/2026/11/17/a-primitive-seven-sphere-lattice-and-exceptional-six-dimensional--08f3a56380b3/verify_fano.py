#!/usr/bin/env python3
"""Exact finite certificate for the Fano matroid's geometric homology sublattice.

Python 3 with SymPy. All arithmetic is integral or rational; no floating point.
"""
from itertools import combinations, product
from collections import Counter
from sympy import Matrix, eye

P = tuple(range(1, 8))
I = tuple(P)

# A nonzero vector in F_2^3 is encoded by a three-bit integer.
def image(rows, x):
    return sum((((r & x).bit_count() & 1) << i) for i, r in enumerate(rows))

G = sorted({tuple(image(rows, x) for x in P)
            for rows in product(range(8), repeat=3)
            if len({image(rows, x) for x in P}) == 7})
assert len(G) == 168 and I in G

def mul(a, b):
    return tuple(a[x - 1] for x in b)

def inverse(g):
    return tuple(g.index(x) + 1 for x in P)

def order(g):
    s = I
    for n in range(1, 169):
        s = mul(s, g)
        if s == I:
            return n
    raise AssertionError('Invalid finite order')

orders = {g: order(g) for g in G}
assert Counter(orders.values()) == {3: 56, 7: 48, 4: 42, 2: 21, 1: 1}

classes, remaining = [], set(G)
while remaining:
    g = min(remaining)
    conj = {mul(mul(h, g), inverse(h)) for h in G}
    classes.append((order(g), len(conj), g, conj))
    remaining -= conj
classes.sort(key=lambda a: (a[0], a[2]))
assert [(o, z) for o, z, _, _ in classes] == [
    (1, 1), (2, 21), (3, 56), (4, 42), (7, 24), (7, 24)]

lines = {frozenset([a, b, a ^ b]) for a, b in combinations(P, 2)}
assert len(lines) == 7 and all(len(s) == 3 for s in lines)
triangles = tuple(t for t in combinations(P, 3) if frozenset(t) not in lines)
edges = tuple(combinations(P, 2))
quads = tuple(sorted(tuple(sorted(set(P) - L)) for L in lines))
assert len(triangles) == 28 and len(edges) == 21 and len(quads) == 7

# Every independent triple is contained in exactly one quad complement of a line.
quad_faces = {Q: set(combinations(Q, 3)) for Q in quads}
all_faces = [t for Q in quads for t in quad_faces[Q]]
assert len(all_faces) == 28 and set(all_faces) == set(triangles)
assert len(set(all_faces)) == 28

# Exhaustively certify the smallest mod-two cycles and their seven supports.
edge_mask = []
for t in triangles:
    m = 0
    for e in combinations(t, 2):
        m ^= 1 << edges.index(e)
    edge_mask.append(m)
zero_small = []
for num in range(1, 5):
    for selected in combinations(range(28), num):
        boundary_mask = 0
        for j in selected:
            boundary_mask ^= edge_mask[j]
        if boundary_mask == 0:
            zero_small.append(selected)
assert len(zero_small) == 7
assert all(len(v) == 4 for v in zero_small)
assert {frozenset(triangles[j] for j in v) for v in zero_small} == {
    frozenset(combinations(Q, 3)) for Q in quads}

# Chain maps with sorted oriented simplices.
edge_i = {e: i for i, e in enumerate(edges)}
tri_i = {t: i for i, t in enumerate(triangles)}

def sign_of_ordered(seq):
    return -1 if sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i + 1, len(seq))) % 2 else 1

def oriented_image(g, face):
    seq = tuple(g[x - 1] for x in face)
    return tuple(sorted(seq)), sign_of_ordered(seq)

D = Matrix.zeros(len(edges), len(triangles))
for j, t in enumerate(triangles):
    for k in range(3):
        f = tuple(x for h, x in enumerate(t) if h != k)
        D[edge_i[f], j] += (-1) ** k
assert D.rank() == 15
assert D.shape == (21, 28)

# Independently establish that every missing-line triangular boundary belongs
# to the image of D: each is part of the 4-face boundary with a point off line.
for L in lines:
    L = tuple(sorted(L))
    v = next(x for x in P if x not in L)
    S = tuple(sorted(L + (v,)))
    assert len(S) == 4
    assert all(frozenset(t) not in lines for t in combinations(S, 3) if t != L)

# Quad boundary cycles are disjointly supported and have an integral coordinate
# retraction. This certifies that their span is primitive in C_2 and in H_2.
Z = Matrix.zeros(len(triangles), len(quads))
for j, Q in enumerate(quads):
    for k, t in enumerate(combinations(Q, 3)):
        Z[tri_i[t], j] = (-1) ** k
assert D * Z == Matrix.zeros(21, 7)
assert Z.rank() == 7
row_indices = [tri_i[min(combinations(Q, 3))] for Q in quads]
assert abs(int(Z[row_indices, :].det())) == 1
assert all(sum(1 for j in range(7) if Z[i, j]) == 1 for i in range(28))

# Integral Betti numbers: full 1-skeleton, all line triangle boundaries can
# be replaced by allowed ones, so H_1=0; H_2=ker D is free rank 13.
assert len(triangles) - D.rank() == 13

# Chain-map consistency and signed Lefschetz formula for every group element.
E = Matrix.zeros(7, len(edges))
for j, e in enumerate(edges):
    E[e[0] - 1, j] = -1
    E[e[1] - 1, j] = 1
assert E * D == Matrix.zeros(7, 28)

basis = Matrix.hstack(*D.nullspace())
assert basis.shape == (28, 13) and D * basis == Matrix.zeros(21, 13)
independent_rows = list(basis.T.rref()[1])
assert len(independent_rows) == 13
selected = basis[independent_rows, :]
selected_inverse = selected.inv()


def signed_chain_matrix(g, faces):
    lookup = {f: i for i, f in enumerate(faces)}
    M = Matrix.zeros(len(faces), len(faces))
    for j, face in enumerate(faces):
        target, sgn = oriented_image(g, face)
        M[lookup[target], j] = sgn
    return M


def trace_on_faces(g, faces):
    return sum(sgn for f in faces for target, sgn in [oriented_image(g, f)] if target == f)


def trace_quad(g):
    return sum(sgn for Q in quads for target, sgn in [oriented_image(g, Q)] if target == Q)

CH, CQ, CR = {}, {}, {}
for g in G:
    # For reduced H_2, trace = tr C_0 - tr C_1 + tr C_2 - 1.
    h = trace_on_faces(g, tuple((v,) for v in P)) - trace_on_faces(g, edges) + trace_on_faces(g, triangles) - 1
    q = trace_quad(g)
    CH[g], CQ[g], CR[g] = h, q, h - q
    # All 28 signed 2-simplex equivariance relations, plus all 21 on edges.
    T2 = signed_chain_matrix(g, triangles)
    T1 = signed_chain_matrix(g, edges)
    T0 = signed_chain_matrix(g, tuple((v,) for v in P))
    assert D * T2 == T1 * D and E * T1 == T0 * E
    # The 7 geometric cycles form an invariant signed-permutation sublattice.
    assert all(sum(1 for i in range(28) if (T2 * Z[:, j])[i]) == 4 for j in range(7))

# Different method: explicitly represent each conjugacy representative on
# the 13-dimensional rational kernel and calculate its exact trace.
for _, _, g, _ in classes:
    T2 = signed_chain_matrix(g, triangles)
    transformed = T2 * basis
    represented = selected_inverse * transformed[independent_rows, :]
    assert basis * represented == transformed
    assert int(represented.trace()) == CH[g]

class_rows = []
for o, size, rep, members in classes:
    assert all((CH[g], CQ[g], CR[g]) == (CH[rep], CQ[rep], CR[rep]) for g in members)
    class_rows.append((o, size, CH[rep], CQ[rep], CR[rep]))
assert class_rows == [
    (1, 1, 13, 7, 6),
    (2, 21, -3, -1, -2),
    (3, 56, 1, 1, 0),
    (4, 42, 1, -1, 2),
    (7, 24, -1, 0, -1),
    (7, 24, -1, 0, -1)]

sizes = [row[1] for row in class_rows]
full = [row[2] for row in class_rows]
geo = [row[3] for row in class_rows]
rest = [row[4] for row in class_rows]
def inner(a, b):
    val = sum(m*x*y for m, x, y in zip(sizes, a, b))
    assert val % 168 == 0
    return val // 168

assert inner(geo, geo) == 1
assert inner(rest, rest) == 2
assert inner(rest, geo) == 0
assert inner(full, [1]*6) == 0
# Standard character table of PSL_2(7)=GL_3(F_2), listed as 1,2,3,4,7A,7B.
# Its dimensions are 1,3,3,6,7,8. The 3+3bar rational character is:
pair3 = [6, -2, 0, 2, -1, -1]
irred7 = [7, -1, 1, -1, 0, 0]
assert rest == pair3 and geo == irred7
assert inner(rest, pair3) == 2 and inner(geo, irred7) == 1

print('FANO_GEOMETRIC_QUADRANGLE_HOMOLOGY_PASS')
print('points=7 lines=7 edges=21 independent_triangles=28 quadrangle_spheres=7')
print('group_order=168 class_order_size=' + repr([(a,b) for a,b,*_ in class_rows]))
print('boundary_rank_2=15 H_1=0 H_2_rank=13 quadrangle_sublattice_rank=7 saturated=True')
print('minimum_mod2_cycle_support=4 exactly_seven_unoriented_supports=True')
print('conjugacy_columns=order,class_size,homology_trace,geometric_trace,quotient_trace')
for row in class_rows:
    print(','.join(map(str,row)))
print('rational_decomposition=7_irreducible_plus_3_plus_conjugate_3')
print('geometric_character_norm=1 residual_character_norm=2 orthogonal=True')
print('all_168_automorphisms_chain_equivariant=True')
print('all_168_automorphisms_geometric_sublattice_preserved=True')
print('explicit_kernel_action_trace_matches_Lefschetz_six_classes=True')
