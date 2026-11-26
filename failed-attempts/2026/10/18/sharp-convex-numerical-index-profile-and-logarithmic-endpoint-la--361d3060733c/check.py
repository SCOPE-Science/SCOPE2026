#!/usr/bin/env python3
"""Finite numerical diagnostics for an analytic two-dimensional numerical-index theorem.

This program is not a substitute for the proof: it checks hyperbolic formulas,
sharp constants, interpolation, and asymptotic patterns at finite parameters.
"""
import math

def zstar():
    lo, hi = 0.0, 4.0
    for _ in range(90):
        z = (lo + hi) / 2
        if z * math.tanh(z) < 1:
            lo = z
        else:
            hi = z
    return (lo + hi) / 2

def zopt(a):
    if not 0 < a < 1:
        raise ValueError('a must be in (0, 1)')
    lo, hi = 0.0, 1.0
    while math.tanh(a * hi) * math.tanh(hi) < a:
        hi *= 2
    for _ in range(100):
        z = (lo + hi) / 2
        if math.tanh(a * z) * math.tanh(z) < a:
            lo = z
        else:
            hi = z
    return (lo + hi) / 2

def value(a, z):
    return math.exp(-(1 - a) * z) * (-math.expm1(-2 * a * z)) / (1 + math.exp(-2 * z))

def n(a):
    return value(a, zopt(a))

def run():
    count = 0
    z0 = zstar()
    c = z0 / math.cosh(z0)
    d = z0 ** 3 / (6 * math.cosh(z0))
    assert 1.19 < z0 < 1.21 and .66 < c < .67
    count += 1
    for i in range(1, 100):
        a = i / 100
        za = zopt(a)
        va = n(a)
        assert abs(math.tanh(a * za) * math.tanh(za) - a) < 1e-13
        assert c * a < va < a
        assert abs(va - value(a, za)) < 1e-14
        count += 1
    for i in range(1, 19):
        left, mid, right = i/20, (i+.5)/20, (i+1)/20
        assert n(mid) < (n(left) + n(right)) / 2
        count += 1
    for a in [.1, .07, .04, .02, .01]:
        residual = abs(n(a) - c*a - d*a**3)
        assert residual < .07 * a**5
        count += 1
    for delta in [.01, .003, .001, .0003, .0001]:
        a = 1 - delta
        z = zopt(a)
        approx = delta/2 * (math.log(4/delta) + 1)
        deficit = 1-n(a)
        assert abs(deficit - approx) / delta < .09
        assert abs(z - .5*math.log(4/delta)) < .1
        slope = z * math.cosh(a*z) / math.cosh(z)
        assert abs(slope - .5*math.log(4/delta)) < .1
        count += 1
    for p in [1.03,1.1,1.2,1.5,2.5,3,6,18,100]:
        q=p/(p-1)
        a=abs(1-2/p)
        b=abs(1-2/q)
        assert abs(a-b)<1e-13
        assert abs(n(a)-n(b))<1e-13
        count+=1
    print(f'PASS: {count} finite diagnostics; z_star={z0:.14f}, c_star={c:.14f}, d_star={d:.14f}')

if __name__ == '__main__':
    run()
