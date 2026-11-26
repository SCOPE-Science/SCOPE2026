#!/usr/bin/env python3
"""Finite exact rational replay of the explicit state inclusions; not a proof for all real parameters."""
from fractions import Fraction as Q

def f(b, x):
    return b*x+(1-b/2) if x<Q(1,2) else b*(x-Q(1,2))

def check(b):
    L=1-b/2; R=b/2; s=b*(b-1)/2; d=1-s
    assert Q(0)<s<Q(1,2)<d<Q(1)
    assert b*(d-Q(1,2))>=L
    assert L+b*s<=R
    assert L*(b+1)==d
    # Certificates for all possible graph arrows, by monotone affine endpoint images.
    assert 0<=L<=R<=1
    assert L<=b*(d-Q(1,2)) and R<=1   # even -2 to odd -1
    assert 0<=L and L+b*s<=R           # even +2 to odd +1
    assert d==b*L+L                    # odd -1 left to even -2
    assert s==b*(R-Q(1,2))           # odd +1 right to even +2
    for j in range(33):
        x=Q(j,32)
        z=x; B=0
        for n in range(401):
            if n%2==0:
                assert (B==0 and 0<=z<=1) or (B==-2 and d<=z<=1) or (B==2 and 0<=z<=s), (b,j,n,B,z)
            else:
                assert (B==-1 and L<=z<=1) or (B==1 and 0<=z<=R), (b,j,n,B,z)
            B += -1 if z<Q(1,2) else +1
            z=f(b,z)
    assert f(b,0)<Q(1,2)<f(b,1)
    print('rational graph and orbit replay OK:',b)

if __name__=='__main__':
    for b in (Q(7,6),Q(5,4),Q(4,3),Q(7,5)):
        check(b)
