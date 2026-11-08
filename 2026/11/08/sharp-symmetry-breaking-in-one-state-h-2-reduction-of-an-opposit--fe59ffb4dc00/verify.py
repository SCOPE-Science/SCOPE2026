#!/usr/bin/env python3
"""Standalone exact and numerical checks for the symmetric two-mode H2 theorem."""
from fractions import Fraction as Q
from math import sqrt, sin, cos
from random import Random


def captured(t, z, a=1.0):
    return 4.0*a*a*(1.0-abs(z)**2)/abs(1.0-t*z*z)**2


def bound(t):
    return 4.0 if t <= 0.5 else 1.0/(t*(1.0-t))


# Rational certificates for the endpoint, interior maximizer and exact sample.
for t in (Q(1, 5), Q(1, 3), Q(1, 2), Q(4, 7), Q(3, 4), Q(9, 10)):
    s = Q(0) if t <= Q(1, 2) else 2-1/t
    actual = 4*(1-s)/(1-t*s)**2
    target = Q(4) if t <= Q(1, 2) else 1/(t*(1-t))
    assert actual == target
    if t > Q(1, 2):
        assert (actual-4) == (2*t-1)**2/(t*(1-t))
        assert 2*(1-s)/(1-t*s) == 1/t
    p, lam = sqrt(float(t)), sqrt(float(s))
    coefficient = float(2*(1-s)/(1-t*s))
    finite_error = sum(
        ((2*(p**n) if n % 2 == 0 else 0) - coefficient*lam**n)**2
        for n in range(300)
    )
    analytic_error = float(4/(1-t*t)-target)
    assert abs(finite_error-analytic_error) < 2e-11


t = Q(3,4)
s = 2-1/t
assert s == Q(2,3)
assert 4/(1-t*t)-1/(t*(1-t)) == Q(80,21)
assert 4/(1-t*t)-4 == Q(36,7)
assert (2*t-1)**2/(t*(1-t)) == Q(4,3)
assert (1-Q(1,10))/(1-Q(1,2)*Q(1,10))**2 < 1

# Distinct complex sampling: the true proof is an angular inequality and a
# one-variable derivative, not this finite test.
comparisons = 0
for ti in range(1, 40):
    t = ti/40.0
    rng = Random(ti)
    if t > 0.5:
        x = sqrt(2.0-1.0/t)
        assert abs(captured(t, x)-bound(t)) < 1e-10
        assert abs(captured(t, -x)-bound(t)) < 1e-10
    else:
        assert captured(t, 0) == 4.0
    for k in range(1500):
        r = rng.uniform(0, 0.9999)
        theta = rng.uniform(0, 2*3.141592653589793)
        z = r*complex(cos(theta), sin(theta))
        assert captured(t, z) <= bound(t) + 1e-8
        comparisons += 1

assert comparisons == 58500
print(f"PASS: {comparisons} complex candidate comparisons, six exact parameter cases, six independent impulse-response sums, exact supercritical example")
