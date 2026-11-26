#!/usr/bin/env python3
"""Bounded exact regression for the coprime Chebyshev Gauss map and Wronskian."""

from math import gcd

from sympy import Poly, Rational, chebyshevt, gcd as polynomial_gcd, symbols

t = symbols("t")
checked = 0
for a in range(2, 13):
    for b in range(a + 1, 19):
        if gcd(a, b) != 1:
            continue
        x, y = (Poly(chebyshevt(k, t), t) for k in (a, b))
        p, q = x.diff(), y.diff()
        w = p * q.diff() - q * p.diff()
        assert polynomial_gcd(p, q).degree() == 0
        assert polynomial_gcd(w, w.diff()).degree() == 0
        assert w.degree() == a + b - 3
        assert w.LC() == a * b * (b - a) * 2 ** (a + b - 2)
        assert w.eval(1) == Rational(a * a * b * b * (b * b - a * a), 3)
        assert w.eval(-1) != 0
        assert (Poly(1 - t**2, t) * w.diff() - Poly(3 * t, t) * w
                + (b * b - a * a) * p * q).is_zero
        assert 3 * (b - 2) - w.degree() == 2 * b - a - 3
        first = p * y - q * x
        assert first.degree() == a + b - 1
        assert first.LC() == (a - b) * 2 ** (a + b - 2)
        assert (first.degree() - q.degree(), first.degree() - p.degree()) == (a, b)
        checked += 1

print(f"Exact Chebyshev Gauss–Wronskian checks passed for {checked} pairs.")
