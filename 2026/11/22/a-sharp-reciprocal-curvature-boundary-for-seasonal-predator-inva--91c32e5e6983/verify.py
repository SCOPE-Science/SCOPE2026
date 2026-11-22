#!/usr/bin/env python3
"""Standalone checks for a periodic logistic prey and generalized type-III invasion theorem.

The proof of the universal statements is analytic; finite quadrature here is
illustrative and is not used as evidence for all frequencies or waveforms.
"""
from fractions import Fraction as F
from math import pi, cos, sin, sqrt


def curvature_num(B, C, D, u):
    return 3*B*B*u*u + 3*B*C*u + C*C-B*D


def g(u, A, B, C, D):
    return A/(B*u*u+C*u+D)


assert curvature_num(F(1), F(1), F(1), F(1,100)) > 0
assert curvature_num(F(1), F(1), F(4), F(7,20)) < 0
assert curvature_num(F(1), F(1), F(4), F(3,20)) < 0
assert F(1,4) > F(1,10)*F(3,2)  # stronger than positivity requirement
assert g(F(1,4), F(1), F(1), F(1), F(4)) == F(16,69)
assert g(F(1,4), F(1), F(1), F(1), F(1)) == F(16,21)


def integrate(A,B,C,D,n=50000):
    return sum(g(.25+.1*cos(2*pi*(i+.5)/n), A,B,C,D) for i in range(n))/n

lo = integrate(1,1,1,4)
hi = integrate(1,1,1,1)
assert lo < 16/69-1e-6, (lo,16/69)
assert hi > 16/21+1e-6, (hi,16/21)
# For the chosen periodic prey, inverse capacity is u+u'/r, whose
# average is u0=1/4: integrate the explicit function independently.
n=50000
mean_invK=sum(.25+.1*(cos(2*pi*(i+.5)/n)-sin(2*pi*(i+.5)/n)) for i in range(n))/n
assert abs(mean_invK-.25)<1e-11
print('PASS: exact curvature, neutral benchmarks, positive capacity, quadrature signs, and harmonic average')
print('seasonal intake, negative-curvature:',lo,'<',16/69)
print('seasonal intake, positive-curvature:',hi,'>',16/21)
