#!/usr/bin/env python3
"""Reproduce the intrinsic squared-distance energy and stationary-point tests
for uniform pairs in a metric cone truncated at radial length R.
"""
import math
import random


def f(x):
    if x <= math.pi:
        return (9*x-8*math.sin(x))/(9*x*x)
    return (17*x-8*math.pi)/(9*x*x)


def G(x):
    return 16*math.sin(x)-x*(9+8*math.cos(x))


def root(fun, lo, hi, steps=100):
    assert fun(lo)*fun(hi) < 0
    for _ in range(steps):
        m=(lo+hi)/2
        if fun(lo)*fun(m)<=0: hi=m
        else: lo=m
    return (lo+hi)/2


def monte_carlo(alpha, samples=220000):
    rng=random.Random(1241+int(alpha*10000))
    # Area A=1, so R^2=2/alpha. A radial coordinate has CDF (r/R)^2.
    R=math.sqrt(2/alpha)
    sm=sm2=0.0
    for _ in range(samples):
        r=R*math.sqrt(rng.random())
        s=R*math.sqrt(rng.random())
        a=rng.random()*alpha
        b=rng.random()*alpha
        sep=abs(a-b)
        sep=min(sep,alpha-sep)
        dist2=r*r+s*s-2*r*s*math.cos(min(math.pi,sep))
        sm+=dist2
        sm2+=dist2*dist2
    mean=sm/samples
    se=math.sqrt(max(0, sm2/samples - mean*mean)/samples)
    theory=f(alpha/2)
    assert abs(mean-theory)<6*se+0.001, (alpha,mean,theory,se)
    return mean,theory,se


def main():
    x1=root(G,0.5,1.2)
    x2=root(G,2.5,3.1)
    assert 0<x1<math.pi/2<x2<math.pi
    assert f(x1)<f(math.pi)<f(x2)
    assert abs(G(x1))<1e-13 and abs(G(x2))<1e-13
    # Sign/monotonicity for geometry-specified intervals; analytical proof
    # establishes the full assertion by G''(x)=8*x*cos(x).
    for lo,hi,sgn in [(0.001,x1,-1),(x1,x2,1),(x2,math.pi,-1),(math.pi,2*math.pi,-1)]:
        xs=[lo+(hi-lo)*j/4000 for j in range(4001)]
        dif=[f(b)-f(a) for a,b in zip(xs,xs[1:])]
        assert all(sgn*d>0 for d in dif), (lo,hi,min(dif),max(dif))
    print('roots x', repr(x1),repr(x2),'angles',repr(2*x1),repr(2*x2))
    print('levels',repr(f(x1)),repr(f(math.pi)),repr(f(x2)))
    # One-sided third derivatives differ by -8/(9*pi^2); check the
    # analytical continuation difference as h ->0.
    for h in [0.1,0.05,0.025,0.0125]:
        x=math.pi+h
        left_analytic=(9*x-8*math.sin(x))/(9*x*x)
        right=f(x)
        asymptotic=-4/(27*math.pi**2)
        ratio=(left_analytic-right)/h**3
        assert abs(ratio-asymptotic)<0.002
    for alpha in [0.8,2*x1,3.0,2*x2,2*math.pi,8.0,12.0]:
        mean,theory,se=monte_carlo(alpha)
        print('MC',repr(alpha),f'{mean:.9f}',f'{theory:.9f}',f'se={se:.5g}')
    print('CONE_AREA_DISTANCE_PHASE_AND_MC_OK')

if __name__=='__main__':main()
