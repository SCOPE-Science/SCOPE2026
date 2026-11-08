"""Reproduce finite exact arithmetic supporting the bipartite Schur-mask theorem.

This checks examples only. The proof in RESULT.md covers all positive integers.
"""
from fractions import Fraction as F
from math import isqrt

def cert(a,b):
    assert a>=1 and b>=1
    v=F(2*(a*b-1),2*a*b+a+b)
    t=1+v
    p=1+a*v
    r=1+b*v
    # P-A is v times a rank-one matrix and vanishes on block fluctuations.
    assert v>=0
    # Determinant of P+A on the two-dimensional block-constant space.
    assert (2+a*v)*(2+b*v)==a*b*(2-v)**2
    # Exact lower-bound identity for the critical constraint.
    assert 4+2*(a+b)*v==4*a*b-4*a*b*v
    assert t==F(4*a*b+a+b-2,2*a*b+a+b)
    assert 1<=t<2 or a==b==1 and t==1
    return t

checks=0
for a in range(1,41):
    for b in range(1,41):
        assert cert(a,b)==cert(b,a)
        checks+=1
for a in range(1,11):
    # Fixed-part limit t=(4a+1)/(2a+1).
    lim=F(4*a+1,2*a+1)
    assert cert(a,100000) < lim
    assert lim-cert(a,100000)<F(1,10000)
    checks+=1
assert cert(2,2)==F(3,2)
assert cert(2,3)==F(27,17)
assert cert(3,3)==F(5,3)
print('PASS',checks,'rational identities and limiting comparisons')
