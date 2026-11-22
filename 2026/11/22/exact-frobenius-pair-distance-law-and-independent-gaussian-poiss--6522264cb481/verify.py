#!/usr/bin/env python3
"""Exact finite checks for the Frobenius pair-distance law of partial permutation matrices.

Run: python3 verify.py  (Python standard library only).
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial


def fall(a, r):
    out = 1
    for j in range(r):
        out *= a-j
    return out


def all_matchings(n):
    for k in range(n + 1):
        for rows in combinations(range(n), k):
            for cols in permutations(range(n), k):
                yield frozenset(zip(rows, cols))


def expected_histogram(n):
    total = sum(comb(n,k)**2 * factorial(k) for k in range(n+1))
    ans = Counter()
    for k in range(n+1):
        A = comb(n,k)**2 * factorial(k)
        for ell in range(n+1):
            B = comb(n,ell)**2 * factorial(ell)
            a = [Fraction(fall(k,r) * fall(ell,r), fall(n,r)**2) for r in range(min(k,ell)+1)]
            for j in range(min(k,ell)+1):
                prob = sum(((-1)**(r-j) * Fraction(comb(r,j),factorial(r))*a[r]
                            for r in range(j,len(a))), Fraction(0))
                ans[k + ell - 2*j] += A*B*prob
    assert all(v.denominator == 1 and v.numerator>=0 for v in ans.values())
    assert sum(ans.values()) == total**2
    return ans


def direct_histogram(n):
    matchings = list(all_matchings(n))
    out = Counter()
    for a in matchings:
        for b in matchings:
            out[len(a ^ b)] += 1
    return out


def conditional_factorial_moments(n):
    all_m = list(all_matchings(n))
    by_k = {k:[a for a in all_m if len(a)==k] for k in range(n+1)}
    for k in range(n+1):
        for ell in range(n+1):
            a, b = by_k[k], by_k[ell]
            for r in range(min(k,ell)+1):
                direct = sum(fall(len(x & y),r) for x in a for y in b)
                exact = Fraction(len(a)*len(b)*fall(k,r)*fall(ell,r),fall(n,r)**2)
                assert direct == exact, (n,k,ell,r,direct,exact)


def check():
    for n in range(1,5):
        exact = expected_histogram(n)
        direct = direct_histogram(n)
        assert exact == direct, (n, exact, direct)
        conditional_factorial_moments(n)
        sizes = [comb(n,k)**2*factorial(k) for k in range(n+1)]
        total = sum(sizes)
        mu = Fraction(sum(k*sizes[k] for k in range(n+1)), total)
        moment = Fraction(sum(j*expected_histogram(n)[j] for j in exact),total*total)
        assert moment == 2*mu-2*mu*mu/(n*n)
        print(f'n={n} vertices={total} distance_spectrum={dict(sorted(exact.items()))}')
    for n in [10,20,40]:
        exact = expected_histogram(n)
        assert sum(exact.values()) == sum(comb(n,k)**2*factorial(k) for k in range(n+1))**2
        assert all(v>=0 for v in exact.values())
    print('PARTIAL_PERMUTATION_METRIC_EXACT_PASS')

if __name__ == '__main__':
    check()
