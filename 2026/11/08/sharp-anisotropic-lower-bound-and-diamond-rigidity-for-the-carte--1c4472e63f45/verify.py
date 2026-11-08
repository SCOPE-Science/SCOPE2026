#!/usr/bin/env python3
"""Deterministic supplementary numerical checks for the joint Cartesian radius bound."""
import math

def formula(r,s):
    if r == 0: return s*s/2
    return .5*r*r+(r*s+(s*s-r*r)*math.atan(s/r))/math.pi

def quadrature(r,s,N=16384):
    return sum(max((r*math.cos(2*math.pi*(k+.5)/N))**2,(s*math.sin(2*math.pi*(k+.5)/N))**2) for k in range(N))/N

assert abs(formula(1,0)-.5)<1e-13
assert abs(formula(0,1)-.5)<1e-13
assert abs(formula(1,1)-(.5+1/math.pi))<1e-13
assert abs(formula(2,3)-formula(3,2))<1e-12
for r in [0,.125,.5,1,2,4]:
    for s in [0,.125,.5,1,2,4]:
        assert abs(quadrature(r,s)-formula(r,s)) < .000005*(1+r*r+s*s)
for e in [.03,.02,.01]:
    deficit=formula(1,e)-.5
    assert abs(deficit/e**3-4/(3*math.pi))<.02
print('CARTESIAN_DIAMOND_CHECK_OK',6*6+3+4)
