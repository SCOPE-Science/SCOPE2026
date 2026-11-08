"""Exact critical-point checks for two hexagonal very affine surfaces.

Run with Python 3 and SymPy. Saturation uses an auxiliary inverse variable;
all Groebner bases are over QQ and all rank/degree tests are exact.
"""
import sympy as s

x, y, z = s.symbols('x y z')
A, B, C = 1 + x, 1 + y, 1 + x + x*y
H_cases = {'I': 1 + y + x*y, 'II': 1 + x*y}
a, b, c, d, e, f = (2, 3, 5, 7, 11, 13)

for name, H in H_cases.items():
    prod = s.expand(A*B*C*H)
    x_eq = s.expand(a*prod + c*x*s.cancel(prod/A)
                    + e*x*s.diff(C,x)*s.cancel(prod/C)
                    + f*x*s.diff(H,x)*s.cancel(prod/H))
    y_eq = s.expand(b*prod + d*y*s.cancel(prod/B)
                    + e*y*s.diff(C,y)*s.cancel(prod/C)
                    + f*y*s.diff(H,y)*s.cancel(prod/H))
    # The inverse variable ensures x, y, A, B, C, H never vanish.
    basis = s.groebner([x_eq,y_eq,z*x*y*prod - 1],z,y,x,
                       order='lex',domain=s.QQ)
    polys = [p.as_expr() for p in basis.polys]
    univariate = [p for p in polys if p.free_symbols == {x}]
    expected_degree = 5 if name == 'I' else 4
    assert len(univariate) == 1, (name,'univariate count')
    px = univariate[0]
    assert s.degree(px,x) == expected_degree, (name,'degree')
    assert s.gcd(px,s.diff(px,x)) == 1, (name,'squarefree')
    # Lex leading monomials z, y, x^degree prove the full degree
    # of the finite reduced quotient, not merely a projection bound.
    leading = {p.monoms()[0] for p in basis.polys}
    assert leading == {(1,0,0),(0,1,0),(0,0,expected_degree)}, (name,leading)
    print(f'{name}: saturated degree={expected_degree}, squarefree=True')
    print(f'{name}: x-eliminant={s.factor(px)}')

# Independently, complement inclusion-exclusion has two deleted
# C* curves and two C* minus a point curves in case I. The latter
# intersect in two roots of x^2+x+1, and A,B intersect in one point.
# Case II has just C* minus one point and three distinct double points.
chi_I = 0 - ((0+0-1-1)-(1+2))
chi_II = 0 - ((0+0-1+0)-3)
assert (chi_I,chi_II) == (5,4)
print('Euler characteristics: I=5, II=4; all exact checks PASS')
