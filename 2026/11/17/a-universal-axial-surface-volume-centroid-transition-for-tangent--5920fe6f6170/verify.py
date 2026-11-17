#!/usr/bin/env python3
"""Exact-moment and independent quadrature checks for tangential frustum centroid laws.

Only standard-library modules are required; all fixed rational moment tests are exact.
"""
from fractions import Fraction as F
from math import comb, sqrt, isclose

def moments(j,a):
    b=1-a
    I=sum((F(comb(j,k))*(-b)**k/F(k+1) for k in range(j+1)),F(0))
    J=sum((F(comb(j,k))*(-b)**k/F(k+2) for k in range(j+1)),F(0))
    return I,J

def exact(d,a):
    m=d-1; im,jm=moments(m,a); il,jl=moments(m-1,a)
    v=jm/im; ell=jl/il; u=m*il; b=1-a
    T=(v*(1+a**m)-a**m)/(u*(ell-v))
    assert T>b and ell>v
    return float(T),float(sqrt(float(T*T-b*b))),float(v),float(ell),float(u)

def simpson(f, count=4096):
    step=1/count
    return step/3*(f(0)+f(1)+4*sum(f(k*step) for k in range(1,count,2))+2*sum(f(k*step) for k in range(2,count,2)))

def independent_centroids(d,a,t):
    m=d-1; b=1-a; S=sqrt(t*t+b*b)
    V0=simpson(lambda z:(1-b*z)**m)
    V1=simpson(lambda z:z*(1-b*z)**m)
    L0=simpson(lambda z:(1-b*z)**(m-1))
    L1=simpson(lambda z:z*(1-b*z)**(m-1))
    return (a**m+m*S*L1)/(1+a**m+m*S*L0), V1/V0

checks=0
for d in range(2,13):
    for a in [F(0), F(1,7), F(1,3), F(2,3), F(9,10), F(99,100)]:
        T,h,v,ell,u=exact(d,a)
        if a==0:
            assert isclose(h,sqrt(d*d-1),rel_tol=1e-8,abs_tol=1e-8)
        if d==2:
            assert isclose(h,sqrt((float(a)+3)*(3*float(a)+1)),rel_tol=1e-9,abs_tol=1e-9)
        for factor in [F(1,2), F(1), F(2)]:
            t=float(factor)*h
            bs,bv=independent_centroids(d,float(a),t)
            assert abs(bv-v)<8e-11,(d,a,'volume',bv,v)
            delta=bs-bv
            if factor==1:
                assert abs(delta)<2e-10,(d,a,'crossing',delta)
            else:
                assert (delta>0)==(factor>1),(d,a,'sign',delta)
            checks+=1
for d in range(2,13):
    h0=exact(d,F(0))[1]
    hn=exact(d,F(9999,10000))[1]
    assert abs(hn-(4-2*1e-4))<0.004, (d,hn)
    if d>=3:
        hnear=exact(d,F(1,10000))[1]
        assert hnear<h0 and hn<4,(d,h0,hnear,hn)
    checks+=1
print('All %d exact-moment and independent quadrature assertions passed.'%checks)
