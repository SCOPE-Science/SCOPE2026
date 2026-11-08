#!/usr/bin/env python3
"""Numerical illustration of characteristic exponents, not a proof of continuum statements."""
from math import log

def root(w, a, b):
    def f(s): return w*a**(-s)+(1-w)*b**(-s)-1.0
    lo=1.0e-9
    assert f(lo)<0.0
    hi=1.0
    while f(hi)<0.0:
        hi*=2.0
    for _ in range(110):
        mid=(lo+hi)/2.0
        if f(mid)>0.0: hi=mid
        else: lo=mid
    return (lo+hi)/2

def check(a,b,p):
    q=1-p
    assert 0<a<1<b and 0<p<1
    assert p*log(a)+q*log(b)>0 and p*log(b)+q*log(a)>0
    xm=(b-1)/(b-a); xp=(1-a)/(b-a)
    assert 0<xp<xm<1
    assert abs(a*xm-(1-b*(1-xm)))<1e-12
    assert abs(b*xp-(1-a*(1-xp)))<1e-12
    k0=root(p,a,b);k1=root(q,a,b)
    assert abs(p*a**(-k0)+q*b**(-k0)-1)<1e-12
    assert abs(p*b**(-k1)+q*a**(-k1)-1)<1e-12
    if p>q: assert k0<k1
    if p<q: assert k0>k1
    if p==q: assert abs(k0-k1)<1e-12
    for weight,k in ((p,k0),(q,k1)):
        func=lambda s:weight*a**(-s)+(1-weight)*b**(-s)
        assert func(k/2)<1 and func(k*1.5)>1
    return k0,k1

if __name__=='__main__':
    for a,b,p in [(1/3,8,11/20),(1/3,8,9/20),(.4,8,.5),(.2,9,.53)]:
        print('parameters',a,b,p,'roots',check(a,b,p))
    print('PASS: four parameter configurations (illustrative finite checks only)')
