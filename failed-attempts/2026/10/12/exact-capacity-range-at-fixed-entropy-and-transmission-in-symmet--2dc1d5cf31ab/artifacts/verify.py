#!/usr/bin/env python3
import math


def capacity_ratio(r, x, y):
    return 2.0*r*r*(1.0+x)*(1.0+y)/(2.0+x+y)


def reduced(r, x, y):
    t=2.0/(2.0+x+y)
    d=(x-y)/2.0
    return r*r/t-r*r*t*d*d


def delta(r,t):
    return 1.0-abs(1.0/t-1.0-1.0/r)

# Reproduce the two values in the source's symmetric-radius table.
r=0.5
assert abs(capacity_ratio(r,2.0,2.0)-0.75) < 1e-14
assert abs(capacity_ratio(r,1.5,2.5)-35.0/48.0) < 1e-14
t=1.0/3.0
assert abs(delta(r,t)-1.0) < 1e-14
lo=r*r/t-r*r*t*delta(r,t)**2
hi=r*r/t
assert abs(lo-2.0/3.0) < 1e-14
assert abs(hi-3.0/4.0) < 1e-14

# Deterministic feasible samples for the exact reduction and strict range.
for r in (0.2,0.35,0.5,0.8):
    a=1.0/r-1.0
    b=1.0/r+1.0
    for frac in (0.15,0.33,0.5,0.71,0.88):
        S=2.0*a+frac*(2.0*b-2.0*a)
        t=2.0/(S+2.0)
        D=delta(r,t)
        assert D > 0.0
        assert r/(1.0+2.0*r) < t < r
        for q in (-0.8,-0.37,0.0,0.42,0.81):
            d=q*D
            x=S/2.0+d
            y=S/2.0-d
            assert a < x < b and a < y < b
            lhs=capacity_ratio(r,x,y)
            rhs=reduced(r,x,y)
            assert abs(lhs-rhs) < 2e-13
            lower=r*r/t-r*r*t*D*D
            upper=r*r/t
            assert lower < lhs <= upper+2e-13
            if d != 0.0:
                assert lhs < upper

print('VERIFY_OK')
