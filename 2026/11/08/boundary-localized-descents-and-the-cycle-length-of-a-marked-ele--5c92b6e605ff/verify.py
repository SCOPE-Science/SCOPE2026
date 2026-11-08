#!/usr/bin/env python3
"""Standalone exact checks for a tagged-cycle/linear-descent theorem."""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from math import factorial

def predicted(n, k, i):
    assert n >= 3 and 1 <= k <= n and 1 <= i <= n - 1
    if i > 1:
        return Fraction(1, 2)
    if k == 1:
        return Fraction(0)
    if k == 2:
        return Fraction(n + 1, 2 * (n - 1))
    if k == n:
        return Fraction(1, 2)
    return Fraction(n, 2 * (n - 1))

def cycle_length_one(p):
    x = p[0]
    k = 1
    while x != 0:
        k += 1
        x = p[x]
    return k

def theoretical_covariance(n):
    return Fraction(n*n - 3*n + 4, 4*n*(n-1))

def test():
    assertions = 0
    total_perm = 0
    for n in range(3, 10):
        counts = defaultdict(int)
        descends = defaultdict(int)
        sum_kd = sum_d = sum_k = 0
        for p in permutations(range(n)):
            total_perm += 1
            k = cycle_length_one(p)
            counts[k] += 1
            d = 0
            for i in range(1, n):
                indicator = p[i - 1] > p[i]
                descends[(k, i)] += indicator
                d += indicator
            sum_kd += k*d
            sum_d += d
            sum_k += k
        N = factorial(n)
        assert total_perm >= N
        for k in range(1,n+1):
            assert counts[k] == factorial(n-1)
            assertions += 1
            for i in range(1,n):
                assert Fraction(descends[(k,i)],counts[k]) == predicted(n,k,i), (n,k,i)
                assertions += 1
        assert Fraction(sum_d,N) == Fraction(n-1,2)
        assert Fraction(sum_k,N) == Fraction(n+1,2)
        assert Fraction(sum_kd,N) - Fraction(sum_k,N)*Fraction(sum_d,N) == theoretical_covariance(n)
        assertions += 3
    # Formulae also retain internal consistency outside the exhaustively checked sizes.
    for n in range(3, 301):
        assert sum(predicted(n,k,1) for k in range(1,n+1)) / n == Fraction(1,2)
        cov = sum((k-Fraction(n+1,2))*predicted(n,k,1) for k in range(1,n+1)) / n
        assert cov == theoretical_covariance(n)
        assert cov > 0
        assertions += 3
    print(f'OK: {assertions} exact rational assertions; {total_perm} complete permutation objects; n=3..9, plus symbolic formulas checked for n=3..300')

if __name__=='__main__': test()
