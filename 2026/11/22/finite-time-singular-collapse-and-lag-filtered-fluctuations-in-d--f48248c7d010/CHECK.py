#!/usr/bin/env python3
"""Exact-rational finite consistency tests for the displayed delayed tent theorem.

The mathematical proof in RESULT.md is required for the all-dimensional claim;
these tests cover finitely many rational states and polynomial identities only.
"""
from fractions import Fraction as F
from itertools import product

ZERO=F(0)
ONE=F(1)

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return tuple(a)

def add(a,b):
    return trim([(a[i] if i<len(a) else ZERO)+(b[i] if i<len(b) else ZERO) for i in range(max(len(a),len(b)))])

def mul(a,b):
    c=[ZERO]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)

def scale(a,t): return trim([t*x for x in a])

def compose(a,v):
    out=(ZERO,)
    for x in reversed(a):out=add(mul(out,v),(x,))
    return out

def P(a):
    plus=(F(1,2),F(-1,2));minus=(F(-1,2),F(1,2))
    return scale(add(compose(a,plus),compose(a,minus)),F(1,2))

def integral(a):
    return sum((a[i]/F(i+1) if i%2==0 else ZERO) for i in range(len(a)))

x=(ZERO,ONE)
b=(F(-1,3),ZERO,ONE)
assert P(x)==(ZERO,)
assert P(b)==add(scale(b,F(1,4)),scale(x,F(-1,2)))
assert integral(mul(b,b))==F(4,45)
assert integral(mul(x,b))==0
q=b
for j in range(1,9):
    q=P(q)
    rhs=add(scale(b,F(1,4)**j),scale(x,F(-1,2)*F(1,4)**(j-1)))
    assert q==rhs
    assert integral(mul(b,q))==F(4,45)*F(1,4)**j
assert F(4,45)*(1+2*F(1,4)/(1-F(1,4)))==F(4,27)

T=lambda t:F(1)-2*abs(t)
def iterate(v,k):return (T(v[k-1]),)+v[:-1]
def H(u,d,k):
    v=[None]*d
    v[d-k:]=u
    for j in range(d-k-1,-1,-1):v[j]=T(v[j+k])
    return tuple(v)
def G(u):return (T(u[-1]),)+u[:-1]

candidates=[F(-1),F(-2,3),F(-1,5),ZERO,F(2,7),F(3,4),ONE]
c=0
for d in range(2,10):
    for k in range(1,d):
        for seed in range(49):
            u=tuple(candidates[(seed+3*j)%len(candidates)] for j in range(k))
            v=tuple(candidates[(seed+5*j)%len(candidates)] for j in range(d))
            w=v
            for _ in range(d-k):w=iterate(w,k)
            assert w==H(v[:k],d,k)
            assert iterate(H(u,d,k),k)==H(G(u),d,k)
            g=u
            for _ in range(k):g=G(g)
            assert g==tuple(T(z) for z in u)
            c+=1
# Inversion of stationary covariance's Fourier expansion at zero:
for k in range(1,13):
    z=F(1,4)
    assert F(4,45)*(1-z*z)/(1+z*z-2*z)==F(4,27)
print('PASS: rational transfer identities, 8 covariance lags,',c,'graph cases, and variance/spectral checks')
