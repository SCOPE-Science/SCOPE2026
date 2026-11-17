"""Finite algebraic checks for the diagonal recurrence in the accompanying theorem.

These checks support, but do not certify, the infinite-dimensional conclusion.
"""
from fractions import Fraction as F
from math import sqrt, cos, pi
import cmath

def delta(n):
    return F(n + 2, n + 1)

def a(n):
    return F(n, 2 * (n + 1))

def b(n, d):
    return sqrt(float(delta(n) * delta(n + d))) / 2

def product(n, d, z):
    v = sqrt((d+1)/((n+1)*(n+d+1)))
    for j in range(1, n+1):
        v *= z + 1/j
    return v

checks = 0
for d in range(7):
    for z in [-1, -0.5, 0, 0.31, 0.75, 1, 1j, cmath.exp(1j*pi/2)]:
        lam = (1+z)/2
        for n in range(35):
            lhs = (lam-float(a(n)))*product(n,d,z)
            rhs = b(n,d)*product(n+1,d,z)
            assert abs(lhs-rhs)<2e-8*(1+abs(lhs)+abs(rhs)), (d,z,n,lhs,rhs)
            checks += 1
for t, should_converge in [(0.2,False),(pi/3,False),(pi/2,True),(pi,True),(5*pi/3,False)]:
    # At exact endpoints, use the mathematical exponent, not floating equality.
    power = cos(t)-1
    if abs(t-pi/3)<1e-10 or abs(t-5*pi/3)<1e-10:
        assert abs(power+0.5)<1e-14
    elif t==pi:
        assert should_converge
    else:
        assert (power < -0.5)==should_converge
    checks += 1
print('CHECK_OK', checks)
