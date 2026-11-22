"""Standalone exact-rational checks for two local meandric component counts.

Requires Python 3.9+ standard library; use `python CHECK.py`.
Finite verification supplements the analytic all-size and limit proofs.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial


@lru_cache(None)
def catalan(n):
    assert n >= 0
    return comb(2 * n, n) // (n + 1)


@lru_cache(None)
def noncrossing(n):
    if n == 0:
        return ((),)
    ans = []
    for k in range(n):
        for left in noncrossing(k):
            for right in noncrossing(n - k - 1):
                ans.append(((0, 2*k + 1),)
                           + tuple((a+1, b+1) for a,b in left)
                           + tuple((a+2*k+2, b+2*k+2) for a,b in right))
    return tuple(ans)


def falling(a,k):
    if k > a:
        return 0
    value = 1
    for j in range(k):
        value *= a - j
    return value


def mixed_factorial(n,r,s):
    if r + 2*s > n:
        return Fraction(0)
    return Fraction((2**s)*falling(2*n-r-3*s,r+s)*catalan(n-r-2*s)**2,
                    catalan(n)**2)


def exact_count_profile(n):
    seq = noncrossing(n)
    assert len(seq) == catalan(n)
    counts = Counter()
    for upper in seq:
        us = set(upper)
        for lower in seq:
            ls = set(lower)
            x = sum((i,i+1) in us and (i,i+1) in ls
                    for i in range(2*n-1))
            y = 0
            for i in range(2*n-3):
                straight = ((i,i+1),(i+2,i+3))
                nested = ((i,i+3),(i+1,i+2))
                y += ((all(e in us for e in straight) and
                       all(e in ls for e in nested)) or
                      (all(e in ls for e in straight) and
                       all(e in us for e in nested)))
            counts[x,y] += 1
    return counts,catalan(n)**2


def checked_profile(n,counts,total,rs):
    assertions=0
    for r,s in rs:
        brute = Fraction(sum(v*falling(x,r)*falling(y,s)
                             for (x,y),v in counts.items()),total)
        expected=mixed_factorial(n,r,s)
        assert brute == expected, (n,r,s,brute,expected)
        assertions+=1
    return assertions


def covariance_formula(n):
    assert n >= 3
    return Fraction(-n*n*(n+1)**2*(10*n**3-41*n**2+32*n+11),
                    32*(2*n-5)*(2*n-3)**2*(2*n-1)**3)


def main():
    assertions=0
    for n in range(1,8):
        counts,total=exact_count_profile(n)
        rs=[(r,s) for s in range(n//2+1) for r in range(n-2*s+1)]
        if n == 7:
            rs=[(r,s) for r,s in rs if r <= 2 and s <= 2]
        assertions+=checked_profile(n,counts,total,rs)
        if n>=3:
            x=mixed_factorial(n,1,0)
            y=mixed_factorial(n,0,1)
            cov=mixed_factorial(n,1,1)-x*y
            assert cov == covariance_formula(n)
            assert cov < 0
            assertions+=2
        print(f'n={n}: {len(counts)} count outcomes, {len(rs)} factorial-moment checks, denominator={total}')
    print(f'PASS: {assertions} exact-rational assertions; all complete paired Catalan matchings through seven pairs')


if __name__=='__main__':
    main()
