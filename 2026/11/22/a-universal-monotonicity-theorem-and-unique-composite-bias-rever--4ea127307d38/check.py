#!/usr/bin/env python3
"""Reproducible finite checks of the classical spatial curve-number theorem.

Scientific definitions and the infinite proof are in RESULT.md. Run: python check.py
"""
import math
import random

S0 = 254.0

def runoff(p, s, lam):
    if p <= lam*s:
        return 0.0
    return (p - lam*s)**2 / (p + (1.0-lam)*s)

def runoff_p(p, s, lam):
    if p <= lam*s:
        return 0.0
    z = (p-lam*s)/(p+(1-lam)*s)
    return 2*z-z*z

def retention(c):
    return S0*(1/c-1)

def mean_runoff(p, masses, cs, lam):
    return sum(w*runoff(p, retention(c),lam) for w,c in zip(masses,cs))

def effective_s(p, masses, cs, lam):
    yy=mean_runoff(p,masses,cs,lam)
    if yy==0:
        raise ValueError('equivalent retention undefined at zero runoff')
    lo=min(retention(c) for c in cs)
    hi=min(max(retention(c) for c in cs),p/lam)
    for _ in range(90):
        m=(lo+hi)/2
        if runoff(p,m,lam)>yy:
            lo=m
        else:
            hi=m
    return (lo+hi)/2

def all_tests():
    n=0
    def near(x,y,rtol=3e-10,atol=1e-10):
        nonlocal n
        assert abs(x-y)<=atol+rtol*max(abs(x),abs(y)),(x,y)
        n+=1
    rng=random.Random(1450)
    # Exact benchmark, with two local CNs and the standard 20% abstraction.
    cs=[0.5,0.9]
    ws=[0.4,0.6]
    lam=0.2
    comp=retention(sum(w*c for w,c in zip(ws,cs)))
    def diff(p):return mean_runoff(p,ws,cs,lam)-runoff(p,comp,lam)
    lo=20.0; hi=500.0
    for _ in range(80):
        mid=(lo+hi)/2
        if diff(mid)>0:lo=mid
        else:hi=mid
    star=(lo+hi)/2
    near(star,228.09380830095736,rtol=1e-12)
    near(diff(50),7.749325559601049)
    near(diff(350),-6.116116506281742)
    for _ in range(2000):
        lam=0.05+0.9*rng.random()
        cs=[0.25+0.7*rng.random() for _ in range(rng.randrange(2,9))]
        weights=[0.1+rng.random() for _ in cs]
        den=sum(weights)
        ws=[w/den for w in weights]
        # Stay well away from first-runoff threshold to avoid tiny numerical runoff.
        p0=lam*min(retention(c) for c in cs)
        p1=max(p0+10,2*p0)
        pp=[p1*(1.7**j) for j in range(5)]
        ss=[effective_s(p,ws,cs,lam) for p in pp]
        for a,b in zip(ss,ss[1:]):
            assert b>a-3e-9, (cs,lam,pp,ss)
            n+=1
        assert ss[0]>=min(retention(c) for c in cs)-1e-10
        n+=1
        for p,s in zip(pp,ss):
            near(runoff(p,s,lam),mean_runoff(p,ws,cs,lam))
            assert 0<1/(1+s/S0)<1
            n+=1
        # Differentiate directly and check the universal response-speed identity.
        s=retention(cs[0]); p=pp[2]
        if p>lam*s:
            h=1e-5*max(1.0,p)
            near((runoff(p+h,s,lam)-runoff(p-h,s,lam))/(2*h),runoff_p(p,s,lam),rtol=1e-8)
    print(f'PASS: {n} finite checks; 2,000 heterogeneous distributions; benchmark crossover {star:.12f} mm')
if __name__=='__main__':all_tests()
