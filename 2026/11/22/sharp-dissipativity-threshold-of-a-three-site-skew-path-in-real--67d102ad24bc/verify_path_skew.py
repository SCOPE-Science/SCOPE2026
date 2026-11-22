#!/usr/bin/env python3
"""Finite diagnostic for an exact real three-site skew-path abscissa.

The universal inequality is proved analytically in RESULT.md, not by this test.
No external dependencies or network access are required.
"""
import math
from fractions import Fraction

S = ((0, 1, 0), (-1, 0, 1), (0, -1, 0))


def numerator(x):
    return sum(x[i]**3 * sum(S[i][j]*x[j] for j in range(3)) for i in range(3))


def quartic(x):
    return sum(t**4 for t in x)


def critical_z():
    lo, hi = 0.0, 1.0
    for _ in range(90):
        m = (lo+hi)/2
        p = 2*m**3-6*m*m-3*m+1
        if p > 0:
            lo = m
        else:
            hi = m
    return (lo+hi)/2


checks = 0
for a in range(-8, 9):
    for b in range(-8, 9):
        for c in range(-8, 9):
            x = (a, b, c)
            if x == (0, 0, 0):
                continue
            F = numerator(x)
            Q = quartic(x)
            # A rational upper bound, strictly above the exact algebraic optimum.
            assert 250*abs(F) <= 167*Q, (x, F, Q)
            u, w = Fraction(a-c, 2), Fraction(a+c, 2)
            assert F == 2*u*b*(u*u+3*w*w-b*b)
            assert Q == 2*u**4+12*u*u*w*w+2*w**4+b**4
            checks += 3

# An exact sum-of-squares identity used in the positive-sign branch.
for a_num in range(0, 21):
    a = Fraction(a_num, 10)
    for w_num in range(0, 21):
        W = Fraction(w_num, 10)
        D = 2*a**4+1+12*a*a*W+2*W*W
        P = D - 4*a*(a*a-1+3*W)
        assert P >= 0
        if 0 <= a <= 1:
            h = 2*(1-a)*(2*a-1)**2+a
            assert P == 2*(W-3*a*(1-a))**2+1+2*a*h
        else:
            h = (a-Fraction(4,3))**2*(a+Fraction(2,3))+Fraction(22,27)
            assert P == 2*W*W+12*a*(a-1)*W+1+2*a*h
        checks += 2

z = critical_z()
r = math.sqrt(z)
c = 2*r*(1-z)/(1+2*z*z)
assert abs(2*z**3-6*z*z-3*z+1) < 1e-13
assert 2/3 < c < 167/250
x_star = (-r,1.0,r)
assert abs(numerator(x_star)/quartic(x_star)-c) < 1e-13
checks += 4

# Independent finite-difference test of the stated instantaneous norm growth.
def step(x, dt, damping):
    sx = [sum(S[i][j]*x[j] for j in range(3)) for i in range(3)]
    return [x[i]+dt*(sx[i]-damping*x[i]) for i in range(3)]

for damping in (0.0,c/2,c,1.0):
    dt = 1e-6
    y = step(x_star,dt,damping)
    numerical_growth = ((quartic(y)/quartic(x_star))**0.25 - 1)/dt
    assert abs(numerical_growth - (c-damping)) < 5e-6
    checks += 1

print(f"THREE_SITE_SKEW_PATH_CHECKS_OK {checks} c={c:.15f} z={z:.15f}")
