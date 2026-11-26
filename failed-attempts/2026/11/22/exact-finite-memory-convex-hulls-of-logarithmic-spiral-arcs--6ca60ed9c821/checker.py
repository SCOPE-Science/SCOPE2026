#!/usr/bin/env python3
"""Independent polygonal-hull diagnostics for exact logarithmic-spiral hull formulas.
Uses Python's standard library; discretization is only a numerical check, not the proof.
"""
import math
import sys

def tangency_lag(a):
    lo, hi = math.pi, 2*math.pi
    def g(x): return math.exp(a*x)*(math.cos(x)-a*math.sin(x))
    for _ in range(85):
        mid = (lo+hi)/2
        if g(mid) < 1.0: lo=mid
        else: hi=mid
    return (lo+hi)/2

def formulas(a,T):
    ell=tangency_lag(a)
    h=min(T,ell)
    q=math.exp(-a*h)
    d=math.hypot(1-q*math.cos(h),q*math.sin(h))
    p=math.sqrt(1+a*a)/a*(1-q)+d
    area=(1-q*q)/(4*a)-0.5*q*math.sin(h)
    return ell,p,area

def cross(o,a,b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

def hull(points):
    pts=sorted(set(points))
    lower=[]
    for p in pts:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0:
            lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(pts):
        while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:
            upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]

def polygon_stats(poly):
    P=A=0.0
    for u,v in zip(poly,poly[1:]+poly[:1]):
        P+=math.hypot(u[0]-v[0],u[1]-v[1])
        A+=u[0]*v[1]-u[1]*v[0]
    return P, abs(A)/2

def run():
    cases=0
    for a in (0.05,0.2,0.75,1.5,4):
        ell=tangency_lag(a)
        assert math.pi<ell<2*math.pi
        g=lambda v:math.exp(a*v)*(math.cos(v)-a*math.sin(v))
        assert abs(g(ell)-1)<1e-8
        for T in (0.4,1,2.2,ell-0.18,ell,ell+0.18,7,10):
            tvals=[T*j/4000 for j in range(4001)]
            pts=[(math.exp(a*(t-T))*math.cos(t-T),
                  math.exp(a*(t-T))*math.sin(t-T)) for t in tvals]
            pp,ar=polygon_stats(hull(pts))
            _,p_exact,a_exact=formulas(a,T)
            assert abs(pp-p_exact) < 0.00014, (a,T,pp,p_exact)
            assert abs(ar-a_exact) < 0.00014, (a,T,ar,a_exact)
            cases+=1
        # verify no earlier support point beats the last ell interval
        T=12.0
        ts=[-T*j/4000 for j in range(4001)]
        old=[t for t in ts if t<-ell]
        new=[t for t in ts if t>=-ell]
        for j in range(120):
            ph=2*math.pi*j/120
            def s(t):return math.exp(a*t)*math.cos(t-ph)
            assert max(s(t) for t in old) <=max(s(t) for t in new)+0.000001
    print("PASS:",cases,"polygonal hull comparisons, 600 support comparisons; finite numerical checks only.")

if __name__=="__main__": run()
