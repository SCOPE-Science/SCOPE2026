#!/usr/bin/env python3
"""Finite diagnostics for the periodic radial Fock Toeplitz heat-gap theorem.
All universal statements require the analytic proof, not this checker.
Requires only Python standard library.
"""
import math


def heat_two(t, x):
    return math.exp(-t)*math.cos(x) + math.exp(-4*t)*math.cos(2*x)


def min_two(t):
    assert 0 < t < math.log(4)/3
    return -math.exp(-4*t)-math.exp(2*t)/8


def fock_eigenvalue(k):
    # Degree m=k-1 in one complex dimension; gamma(shape=k, rate=1).
    center = math.sqrt(k)
    lo, hi = max(1e-10, center-7), center+7
    steps = 4000
    dx = (hi-lo)/steps
    s = 0.0
    for j in range(steps+1):
        y = lo+j*dx
        density = math.exp(math.log(2)+(2*k-1)*math.log(y)-y*y-math.lgamma(k))
        v = (math.cos(y)+math.cos(2*y))*density
        s += (1 if j in (0,steps) else 4 if j%2 else 2)*v
    return s*dx/3


def berezin_2d(radius):
    # Gaussian coherent-state convolution in one complex dimension.
    steps = 120
    dx = 10/steps
    s = 0.0
    for j in range(steps+1):
        x = -5+j*dx
        wx = 1 if j in (0,steps) else 4 if j%2 else 2
        for k in range(steps+1):
            y = -5+k*dx
            wy = 1 if k in (0,steps) else 4 if k%2 else 2
            r = math.hypot(radius+x,y)
            s += wx*wy*math.exp(-x*x-y*y)*(math.cos(r)+math.cos(2*r))
    return s*(dx/3)**2/math.pi


def run():
    assert math.exp(3/8)<4 and math.exp(3/4)<4
    lower_e = min_two(1/8)
    lower_b = min_two(1/4)
    assert -0.77 < lower_e < -0.76
    assert -0.58 < lower_b < -0.57
    assert 2/3+lower_b > 0 and 2/3+lower_e < 0
    checks = 5
    for t in (1/8,1/4):
        for j in range(2001):
            x=2*math.pi*j/2000
            assert heat_two(t,x) >= min_two(t)-1e-12
            checks += 1
    for k in (150,600,3000,9000):
        got=fock_eigenvalue(k)
        want=heat_two(1/8, math.sqrt(k))
        assert abs(got-want)<0.065, (k,got,want)
        checks += 1
    for r in (40.,100.):
        got=berezin_2d(r)
        want=heat_two(1/4,r)
        assert abs(got-want)<0.04, (r,got,want)
        checks += 1
    print('PASS',checks,'finite assertions; bottom spectral',lower_e,'bottom Berezin',lower_b)

if __name__=='__main__':
    run()
