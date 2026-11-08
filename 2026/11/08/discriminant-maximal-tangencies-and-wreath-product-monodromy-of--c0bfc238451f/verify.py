#!/usr/bin/env python3
"""Exact symbolic checks for even Fermat projection discriminants."""
import sympy as sp

u, t, s = sp.symbols('u t s')
for d in (4, 6, 8, 10):
    m = d // 2
    H = sp.expand(sum(2 * sp.binomial(d, 2*j) * t**j for j in range(m+1)))
    F = sp.expand((u + 1)**d + (u - 1)**d + s)
    assert sp.expand(F - H.subs(t, u**2) - s) == 0
    deriv = sp.diff(H, t)
    assert deriv.subs(t, 0) == d*(d-1)
    R = sp.factor(sp.resultant(H + s, deriv, t))
    disc = sp.factor(sp.discriminant(F, u))
    assert sp.simplify(disc - (-1)**m * 2**(d-1) * (s+2) * R**2) == 0
    assert sp.Poly(R, s).degree() == m-1
    assert sp.gcd(sp.Poly(R, s), sp.Poly(sp.diff(R, s), s)).degree() == 0
    assert sp.expand(R).subs(s, -2) != 0
    r=d-1
    assert -sp.Integer(2)**d / (-2)**r == 2
print('VERIFY_OK')
