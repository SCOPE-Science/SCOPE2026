#!/usr/bin/env python3
"""Independent exact-rational spot checks for an eight-dimensional obstruction bound."""
from fractions import Fraction
from itertools import combinations_with_replacement
from random import Random

def direct_score(v):
    # Partition [0,1/2] into intervals with fixed nearest half-integer centers.
    breaks = sorted({Fraction(0), Fraction(1,2)} |
                    {Fraction(k,a) for a in v for k in range(a+1)
                     if 0 < 2*k < a})
    vals = []
    for left, right in zip(breaks, breaks[1:]):
        mid = (left + right) / 2
        c = [int(mid*a) + Fraction(1,2) for a in v]
        tstar = sum(Fraction(a)*z for a,z in zip(v,c)) / sum(a*a for a in v)
        tstar = max(left,min(right,tstar))
        vals.append(sum((tstar*a-z)**2 for a,z in zip(v,c)))
    return min(vals)

def projected_score(v):
    # Independent from C++ source: calculate all projection residuals with Fractions.
    breaks = sorted({Fraction(0), Fraction(1,2)} |
                    {Fraction(k,a) for a in v for k in range(a+1)
                     if 0 < 2*k < a})
    Q = sum(a*a for a in v)
    vals = []
    for left,right in zip(breaks,breaks[1:]):
        m=(left+right)/2
        c=[int(a*m)+Fraction(1,2) for a in v]
        vals.append(sum(z*z for z in c)-sum(a*z for a,z in zip(v,c))**2/Q)
    return min(vals)

def main():
    v=(1,2,3,4,5,7,9,11)
    assert direct_score(v)==projected_score(v)==Fraction(8,17)
    checked=0
    for w in combinations_with_replacement(range(1,8),8):
        assert direct_score(w)==projected_score(w), w
        checked+=1
    rng=Random(62026)
    for _ in range(300):
        w=tuple(sorted(rng.randint(1,24) for i in range(8)))
        assert direct_score(w)==projected_score(w),w
    print('EXACT_INDEPENDENT_OK hero=8/17 small_sorted_vectors=%d deterministic_large_vectors=300'%checked)

if __name__=='__main__': main()
