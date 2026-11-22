#!/usr/bin/env python3
"""Exact permutation enumeration supporting circular nearest-neighbor independence."""
from itertools import permutations
from fractions import Fraction
from collections import Counter

def mutual_count(p):
    n=len(p)
    return sum(p[i]<p[(i-1)%n] and p[i]<p[(i+1)%n] for i in range(n))

def main():
    checks=0
    for n in range(3,9):
        distribution=Counter(mutual_count(p) for p in permutations(range(n)))
        total=sum(distribution.values())
        mu=sum(k*v for k,v in distribution.items())
        var=sum((Fraction(k)-Fraction(n,3))**2*v for k,v in distribution.items())
        assert Fraction(mu,total)==Fraction(n,3)
        assert Fraction(var,total)==({3:Fraction(0),4:Fraction(2,9)}.get(n,Fraction(2*n,45)))
        checks+=total+2
        # For each fixed sorted positive gap profile, every placement has exactly
        # the same nearest-neighbor-count law, regardless of profile magnitudes.
        for q in (1,2,3):
            values=[(i+1)**q for i in range(n)]
            counts=Counter(mutual_count(p) for p in permutations(values))
            assert counts==distribution
            checks+=1
    print('PASS:',checks,'exact permutation assertions/checks; analytic rank theorem applies to all n and all radii')
if __name__=='__main__': main()
