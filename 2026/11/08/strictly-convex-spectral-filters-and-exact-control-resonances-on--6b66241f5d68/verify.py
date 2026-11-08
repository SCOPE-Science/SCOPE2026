#!/usr/bin/env python3
"""Exact-rational finite checks for coordinate reachability on complete bipartite graphs.

The finite checks are not a proof of the all-parameter theorem; the latter uses
spectral projections and strict convexity, as established in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def laplacian(p, q):
    n = p + q
    L = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        L[i][i] = F(q if i < p else p)
    for i in range(p):
        for j in range(p, n):
            L[i][j] = L[j][i] = F(-1)
    return L


def taylor_matrix(L, h, order):
    n = len(L)
    I = [[F(i == j) for j in range(n)] for i in range(n)]
    R = [[F(0) for _ in range(n)] for _ in range(n)]
    power = I
    for k in range(order + 1):
        coeff = (-h)**k / F(factorial(k))
        for i in range(n):
            for j in range(n):
                R[i][j] += coeff * power[i][j]
        if k < order:
            power = mm(power, L)
    return R


def controllability_rank(T, S):
    n = len(T)
    pivots = {}
    block = [[F(i == j) for i in range(n)] for j in S]
    for _ in range(n):
        for v0 in block:
            v = list(v0)
            for p in sorted(pivots):
                if v[p]:
                    c = v[p]
                    v = [x - c * y for x, y in zip(v, pivots[p])]
            p = next((i for i, x in enumerate(v) if x), None)
            if p is not None:
                c = v[p]
                pivots[p] = [x / c for x in v]
                if len(pivots) == n:
                    return n
        block = [[sum(T[i][j] * v[j] for j in range(n)) for i in range(n)]
                 for v in block]
    return len(pivots)


def p_gamma(x):
    return F(24) - 36*x + 28*x*x - 15*x*x*x


def p_beta(x):
    return x*x*x - 4*x*x + 12*x - 24


def main():
    # Exact rational-root isolation and monotonicity are independently proved.
    assert p_gamma(F(1038933, 1000000)) > 0
    assert p_gamma(F(1038934, 1000000)) < 0
    assert p_beta(F(2785293, 1000000)) < 0
    assert p_beta(F(2785294, 1000000)) > 0
    assert p_gamma(F(1)) > 0 and p_gamma(F(11,10)) < 0
    assert p_beta(F(11,5)) < 0 and p_beta(F(3)) > 0
    count_pairs = 0
    count_matrix_checks = 0
    count_rank_checks = 0
    for p in range(2, 5):
        for q in range(2, 5):
            n = p+q
            L = laplacian(p,q)
            steps = sorted(set([F(1,7), F(1,3), F(1,2), F(2,p+q),
                                F(2,p+2*q), F(2,3*p), F(2,p)]))
            for order in [2,4]:
                for h in steps:
                    T = taylor_matrix(L,h,order)
                    count_matrix_checks += 1
                    assert all(sum(row) == 1 for row in T)
                    assert all(T[i][j] == T[j][i] for i in range(n) for j in range(n))
                    resonant = (order==2 and p==q and h*p in (F(2,3), F(2)))
                    for u,v in combinations(range(n),2):
                        S = [i for i in range(n) if i not in (u,v)]
                        rank = controllability_rank(T,S)
                        should_control = (u<p)!=(v<p) and not resonant
                        if (rank == n) != should_control:
                            raise AssertionError((p,q,order,h,u,v,rank,should_control))
                        count_rank_checks += 1
                        count_pairs += 1
                    for omitted in [0,p,n-1]:
                        S = [i for i in range(n) if i!=omitted]
                        assert controllability_rank(T,S)==n
                        count_rank_checks += 1
            # At h=0, T is scalar identity; one coordinate input per node needed.
            Z = taylor_matrix(L,F(0),4)
            assert controllability_rank(Z,list(range(n-1)))==n-1
    # Exact second-order resonance identities:
    #  F2(2/3)=F2(4/3)=5/9; F2(2)=F2(0)=1.
    f2=lambda x: F(1)-x+x*x/F(2)
    assert f2(F(2,3))==f2(F(4,3))==F(5,9)
    assert f2(F(2))==f2(F(0))==F(1)
    print('OK', 'rational_matrix_checks',count_matrix_checks,
          'exact_coordinate_rank_checks',count_rank_checks,
          'two_missing_coordinate_tests',count_pairs,
          'positive_RK2_resonance',str(F(5,9)),
          'isolated_RK4_roots',2)

if __name__=='__main__':
    main()
