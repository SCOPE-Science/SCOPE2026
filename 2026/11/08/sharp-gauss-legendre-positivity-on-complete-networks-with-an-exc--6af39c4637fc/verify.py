#!/usr/bin/env python3
"""Exact-rational checks for a Gauss--Legendre graph-heat positivity theorem.

Requires only Python's standard library. The infinite proof is in RESULT.md;
these tests check its rational projector identities on finite examples.
"""
from fractions import Fraction as Q
from itertools import combinations


def mul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def solve(A, B):
    n = len(A)
    Z = [list(A[i]) + list(B[i]) for i in range(n)]
    for j in range(n):
        k = next(i for i in range(j, n) if Z[i][j])
        Z[j], Z[k] = Z[k], Z[j]
        pivot = Z[j][j]
        Z[j] = [v/pivot for v in Z[j]]
        for i in range(n):
            if i != j:
                c = Z[i][j]
                if c:
                    Z[i] = [Z[i][s]-c*Z[j][s] for s in range(2*n)]
    return [row[n:] for row in Z]


def F(x):
    return (x*x-6*x+12)/(x*x+6*x+12)


def graph_matrix(n, weights):
    L = [[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            w = weights.get((i,j), Q(1))
            L[i][i] += w; L[j][j] += w
            L[i][j] -= w; L[j][i] -= w
    return L


def rational_transition(n, weights, h):
    L = graph_matrix(n, weights)
    X = [[h*L[i][j] for j in range(n)] for i in range(n)]
    X2 = mul(X, X)
    denominator = [[X2[i][j]+6*X[i][j]+(12 if i==j else 0)
                    for j in range(n)] for i in range(n)]
    numerator = [[X2[i][j]-6*X[i][j]+(12 if i==j else 0)
                  for j in range(n)] for i in range(n)]
    return solve(denominator, numerator)


def scalar_transition(n, weights, h):
    matched = set()
    for a,b in weights:
        assert a not in matched and b not in matched
        matched.add(a); matched.add(b)
    p0 = Q(1,n)
    fn = F(n*h)
    T = [[p0+fn*((1 if i==j else 0)-p0) for j in range(n)] for i in range(n)]
    for (a,b), t in weights.items():
        lam = n-2+2*t
        change = (F(lam*h)-fn)/2
        T[a][a] += change; T[b][b] += change
        T[a][b] -= change; T[b][a] -= change
    return T


def numerator(n,t,h):
    lam = n-2+2*t
    return lam*(n*n-(n-2)*lam)*h*h+12*lam*h+24*t


def denominator(z,h):
    return z*z*h*h+6*z*h+12

checks = 0
for n in range(3,10):
    pair_pool=[(2*k,2*k+1) for k in range(n//2)]
    for k in range(n//2+1):
        for t in (Q(1,3),Q(1),Q(5,2),Q(5), Q(2*(n-1),n-2)):
            weights={e: t+Q(idx,7) for idx,e in enumerate(pair_pool[:k])}
            for h in (Q(1,11),Q(1),Q(9)):
                T=rational_transition(n,weights,h)
                assert T == scalar_transition(n,weights,h)
                assert all(sum(row) == 1 for row in T)
                for (a,b),w in weights.items():
                    lam = n-2+2*w
                    assert T[a][b] == 6*h*numerator(n,w,h)/(denominator(n,h)*denominator(lam,h))
                checks += 1
for n in range(3,25):
    critical=Q(2*(n-1),n-2)
    for t in (Q(1,2),critical,critical+1):
        lam = n-2+2*t
        coeff=lam*(n*n-(n-2)*lam)
        assert (coeff >= 0) == (t <= critical)
        for h in (Q(1,10),Q(1),Q(10000)):
            assert numerator(n,t,h) == (lam*denominator(n,h) -(n-2)*denominator(lam,h))
            checks += 1
for t in (Q(1,4),Q(1),Q(3)):
    for h in (Q(1,3),Q(10)):
        T=rational_transition(2,{(0,1):t},h)
        assert T[0][1] > 0 and T[0][0] > 0
        checks += 1
print('VERIFY_OK exact_cases=',checks)
