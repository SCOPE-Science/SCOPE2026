#!/usr/bin/env python3
"""Exact checks for dyadic-floor subset-sum gap formulas."""
from collections import Counter
from fractions import Fraction
from math import comb, gcd


def weight(n):
    return n.bit_count()


def terms(t, n):
    return [(t.numerator*(1<<j))//t.denominator for j in range(1,n+1)]


def defect(t,n):
    a=terms(t,n+1)
    return a[-1]-sum(a[:-1])-1

# Direct integer-floor and independent binary-popcount comparison.
identities=0
for q in range(2,91):
    for p in range(1,q):
        if gcd(p,q)!=1: continue
        t=Fraction(p,q)
        for n in range(1,20):
            assert defect(t,n)==weight(terms(t,n+1)[-1])-1,(t,n)
            identities+=1

# Every uniform binary cell has one equiprobable (n+1)-bit prefix.
cells=0
for n in range(1,12):
    hist=Counter()
    for m in range(1<<(n+1)):
        # Strictly inside this dyadic cylinder.
        t=Fraction(2*m+1,1<<(n+2))
        observed=max(0,defect(t,n))
        predicted=max(0,weight(m)-1)
        assert observed==predicted
        hist[observed]+=1
        cells+=1
    assert hist[0] == comb(n+1,0)+comb(n+1,1)
    for ell in range(1,n+1):
        assert hist[ell] == comb(n+1,ell+1)

# Independent literal subset sums: every proposed canonical gap is absent.
missing=0
for t in (Fraction(1,3),Fraction(1,7),Fraction(3,7),Fraction(3,8),Fraction(5,16),Fraction(7,12)):
    a=terms(t,15)
    reachable={0}
    for v in a:
        reachable |= {s+v for s in reachable}
    for n in range(1,13):
        lo=sum(a[:n])+1
        hi=a[n]-1
        for x in range(lo,hi+1):
            assert x not in reachable,(t,n,x)
            missing+=1

# Exact rational periodic orbit means for two distinct arithmetic phases.
for numerator,theta in ((1,Fraction(1,3)),(3,Fraction(2,3))):
    t=Fraction(numerator,7)
    r=[(numerator*pow(2,j,7))%7 for j in range(1,4)]
    assert Fraction(sum(r),21)==theta
    assert abs(Fraction(defect(t,900),900)-theta)<Fraction(1,100)

print('VERIFY_OK identities=',identities,'binary_cells=',cells,
      'direct_missing_integers=',missing,
      'periodic_slopes=1/3,2/3','exact_arithmetic=yes')
