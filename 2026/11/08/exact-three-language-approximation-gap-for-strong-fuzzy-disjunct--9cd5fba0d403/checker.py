#!/usr/bin/env python3
"""Finite rational corroboration of analytic approximation bounds. No dependencies."""
from fractions import Fraction as Q
from itertools import product

def verify(n, denom=12):
    d=Q(n-1,n)
    c=d/2
    ez=Q(0)
    ene=Q(0)
    for k in product(range(denom+1), repeat=n):
        x=[Q(z,denom) for z in k]
        f=min(Q(1),sum(x))
        m=max(x)
        h=min(Q(1),m+c)
        ez=max(ez,abs(f-m))
        ene=max(ene,abs(f-h))
        assert abs(f-m)<=d and abs(f-h)<=c
    assert ez==d and ene==c
    a=[Q(0)]*n
    b=[Q(1,n)]*n
    assert min(Q(1),sum(b))-min(Q(1),sum(a))==1
    assert max(b)==Q(1,n)
    return n,ez,ene

if __name__=='__main__':
    for n in (2,3,4):
        print('grid',verify(n))
    print('FUZZY_APPROXIMATION_OK')
