#!/usr/bin/env python3
"""Reproducibility diagnostics for the oscillatory sewing-field basin/rate theorem."""
import math
from fractions import Fraction

N=27
R=Fraction(2,N)
assert 2*float(R)**2+math.pi*float(R)<1

def H(r,k):
    if r==0: return 0.0
    return r*r-r**(2*k)*math.sin(2*math.pi/r)
def G(r,k):
    if r==0: return 0.0
    return r*r+r**(2*k)*math.sin(2*math.pi/r)
def P(r,k):
    v=G(r,k); a,b=0.0,float(R)
    for j in range(75):
        c=(a+b)/2
        if H(c,k)<v:a=c
        else:b=c
    return (a+b)/2

def mu(n,k):
    z=(-1)**n*math.pi*(2/n)**(2*k-3)
    return (1-z)/(1+z)
def neg_rate(n,k):
    z=math.pi*(2/n)**(2*k-3)
    return n/4*math.atanh(z)

# Exact arithmetic: basin lengths and complete probability tail.
for L in (2,5,25,250):
    S=sum((Fraction(4,n*n-1) for n in range(N+1,N+1+2*L,2)),Fraction(0))
    K=N+1+2*L
    assert S+Fraction(2,K-1)==R
    W=sum((Fraction(2*N,n*n-1) for n in range(N+1,N+1+2*L,2)),Fraction(0))
    assert W+Fraction(N,K-1)==1

# Floating diagnostic only: the proof establishes monotonicity and invariance analytically.
for k in (2,3,4,6):
    for n in (28,29,30,31,32,33,42,43):
        a,b=2/(n+1),2/n
        for factor in (0.2,0.5,0.8):
            r=a+factor*(b-a)
            s=P(r,k)
            assert a<s<b,(k,n,r,s,a,b)
            assert (s>r)==(math.sin(2*math.pi/r)>0),(k,n,r,s)
        if n%2==0:
            assert 0<mu(n,k)<1
        else:
            assert mu(n,k)>1
    for n in (28,30,60):
        z=math.pi*(2/n)**(2*k-3)
        assert abs(mu(n,k)-(1-z)/(1+z))<1e-14
        assert neg_rate(n,k)>0

assert neg_rate(28,2)>math.pi/2
assert neg_rate(2000,2)>math.pi/2
assert abs(neg_rate(2000,2)-math.pi/2)<0.00001
for k in (3,4,5):
    q=2*k-4
    A=math.pi*2**(2*k-5)
    for n in (100,500,1000):
        relative=neg_rate(n,k)/(A*n**(-q))
        assert abs(relative-1)<2e-5,(n,k,relative)
print('SEWED_FOCUS_BASIN_RATE_CHECK_OK')
