#!/usr/bin/env python3
"""Exact simplicial boundary and affine character check for the Paley-17 clique complex.
Python standard library only; each assertion is independently reproducible.
"""
from itertools import combinations, permutations
from collections import Counter

P = 17
Q = frozenset(pow(x, 2, P) for x in range(1, P))
VERTICES = [(i,) for i in range(P)]
EDGES = [e for e in combinations(range(P), 2) if (e[1]-e[0]) % P in Q]
ESET = set(EDGES)
TRIANGLES = [f for f in combinations(range(P), 3)
             if all(e in ESET for e in combinations(f, 2))]
assert Q == frozenset([1, 2, 4, 8, 9, 13, 15, 16])
assert (len(VERTICES), len(EDGES), len(TRIANGLES)) == (17, 68, 68)
assert not any(all(e in ESET for e in combinations(face, 2))
               for face in combinations(range(P), 4))

# Independent full-automorphism certificate. Fix a vertex using translations.
# Its eight neighbors have eight distinct non-neighbor incidence signatures,
# hence each neighbor permutation has at most one extension.
NBR = sorted(Q)
OTHER = sorted(set(range(P))-set(Q)-{0})
SIGNATURE = {x: frozenset(q for q in NBR if (x-q)%P in Q) for x in OTHER}
assert len(set(SIGNATURE.values())) == 8
INVERSE_SIGNATURE = {sig:x for x,sig in SIGNATURE.items()}
FIX_ZERO = 0
for candidate in permutations(NBR):
    m = dict(zip(NBR, candidate));m[0]=0
    if any(((u-v)%P in Q) != ((m[u]-m[v])%P in Q)
           for u,v in combinations(NBR,2)):
        continue
    for x in OTHER:
        tgt = frozenset(m[y] for y in SIGNATURE[x])
        if tgt not in INVERSE_SIGNATURE:break
        m[x]=INVERSE_SIGNATURE[tgt]
    if len(m)!=P or len(set(m.values())) != P:
        continue
    if all(((u-v)%P in Q) == ((m[u]-m[v])%P in Q)
           for u,v in combinations(range(P),2)):
        FIX_ZERO += 1
assert FIX_ZERO == 8, FIX_ZERO
assert 17*FIX_ZERO == 136

edge_number = {e: i for i, e in enumerate(EDGES)}
B = [[0] * len(TRIANGLES) for _ in EDGES]
for j, (i, k, l) in enumerate(TRIANGLES):
    B[edge_number[(k, l)]][j] += 1
    B[edge_number[(i, l)]][j] -= 1
    B[edge_number[(i, k)]][j] += 1
assert all(B[r][j] in (-1, 0, 1) for r in range(68) for j in range(68))

# Every C_1 cycle is determined integrally by its coefficients on
# nontree edges. The following 16 row indices form a spanning tree.
TREE_ROWS = (0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 13, 17, 19, 30, 42)
PIVOT_COLUMNS = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
    29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44,
    45, 46, 47, 49, 52, 56, 59, 61)
assert len(TREE_ROWS) == 16 and len(set(TREE_ROWS)) == 16
assert len(PIVOT_COLUMNS) == 52 and len(set(PIVOT_COLUMNS)) == 52
parent = list(range(P))
def find(x):
    while parent[x] != x:
        x = parent[x]
    return x
for e_i in TREE_ROWS:
    u, v = EDGES[e_i]
    assert find(u) != find(v)
    parent[find(u)] = find(v)
assert len({find(i) for i in range(P)}) == 1

NON_TREE = [i for i in range(len(EDGES)) if i not in TREE_ROWS]
MINOR = [[B[row][col] for col in PIVOT_COLUMNS] for row in NON_TREE]

def bareiss_det(mat):
    """Fraction-free exact determinant with row pivoting, over integers."""
    a = [list(row) for row in mat]
    n = len(a)
    assert n > 0 and all(len(row) == n for row in a)
    sign = 1
    last_pivot = 1
    for k in range(n-1):
        if a[k][k] == 0:
            target = next((i for i in range(k+1, n) if a[i][k]), None)
            if target is None:
                return 0
            a[k], a[target] = a[target], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, n):
            a_i_k = a[i][k]
            for j in range(k+1, n):
                num = a[i][j] * pivot - a_i_k * a[k][j]
                assert num % last_pivot == 0
                a[i][j] = num // last_pivot
            a[i][k] = 0
        last_pivot = pivot
    return sign * a[n-1][n-1]

minor_det = bareiss_det(MINOR)
assert minor_det == 1, minor_det
# The unimodular boundary submatrix is an integral certificate that
# H_1=0 and H_2 is free of rank 68-52=16.
assert len(TRIANGLES) - len(NON_TREE) == 16

def orientation_sign(face):
    sign = 1
    for i in range(len(face)):
        for j in range(i+1, len(face)):
            if face[i] > face[j]: sign = -sign
    return sign

def signed_trace(faces, a, b):
    total = 0
    for face in faces:
        mapped = tuple((a*x + b) % P for x in face)
        if set(mapped) == set(face):
            total += orientation_sign(mapped)
    return total

counts = Counter()
for a in sorted(Q):
    for b in range(P):
        tr0 = signed_trace(VERTICES, a, b)
        tr1 = signed_trace(EDGES, a, b)
        tr2 = signed_trace(TRIANGLES, a, b)
        homology_character = tr0-tr1+tr2-1
        fixed_vertices = sum(1 for i in range(P) if (a*i+b)%P == i)
        assert homology_character == fixed_vertices-1
        if a == 1 and b == 0:
            assert (tr0, tr1, tr2, homology_character) == (17,68,68,16)
            category = 'identity'
        elif a == 1:
            assert (tr0,tr1,tr2,homology_character) == (0,0,0,-1)
            category = 'nontrivial_translation'
        else:
            assert tr0 == 1 and homology_character == 0
            category = 'nontranslation_affine'
        counts[category] += 1
assert counts == dict(identity=1, nontrivial_translation=16, nontranslation_affine=119)

# Additional integral obstruction for the involution x -> -x.
# Since the 52-column minor has determinant one, the 16 remaining
# triangle coordinates form an integral basis for the cycle lattice.
# Reconstruct that basis modulo two and compute the involution there.
FREES = [i for i in range(68) if i not in set(PIVOT_COLUMNS)]
assert len(FREES) == 16
N = 52
INV_WORK = [[x % 2 for x in row] + [int(i == j) for j in range(N)]
            for i, row in enumerate(MINOR)]
for col in range(N):
    target = next(i for i in range(col, N) if INV_WORK[i][col])
    INV_WORK[col], INV_WORK[target] = INV_WORK[target], INV_WORK[col]
    for i in range(N):
        if i != col and INV_WORK[i][col]:
            INV_WORK[i] = [x^y for x,y in zip(INV_WORK[i], INV_WORK[col])]
assert all(INV_WORK[i][j] == int(i == j)
           for i in range(N) for j in range(N))
INVERSE = [row[N:] for row in INV_WORK]
KERNEL_BASIS_MOD2 = []
for free in FREES:
    vector = [0] * 68
    vector[free] = 1
    rhs = [B[r][free] % 2 for r in NON_TREE]
    for i, pivot in enumerate(PIVOT_COLUMNS):
        vector[pivot] = sum(x*y for x,y in zip(INVERSE[i],rhs)) % 2
    assert all(sum(B[r][j]*vector[j] for j in range(68)) % 2 == 0
               for r in range(68))
    KERNEL_BASIS_MOD2.append(vector)
triangle_index = {face: i for i, face in enumerate(TRIANGLES)}
involuted_triangle = [triangle_index[tuple(sorted((-x)%P for x in face))]
                      for face in TRIANGLES]
INV_ACTION_COLUMNS = []
for basis_vector in KERNEL_BASIS_MOD2:
    moved = [0] * 68
    for j, value in enumerate(basis_vector):
        if value: moved[involuted_triangle[j]] ^= 1
    INV_ACTION_COLUMNS.append([moved[f] for f in FREES])
A_PLUS_ID = [[INV_ACTION_COLUMNS[j][i] ^ int(i == j)
              for j in range(16)] for i in range(16)]
rank = 0
for col in range(16):
    target = next((i for i in range(rank, 16) if A_PLUS_ID[i][col]), None)
    if target is None: continue
    A_PLUS_ID[rank], A_PLUS_ID[target] = A_PLUS_ID[target], A_PLUS_ID[rank]
    for i in range(16):
        if i != rank and A_PLUS_ID[i][col]:
            A_PLUS_ID[i] = [x^y for x,y in zip(A_PLUS_ID[i],A_PLUS_ID[rank])]
    rank += 1
assert rank == 8, rank
# The involution has trace zero over Q, so both eigensublattices
# have rank 8. Their sum contains 2L. Its F_2 image is annihilated
# by (u-1), which has rank 8. Conversely L/(L^++L^-) embeds into
# L^+/2L^+ via [z] -> (1+u)z mod 2L^+, so its F_2 dimension <= 8.
# Thus its exact structure is (Z/2)^8.
print('Paley-17 clique complex faces:', (17,68,68), 'and no 3-simplices')
print('Spanning tree edges:', len(TREE_ROWS), '; complementary cycle edges:', len(NON_TREE))
print('Exact 52x52 boundary minor determinant:', minor_det)
print('Integral reduced homology: H_2=Z^16, H_1=0, others zero')
print('Full graph automorphism group order:', 17*FIX_ZERO, '(independent fixed-vertex backtracking)')
print('Affine group order:', sum(counts.values()), '; categories:', dict(counts))
print('H_2 character: identity=16, nonidentity translations=-1, other affine maps=0')
print('H_2(Q) is the 17-point augmentation representation; irreducible over Q')
print('Involution x -> -x: rank_F2(u+1) =',rank,'; integral eigensum quotient = (Z/2)^8')
print('PALEY17_AFFINE_HOMOLOGY_CHARACTER_PASS')
