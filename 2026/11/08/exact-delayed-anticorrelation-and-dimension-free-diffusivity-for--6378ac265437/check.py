#!/usr/bin/env python3
"""Exact finite-dimensional checks for affine observables of a specified piecewise map.

No third-party packages required. Infinite-dimensional and limit statements are
proved in the accompanying paper, not by this finite checker.
"""
from fractions import Fraction as Q


def affine_matrix(m):
    assert m >= 2
    a = [[Q(0) for _ in range(m)] for _ in range(m)]
    a[0][0], a[0][1] = Q(1, 4), Q(1, 2)
    for i in range(1, m-1):
        a[i][i], a[i][i+1] = Q(1, 2), Q(1, 2)
    a[-1][0], a[-1][-1] = Q(-1, 4), Q(1, 2)
    return a


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def eye(m):
    return [[Q(i == j) for j in range(m)] for i in range(m)]


def det(a):
    m = len(a)
    b = [row[:] for row in a]
    out = Q(1)
    for j in range(m):
        pivot = next((i for i in range(j, m) if b[i][j] != 0), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            b[pivot], b[j] = b[j], b[pivot]
            out = -out
        p = b[j][j]
        out *= p
        for i in range(j+1, m):
            if b[i][j]:
                fac = b[i][j] / p
                for k in range(j+1, m):
                    b[i][k] -= fac*b[j][k]
                b[i][j] = Q(0)
    return out


def solve(a, rhs):
    m = len(a)
    b = [a[i][:]+[rhs[i]] for i in range(m)]
    for j in range(m):
        p = next(i for i in range(j, m) if b[i][j])
        b[j], b[p] = b[p], b[j]
        c = b[j][j]
        for k in range(j, m+1):
            b[j][k] /= c
        for i in range(m):
            if i != j:
                fac = b[i][j]
                for k in range(j, m+1):
                    b[i][k] -= fac * b[j][k]
    return [b[i][m] for i in range(m)]


def F(x):
    if x[0] < 0:
        return (1+2*x[0],)+tuple(x[1:])
    return (1-2*x[-1],x[0])+tuple(x[1:-1])


def H(x):
    return sum((v-Q(1, 2) for v in x[1:]), Q(0))


def d(x):
    return x[0]+H(x)-H(F(x))


def preimages(y):
    left = ((y[0]-1)/2,)+tuple(y[1:])
    right = tuple(y[1:])+((1-y[0])/2,)
    return left, right


for m in range(2, 11):
    A = affine_matrix(m)
    I = eye(m)
    # Polynomial identity follows because two degree-m polynomials agree
    # at m+1 distinct rational arguments.
    for k in range(m+1):
        z = Q(k, m+1)
        B = [[I[i][j]-z*A[i][j] for j in range(m)] for i in range(m)]
        closed = (1-z/4)*(1-z/2)**(m-1)+z**m/Q(2)**(m+1)
        assert det(B) == closed, (m, k)
    # The row coefficient of the complete resolvent is (1,...,1).
    B = [[I[i][j]-A[i][j] for j in range(m)] for i in range(m)]
    ones = [Q(1)]*m
    assert [sum(ones[i]*B[i][j] for i in range(m)) for j in range(m)] == [Q(j==0) for j in range(m)]
    P = eye(m)
    for n in range(m+1):
        actual = P[0][0]
        if n < m:
            assert actual == Q(1, 4)**n, (m,n,actual)
        else:
            assert actual == Q(1, 4)**m - Q(1, 2)**(m+1), (m,n,actual)
        P = mul(P, A)
    # Verify both inverse branches and the elementary martingale identity
    # at deterministic points with exact rational coordinates.
    for j in range(1, 12):
        y = tuple([Q(2*j-12, 12)]+[Q((i*j) % 13, 13) for i in range(1,m)])
        xl, xr = preimages(y)
        assert F(xl) == y and F(xr) == y, (m,j)
        assert d(xl) == xl[0] and d(xr) == xr[-1]
        assert d(xl) + d(xr) == 0
        assert (d(xl)**2+d(xr)**2)/2 == (1-y[0])**2/4

print('AFFINE_TRANSFER_DETERMINANTS_AND_RESOLVENT_OK dimensions=2..10')
print('FIRST_NEGATIVE_CORRELATION_AT_DIMENSION_OK dimensions=2..10')
print('MARTINGALE_PREIMAGES_AND_CONDITIONAL_VARIANCE_OK dimensions=2..10')
