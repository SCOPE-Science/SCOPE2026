#!/usr/bin/env python3
"""Numerical consistency checks for an order-two Hermite interval Gram matrix.

Run: python3 strip_checker.py (Python standard library only).
These finite tests are not proofs of the universal assertions.
"""
import math
import random

SQRT_PI = math.sqrt(math.pi)
SQRT_2PI = math.sqrt(2 * math.pi)


def hermite(t):
    y = math.exp(-t*t/2) / math.pi**0.25
    return y, math.sqrt(2)*t*y


def matrix(a, x):
    lo, hi = x-a, x+a
    A = (math.erf(hi)-math.erf(lo))/2
    B = (math.exp(-lo*lo)-math.exp(-hi*hi))/SQRT_2PI
    C = A + (lo*math.exp(-lo*lo)-hi*math.exp(-hi*hi))/SQRT_PI
    return A, B, C


def top(a, x):
    A, B, C = matrix(a, x)
    return (A+C+math.hypot(A-C,2*B))/2


def quadrature(a, x, N=2000):
    assert N % 2 == 0
    lo=x-a; step=2*a/N
    sums=[0.,0.,0.]
    for k in range(N+1):
        t=lo+k*step; u,v=hermite(t)
        w=1 if k in (0,N) else 4 if k%2 else 2
        sums[0]+=w*u*u; sums[1]+=w*u*v; sums[2]+=w*v*v
    return [x*step/3 for x in sums]


def tail(a,x):
    assert 0 <= x < a
    t1,t2=a-x,a+x
    e1,e2=math.exp(-t1*t1),math.exp(-t2*t2)
    p1,p2=math.erfc(t1)/2,math.erfc(t2)/2
    m1,m2=e1/SQRT_2PI,e2/SQRT_2PI
    v1,v2=p1+t1*e1/SQRT_PI,p2+t2*e2/SQRT_PI
    det1=p1*v1-m1*m1
    det2=p2*v2-m2*m2
    determinant=det1+det2+p1*v2+p2*v1+2*m1*m2
    tr=p1+p2+v1+v2
    return 2*determinant/(tr+math.sqrt(max(0.,tr*tr-4*determinant)))


def golden_min(fun,low,high):
    r=(math.sqrt(5)-1)/2
    c=high-r*(high-low);d=low+r*(high-low)
    for _ in range(180):
        if fun(c)<fun(d):
            high=d; d=c; c=high-r*(high-low)
        else:
            low=c; c=d; d=low+r*(high-low)
    return (low+high)/2


def run():
    nchecks=0
    rng=random.Random(311703)
    for _ in range(85):
        a=0.04+3.1*rng.random(); x=5*rng.random()-2.5
        direct=matrix(a,x); quad=quadrature(a,x,1200)
        for u,v in zip(direct,quad):
            assert abs(u-v)<1.8e-9,(a,x,u,v)
            nchecks+=1
        assert abs(top(a,x)-top(a,-x))<2e-14
        nchecks+=1
    for a in (0.1,0.5,1.,2.,3.,5.):
        curvature=4*a*math.exp(-a*a)/SQRT_PI
        h=0.0005 if a<3 else 0.002
        observed=(top(a,h)+top(a,-h)-2*top(a,0))/h**2
        assert abs(observed-curvature)<max(3e-6,abs(curvature)*3e-4),(a,curvature,observed)
        assert top(a,h)>top(a,0)
        nchecks+=2
    for a in (0.015,0.025,0.045):
        optimum=golden_min(lambda x:-top(a,x),0.15,1.5)
        assert abs(optimum-1/math.sqrt(2))<0.004
        assert abs(top(a,optimum)/a-4*math.exp(-.5)/SQRT_PI)<0.02
        nchecks+=2
    for a in (2.,3.,4.,5.,7.,10.,15.):
        xm=golden_min(lambda x:tail(a,x),0.01,min(a/2,2.0))
        assert abs(a*xm-math.log(2*a))<0.25,(a,xm)
        asym=math.exp(-a*a)/(SQRT_PI*a**3)
        assert 0.70<tail(a,xm)/asym<1.2,(a,xm,tail(a,xm)/asym)
        assert tail(a,xm)<tail(a,0)
        nchecks+=3
    for _ in range(25):
        a=1.5+3*rng.random();x=a*.5*rng.random()
        assert abs((1-top(a,x))-tail(a,x))<3e-13
        nchecks+=1
    print('ORDER_TWO_STRIP_CHECKS_PASS',nchecks)

if __name__=='__main__':run()
