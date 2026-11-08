#!/usr/bin/env python3
"""Exact-rational checks for the six-state Radau IIA pure-birth formula.

No third-party packages needed. Proof of the infinite assertions is in RESULT.md.
"""
from fractions import Fraction as F


def mul(A, B):
    m, p, n = len(A), len(B), len(B[0])
    assert len(A[0]) == p
    return [[sum((A[i][k] * B[k][j] for k in range(p)), F(0))
             for j in range(n)] for i in range(m)]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def inv(A):
    n = len(A)
    B = [A[i][:] + eye(n)[i] for i in range(n)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if B[i][j]), None)
        assert pivot is not None
        B[j], B[pivot] = B[pivot], B[j]
        d = B[j][j]
        B[j] = [v / d for v in B[j]]
        for i in range(n):
            if i != j:
                factor = B[i][j]
                B[i] = [v - factor * w for v, w in zip(B[i], B[j])]
    return [row[n:] for row in B]


def radau_on_birth(h):
    n = 6
    L = [[F(0) for j in range(n)] for i in range(n)]
    for i in range(n - 1):
        L[i][i] = F(1)
        L[i][i + 1] = F(-1)
    L2 = mul(L, L)
    M = [[h*h*L2[i][j] + 4*h*L[i][j] + 6*F(i == j)
          for j in range(n)] for i in range(n)]
    N = [[6*F(i == j) - 2*h*L[i][j] for j in range(n)]
         for i in range(n)]
    return mul(N, inv(M))


def coefficients(h):
    d = h*h + 4*h + 6
    return [
        2*(3-h)/d,
        2*h*(18+6*h-h*h)/d**2,
        2*h*h*(h+3)*(18+12*h-h*h)/d**3,
        2*h**3*(108+216*h+108*h*h+12*h**3-h**4)/d**4,
        2*h**4*(108+540*h+540*h*h+180*h**3+15*h**4-h**5)/d**5,
    ]


def absorber(h, j):
    # j is the number of transient states ahead, from 1 to 5.
    d = h*h + 4*h + 6
    polynomials = [
        h*(h+6),
        h**2*(h*h+12*h+18),
        h**3*(h**3+18*h*h+54*h+36),
        h**4*(h**4+24*h**3+108*h*h+144*h+36),
        h**5*(h**5+30*h**4+180*h**3+360*h*h+180*h-72),
    ]
    return polynomials[j-1] / d**j


def reference_matrix(h):
    c = coefficients(h)
    P = [[F(0) for j in range(6)] for i in range(6)]
    for i in range(5):
        for j in range(i, 5):
            P[i][j] = c[j-i]
        P[i][5] = absorber(h, 5-i)
    P[5][5] = F(1)
    return P


def series_coefficients():
    # (1 - 2z/3 + z^2/6) r(z) = 1 + z/3.
    a = []
    for n in range(6):
        v = (F(1) if n == 0 else F(1, 3) if n == 1 else F(0))
        if n > 0: v += F(2, 3)*a[n-1]
        if n > 1: v -= F(1, 6)*a[n-2]
        a.append(v)
    return a


def main():
    assert series_coefficients() == [F(1),F(1),F(1,2),F(1,6),F(1,36),F(-1,108)]
    samples = [F(0),F(1,1000),F(1,100),F(1,10),F(1,4),F(13,50),
               F(1,2),F(1),F(3,2),F(2),F(3),F(4),F(5),F(11)]
    num = 0
    for h in samples:
        A = radau_on_birth(h)
        B = reference_matrix(h)
        for i in range(6):
            assert sum(A[i]) == 1
            for j in range(6):
                assert A[i][j] == B[i][j], (h,i,j,A[i][j],B[i][j])
                num += 1
    def p(h): return h**5 + 30*h**4 + 180*h**3 + 360*h*h + 180*h - 72
    assert p(F(0)) < 0 and p(F(1,4)) < 0 and p(F(13,50)) > 0
    assert radau_on_birth(F(1,10))[0][5] < 0
    assert all(x>=0 for row in radau_on_birth(F(1)) for x in row)
    assert all(x>=0 for row in radau_on_birth(F(3)) for x in row)
    assert radau_on_birth(F(4))[0][0] < 0
    print(f'VERIFY_OK: {len(samples)} exact-matrix samples, {num} entry equalities,')
    print('14 exact row-sum equalities; Maclaurin coefficients;')
    print('positive-root bracket; four exact sign witnesses.')

if __name__ == '__main__':
    main()
