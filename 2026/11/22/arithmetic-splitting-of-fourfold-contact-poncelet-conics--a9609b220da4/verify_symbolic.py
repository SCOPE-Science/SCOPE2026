"""Symbolic proof-identity checks for the fourfold-contact conic construction.

Run `python3 verify_symbolic.py`; requires SymPy (no network).
"""
import sympy as S
X, Y, Z, u, v, lam, a, b, s, t = S.symbols('X Y Z u v lam a b s t')
B = S.Matrix([[lam,0,S.Rational(1,2)],[0,-1,0],[S.Rational(1,2),0,0]])
assert S.factor(B.det()) == S.Rational(1,4)
L=S.Matrix([u*v, -u-v, 1])
assert S.simplify(4*(L.T*B.adjugate()*L)[0] + (u-v)**2 + 4*lam)==0
Linf=S.Matrix([-u,1,0])
assert S.factor(4*(Linf.T*B.adjugate()*Linf)[0]) == -1
Q=X*Z-Y**2
Xp, Yp, Zp=X,b*X+a*Y,b**2*X+2*a*b*Y+a**2*Z
assert S.expand(Xp*Zp-Yp**2-a**2*Q)==0
assert S.expand(Q.subs({X:s**2,Y:s*t,Z:t**2}, simultaneous=True)) == 0
assert S.expand((Q+lam*X**2).subs({X:s**2,Y:s*t,Z:t**2}, simultaneous=True)-lam*s**4)==0
print('ALL SYMBOLIC IDENTITIES PASSED')
