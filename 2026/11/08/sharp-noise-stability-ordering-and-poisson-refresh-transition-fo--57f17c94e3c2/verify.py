#!/usr/bin/env python3
"""Exact rank-enumeration cross-checks for cycle-maximum concurrence under coordinate refresh."""
from fractions import Fraction as F
from itertools import permutations, product
from math import comb
import math
from functools import lru_cache
from collections import Counter

def conditional_formula(n,r):
    return F(n-r, n+r) + F(2*r,n*(n+r))

def direct_conditional(n,r):
    # Old coordinates are indexed 0..n-1. Replacement values for 0..r-1
    # are indexed n..n+r-1. Every strict ordering of n+r independent
    # continuous uniform values has equal probability.
    found=0
    for perm in permutations(range(n+r)):
        oldmax=max(range(n), key=lambda i:perm[i])
        newmax=max(range(n), key=lambda i:perm[n+i] if i<r else perm[i])
        found+=(oldmax==newmax)
    from math import factorial
    return F(found,factorial(n+r))

@lru_cache(None)
def stable(n,e):
    return sum(F(comb(n,r))*e**r*(1-e)**(n-r)*conditional_formula(n,r) for r in range(n+1))

def test():
    assertions=0
    for n in range(2,5):
        for r in range(n+1):
            got=direct_conditional(n,r)
            want=conditional_formula(n,r)
            assert got==want, (n,r,got,want)
            assertions+=1
    # Completely independent order comparisons (finite enumerations above).
    for e in [F(1,10),F(1,4),F(1,2),F(3,4),F(1)]:
        ss={n:stable(n,e) for n in range(2,22)}
        for n in range(3,21):
            assert ss[n]>ss[n+1], (n,e)
            assert ss[n]**2 < ss[n-1]*ss[n+1], (n,e)
            assertions+=2
        for n in range(2,22):
            d=1-ss[n]
            lam=F(2*(n-1),n+1)
            assert 0 <= lam*e-d<=2*e*e
            assert F(2,3)*e<=d<=2*e if n>=3 else F(1,2)*e<=d<=2*e
            assertions+=2
    for e in [F(1,7),F(1,2),F(1)]:
        for c in range(2,5):
            for m in range(3*c,3*c+9):
                profiles=[t for t in product(range(3,m+1),repeat=c) if sum(t)==m]
                vals=[math.prod(stable(n,e) for n in t) for t in profiles]
                low=tuple([m//c]*(c-m%c)+[m//c+1]*(m%c))
                high=(m-3*(c-1),)+(3,)*(c-1)
                assert min(vals)==math.prod(stable(n,e) for n in low)
                assert max(vals)==math.prod(stable(n,e) for n in high)
                # Equality uniqueness up to permutation, strict for non-balanced profiles.
                for profile,val in zip(profiles,vals):
                    if val==min(vals): assert sorted(profile)==sorted(low)
                    if val==max(vals): assert sorted(profile)==sorted(high)
                assertions+=2
    print("VERIFY_OK",assertions,"exact rational assertions")

if __name__=="__main__":
    test()
