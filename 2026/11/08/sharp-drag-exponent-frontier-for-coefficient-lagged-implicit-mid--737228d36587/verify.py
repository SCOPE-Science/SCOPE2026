#!/usr/bin/env python3
"""Supplementary reproducible checks for a scalar coefficient-lagged midpoint analysis."""
from fractions import Fraction as Q
from math import sqrt, log, isclose
from random import Random

def f(x,A,B,y):
    return x/(A+B*y*y)

def check():
    rng=Random(20261103)
    checks=0
    # Exact rational 2-cycle algebra, no floating tolerance.
    for _ in range(2500):
        A=Q(rng.randint(2,10),rng.randint(1,5))
        B=Q(rng.randint(1,10),rng.randint(1,5))
        # parameterize a two-cycle via arbitrary rational y,z with yz=A/B
        y=Q(rng.randint(1,20),rng.randint(1,10))
        z=A/(B*y)
        x=A*(y+z)
        assert f(x,A,B,y)==z and f(x,A,B,z)==y
        assert x*x>=4*A*A*A/B
        deriv=4*A*A*A/(B*x*x)
        assert deriv<=1
        checks+=1
    # Check explicit transition and limits from the physical initial guess y_0=x.
    for A,B,x in [(1.5,2.,1.),(2.,1.,4.),(2.,1.,8.),(1.2,4.,5.),(1.8,0.6,11.)]:
        xcrit=2*A**1.5/sqrt(B)
        v=x
        for i in range(4000):
            v=f(x,A,B,v)
        if x<xcrit-1e-9:
            assert abs(v-f(x,A,B,v))<1e-9
        elif x>xcrit+1e-9:
            lo=(x/A-sqrt((x/A)**2-4*A/B))/2
            hi=(x/A+sqrt((x/A)**2-4*A/B))/2
            assert min(abs(v-lo),abs(v-hi))<1e-7
            assert abs(f(x,A,B,lo)-hi)<1e-10
            assert abs(f(x,A,B,hi)-lo)<1e-10
        checks+=1
    # General exponent threshold (analytic derivative at root) and log contraction.
    for m in [0.25,0.5,1.,1.25,1.5,2.,3.,4.]:
        for s,b in [(0.1,0.4),(0.8,1.3),(2.,3.)]:
            D=lambda y:1+s*(1+b*y*y)**(m/2)
            elast=lambda y:m*(b*y*y/(1+b*y*y))*(s*(1+b*y*y)**(m/2)/(1+s*(1+b*y*y)**(m/2)))
            assert all(elast(y+1.e-6)<elast(2*y+2.e-6) for y in [0.01,0.1,1.,10.])
            if m<=1:
                for x in [0.1,1.,10.,100.]:
                    y=x
                    q=elast(x)
                    assert 0<q<1
                    lo=0;hi=x
                    for z in range(200):
                        mid=(lo+hi)/2
                        if mid*D(mid)<x:lo=mid
                        else:hi=mid
                    root=(hi+lo)/2
                    for k in range(35):
                        assert abs(log(y/root)) <= q**k*abs(log(x/root))+5e-12
                        y=x/D(y)
                    checks+=1
            else:
                # analytic unique y at q(y)=1
                lo=0.;hi=1.
                while elast(hi)<1:hi*=2
                for z in range(100):
                    mid=(lo+hi)/2
                    if elast(mid)<1:lo=mid
                    else:hi=mid
                yc=(lo+hi)/2
                xc=yc*D(yc)
                x=1.8*xc
                rootlo=0.;roothi=x
                for z in range(200):
                    mid=(rootlo+roothi)/2
                    if mid*D(mid)<x:rootlo=mid
                    else:roothi=mid
                root=(rootlo+roothi)/2
                assert elast(root)>1
                y=x
                for z in range(3000):y=x/D(y)
                assert abs(y-root)>1.e-4*root
                assert abs(x/D(x/D(y))-y)<max(1e-8,1e-8*x)
                checks+=1
    # Actual two-midpoint-stage frozen-alpha solve: equal stages for equal guesses.
    for _ in range(400):
        x=Q(rng.randint(1,20),rng.randint(1,10))
        eps=Q(rng.randint(1,8),rng.randint(1,8))
        h=Q(rng.randint(1,12),rng.randint(1,12))
        alpha=Q(rng.randint(1,12),rng.randint(1,6))
        # M=(1/4)[[1,1],[1,1]]; source velocity rate -(1+eps)alpha*y
        y=x/(1+(h/2)*(1+eps)*alpha)
        K=-(1+eps)*alpha*y
        assert y == x + h*(K+K)/4
        checks+=1
    return checks

if __name__=='__main__':
    n=check()
    print(f'VERIFY_OK {n} finite checks (analytic infinite-parameter proof separate)')
