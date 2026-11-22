#!/usr/bin/env python3
"""Exact, dependency-free Hesse flex--line graph Jacobian verification.

Run: python3 verify_hesse.py
All integer and modular computations are deterministic.
"""
from itertools import product, combinations
from math import prod

P = list(product(range(3), repeat=2))
LINES = []
for slope in range(4):
    for a in range(3):
        q = tuple(i for i, (x, y) in enumerate(P)
                  if (x == a if slope == 3 else (y - slope*x) % 3 == a))
        assert len(q) == 3
        LINES.append(q)
assert len(LINES) == len(set(LINES)) == 12
# Geometrically independent collinearity characterization: a triple sums to zero.
triples = {tuple(c) for c in combinations(range(9), 3)
           if all(sum(P[i][j] for i in c) % 3 == 0 for j in range(2))}
assert triples == set(LINES)

B = [[int(i in t) for t in LINES] for i in range(9)]
assert all(sum(row) == 4 for row in B)
assert all(sum(B[i][j] for i in range(9)) == 3 for j in range(12))
assert all(sum(B[i][k]*B[j][k] for k in range(12)) == (4 if i == j else 1)
           for i in range(9) for j in range(9))

L = [[0]*21 for _ in range(21)]
for i in range(9):
    for j in range(12):
        if B[i][j]:
            L[i][i] += 1
            L[9+j][9+j] += 1
            L[i][9+j] -= 1
            L[9+j][i] -= 1
assert all(sum(row) == 0 for row in L)
assert sum(-L[i][j] for i in range(9) for j in range(9,21)) == 36


def minor(remove):
    return [[L[i][j] for j in range(21) if j != remove]
            for i in range(21) if i != remove]


def det_bareiss(m):
    """Fraction-free elimination; exact determinant over the integers."""
    a = [row[:] for row in m]
    n = len(a)
    if n == 1: return a[0][0]
    prev, sign = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivotrow = next((i for i in range(k+1, n) if a[i][k]), None)
            if pivotrow is None: return 0
            a[k],a[pivotrow] = a[pivotrow],a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                t = a[i][j]*pivot-a[i][k]*a[k][j]
                assert t % prev == 0
                a[i][j] = t//prev
            a[i][k] = 0
        prev = pivot
    return sign*a[-1][-1]


def valuation(x,p,k):
    if x == 0: return k
    i = 0
    while x % p == 0:
        x //= p
        i += 1
    return min(i,k)


def local_smith(m,p=3,k=6):
    """Smith diagonal valuations via invertible row/column operations in Z/p^k.

    At each step choose a pivot of minimum p-valuation, scale its row by
    a unit, then use elementary operations to clear the pivot column/row.
    Any remaining valuation k would be ambiguous, so callers reject it.
    """
    modulus = p**k
    a = [[x % modulus for x in row] for row in m]
    n = len(a)
    ans = []
    for j in range(n):
        e,i0,j0 = min((valuation(a[i][h],p,k),i,h)
                      for i in range(j,n) for h in range(j,n))
        assert e < k, 'Precision too small for a complete Smith result'
        a[j],a[i0] = a[i0],a[j]
        for row in a: row[j],row[j0] = row[j0],row[j]
        pe = p**e
        u = a[j][j]//pe
        inv = pow(u,-1,modulus)
        a[j] = [(inv*x) % modulus for x in a[j]]
        assert a[j][j] == pe
        for i in range(j+1,n):
            assert a[i][j] % pe == 0
            c = a[i][j]//pe
            a[i] = [(x-c*y)%modulus for x,y in zip(a[i],a[j])]
            assert a[i][j] == 0
        for h in range(j+1,n):
            assert a[j][h] % pe == 0
            c = a[j][h]//pe
            for i in range(n): a[i][h] = (a[i][h]-c*a[i][j])%modulus
            assert a[j][h] == 0
        ans.append(e)
    return ans

EXPECTED_VALS = [0]*12 + [1] + [2]*4 + [3]*3
for sink in (0, 4, 8, 9, 15, 20):
    m = minor(sink)
    vals = local_smith(m)
    assert vals == EXPECTED_VALS,(sink,vals)
    determinant = det_bareiss(m)
    assert determinant == 3**18, (sink,determinant)
    assert prod(3**v for v in vals) == determinant
# From BB^t=3I_9+J_9, nonzero Laplacian eigenvalues are
# 7 (once), 3 (three times), and roots of u^2-7u+9 (each eight times).
assert (7 * 3**3 * 9**8)//21 == 3**18
assert 36-21+1 == 16
print('HESSE_3_PRIMARY_COMPONENT_GROUP_VERIFIED_OK')
print('SNF 1^12 3^1 9^4 27^3; tree_count=3^18; stable_genus=16')
