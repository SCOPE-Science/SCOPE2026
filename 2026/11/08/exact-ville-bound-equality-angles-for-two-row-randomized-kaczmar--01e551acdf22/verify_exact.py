#!/usr/bin/env python3
"""Reproducible supplementary checks for the two-row randomized projection theorem.

Only Python 3 standard-library modules are needed. The infinite-horizon theorem
is proved analytically in RESULT.md; finite checks here are not substitutes.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from math import comb, sqrt
from itertools import product

class Q5:
    """Exact a+b*sqrt(5) arithmetic with rational coefficients."""
    def __init__(self, a=0, b=0):
        self.a, self.b = Fraction(a), Fraction(b)
    def __add__(self, other):
        other = other if isinstance(other, Q5) else Q5(other)
        return Q5(self.a + other.a, self.b + other.b)
    __radd__ = __add__
    def __neg__(self): return Q5(-self.a, -self.b)
    def __sub__(self, other): return self + -Q5.coerce(other)
    @staticmethod
    def coerce(x): return x if isinstance(x, Q5) else Q5(x)
    def __mul__(self, other):
        other = Q5.coerce(other)
        return Q5(self.a*other.a + 5*self.b*other.b,
                  self.a*other.b + self.b*other.a)
    __rmul__ = __mul__
    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        out = Q5(1)
        for _ in range(n): out = out*self
        return out
    def __eq__(self, other):
        other = Q5.coerce(other)
        return self.a == other.a and self.b == other.b

# The k=3 member: r=(sqrt(5)-1)/2 and c=sqrt(5)-2.
r = Q5(Fraction(-1,2), Fraction(1,2))
c = Q5(-2, 1)
assert (Q5(1)+c) * Q5(Fraction(1,2)) == r
assert r**3 == c
assert r**2 + r == Q5(1)
assert c**2 + 4*c == Q5(1)

# The real RK projections generate a Bernoulli count of decreases.
for c0 in (0.13, sqrt(5)-2, 0.63):
    u = sqrt(c0)
    v = sqrt(1-c0)
    for n in range(0, 11):
        histogram = [0]*(n+1)
        for seq in product((1,2), repeat=n):
            ex, ey = 0., 1.
            old = 1
            decreases = 0
            for label in seq:
                if label == 1:
                    ex = 0.
                else:
                    ip = u*ex+v*ey
                    ex, ey = ex-ip*u, ey-ip*v
                if label != old:
                    decreases += 1
                old = label
            squared = ex*ex+ey*ey
            assert abs(squared-c0**decreases) < 2e-12, (c0,n,seq)
            histogram[decreases] += 1
        assert histogram == [comb(n,j) for j in range(n+1)]

# A finite-horizon hitting probability, counted with exact integer path weights.
def hitting_probability(k,m,horizon):
    live = {0: 1}
    hits = 0
    for n in range(1,horizon+1):
        new = {}
        hits *= 2
        for h, ct in live.items():
            for shift in (-1,k-1):
                newh = h+shift
                if newh <= -m:
                    hits += ct
                else:
                    new[newh] = new.get(newh,0)+ct
        live = new
        assert hits+sum(live.values()) == 2**n
    return Fraction(hits, 2**horizon)

with localcontext() as ctx:
    ctx.prec = 70
    for k in range(3,8):
        lo, hi = Decimal('0.000001'), Decimal('0.999999')
        def f(x): return x**k - 2*x + 1
        assert f(lo)>0 and f(hi)<0
        for _ in range(250):
            mid = (lo+hi)/2
            if f(mid) > 0: lo=mid
            else: hi=mid
        rk=(lo+hi)/2
        ck=rk**k
        assert abs((1+ck)/2-rk) < Decimal('1e-60')
        if k <= 5:
            for m in (1,2,3):
                exact_finite = Decimal(hitting_probability(k,m,300).numerator) / Decimal(hitting_probability(k,m,300).denominator)
                limit = rk**m
                assert exact_finite <= limit + Decimal('1e-58')
                assert limit-exact_finite < Decimal('0.002'), (k,m,limit-exact_finite)
    print('VERIFY_OK: exact Q(sqrt5) identities; all row sequences up to length 10;')
    print('           binomial count; k=3..7 tuned roots; finite-horizon hitting bounds.')
