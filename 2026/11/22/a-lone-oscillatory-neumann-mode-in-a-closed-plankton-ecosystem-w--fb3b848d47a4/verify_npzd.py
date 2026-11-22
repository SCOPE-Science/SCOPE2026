#!/usr/bin/env python3
"""Exact finite algebraic certificate for a conservative four-field plankton spectrum.

Requires Python 3 and SymPy. A coefficient-positivity proof treats infinitely
many harmonics; no numerical spectral sampling is used to certify the tail.
"""
import sympy as S

q, z, u = S.symbols('q z u', real=True)
nu, g, lam, delta, alpha = map(S.Integer, (22, 2, 1, 1, 2))
N, P, Z, D = S.symbols('N P Z D', real=True)
X = S.Matrix([N, P, Z, D])
F = S.Matrix([
    -nu*P*N/(N+1) + alpha*D,
    nu*P*N/(N+1)-g*Z*P/(P+1)-lam*P,
    g*Z*P/(P+1)-delta*Z,
    lam*P+delta*Z-alpha*D,
])
equilibrium = {N:S.Integer(1),P:S.Integer(1),Z:S.Integer(10),D:S.Rational(11,2)}
assert all(S.cancel(v.subs(equilibrium)) == 0 for v in F)
assert sum(equilibrium[v] for v in X) == S.Rational(35,2)
J = S.simplify(F.jacobian(X).subs(equilibrium))
J_expected = S.Matrix([
    [-S.Rational(11,2), -11, 0, 2],
    [S.Rational(11,2), 5, -1, 0],
    [0,5,0,0],
    [0,1,1,-2],
])
assert J == J_expected
M = J-q*S.diag(20,1,1,1)
co = S.Poly((z*S.eye(4)-M).det(),z)
b3,b2,b1,b0 = [S.factor(t) for t in co.all_coeffs()[1:]]
expected = [
    (46*q+5)/2,
    S.Rational(3,2)*(42*q**2-33*q+26),
    (122*q**3-213*q**2-34*q+185)/2,
    q*(40*q**3-109*q**2-112*q+565)/2,
]
assert all(S.cancel(a-b)==0 for a,b in zip((b3,b2,b1,b0),expected))
H2 = S.factor(b3*b2-b1)
H3 = S.factor(b3*b2*b1-b1**2-b3**2*b0)
assert S.cancel(H2-(5552*q**3-3498*q**2+3161*q+20)/4)==0
assert S.cancel(H3-(148176*q**6-349272*q**5+307020*q**4-166524*q**3-253991*q**2+142495*q+925)/2)==0
assert S.factor(co.as_expr().subs(q,0)) == z*(2*z**3+5*z**2+78*z+185)/2
assert S.Rational(5,2)*39>S.Rational(185,2)

a = 40*q**3-109*q**2-112*q+565
assert S.discriminant(a,q)==-5523716316
assert a.subs(q,0)>0 and S.LC(S.Poly(a,q))>0
vals=(b3,b2,b1,b0,H2,H3)
assert tuple(S.factor(v.subs(q,S.Rational(1,4))) for v in vals)==(
    S.Rational(33,4),S.Rational(489,16),S.Rational(5283,64),
    S.Rational(8493,128),S.Rational(5427,32),S.Rational(4855491,512))
assert tuple(S.factor(v.subs(q,1)) for v in vals)==(
    S.Rational(51,2),S.Rational(105,2),S.Integer(30),
    S.Integer(192),S.Rational(5235,4),-S.Rational(171171,2))
assert all(v.subs(q,S.Rational(1,4))>0 for v in vals)
assert all(v.subs(q,1)>0 for v in vals[:5]) and H3.subs(q,1)<0
for expr in vals:
    shifted = S.Poly(S.expand(expr.subs(q,u+S.Rational(9,4))),u)
    assert all(c>0 for c in shifted.all_coeffs()), (expr,shifted)
print('PASS: exact feasible equilibrium, Jacobian, dispersion coefficients,')
print('      continuum positive determinant, Routh tables, and infinite tail.')
