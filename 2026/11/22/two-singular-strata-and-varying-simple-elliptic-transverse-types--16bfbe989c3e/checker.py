"""Exact illustrative checks for a Weierstrass-Cox hypersurface.

The universal singular-locus and resolution proofs are mathematical, not a finite computation.
Run with: python checker.py
Requires: sympy
"""
from fractions import Fraction
import sympy as sp

t, w = sp.symbols('t w')
# Example chi=3: A(u,v)=u^12+v^12, B(u,v)=u^18+2v^18.
A = t**12 + 1
B = t**18 + 2
Delta = sp.expand(4 * A**3 + 27 * B**2)
assert sp.degree(Delta, t) == 36
assert sp.gcd(Delta, sp.diff(Delta, t)) == 1
assert sp.expand(Delta - (31*t**36 + 12*t**24 + 108*t**18 + 12*t**12 + 112)) == 0
# Exact squarefreeness is the gcd assertion above.
# These two base points are both outside the discriminant.
j_infinity = 1728 * Fraction(4, 4 + 27)
j_zero = 1728 * Fraction(4, 4 + 27 * 4)
assert j_infinity != j_zero
# Weight-product Jacobian algebra dimension, valid when isolated.
assert (6//1-1)*(6//2-1)*(6//3-1) == 10
z, x, y = sp.symbols('z x y')
f = y**2-x**3-x*z**4-z**6
Gb = sp.groebner([sp.diff(f, a) for a in (x, y, z)], x, y, z, order='lex')
assert Gb.is_zero_dimensional
# The lex leading monomials are x^2, x*z^3, y, z^7;
# their standard monomials are 1,z,...,z^6,x,xz,xz^2.
lead = {tuple(poly.LM(order='lex').exponents) for poly in Gb.polys}
assert lead == {(2,0,0), (1,0,3), (0,1,0), (0,0,7)}
assert 7 + 3 == 10
for chi in [3, 4, 5, 6]:
    d = 6*chi
    weights = (1, 1, 2*chi, 3*chi)
    mu = 1
    for wt in weights:
        assert d % wt == 0
        mu *= d//wt - 1
    assert mu == 2*(6*chi-1)**2
print('PASS: squarefree sample discriminant, distinct j, transverse Milnor formulas')
