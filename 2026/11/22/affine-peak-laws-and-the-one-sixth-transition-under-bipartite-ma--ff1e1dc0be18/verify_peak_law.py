#!/usr/bin/env python3
"""Exact independent checks for partial-matching-deletion peak laws.

Requires Python >=3.9; no third-party modules. Run: python verify_peak_law.py
"""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from math import factorial


def initial_run_probability(n, k):
    assert n >= 2 and 1 <= k <= n
    out = Fraction(1)
    for j in range(1, k):
        out *= Fraction(n - j, 2*n - j)
    return out * Fraction(n, 2*n - k)


def peak_distribution(n, m):
    assert n >= 2 and 0 <= m <= n
    d = defaultdict(Fraction)
    for k in range(1, n+1):
        q = initial_run_probability(n, k)
        r = Fraction(m*(n-k+(2*n-1 if k == 1 else 0)), n**3)
        d[k] += q*(1-r)
        d[k+1] += q*r
    return {k: v for k, v in d.items() if v}


def brute_permutations(n, m):
    N = 2*n
    counts = defaultdict(int)
    for order in permutations(range(N)):
        rank = [0]*N
        for r, v in enumerate(order):
            rank[v] = r
        s = 0
        for i in range(n):
            s += all(rank[i] < rank[n+j] for j in range(n)
                     if not (i == j and i < m))
            s += all(rank[n+i] < rank[j] for j in range(n)
                     if not (i == j and i < m))
        counts[s] += 1
    return {k: Fraction(v, factorial(N)) for k, v in counts.items()}


def independent_subset_dp(n, m):
    # Descending-label permutations. A newly placed vertex is a peak iff
    # no higher-labelled neighbor has previously been placed.
    N = 2*n
    adj = [0]*N
    for i in range(n):
        for j in range(n):
            if i == j and i < m:
                continue
            adj[i] |= 1 << (n+j)
            adj[n+j] |= 1 << i
    dp = [None]*(1 << N)
    dp[0] = [1]
    for mask in range((1 << N)-1):
        arr = dp[mask]
        if arr is None:
            continue
        c = mask.bit_count()
        for v in range(N):
            if mask & (1 << v):
                continue
            nxt = mask | (1 << v)
            if dp[nxt] is None:
                dp[nxt] = [0]*(c+2)
            delta = int((adj[v] & mask) == 0)
            for k, value in enumerate(arr):
                dp[nxt][k+delta] += value
    return {k: Fraction(x, factorial(N))
            for k, x in enumerate(dp[-1]) if x}


def geometric_tv(n, m):
    d = peak_distribution(n, m)
    # Geometric(1/2) supported on all positive integers.
    discrepancy = sum(abs(d.get(k, 0) - Fraction(1, 2**k))
                      for k in range(1, n+1))
    discrepancy += Fraction(1, 2**n)
    return discrepancy/2


def first_order_coefficient(n, m):
    rho = Fraction(m,n)
    return (3-rho)/8 if rho <= Fraction(1, 6) else (1+11*rho)/8


def main():
    assert peak_distribution(3, 3) == {
        1: Fraction(2,15), 2: Fraction(11,15), 3: Fraction(2,15)}
    for n in range(2,5):
        for m in range(n+1):
            assert brute_permutations(n,m) == peak_distribution(n,m)
        print('INDEPENDENT_FULL_PERMUTATIONS_PASS',n, n+1)
    for n in range(2,7):
        for m in range(n+1):
            p = peak_distribution(n,m)
            assert independent_subset_dp(n,m) == p
            assert sum(p.values()) == 1
            assert sum(k*v for k,v in p.items()) == (
                Fraction(2*n,n+1)+Fraction(2*m,n*(n+1)))
            # Exact affine deletion-mixture identity at every coefficient.
            p0 = peak_distribution(n,0)
            pn = peak_distribution(n,n)
            for k in range(1,n+1):
                assert p.get(k,0) == (Fraction(n-m,n)*p0.get(k,0)
                                      + Fraction(m,n)*pn.get(k,0))
        print('INDEPENDENT_SUBSET_DP_AND_AFFINE_MIXTURE_PASS', n, n+1)
    assert independent_subset_dp(7,3) == peak_distribution(7,3)
    print('INDEPENDENT_SUBSET_DP_PASS',7,3)
    for n in (30,100,500):
        for m in (0,round(n/6),n//2,n):
            a = first_order_coefficient(n,m)
            scaled = n*geometric_tv(n,m)
            assert abs(float(a-scaled)) < 0.3/n
        print('FIRST_ORDER_TV_NUMERICAL_CROSSCHECK_PASS',n)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
