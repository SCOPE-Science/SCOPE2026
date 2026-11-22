"""Exact checks for a soft interlayer rung in two hard-core path replicas.

Requires Python 3.10+ and SymPy. Verifies small instances only;
the theorem for all path sizes is proved analytically in RESULT.md.
"""
from math import gcd
from fractions import Fraction
import sympy as sp

z = sp.Symbol('z')

def path_poly(n):
    if n <= 0:
        return sp.Integer(1)
    a, b = sp.Integer(1), 1 + z
    for _ in range(2, n + 1):
        a, b = b, sp.expand(b + z * a)
    return b

def independent_sets(n):
    return [mask for mask in range(1 << n) if not (mask & (mask << 1))]

def direct_poly(n, v, a):
    masks = independent_sets(n)
    total = sp.Integer(0)
    av = sp.Rational(a)
    for p in masks:
        for q in masks:
            weight = av if (p & q) & (1 << (v - 1)) else 1
            total += weight * z ** (p.bit_count() + q.bit_count())
    return sp.Poly(total, z)

def formula_poly(n, v, a):
    a = sp.Rational(a)
    A = path_poly(n)
    B = path_poly(v - 2) * path_poly(n - v - 1)
    return sp.Poly(sp.expand(A * A + (a - 1) * z * z * B * B), z)

identity_checks = 0
for n in range(1, 8):
    for v in range(1, n + 1):
        for a in (sp.Rational(0), sp.Rational(2, 5), sp.Rational(1), sp.Rational(3, 2)):
            assert direct_poly(n, v, a) == formula_poly(n, v, a)
            identity_checks += 1

root_checks = 0
for n in range(1, 13):
    m = (n + 1) // 2
    for v in range(1, n + 1):
        d0 = gcd(n + 2, v)
        d1 = gcd(n + 2, v + 1)
        protected = (d0 - 1) // 2 + (d1 - 1) // 2
        for a in (sp.Rational(1, 4), sp.Rational(1), sp.Rational(3, 2), sp.Rational(2)):
            P = formula_poly(n, v, a)
            real_distinct = sp.polys.polytools.count_roots(P, -sp.oo, sp.oo)
            expected = 2 * m - protected if a < 1 else (m if a == 1 else protected)
            assert real_distinct == expected, (n, v, a, real_distinct, expected)
            assert P.degree() == 2 * m
            root_checks += 1

print('IDENTITY_CHECKS_PASSED', identity_checks)
print('ROOT_COUNT_CHECKS_PASSED', root_checks)
