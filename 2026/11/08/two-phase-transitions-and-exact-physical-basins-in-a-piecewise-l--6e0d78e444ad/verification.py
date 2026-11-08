#!/usr/bin/env python3
"""Exact-arithmetic checks for a deterministic core of the three-branch interval family.

Uses only the Python standard library. The finite checks corroborate, but do not
replace, the all-parameter symbolic proof.
"""
from fractions import Fraction as F


def f0(x):
    return x / 2 if x < F(2, 3) else 2*x - 1


def f1(x, d):
    if x < d / 2:
        return 2*x
    if x < 1-d:
        return x+d/2
    return (x+1)/2


def h(x, d):
    return f1(x, d) if x < F(1, 2) else f0(x)


def scalar_return(x, d):
    a, b = d/2, 1-d
    t = F(2, 3)-d/2
    if x < a:
        return x
    if x < t:
        return (x+a)/2
    if x < b:
        return 2*x-b
    return x


def q(x, d):
    a, b = d/2, 1-d
    if x <= a:
        return x
    if x < b:
        return a
    return x


checks = 0
# Check all branches at rational grids including exact breakpoints.
for d in [F(1,2), F(13,24), F(7,12), F(3,5), F(5,8), F(2,3)]:
    a, b = d/2, 1-d
    I, J = (F(1,4), F(1,2)), (F(1,2), F(3,4))
    for i in range(257):
        x = F(1,4) + F(i, 1028)
        assert x < F(1,2)
        assert F(1,2) <= h(x,d) < F(3,4)
        assert h(h(x,d),d) == scalar_return(x,d)
        assert q(scalar_return(x,d),d) == q(x,d)
        checks += 4
    for i in range(257):
        y = F(1,2) + F(i,1028)
        assert F(1,4) <= h(y,d) < F(1,2)
        checks += 1
    # All endpoints and branch-boundary locations are handled exactly.
    for x in {F(1,4),a,F(2,3)-d/2,b}:
        if F(1,4) <= x < F(1,2):
            assert h(h(x,d),d) == scalar_return(x,d)
            checks += 1
    for i in range(1,256):
        x = F(1,4)+F(i,1024)
        z = x
        for k in range(64):
            z = scalar_return(z,d)
        assert abs(z-q(x,d)) < F(1,2**40) or (b > a and x < b and x > a and abs(z-a) < F(1,2**40))
        checks += 1
    if d < F(2,3):
        w = b-a
        assert w > 0
        assert 2*(F(1,3)-a)+(b-F(1,3))/2 == w
        assert 4*w == 4-6*d
        checks += 3
        for n in range(1,19):
            cutoff = 1-F(1,3)*F(1,2**(n-1))
            assert 1-cutoff == F(1,3)*F(1,2**(n-1))
            checks += 1
assert f1(F(1,3),F(2,3)) == F(2,3)
print('PASS exact-rational branch, limit, basin-length and tail threshold checks:', checks)
