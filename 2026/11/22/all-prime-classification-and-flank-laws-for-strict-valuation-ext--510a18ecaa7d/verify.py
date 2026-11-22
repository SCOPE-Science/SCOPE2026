#!/usr/bin/env python3
"""Exact integer checks for the local valuation-extrema theorem for ternary Fuss-Catalan numbers."""
from math import comb

PRIMES=(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61)
LIMIT=20000
checks=0

def vp(x,p):
    if x==0: raise ValueError('valuation of zero')
    k=0
    while x%p==0:
        k+=1
        x//=p
    return k

def factorial_v(n,p):
    total=0
    while n:
        n//=p
        total+=n
    return total

def val_F(n,p):
    return factorial_v(3*n,p)-factorial_v(2*n,p)-factorial_v(n,p)-vp(2*n+1,p)

def jump(n,p):
    return vp(3,p)+vp(3*n+1,p)+vp(3*n+2,p)-vp(2,p)-vp(n+1,p)-vp(2*n+3,p)

def peak_class(n,p):
    return ((p==2 and n%4==3) or
            (p==3 and n%9==8) or
            (p==5 and n%5==4) or
            (p==11 and n%11==4) or
            (p==13 and n%13==5))

def valley_class(n,p):
    return p==3 and n%9==4

def peak_gaps(n,p):
    if p==2:return vp(3*n-1,2)-1,vp(n+1,2)
    if p==3:return 1,vp(n+1,3)-1
    if p==5:return vp(3*n-2,5),vp(n+1,5)
    if p==11:return vp(3*n-1,11),vp(2*n+3,11)
    if p==13:return vp(3*n-2,13),vp(2*n+3,13)
    raise ValueError('no peaks')

for p in PRIMES:
    vals=[val_F(n,p) for n in range(LIMIT+1)]
    for n in range(1,LIMIT):
        left=vals[n]-vals[n-1]
        right=vals[n]-vals[n+1]
        assert left==jump(n-1,p)
        assert right==-jump(n,p)
        assert (left>0 and right>0)==peak_class(n,p),(p,n,left,right)
        assert (left<0 and right<0)==valley_class(n,p),(p,n,left,right)
        if left>0 and right>0:
            assert (left,right)==peak_gaps(n,p),(p,n,left,right)
            if p in (5,11,13):assert min(left,right)==1
            if p==2:assert left==1 or right==2
            if p==3:assert left==1
        if p==3 and left<0 and right<0:
            assert (-left,-right)==(vp(2*n+1,3)-1,1)
        checks+=6
    # Independent direct binomial calculation for small n, without using v((3n)!).
    for n in range(60):
        F=comb(3*n,n)//(2*n+1)
        assert val_F(n,p)==vp(F,p)
        checks+=1
print('PASS:',checks,'exact assertions over',len(PRIMES),'primes, n <',LIMIT)
