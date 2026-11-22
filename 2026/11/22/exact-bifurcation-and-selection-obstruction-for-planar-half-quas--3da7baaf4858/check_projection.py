#!/usr/bin/env python3
"""Self-contained supplementary tests for two-dimensional half-quasinorm projection.

Run: python3 check_projection.py
Only standard-library Python is needed. Numerical scans supplement a complete analytic proof.
"""
from fractions import Fraction as F
from math import sqrt, isclose

# Polynomial identity, tested as an identity in two variables by exact coefficient
# evaluation on a 5x5 rational grid (degree <=4 in u and <=2 in t).
for i in range(5):
    u=F(i,4)
    v=u*(1-u)
    for j in range(5):
        t=F(j,4)
        lhs=(u*u-t)**2+((1-u)**2-t)**2
        rhs=2*v*v+4*(t-1)*v+1-2*t+2*t*t
        assert lhs==rhs,(u,t,lhs,rhs)


def d2(t):
    t=F(t)
    if t<=F(1,4): return F(0)
    if t<=F(3,4): return 2*(t-F(1,4))**2
    if t<=1: return 2*t-1
    return (t-1)**2+t*t


def points(t):
    t=float(t)
    if t<=0.25:return [(t,t)]
    if t<=0.75:return [(0.25,0.25)]
    if t<1:
        a=t-.5+sqrt(t-.75)
        b=t-.5-sqrt(t-.75)
        return [(a,b),(b,a)]
    return [(1.,0.),(0.,1.)]

# All boundary minima are found by the clipped optimum v, independent of
# numerical optimization. Compare numerical values of projection coordinates.
for k in range(1001):
    t=F(k,500)
    pts=points(t)
    assert len(pts)==(2 if t>F(3,4) else 1)
    for x,y in pts:
        assert x>=-1e-12 and y>=-1e-12
        assert isclose(sqrt(max(0,x))+sqrt(max(0,y)),1.,abs_tol=3e-8) if t>F(1,4) else True
        val=(x-float(t))**2+(y-float(t))**2
        assert isclose(val,float(d2(t)),abs_tol=3e-10,rel_tol=1e-10),(t,val,d2(t))

# Exact rational formula for the middle branch and exact algebraic optimum.
for k in range(251,1001):
    t=F(k,1000)
    v=max(F(0),min(F(1,4),1-t))
    objective=2*v*v+4*(t-1)*v+1-2*t+2*t*t
    assert objective==d2(t),(t,objective,d2(t))

# Dense independent boundary grid check at representative times.
for t in [0.27,0.5,0.741,0.7501,0.80,0.93,0.9999,1.0,1.22,2.0]:
    best=min(((i/5000)**2-t)**2+(((1-i/5000)**2)-t)**2 for i in range(5001))
    assert best+1e-11>=float(d2(t)),(t,best,d2(t))
    assert best-float(d2(t))<4e-7,(t,best,d2(t))

# Square-root splitting and distinct directional limits.
for k in range(1,100):
    d=k/1000
    a,b=points(.75+d)
    assert isclose(sqrt((a[0]-b[0])**2+(a[1]-b[1])**2),2*sqrt(2*d),abs_tol=1e-11)
print('PASS: exact polynomial and rational branch tests, dense boundary checks, and square-root splitting')
