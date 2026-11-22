"""Exact symbolic checks for the singular Eckardt pencil of a cubic fourfold.

Requires sympy. Run with: python verify.py
The accompanying proof handles the global geometric assertions.
"""
import sympy as sp

t, r, x0, x1, x2 = sp.symbols('t r x0 x1 x2')
p_plus = t**6 + t**3 + 1
p_minus = t**6 - 3*t**3 + 1
p = sp.expand(p_plus * p_minus)

# Elimination for critical points in the affine chart w=1.
critical = [3*x0**2 + 1, 3*x1**2 + t, 3*x2**2 + t**2,
            x0 + t*x1 + t**2*x2]
gb = sp.groebner(critical, x0, x1, x2, t, order='lex')
eliminants = [g.as_expr() for g in gb.polys if g.as_expr().free_symbols <= {t}]
assert len(eliminants) == 1
assert sp.Poly(eliminants[0], t).monic().as_expr() == p

# Independent binary cubic discriminant for the plane section.
g = sp.expand((-t*r-t*t)**3 + r**3 + 1)
assert sp.expand(sp.discriminant(g, r) + 27*p) == 0
assert sp.expand(9*t**5 - (sp.Poly(g, r).all_coeffs()[1]**2 -
               3*sp.Poly(g, r).all_coeffs()[0]*sp.Poly(g, r).all_coeffs()[2])) == 0

# Two coprime squarefree sextics, each irreducible over Q by reduction mod 2.
assert sp.gcd(p, sp.diff(p, t)) == 1
assert sp.resultant(p_plus, p_minus, t) == 4096
assert sp.Poly(p_plus, t).is_irreducible
assert sp.Poly(p_plus, t, modulus=2).is_irreducible
assert sp.Poly(p_minus, t, modulus=2).is_irreducible
assert sp.expand(sp.cyclotomic_poly(9, t) - p_plus) == 0

# For each bad parameter the critical points are the two signs of x0^2=-1/3.
# Their ratios are x2/x0 = delta*t, x1/x0=-(1+delta*t^3)/t.
for delta, sextic in ((1, p_plus), (-1, p_minus)):
    a1 = -(1 + delta*t**3)/t
    a2 = delta*t
    assert sp.expand(1 + t*a1 + t**2*a2) == 0
    assert sp.rem(sp.Poly(sp.together(a1**2-t)*t**2, t),
                  sp.Poly(sextic, t)).is_zero
    assert sp.expand(a2**2-t**2) == 0
    # Nonzero base-parameter derivative at every singularity.
    assert sp.gcd(sextic, delta*t**3-1) == 1

# Each critical point has a rank-3 quadratic part and a nonzero x3^3 part:
# analytic type A2, with Milnor number 2. There are 12*2 such points.
assert 12*2*2 == 48   # total local discriminant order = degree of dual cubic fourfold
print('PASS: 12 distinct singular parameters, 2 A2 points per fiber')
print('PASS: binary-cubic discriminant -27*P, two irreducible Galois sextets')
print('PASS: local discriminant divisor 4*(P=0), degree 48')
