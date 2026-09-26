#!/usr/bin/env python3
"""Verifier for lane-372 M8-/M9+ realizability certificate (stdlib only).
Run: python3 verify_m9.py  -> prints VERIFY_OK on success.
Checks (exact Fractions):
 1. M8- = Vamos relaxed at 5678: dependent 4-sets of first 8 columns are
    exactly {1234,1256,3456,3478}; 5678 is a basis (det != 0).
 2. Points are distinct, no two proportional, no three affinely collinear.
 3. M9+: column 9 lies in affine span of {5,6,7,8} (coeffs sum to 1);
    no 4-set containing 9 is dependent (9 generic in that plane);
    full dependent list on 9 points = the same four planes.
 4. Contraction M9+/9 realized over Q by projecting from column 9
    (row-reduce 9 to e4, drop last row): rank 3 exhibited.
 5. Chirotope: every basis determinant nonzero with recorded sign split.
"""
from fractions import Fraction
from itertools import combinations

# Affine points p1..p9 in Q^3; homogeneous columns (x,y,z,1).
P = {
    1: (1, 2, 0), 2: (2, 1, 0), 3: (0, 0, 0), 4: (1, 0, 0),
    5: (2, 0, 1), 6: (0, 0, 3), 7: (-1, 1, 1), 8: (0, 1, 1),
    9: (7, 11, 13),
}
OLD_PLANES = {(1, 2, 3, 4), (1, 2, 5, 6), (3, 4, 5, 6), (3, 4, 7, 8)}

def H(c):
    x, y, z = P[c]
    return [Fraction(x), Fraction(y), Fraction(z), Fraction(1)]

def det4(q, cols=None):
    A = [[(cols[c] if cols else H(c))[r] for c in q] for r in range(4)]
    B = [row[:] for row in A]
    s = Fraction(1)
    for i in range(4):
        piv = next((r for r in range(i, 4) if B[r][i] != 0), None)
        if piv is None:
            return Fraction(0)
        if piv != i:
            B[i], B[piv] = B[piv], B[i]
            s = -s
        for r in range(i + 1, 4):
            f = B[r][i] / B[i][i]
            for c in range(i, 4):
                B[r][c] -= f * B[i][c]
    return s * B[0][0] * B[1][1] * B[2][2] * B[3][3]

# 1. M8- dependent 4-sets
deps8 = {s for s in combinations(range(1, 9), 4) if det4(s) == 0}
assert deps8 == OLD_PLANES, f"M8- planes wrong: {sorted(deps8)}"
assert det4((5, 6, 7, 8)) == 2, "5678 must be a basis with det 2"
assert len(deps8) == 4 and len(list(combinations(range(1, 9), 4))) == 70

# 2. simplicity: distinct points, no collinear triple
assert len(set(P[c] for c in range(1, 10))) == 9
def sub(a, b): return (a[0]-b[0], a[1]-b[1], a[2]-b[2])
def cross(u, v): return (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])
coll = [t for t in combinations(range(1, 10), 3)
        if cross(sub(P[t[1]], P[t[0]]), sub(P[t[2]], P[t[0]])) == (0, 0, 0)]
assert coll == [], f"collinear triples: {coll}"

# 3. principal extension geometry: 9 in affine span of 5,6,7,8
rows = [[Fraction(2), Fraction(0), Fraction(-1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(1)],
        [Fraction(1), Fraction(3), Fraction(1), Fraction(1)],
        [Fraction(1), Fraction(1), Fraction(1), Fraction(1)]]
rhs = [Fraction(7), Fraction(11), Fraction(13), Fraction(1)]
A = [r[:] + [rhs[i]] for i, r in enumerate(rows)]
for i in range(4):
    piv = next(r for r in range(i, 4) if A[r][i] != 0)
    A[i], A[piv] = A[piv], A[i]
    d = A[i][i]
    A[i] = [x / d for x in A[i]]
    for r in range(4):
        if r != i and A[r][i] != 0:
            f = A[r][i]
            A[r] = [a - f * b for a, b in zip(A[r], A[i])]
lam = [A[i][4] for i in range(4)]
assert sum(lam) == 1, lam
got = [sum(lam[j] * Fraction(P[5+j][k]) for j in range(4)) for k in range(3)]
assert got == [Fraction(7), Fraction(11), Fraction(13)], (got, lam)
deps9 = {s for s in combinations(range(1, 10), 4) if det4(s) == 0}
assert deps9 == OLD_PLANES, f"M9+ extra deps: {sorted(deps9 - OLD_PLANES)}"
assert all(9 not in s for s in deps9)
assert len(list(combinations(range(1, 10), 4))) == 126

# 4. contraction M9+/9 over Q: row-reduce col 9 to e4, drop row 4
M = {c: H(c)[:] for c in range(1, 10)}
order = [9, 1, 2, 3]
R = [M[c][:] for c in order]  # columns as vectors; build matrix rows
# {9,1,2,3} is a basis, so projecting from column 9 is valid over Q.
assert det4((9, 1, 2, 3)) != 0, "need {9,1,2,3} independent for projection"
# project: drop 4th coordinate of every column expressed in this basis:
# coordinates of column c in new basis = solution of mat_full * x = col; use
# full 4x4 change-of-basis inverse applied to each column.
import copy
B4 = [[H(c)[r] for c in order] for r in range(4)]  # original matrix of basis cols
# invert B4
N = 4
aug = [B4[r][:] + [Fraction(1) if r == k else Fraction(0) for k in range(N)] for r in range(N)]
for i in range(N):
    piv = next(r for r in range(i, N) if aug[r][i] != 0)
    aug[i], aug[piv] = aug[piv], aug[i]
    d = aug[i][i]
    aug[i] = [x / d for x in aug[i]]
    for r in range(N):
        if r != i and aug[r][i] != 0:
            f = aug[r][i]
            aug[r] = [a - f * b for a, b in zip(aug[r], aug[i])]
inv = [row[N:] for row in aug]
proj = {}
for c in range(1, 10):
    v = H(c)
    w = [sum(inv[i][k] * v[k] for k in range(4)) for i in range(4)]
    assert (w[0] == Fraction(1)) if c == 9 else True, (c, w)
    proj[c] = w[1:]
def det3(q):
    A3 = [[proj[c][r] for c in q] for r in range(3)]
    B3 = [row[:] for row in A3]
    s = Fraction(1)
    for i in range(3):
        piv = next((r for r in range(i, 3) if B3[r][i] != 0), None)
        if piv is None:
            return Fraction(0)
        if piv != i:
            B3[i], B3[piv] = B3[piv], B3[i]
            s = -s
        for r in range(i + 1, 3):
            f = B3[r][i] / B3[i][i]
            for cc in range(i, 3):
                B3[r][cc] -= f * B3[i][cc]
    return s * B3[0][0] * B3[1][1] * B3[2][2]
bases3 = [t for t in combinations([c for c in range(1, 10) if c != 9], 3) if det3(t) != 0]
assert len(bases3) > 0, "contraction must have rank 3"
assert det3((1, 5, 7)) != 0, "witness triple {1,5,7} a basis of M9+/9"

# 5. chirotope sign split on M9+
signs = [1 if det4(s) > 0 else -1 for s in combinations(range(1, 10), 4) if det4(s) != 0]
assert len(signs) == 126 - 4
print(f"bases={len(signs)} pos={sum(1 for x in signs if x > 0)} "
      f"neg={sum(1 for x in signs if x < 0)} planes={len(deps9)}")
print(f"affine coeffs l5..l8 = {[str(x) for x in lam]}")
print("VERIFY_OK")
