#!/usr/bin/env python3
"""Standalone consistency tests for the harvested Holling-II Ricker map.

Finite checks do not establish the asymptotic theorem; see RESULT.md for proof.
"""
from fractions import Fraction as Q
from math import exp,log,isfinite


def step(x,y,a,b,d,s):
    return (x*exp(1-a-x-y/(b+x)),y*exp(d*x/(b+x)-s))


def algebraic_checks():
    cases=[(Q(3,10),Q(2,5),Q(6,5)),
           (Q(7,10),Q(3),Q(7,10)),
           (Q(1,10),Q(1,20),Q(4)),
           (Q(1,5),Q(5,2),Q(1))]
    for a,b,d in cases:
        r=1-a
        s=d*r/(b+r)
        k=d*b/(b+r)**3
        pred_y=(b+r)**3/(d*b)
        pred_prey=(b+r)**2/(d*b)
        A=1-r
        B=-r/(b+r)
        limit_ratio=B/(1-A)
        assert limit_ratio == -1/(b+r)
        assert k*pred_y == 1
        assert pred_prey == -limit_ratio*pred_y
        assert d*r/(b+r)-s == 0
    return cases


def critical_checks(cases):
    count=0
    for a,b,d in cases:
        aa,bb,dd=float(a),float(b),float(d)
        r=1-aa
        s=dd*r/(bb+r)
        yy=(bb+r)**3/(dd*bb)
        xx=(bb+r)**2/(dd*bb)
        # Chosen nonzero starts remain away from underflow and boundary roundoff.
        for x,y in [(r+0.05,0.08),(r-0.06,0.05)]:
            for n in range(1,200001):
                x,y=step(x,y,aa,bb,dd,s)
                assert isfinite(x) and isfinite(y) and x>0 and y>0
            assert abs(n*y/yy-1)<0.04,(aa,bb,dd,'predator',n*y/yy)
            assert abs(n*(r-x)/xx-1)<0.04,(aa,bb,dd,'prey',n*(r-x)/xx)
            count+=1
    return count


def strict_checks():
    count=0
    for a,b,d,s in [(0.3,0.4,1.2,1.0),(0.2,2.5,1.,0.8)]:
        r=1-a
        delta=d*r/(b+r)-s
        assert delta<0
        # Telescope the logarithmic predator recurrence directly to avoid underflow.
        x,y=r+0.1,0.05
        accum=0.0
        for n in range(1,15001):
            accum+=d*x/(b+x)-s
            xn=x*exp(r-x-y/(b+x))
            yn=y*exp(d*x/(b+x)-s)
            x,y=xn,max(yn,1e-300)
        assert abs(accum/n-delta)<0.005,(accum/n,delta)
        count+=1
    return count

if __name__=='__main__':
    cases=algebraic_checks()
    n=critical_checks(cases)
    m=strict_checks()
    print('PASS: 4 rational identities,',n,'critical trajectories,',m,'strict-threshold tests')
