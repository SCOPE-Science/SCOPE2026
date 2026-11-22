#!/usr/bin/env python3
"""Standalone exact checks for central Delannoy quartic-character correlations."""
from fractions import Fraction
from functools import lru_cache
from math import comb

# Phases 1,i,-1,-i are encoded by exponent in Z/4Z.
def phase(n):
    v=0
    while n:
        if n%5 in (1,2,3): v+=1
        n//=5
    return v%4

def cmul(z, w):
    return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])

def phi(n):
    return ((1,0),(0,1),(-1,0),(0,-1))[phase(n)]

@lru_cache(None)
def corr(h):
    if h==0: return Fraction(1)
    if h==1: return Fraction(1,2)
    a,r=divmod(h,5)
    if r==0: return corr(a)
    ca,cb=corr(a),corr(a+1)
    return ( ((2*ca+cb) if r==1 else ca if r==2 else cb if r==3 else ca+2*cb) / 5 )

def delannoy(n):
    return sum(comb(n,j)**2 * 2**j for j in range(n+1))

def direct_block(N,h):
    re=im=0
    for n in range(N):
        z1=phi(n+h);z0=phi(n)
        re+=z1[0]*z0[0]+z1[1]*z0[1]
        im+=z1[1]*z0[0]-z1[0]*z0[1]
    return re,im

def main():
    checks=0
    for n in range(190):
        assert pow(3, sum(d in (1,2,3) for d in digits(n)), 5) == delannoy(n)%5
        checks+=1
    for h in range(1,5000):
        assert 0<corr(h)<=Fraction(1,2)
        eq=(corr(h)==Fraction(1,2))
        v=h
        while v%5==0:v//=5
        assert eq == (v==1)
        checks+=2
    for r in range(1,8):
        total=sum((corr(h) for h in range(5**r)),Fraction(0))
        assert total==Fraction(1,4)+Fraction(3,4)*Fraction(13,5)**r
        assert corr((5**r-1)//2)==Fraction(1,5**r)
        checks+=2
    for r in range(1,6):
        N=5**r
        for h in range(1, min(90,N)):
            re,im=direct_block(N,h)
            assert abs(Fraction(re)-N*corr(h)) <= 2*h, (N,h,re,corr(h))
            assert abs(im)<=2*h,(N,h,im)
            checks+=2
    print('PASS:', checks, 'exact assertions; modular Delannoy formula, all-lag bounds, extremal equality, lag sum, finite quintary-block error bound')

def digits(n):
    if n==0:return [0]
    ds=[]
    while n:ds.append(n%5);n//=5
    return ds

if __name__=='__main__':main()
