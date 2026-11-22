#!/usr/bin/env python3
"""Reproducibility checks for a critical discrete sine-memory separatrix.

Only finite diagnostics are provided: the infinite statements use the proof.
No nonstandard Python packages are required.
"""
import math
from fractions import Fraction


def full_step(x, y, z, k=0.1):
    q = k / math.log(3)
    return (q + 0.5 * math.sin(z) * (x-y),
            q - 0.5 * math.sin(z) * (x-y), z + x - y)


def reduced_step(w, u):
    return w-u, u*math.cos(w)


def integral(w):
    return w-math.sin(w)


def classify(w, u, cap=20000):
    # The 'below' branch uses the analytic lower bound for the separatrix.
    for n in range(cap):
        if u >= w:
            return 'cross', n
        if u < integral(w):
            return 'below', n
        w, u = reduced_step(w, u)
    return 'undetermined', cap


def main():
    count = 0
    q = .1 / math.log(3)
    for w in (.1, .2, .4):
        for u in (.0001, .001, .005):
            x, y, z = q+u/2, q-u/2, math.pi/2-w
            X,Y,Z = full_step(x,y,z)
            W,U = reduced_step(w,u)
            assert abs(X+Y-2*q) < 1e-14
            assert abs((X-Y)-U) < 1e-14
            assert abs((math.pi/2-Z)-W) < 1e-14
            count += 3
    a, b = Fraction(1,6), Fraction(1,120)
    assert a/2-3*a*a == 0
    assert 72*a**3-192*a*b-a+12*b == 0
    count += 2
    for w in (.08,.1,.2,.4,.8):
        # Rigorous inequalities on the critical threshold itself (independent
        # of its numerical approximation).
        lower = integral(w)
        upper = lower/(1-w*w/2)
        assert 0 < lower < upper < w
        assert classify(w,lower/2)[0] == 'below'
        assert classify(w,.9*w)[0] == 'cross'
        count += 3
    # A ninth-order formal invariant-graph approximation is used ONLY as a
    # trajectory diagnostic, not as an exact initial condition.
    w, u = .1, .1**3/6+.1**5/120+2*.1**7/945+769*.1**9/1088640
    values = {}
    for n in range(1,100001):
        w,u = reduced_step(w,u)
        assert 0 < u < w < 1
        if n in (10000,50000,100000):
            values[n] = (n*w*w, (n**1.5)*u)
    assert 2.9 < values[10000][0] < 3.0
    assert abs(values[100000][0]-3) < .02
    assert abs(values[100000][1]-math.sqrt(3)/2) < .015
    count += 100003
    print('PASS: %d finite checks; near-critical diagnostics (n*w^2, n^1.5*u):' % count)
    for n in values: print('%d: %.9f %.9f' % (n,*values[n]))
    print('These finite checks do not prove uniqueness, asymptotic limits, or originality.')

if __name__ == '__main__':
    main()
