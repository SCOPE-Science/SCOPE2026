#!/usr/bin/env python3
"""Exact-rational checks for the prescribed-pair taxicab torus radius formula."""
from fractions import Fraction as Q
from itertools import product
from random import Random

def d1(u, v, periods):
    return sum(min(abs((x-y)%L), L-abs((x-y)%L)) for x,y,L in zip(u,v,periods))

def witness(a, b, periods):
    # Reflect coordinates so the shorter directed displacement is nonnegative.
    out=[]
    for x,y,L in zip(a,b,periods):
        s=(y-x)%L
        if s<=L/2:
            out.append((x+(L+s)/2)%L)
        else:
            t=L-s
            out.append((x-(L+t)/2)%L)
    return tuple(out)

def verify():
    rng=Random(261115)
    checks=0
    for dimension in range(1,6):
        for trial in range(100):
            periods=tuple(Q(rng.randint(2,30),rng.randint(1,9)) for _ in range(dimension))
            a=tuple(L*Q(rng.randint(0,20),21) for L in periods)
            b=tuple(L*Q(rng.randint(0,23),24) for L in periods)
            D=sum(periods)/2
            sep=d1(a,b,periods)
            cap=D-sep/2
            x=witness(a,b,periods)
            assert d1(x,a,periods)==cap and d1(x,b,periods)==cap
            assert cap-D/2 == sum(L/2-min((y-x)%L,L-(y-x)%L) for x,y,L in zip(a,b,periods))/2
            checks+=2
            for i in range(30):
                z=tuple(L*Q(rng.randint(0,40),41) for L in periods)
                opposite=tuple((zj+L/2)%L for zj,L in zip(z,periods))
                assert d1(opposite,a,periods)==D-d1(z,a,periods)
                assert min(d1(z,a,periods),d1(z,b,periods))<=cap
                checks+=2
            antipodal=tuple((x+L/2)%L for x,L in zip(a,periods))
            assert d1(a,antipodal,periods)==D
            assert d1(witness(a,antipodal,periods),a,periods)==D/2
            checks+=2
    print(f'PASS: {checks} exact rational assertions, dimensions 1..5; infinite theorem uses analytic proof')

if __name__=='__main__':
    verify()
