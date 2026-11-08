#!/usr/bin/env python3
"""Supplementary arithmetic checks for the product-of-simplices ridge inequality.
All infinite-dimensional conclusions are established in the accompanying proof.
"""
from math import comb, factorial, sqrt, e
from itertools import product

def face(d,k):
    if k<0 or k>d:return 0.0
    return comb(d+1,k+1)*(d*(d+1))**(k/2)*sqrt(k+1)/factorial(k)

def convol(a,b):
    out=[0.]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def compositions(n):
    if n==0:
        yield ()
    else:
        for j in range(1,n+1):
            for rest in compositions(n-j):yield (j,)+rest

checks=0
smallest=(float('inf'), None)
for n in range(3,14):
    for dims in compositions(n):
        phi=[1.0]
        for d in dims:phi=convol(phi,[face(d,k) for k in range(d+1)])
        v=1.0
        diff=0.0
        for d in dims:
            v*=face(d,d)
            if d>=2:diff+=(d*(d-1)/2)*(1-sqrt((d-1)/(d+1)))
        predicted=v*(comb(n,2)-diff)
        assert abs(phi[n-2]-predicted) < 2e-10*max(1,predicted)
        ratio=phi[n-2]/(2**n*comb(n,2))
        assert ratio >= 1-1e-10, (dims,ratio)
        if abs(ratio-1)<1e-10:assert all(d==1 for d in dims)
        else:assert ratio>1
        if any(d>=2 for d in dims) and ratio<smallest[0]:smallest=(ratio,dims)
        checks+=3
alpha=1-1/sqrt(2)
beta=1-1/sqrt(3)
a2=3*sqrt(3)/4
assert beta<3*alpha
assert a2*(1-beta/3)>1
assert sqrt(6/e)>sqrt(2)
checks+=3
print('PASS: coefficient-convolution, codimension-two identity, sharp bound, and equality cases')
print('ordered compositions of dimensions 3..13:',checks//3-1)
print('supplementary assertions:',checks)
print('smallest non-cube quotient:',repr(smallest))
