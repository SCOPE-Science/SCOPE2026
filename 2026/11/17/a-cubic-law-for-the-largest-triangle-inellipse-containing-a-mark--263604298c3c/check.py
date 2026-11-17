#!/usr/bin/env python3
"""Independent numerical and exact-arithmetic checks of a point-constrained triangle inellipse formula."""
from math import sqrt, pi, isclose
from fractions import Fraction as Q
import random

def F(u,w):
    z=[u[i]*w[i] for i in range(3)]
    return sum(v*v for v in z)-2*sum(z[i]*z[j] for i,j in ((0,1),(0,2),(1,2)))

def is_inside(u,w,atol=1e-12):
    return F(u,w)<=atol

def solution(w):
    if 2*sum(x*x for x in w)<=1+1e-14:
        return [1/3]*3
    k=next(i for i in range(3) if sqrt(w[i])>sum(sqrt(w[j]) for j in range(3) if j!=i))
    inds=[k]+[j for j in range(3) if j!=k]
    A,B,C=[1/w[j] for j in inds]
    def pol(q): return (A+B)*q**3+(A+2*B)*q**2-(A+2*C)*q-(A+C)
    lo,hi=0.,1.
    while pol(hi)<0:hi*=2
    for _ in range(100):
        mid=(lo+hi)/2
        if pol(mid)>0:hi=mid
        else:lo=mid
    q=(lo+hi)/2
    den=A*(1+q)**2+B*q*q+C
    v=[A*(1+q)**2/den,B*q*q/den,C/den]
    out=[None]*3
    for i,x in zip(inds,v): out[i]=x
    return out

def area_ratio(u): return pi*sqrt(u[0]*u[1]*u[2])

# Exact rational identities on a full off-center median example.
w=[Q(4,5),Q(1,10),Q(1,10)]
u=[Q(1,5),Q(2,5),Q(2,5)]
assert F(u,w)==0
assert sum(u)==1
assert u[0]*u[1]*u[2]==Q(4,125)
assert isclose(area_ratio([float(a) for a in u]),2*pi/(5*sqrt(5)),rel_tol=1e-14)

# Randomized independent conic and numerical feasible competitors.
rng=random.Random(20261114)
N=500
for idx in range(N):
    w0=[rng.gammavariate(0.8,1) for _ in range(3)]
    w=[x/sum(w0) for x in w0]
    u=solution(w)
    assert abs(sum(u)-1)<1e-12 and min(u)>0
    assert is_inside(u,w,atol=2e-12)
    if sum(x*x for x in w)>0.50000001:
        assert abs(F(u,w))<2e-12
    assert area_ratio(u)<=pi/(3*sqrt(3))+1e-12
    # Check directly from the quadratic equation that the resulting conic is elliptic.
    prod=u[0]*u[1]*u[2]
    assert prod>0
    # Independently sample feasible inellipse parameters over the entire simplex.
    for _ in range(600):
        a,b,c=[rng.expovariate(1) for j in range(3)]
        v=[a/(a+b+c),b/(a+b+c),c/(a+b+c)]
        if is_inside(v,w,atol=0):
            assert area_ratio(v)<=area_ratio(u)+2e-9,(w,u,v)

# Exact phase boundary and two derivatives for the vertex-median restriction.
for t in [0.02, 0.33, 2/3, 0.71, 0.81,0.99]:
    w=[t,(1-t)/2,(1-t)/2]
    u=solution(w)
    if t<=2/3:
        assert all(abs(x-1/3)<1e-12 for x in u)
    else:
        target=[1-t,t/2,t/2]
        assert max(abs(x-y) for x,y in zip(u,target))<1e-12
        assert isclose(area_ratio(u),pi*t*sqrt(1-t)/2,rel_tol=1e-12)
print('POINT_CONSTRAINED_TRIANGLE_INELLIPSE_CHECKS_OK')
