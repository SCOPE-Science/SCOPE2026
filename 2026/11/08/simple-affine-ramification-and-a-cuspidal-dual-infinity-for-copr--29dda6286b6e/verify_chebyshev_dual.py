#!/usr/bin/env python3
"""Exact finite checks for Chebyshev dual ramification (requires sympy).
These are regression checks, not a proof for unrestricted parameters.
"""
import math
import sympy as sp

t = sp.symbols('t')
checked = 0
for a in range(2, 13):
    for b in range(a + 1, 19):
        if math.gcd(a, b) != 1:
            continue
        x, y = sp.chebyshevt(a, t), sp.chebyshevt(b, t)
        P, Q = sp.diff(x, t), sp.diff(y, t)
        W = sp.Poly(sp.expand(P * sp.diff(Q, t) - Q * sp.diff(P, t)), t)
        assert sp.gcd(sp.Poly(P, t), sp.Poly(Q, t)).degree() == 0
        assert W.degree() == a + b - 3
        assert sp.gcd(W, W.diff()).degree() == 0
        assert W.eval(1) == sp.Integer(a*a*b*b*(b*b - a*a))/3
        assert W.eval(-1) != 0
        leading = sp.Integer(2)**(a+b-2) * a * b * (b-a)
        assert W.LC() == leading
        assert 3*(b-2) - W.degree() == 2*b-a-3
        # The last coordinate of the Gauss parametrization has degree a+b-1.
        L = sp.Poly(sp.expand(P*y-Q*x), t)
        assert L.degree() == a + b - 1
        assert L.LC() != 0
        checked += 1
print('EXACT_CHEBYSHEV_WRONSKIAN_CHECKS_PASS', checked)
print('FINITE_COMPLEX_RAMIFICATION_SIMPLE_PASS')
print('DUAL_MAP_DEGREE_AND_INFINITY_WEIGHT_PASS')
