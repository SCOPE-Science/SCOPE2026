#!/usr/bin/env python3
"""Exact rational verification for ordered-variation and Dobrushin estimates.
Standard library only. This verifies finite instances, not the universal proof.
"""
from fractions import Fraction as F
from random import Random


def invariants(P):
    n = len(P)
    assert all(len(row) == n for row in P)
    assert all(sum(row) == 1 and all(x >= 0 for x in row) for row in P)
    tails = [[sum(row[k+1:]) for k in range(n-1)] for row in P]
    assert all(tails[i][k] <= tails[i+1][k]
               for i in range(n-1) for k in range(n-1))
    beta = max(tails[-1][k] - tails[0][k] for k in range(n-1))
    delta = max(sum(abs(P[i][j]-P[h][j]) for j in range(n))/2
                for i in range(n) for h in range(i+1, n))
    return beta, delta


def sharp_kernel(n, eps):
    m = n//2
    u = [F(1,m) if j%2 == 0 and j < 2*m else F(0) for j in range(n)]
    v = [F(1,m) if j%2 == 1 and j < 2*m else F(0) for j in range(n)]
    assert sum(u) == sum(v) == 1
    out = []
    for i in range(n):
        s = F(i,n-1)
        out.append([(1-eps)*((1-s)*u[j]+s*v[j])+eps*F(1,n)
                    for j in range(n)])
    return out


def endpoint_kernel(n, eps):
    return [[(1-eps)*int(i==j) + eps*F(1,n)
             for j in range(n)] for i in range(n)]


def random_monotone(n, rng):
    weights = [rng.randint(1,8) for _ in range(rng.randint(2,9))]
    S = sum(weights)
    P = [[F(0) for _ in range(n)] for _ in range(n)]
    for w in weights:
        phi = sorted(rng.randrange(n) for _ in range(n))
        for i,j in enumerate(phi):
            P[i][j] += F(w,S)
    return [[F(9,10)*P[i][j]+F(1,10*n) for j in range(n)]
            for i in range(n)]


def main():
    sharp_tests = 0
    for n in range(2,33):
        for eps in [F(0),F(1,17),F(2,7)]:
            beta, delta = invariants(sharp_kernel(n,eps))
            assert beta == (1-eps)/ (n//2)
            assert delta == (1-eps)
            sharp_tests += 1
    print('EXACT_SHARP_ALL_DIMENSIONS_N2_TO32_AND_THREE_SMOOTHINGS_PASS',sharp_tests)
    left_tests = 0
    for n in range(2,33):
        for eps in [F(0),F(1,11)]:
            beta, delta = invariants(endpoint_kernel(n,eps))
            assert beta == delta == (1-eps)
            left_tests += 1
    print('EXACT_LOWER_EQUALITY_POSITIVE_KERNELS_PASS',left_tests)
    rng=Random(723479)
    random_tests=0
    for n in range(2,13):
        for _ in range(120):
            beta,delta=invariants(random_monotone(n,rng))
            assert beta <= delta <= (n//2)*beta
            if n <= 3:assert beta==delta
            random_tests+=1
    print('EXACT_MONOTONE_RANDOM_KERNEL_BOUND_CHECKS_PASS',random_tests)
    print('ALL_ORDERED_MARKOV_COEFFICIENT_CHECKS_PASS')

if __name__=='__main__':main()
