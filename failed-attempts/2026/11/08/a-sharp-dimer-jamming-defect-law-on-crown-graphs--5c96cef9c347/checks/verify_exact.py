#!/usr/bin/env python3
"""Exact compressed-state transition verification for uniform dimer deposition."""
from fractions import Fraction
from functools import lru_cache

@lru_cache(None)
def deficit(m, c):
    assert 0 <= c <= m
    if m == 1:
        return Fraction(c, 1)
    d = m*m-c
    if not d:
        return Fraction(0)
    numer = Fraction(0)
    for weight, cc in ((c*(c-1), c-2), (2*c*(m-c),c-1), ((m-c)**2,c)):
        if weight:
            assert 0 <= cc <= m-1
            numer += Fraction(weight,d)*deficit(m-1,cc)
    assert Fraction(0) <= numer <= Fraction(1)
    return numer

reference = {2:'0',3:'1/3',4:'4/21',5:'4/21',6:'172/1029',7:'4870/31899',8:'8840593/63096222',9:'817773175/6306878886',10:'630349391777099/5220500077249842'}
for n, ref in reference.items():
    q = deficit(n,n)
    assert q == Fraction(ref), (n,q,ref)
    H = sum((Fraction(1,j) for j in range(1,n)),Fraction(0))
    lower = Fraction(2,n+1)-4*H/(n*(n+1))
    assert lower <= q <= Fraction(2,n+1)

# Verify all pointwise conditional moment equalities, and supermartingale comparison.
for m in range(3,90):
    for c in range(m+1):
        d=m*m-c
        counts=[(c*(c-1),c-2),(2*c*(m-c),c-1),((m-c)**2,c)]
        assert sum(w for w,_ in counts)==d
        ec=sum(Fraction(w*cc,d) for w,cc in counts if w)
        expected=Fraction(c,1)*(1-Fraction(2*(m-1),d))
        assert ec==expected,(m,c,ec,expected)
        e2=sum(Fraction(w*cc*(cc-1),d) for w,cc in counts if w)
        proposed=Fraction(c*(c-1)*((m-2)**2-c+2),d)
        assert e2==proposed,(m,c,e2,proposed)
        if c>=2:
            assert proposed <= Fraction(c*(c-1)*(m-1)*(m-2),m*(m+1))
print('PASS exact q_n n=2..10, first two conditional moments m=3..89, harmonic bounds')
