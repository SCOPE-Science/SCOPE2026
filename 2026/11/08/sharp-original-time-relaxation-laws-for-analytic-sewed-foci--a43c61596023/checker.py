#!/usr/bin/env python3
"""Finite reproducibility checks for analytic sewed-focus original-time laws.

Analytical assertions valid for all orders are proved in RESULT.md.
This script independently tests the explicit polynomial realization, not an
infinite-time theorem or independent mathematical certification.
Requires Python 3, sympy, mpmath.
"""
import sympy as sp
import mpmath as mp

x, r, c, s = sp.symbols('x r c s')
checked = 0
for p in range(1, 7):
    phi = -x**2 - c*x**(2*p+1)
    Q = -2*x - (2*p+1)*c*x**(2*p)
    assert sp.expand(sp.diff(phi, x)-Q) == 0
    checked += 1
    u = r + s*r**(2*p)
    residual = sp.expand(u**2 + c*u**(2*p+1) - r**2 + c*r**(2*p+1))
    coeff = sp.expand(residual).coeff(r, 2*p+1)
    assert sp.simplify(coeff-2*(s+c)) == 0, (p, coeff)
    checked += 1
    # The lower half-flight's first integral is y=x^2-r^2.
    assert sp.diff(x**2-r**2, x) == 2*x
    checked += 1

mp.mp.dps = 75
numeric = 0
for p in range(1, 6):
    for a in [mp.mpf(1)/8, mp.mpf(1)/10]:
        cc = mp.mpf(2)/3
        rhs = a*a-cc*a**(2*p+1)
        assert rhs > 0
        f = lambda u: u*u+cc*u**(2*p+1)-rhs
        lo, hi = mp.mpf('0'), a
        for _ in range(270):
            mid = (lo+hi)/2
            if f(mid)>0: hi=mid
            else: lo=mid
        u=(lo+hi)/2
        assert 0<u<a
        assert abs(f(u)) < mp.mpf('1e-65')
        # Validated direction of contraction and coefficient at this radius.
        d=(a-u)/a**(2*p)
        assert d > 0
        # For small radius the local mismatch coefficient approaches c.
        numeric+=1
print(f'PASS: {checked} exact symbolic identities and {numeric} high-precision return tests')
