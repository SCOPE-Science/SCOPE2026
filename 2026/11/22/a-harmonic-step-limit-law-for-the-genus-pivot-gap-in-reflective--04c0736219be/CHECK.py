#!/usr/bin/env python3
"""Independent integer checks for genus-pivot gap-run lengths of reflective semigroups.

The algebraic proof and limiting law are in RESULT.md. This program checks
finite cases, not the infinitely quantified assertions.
"""
from collections import Counter
from math import isqrt


def divisor_count(n):
    return sum(2 if d*d != n else 1 for d in range(1, isqrt(n)+1) if n % d == 0)


def sigma(n):
    return sum(d + (n//d if d*d != n else 0) for d in range(1, isqrt(n)+1) if n % d == 0)


def expected_count(g, t):
    if t == g:
        return 1
    if not 1 <= t < g:
        return 0
    n = g-t
    return sum(1 for a in range(t+1, n+1) if n%a == 0)


def semigroup_elements(g, a):
    r=g%a
    generators = [a, 2*g+a-r] + list(range(g+1,g+a))
    reachable=[False]*(2*g+1)
    reachable[0]=True
    for n in range(1, 2*g+1):
        reachable[n]=any(n>=v and reachable[n-v] for v in generators)
    return reachable


def check_g(g):
    histogram=Counter()
    for a in range(2,g+2):
        if g%a==0:
            continue
        r=g%a
        histogram[r]+=1
        # Verify independent generator membership, reflective gap count,
        # and the maximal gap block containing the genus pivot.
        reachable=semigroup_elements(g,a)
        gaps={i for i in range(1,2*g) if not reachable[i]}
        q=g//a
        expected={z for z in range(1,g) if z%a} | {g+j*a for j in range(q+1)}
        assert gaps == expected, (g,a,'gapset')
        assert len(gaps)==g
        assert all(j in gaps for j in range(q*a+1,g+1))
        assert q*a not in gaps and (g+1) not in gaps
        assert len(range(q*a+1,g+1))==r
    assert sum(histogram.values())==g+1-divisor_count(g)
    assert sum(t*c for t,c in histogram.items())==g*(g+1)-sum(sigma(n) for n in range(1,g+1))
    assert all(histogram[t]==expected_count(g,t) for t in range(1,g+1)),g
    return len(histogram)


def main():
    assert sum(check_g(g) for g in range(1,91))>0
    print('PASS: 90 genera, all permitted multiplicities, direct generating-set reachability,')
    print('      complete gap sets, exact genus-pivot run lengths, all divisor histogram bins,')
    print('      cardinality and first-moment identities.')


if __name__=='__main__':
    main()
