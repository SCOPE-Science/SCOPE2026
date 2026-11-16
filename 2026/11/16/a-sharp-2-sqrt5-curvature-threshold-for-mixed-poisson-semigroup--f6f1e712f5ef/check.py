#!/usr/bin/env python3
"""Exact rational spot checks for the two-height Poisson curvature theorem.

Standard-library only. Algebraic proof and scope are in RESULT.md; finite checks
are not a substitute for a theorem about all positive real parameters.
"""
from fractions import Fraction as F


def polynomial_multiply(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def polynomial_add(a, b):
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
            for i in range(max(len(a), len(b)))]


def poly_eval(p, x):
    r = F(0)
    for a in p[::-1]:
        r = r*x+a
    return r


# The witness denominator is positive for every u >= 0.
# The numerator equals (3u-1)(u+25)^3+180(3u-25)(u+1)^3.
def cube_shift(c):
    return polynomial_multiply(polynomial_multiply([c, 1], [c, 1]), [c, 1])

P = polynomial_add(polynomial_multiply([-1, 3], cube_shift(25)),
                   [180*x for x in polynomial_multiply([-25, 3], cube_shift(1))])
assert P == [-20125, 32040, -6330, -2656, 543], P
brackets = [(F(1,2),F(1)), (F(2),F(3)), (F(5),F(6))]
for a,b in brackets:
    assert poly_eval(P,a)<0 and poly_eval(P,b)>0 or poly_eval(P,a)>0 and poly_eval(P,b)<0
# Coefficients in decreasing order have exactly three changes of sign;
# hence three disjoint sign-changing positive intervals are exhaustive.
assert [1 if x>0 else -1 for x in P[::-1]] == [1,-1,-1,1,-1]


def derivative_of_ratio(t,u):
    # Compare a quotient-rule derivative with the independently simplified identity.
    N=(3*u-1)*(u+t)**3
    D=(t-3*u)*(u+1)**3
    dN=3*(u+t)**3+3*(3*u-1)*(u+t)**2
    dD=-3*(u+1)**3+3*(t-3*u)*(u+1)**2
    direct=(dN*D-N*dD)/D**2
    q=5*u*u-(t+1)*u+t
    formula=6*(t-1)*(u+t)**2*q/((t-3*u)**2*(u+1)**4)
    assert direct==formula

count=0
for t in [F(2),F(4),F(16),F(18),F(25),F(36),F(100),F(121)]:
    for k in range(1,31):
        u=F(k,5)
        if u==t/3:
            continue
        derivative_of_ratio(t,u)
        count+=1

for t in [F(2),F(4),F(16),F(18),F(25),F(36)]:
    disc=t*t-18*t+1
    assert (disc>0)==(t>=18)
assert (F(5)**2-18*F(5)+1)<0

print('PASS: witness polynomial, three rational sign brackets, Descartes bound')
print('PASS: independent quotient-rule checks',count)
print('PASS: exact discriminant checks on both sides of the sharp scale threshold')
