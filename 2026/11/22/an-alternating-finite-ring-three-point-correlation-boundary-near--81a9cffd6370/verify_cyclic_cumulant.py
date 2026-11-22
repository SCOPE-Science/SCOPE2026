#!/usr/bin/env python3
"""Independent exact-rational verification of finite hard-core ring three-site cumulants.

Standalone standard-library script. Run: python3 verify_cyclic_cumulant.py
The infinite-family theorem rests on the symbolic proof in RESULT.md; this
checks independent configuration enumeration and exact rational identities.
"""
from fractions import Fraction
from itertools import combinations


def cumulant_from_enumeration(n, gaps, t):
    lam = t/(1-t)**2
    positions = (0, gaps[0], gaps[0]+gaps[1])
    assert sum(gaps) == n
    Z = Fraction(0)
    counts = [Fraction(0) for _ in range(8)]
    for mask in range(1 << n):
        if (mask & ((mask << 1 | mask >> (n-1)) & ((1 << n)-1))):
            continue
        weight = lam**mask.bit_count()
        Z += weight
        for subsets in range(1,8):
            if all((mask >> positions[j]) & 1 for j in range(3) if subsets >> j & 1):
                counts[subsets] += weight
    p = [v/Z for v in counts]
    return p[7]-p[3]*p[4]-p[5]*p[2]-p[6]*p[1]+2*p[1]*p[2]*p[4]


def exact_closed_formula(m, t):
    r=(-t)**m
    H=(r**4*t**3-2*r**4*t**2-r**3*t+2*r**2*t**2
       -2*r**2*t+r*t**2+2*t-1)
    V=-r**2*t*(r-1)*(t-1)*H
    Q=1+(-t)**(3*m+1)
    return V/((1+t)**3*Q**3)


def direct_transfer_identity(m,t):
    n=3*m+1
    def F(k):return (t+(-t)**k)/(1+t)
    Q=1+(-t)**n
    p1=F(n)/Q
    # distinct pair spacings m, m, m+1
    p2a=F(m)*F(n-m)/Q
    p2c=F(m+1)*F(n-m-1)/Q
    p3=F(m)*F(m)*F(m+1)/Q
    return p3-p1*(2*p2a+p2c)+2*p1**3


def main():
    total=0
    for m in range(2,6):
        for t in (Fraction(1,5),Fraction(1,3),Fraction(1,2),Fraction(2,3),Fraction(4,5)):
            direct=cumulant_from_enumeration(3*m+1,(m,m,m+1),t)
            expected=exact_closed_formula(m,t)
            transfer=direct_transfer_identity(m,t)
            assert direct==expected==transfer,(m,t,direct,expected,transfer)
            total+=1
    for m in range(2,13):
        for t in (Fraction(1,4),Fraction(1,2),Fraction(3,4)):
            assert direct_transfer_identity(m,t)==exact_closed_formula(m,t)
            total+=1
        at_half=exact_closed_formula(m,Fraction(1,2))
        assert (at_half>0) == (m%2==1)
        total+=1
    print('CYCLIC_THIRD_CUMULANT_EXACT_OK',total,'checks')

if __name__=='__main__':main()
