#!/usr/bin/env python3
"""Exact rational and quadratic-field checks of two polynomial certificates.

All universal conclusions use the independent analytic proof in RESULT.md.
This program checks the displayed algebraic identities symbolically and
performs optional finite checks of the norm expressions.
"""
from fractions import Fraction as Q
from math import sqrt

class K:
    """The exact number field Q(sqrt(6))."""
    def __init__(self, a=0, b=0):
        if isinstance(a, K):
            self.a, self.b = a.a, a.b
        else:
            self.a, self.b = Q(a), Q(b)
    def __add__(self, other):
        other = K(other)
        return K(self.a + other.a, self.b + other.b)
    __radd__ = __add__
    def __neg__(self):
        return K(-self.a, -self.b)
    def __sub__(self, other):
        return self + (-K(other))
    def __rsub__(self, other):
        return K(other) - self
    def __mul__(self, other):
        other = K(other)
        return K(self.a * other.a + 6 * self.b * other.b,
                 self.a * other.b + self.b * other.a)
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = K(other)
        den = other.a * other.a - 6 * other.b * other.b
        if den == 0:
            raise ZeroDivisionError
        return K((self.a * other.a - 6 * self.b * other.b) / den,
                 (self.b * other.a - self.a * other.b) / den)
    def __eq__(self, other):
        other = K(other)
        return (self.a, self.b) == (other.a, other.b)
    def __repr__(self):
        return f'{self.a}+({self.b})sqrt(6)'

class P:
    """Exact univariate polynomials over Q(sqrt(6))."""
    def __init__(self, cs):
        if isinstance(cs, P):
            self.c = cs.c
        elif isinstance(cs, (tuple, list)):
            self.c = tuple(K(x) for x in cs)
        else:
            self.c = (K(cs),)
    def __add__(self, other):
        other = P(other)
        return P([ (self.c[i] if i < len(self.c) else K(0)) +
                   (other.c[i] if i < len(other.c) else K(0))
                   for i in range(max(len(self.c), len(other.c))) ])
    __radd__ = __add__
    def __neg__(self):
        return P([-x for x in self.c])
    def __sub__(self, other):
        return self + (-P(other))
    def __rsub__(self, other):
        return P(other) - self
    def __mul__(self, other):
        other = P(other)
        cs = [K(0)] * (len(self.c) + len(other.c) - 1)
        for i, x in enumerate(self.c):
            for j, y in enumerate(other.c):
                cs[i+j] = cs[i+j] + x*y
        return P(cs)
    __rmul__ = __mul__
    def __truediv__(self, other):
        return P([x / K(other) for x in self.c])
    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        result = P(1)
        for _ in range(n):
            result = result * self
        return result
    def __eq__(self, other):
        other = P(other)
        n = max(len(self.c), len(other.c))
        return all((self.c[i] if i < len(self.c) else K(0)) ==
                   (other.c[i] if i < len(other.c) else K(0))
                   for i in range(n))
    def __repr__(self):
        return repr(self.c)

checks = 0
b = P([0, 1])
r = P([0, 1])
# Universal lower certificate after selecting test radius |w|=b/2.
fb = (1-(b/2)*(b/2)) * ((1-b*b+b*(b/2))**2+b*b)
lower = (8-3*b*b)*(3*b*b-2)**2 * P(K(Q(1,432)))
assert fb-P(K(Q(25,27))) == lower
checks += 1
# Exceptional coefficient b=sqrt(2/3)=sqrt(6)/3, a=1/3.
s6 = K(0, 1)
b_star = s6 / 3
r_star = s6 / 6
Fstar = (1-r*r)*((P(K(Q(1,3))) + P(b_star)*r)**2+K(Q(2,3)))
upper = (r-r_star)**2 * (r*r+P(2*s6/3)*r+P(K(Q(4,3))))*K(Q(2,3))
assert P(K(Q(25,27)))-Fstar == upper
checks += 1
assert r_star*r_star == K(Q(1,6))
checks += 1
# 501 by 101 finite spot checks (corroborative, not a substitute for proof).
for i in range(501):
    bv = i/500
    av = 1-bv*bv
    norm=(av+sqrt(av*av+4*bv*bv))/2
    assert abs(norm-1)<1e-12
    v0=(1-(bv/2)**2)*((av+bv*bv/2)**2+bv*bv)
    assert v0 >= 25/27-2e-12
    checks+=2
for i in range(1001):
    rv = i/1001
    b0 = sqrt(2/3)
    f=(1-rv*rv)*((1/3+b0*rv)**2+b0*b0)
    assert f <= 25/27+2e-12
    checks+=1
print('QUADRATIC_HANKEL_EXACT_CHECK_OK', checks, 'checks')
