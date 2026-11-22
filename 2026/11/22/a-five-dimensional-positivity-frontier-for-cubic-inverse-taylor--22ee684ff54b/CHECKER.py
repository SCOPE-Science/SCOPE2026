"""Exact symbolic certificate for Boolean-cube [0/3] Padé heat steps.

Requires Python 3 and SymPy. Run `python CHECKER.py` from this directory.
All claims about continuous steps are proved by polynomial identities and
sign certificates, not by testing finitely many positive steps.
"""
from math import comb
from pathlib import Path
import json
import sympy as sp

h, t = sp.symbols('h t')

def q(z):
    return 1 + z + z**2/sp.Integer(2) + z**3/sp.Integer(6)

def coefficient(d, dist):
    total = 0
    for k in range(d + 1):
        signed = sum((-1)**ell * comb(dist, ell) * comb(d-dist, k-ell)
                     for ell in range(max(0, k-(d-dist)), min(dist, k)+1))
        total += signed / q(2*h*k)
    return sp.factor(total / 2**d)

# Reconstruct independently and match the portable exact certificate.
certificate = json.loads((Path(__file__).parent / 'CERTIFICATE.json').read_text())

# For dimension five the common denominator has positive coefficients.
D = sp.factor(sp.fraction(coefficient(5, 0))[1])
assert all(c > 0 for c in sp.Poly(D, h).all_coeffs())

for j in range(6):
    v = coefficient(5, j)
    num, den = sp.fraction(v)
    assert sp.simplify(den-D) == 0
    assert sp.rem(sp.Poly(num,h), sp.Poly(h**j,h)).is_zero
    p = sp.Poly(sp.cancel(num/h**j), h)
    expected = [sp.Rational(v) for v in certificate[str(j)]['ascending_numerator_quotient_coefficients']]
    assert list(reversed(p.all_coeffs())) == expected
    if j < 5:
        assert all(c > 0 for c in p.all_coeffs())
    else:
        assert p.degree() == 10
        # Cover [0,1/6] and [1/6,infinity) by two exact
        # nonnegative-coefficient changes of variable.
        left = sp.Poly(sp.cancel((1+t)**10 * p.as_expr().subs(
            h, t/(6*(1+t)))), t)
        right = sp.Poly(p.as_expr().subs(h, t+sp.Rational(1,6)),t)
        assert left.degree() == right.degree() == 10
        assert list(reversed(left.all_coeffs())) == [sp.Rational(v) for v in certificate['left_ascending_coefficients']]
        assert all(c > 0 for c in left.all_coeffs())
        assert list(reversed(right.all_coeffs())) == [sp.Rational(v) for v in certificate['right_ascending_coefficients']]
        assert all(c > 0 for c in right.all_coeffs())

# Exact negative opposite-corner entry of Q_6.
bad = coefficient(6, 6).subs(h, sp.Rational(1,6))
assert bad == sp.Rational(certificate['Q6_distance_6_h_1_over_6']), bad

# Directly check Walsh formula against inverse on Q_3, independently
# constructing the 8-by-8 matrix in vertex coordinates.
from itertools import product
verts = list(product((0, 1), repeat=3))
A = sp.zeros(8)
for i, x in enumerate(verts):
    A[i,i] = 3
    for j,y in enumerate(verts):
        if sum(a != b for a,b in zip(x,y)) == 1:
            A[i,j] = -1
hh = sp.Rational(2,7)
B = (sp.eye(8)+hh*A+(hh*A)**2/2+(hh*A)**3/6).inv()
for i,x in enumerate(verts):
    for j,y in enumerate(verts):
        dist = sum(a != b for a,b in zip(x,y))
        assert B[i,j] == coefficient(3,dist).subs(h,hh)
assert B * sp.ones(8,1) == sp.ones(8,1)
print('PASS: Q5 six rational-function identities; strict positivity certificate;')
print('Q6 exact negative fraction; Q3 64 direct inverse comparisons and row sums')
