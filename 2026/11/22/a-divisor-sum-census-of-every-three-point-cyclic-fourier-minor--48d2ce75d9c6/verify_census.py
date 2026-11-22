#!/usr/bin/env python3
"""Exact divisor-sum census and independent brute-force incidence checks.

Python 3 standard library only.  Unordered triples are counted; row/column
choices are ordered.  This is a finite check, not a substitute for the proof.
"""
from itertools import combinations
from math import comb, gcd


def choose(n, k):
    return comb(n, k) if n >= k else 0


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def phi(n):
    return sum(gcd(n, j) == 1 for j in range(1, n + 1))


def mobius(n):
    d, primes = 2, 0
    while d * d <= n:
        if n % d == 0:
            n //= d
            primes += 1
            if n % d == 0:
                return 0
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        primes += 1
    return -1 if primes % 2 else 1


def census(n):
    ds = divisors(n)
    t = choose(n, 3)
    # P = number of (proportional row pair, selected 3x3 minor).
    p_num = sum(n*n*(n-2)*phi(n//a)*choose(a,3)//a for a in ds if a<n)
    assert p_num % 2 == 0
    p = p_num//2
    # Q = number of (proportional row pair, proportional column pair, minor).
    q_num = sum(n*n*phi(n//a)*phi(n//b)*(a-2)*(b-2)
                for a in ds for b in ds if a<n and b<n and (a*b)%n == 0)
    assert q_num % 4 == 0
    q = q_num//4
    # Rank 1 from Mobius inversion on the exact gcd of the row differences.
    rank1 = 0
    for h in ds:
        exact = sum(mobius(k//h)*k*choose(n//k,3) for k in ds if k%h == 0)
        assert exact >= 0
        rank1 += exact*(n//h)*choose(h,3)
    rank2 = 2*p - q + 3*rank1
    rank3 = t*t - 2*p + q - 4*rank1
    assert all(k>=0 for k in (rank1,rank2,rank3))
    assert rank1+rank2+rank3 == t*t
    return rank1,rank2,rank3


def brute(n):
    triples = list(combinations(range(n),3))
    # Count rank via proportional-pair incidence, independent of divisor sums.
    counts = [0,0,0,0]
    for r in triples:
        rd = [r[1]-r[0],r[2]-r[0],r[2]-r[1]]
        for c in triples:
            cd = [c[1]-c[0],c[2]-c[0],c[2]-c[1]]
            kr = sum(all(d*(c[j]-c[0])%n==0 for j in (1,2)) for d in rd)
            kc = sum(all(d*(r[j]-r[0])%n==0 for j in (1,2)) for d in cd)
            rank = 1 if kr==3 and kc==3 else (2 if kr or kc else 3)
            assert kr in (0,1,3) and kc in (0,1,3)
            if kr==3 or kc==3: assert kr==kc==3
            counts[rank] += 1
    return tuple(counts[1:])


if __name__ == '__main__':
    samples = {3:(0,0,1),5:(0,0,100),6:(0,48,352),
               10:(0,1600,12800),12:(96,6624,41680),
               15:(300,13800,192925),21:(1470,91728,1675702),
               30:(18000,1519200,14946400)}
    for n, expected in samples.items():
        actual = census(n)
        assert actual == expected,(n,actual,expected)
        print('DIVISOR_SUM',n,*actual)
    for n in (3,4,5,6,8,9,10,12):
        actual, direct = census(n), brute(n)
        assert actual == direct,(n,actual,direct)
        print('INDEPENDENT_PAIR_INCIDENCE',n,*actual)
    print('UNIVERSAL_CYCLIC_TRIPLE_CENSUS_CHECKS_PASS')
