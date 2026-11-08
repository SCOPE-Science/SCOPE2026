#!/usr/bin/env python3
"""Exact finite-field certificates for an exceptional dual plane quintic.
Requires Python 3 and SymPy. All polynomial equalities are over GF(7).
"""
from itertools import product
from sympy import Matrix, Poly, symbols

r, x, y, z, a, b, c, s = symbols('r x y z a b c s')
K = lambda expr, gens=(r,): Poly(expr, *gens, modulus=7)
X = K(r**4 + r**2 - r - 3)
Y = K(2*r**4 + r**2 - 2*r + 2)
Z = K(-3*r**4 + r**2 + 3*r + 1)
forms = [X, Y, Z]
assert X.gcd(Y).gcd(Z).degree() == 0
F = x**3*y + y**3*z + z**3*x
assert K(F.subs({x:X.as_expr(), y:Y.as_expr(), z:Z.as_expr()})).is_zero
assert int(Matrix([[int(P.nth(i)) % 7 for P in forms] for i in range(3)]).det()) % 7 == 3
quadrics = [X**2, X*Y, X*Z, Y**2, Y*Z, Z**2]
assert int(Matrix([[int(P.nth(i))%7 for P in quadrics] for i in range(6)]).det()) % 7 == 6
G = [K(Y.as_expr()*Z.diff().as_expr()-Z.as_expr()*Y.diff().as_expr()),
     K(Z.as_expr()*X.diff().as_expr()-X.as_expr()*Z.diff().as_expr()),
     K(X.as_expr()*Y.diff().as_expr()-Y.as_expr()*X.diff().as_expr())]
A = K(-3*r**5+3*r**3+2*r**2+2*r+1)
B = K(r**5+3*r**3-3*r**2+r+1)
C = K(2*r**5+3*r**3+r**2-3*r+1)
assert G == [A,B,C]
assert A.gcd(B).gcd(C).degree() == 0
assert int(Matrix([[int(P.nth(i)) % 7 for P in (A,B,C)] for i in range(3)]).det()) % 7 == 4
D = a**3*c**2 - 3*a**2*b**3 + 2*b**2*c**3
assert K(D.subs({a:A.as_expr(), b:B.as_expr(), c:C.as_expr()})).is_zero
# At all four listed singularities, both the quintic and its gradient vanish.
for pt in [(1,0,0),(0,1,0),(0,0,1),(1,2,4)]:
 vals = {a:pt[0], b:pt[1], c:pt[2]}
 assert int(D.subs(vals))%7 == 0
 for w in (a,b,c):
  assert int(D.diff(w).subs(vals))%7 == 0
# The exceptional point has no finite preimage: its sole preimage is r=infinity.
assert (B-2*A).gcd(C-4*A).degree() == 0
assert [P.nth(5)%7 for P in (A,B,C)] == [4,1,2]
# Local jets of the normalization at infinity, with s=1/r.
order=9
coeff = [4, 0, 3, 2, 2, 1]
inv = [0]*order
inv[0] = pow(coeff[0], -1, 7)
for i in range(1, order):
 inv[i] = -inv[0]*sum(coeff[j]*inv[i-j] for j in range(1, min(i,5)+1))%7
jet=lambda expr:[int(Poly(expr,s).nth(i))%7 for i in range(order)]
def mul(p,q):
 return [sum(p[j]*q[i-j] for j in range(i+1))%7 for i in range(order)]
A_s = 4+3*s**2+2*s**3+2*s**4+s**5
B_s = 1+3*s**2+4*s**3+s**4+s**5
C_s = 2+3*s**2+s**3+4*s**4+s**5
u = mul(jet(B_s-2*A_s), inv)
v = mul(jet(C_s-4*A_s), inv)
u2 = mul(u,u);u3=mul(u2,u)
w = [(v[i]-3*u[i]-3*u2[i]-5*u3[i])%7 for i in range(order)]
assert u[:4] == [0,0,1,0]
assert w[:8] == [0,0,0,0,0,0,0,3]
# The three coordinate-chart tangent cones are cuspidal (square + cube).
# Local tangent-cone and cubic witnesses at the three coordinate cusps.
assert K(D.subs({a:1,b:x,c:y}),(x,y)).coeff_monomial(y**2) == 1
assert K(D.subs({a:1,b:x,c:y}),(x,y)).coeff_monomial(x**3) == -3
assert K(D.subs({a:x,b:1,c:y}),(x,y)).coeff_monomial(x**2) == -3
assert K(D.subs({a:x,b:1,c:y}),(x,y)).coeff_monomial(y**3) == 2
assert K(D.subs({a:x,b:y,c:1}),(x,y)).coeff_monomial(y**2) == 2
assert K(D.subs({a:x,b:y,c:1}),(x,y)).coeff_monomial(x**3) == 1
print('KLEIN7_DUAL: quartic normalization degree four, nondegenerate, not conic')
print('KLEIN7_DUAL: exact Gauss map has three quintic forms without common zero')
print('KLEIN7_DUAL: irreducible image quintic a^3*c^2-3*a^2*b^3+2*b^2*c^3')
print('KLEIN7_DUAL: cusp at [1:2:4] has local orders 2,7; three coordinate A2 cusps')
print('VERIFY_OK')
