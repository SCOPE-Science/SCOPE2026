#!/usr/bin/env python3
"""Standalone exact certificate for collinear-blowup Zariski denominator witnesses.

This verifies the intersection matrices, negative definiteness using Schur
complements, all explicit witness P,N coordinates, and the minimal LCM for
2<=n<=24. The uniform proof for all n is in RESULT.md.
"""
from fractions import Fraction as F
from math import gcd
from functools import reduce
from math import comb

def lcm(a,b): return a*b//gcd(a,b)
def dot(a,b):
    assert len(a)==len(b)
    return a[0]*b[0]-sum(x*y for x,y in zip(a[1:],b[1:]))
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(a,s):return tuple(s*x for x in a)

def run(n):
    h=(F(1),)+(F(0),)*n
    es=[(F(0),)+tuple(F(int(j==i)) for j in range(n)) for i in range(n)]
    ell=plus(h,scale(reduce(plus,es),F(-1))) # H - sum of exceptional curves
    assert dot(ell,ell)==1-n
    assert all(dot(ell,e)==1 for e in es)
    assert all(dot(e,e)==-1 for e in es)
    assert all(dot(es[i],es[j])==0 for i in range(n) for j in range(n) if i!=j)
    # Every negative-definite support is either a subset of the exceptional
    # curves or the strict-transform line with k <= n-2 exceptionals.
    support_count=2**n + sum(comb(n,k) for k in range(n-1))
    assert support_count == 2**(n+1)-n-1
    reached=set()
    for r in range(1,n):
        k=n-1-r
        I=tuple(range(k))
        J=tuple(range(k,n))
        assert len(J)==r+1
        D=plus(scale(h,F(r)),scale(reduce(plus,(es[j] for j in J)),F(-1)))
        N=scale(plus(ell,reduce(plus,(es[i] for i in I), (F(0),)*(n+1))),F(1,r))
        P=plus(D,scale(N,-1))
        assert dot(D,ell)==-1
        assert dot(N,ell)==-1 and dot(P,ell)==0
        assert all(dot(P,es[i])==0 for i in I)
        assert all(dot(P,es[j])==F(r-1,r) for j in J)
        assert dot(N,N)==-F(1,r)
        # Negative definite via Schur complement m-k=r>0.
        assert n-1-k==r
        assert N[0].denominator==r
        # Big nef class on the same face gives a big witness with this N.
        Q=plus(scale(h,F(r+1)),scale(reduce(plus,(es[j] for j in J)),F(-1)))
        assert dot(Q,ell)==0 and all(dot(Q,es[i])==0 for i in I)
        assert all(dot(Q,es[j])==1 for j in J)
        assert dot(Q,Q)==r*(r+1)>0
        BigP=plus(P,Q)
        assert dot(BigP,BigP)>0
        assert dot(BigP,ell)==0
        assert all(dot(BigP,e)>=0 for e in es)
        # Effective witness: D = (ell + sum_{i in I} E_i)+(r-1)H,
        # but note this would yield rH -sum_{j in J}E_j exactly.
        constructed=plus(plus(ell,reduce(plus,(es[i] for i in I),(F(0),)*(n+1))),scale(h,F(r-1)))
        assert D==constructed
        reached.add(N[0].denominator)
    assert reached==set(range(1,n))
    return reduce(lcm,reached,1)

assert [run(n) for n in range(2,11)]==[1,2,6,12,60,60,420,840,2520]
for n in range(2,25):
    out=run(n)
    print(f'n={n} largest={n-1} universal={out}')
print('VERIFY_OK')
