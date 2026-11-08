"""Exact integer-polynomial identities underpinning cyclic-cubic singularity classification.
Run: python3 verify_local.py (requires SymPy).
These identities complement, but do not replace, the general finite-field proof.
"""
import sympy as s
X,Y,Z,a,b,c,d,u,v=s.symbols('X Y Z a b c d u v')
F=a*X**2*Y+b*Y**2*Z+c*Z**2*X+d*X*Y*Z
x0,y0,z0=1,-d/(3*b),-3*a/d
D=d**3+27*a*b*c
for expr in [F,*[s.diff(F,T) for T in (X,Y,Z)]]:
    E=s.factor(expr.subs({X:x0,Y:y0,Z:z0}) * (3*b*d)**4)
    num=s.Poly(E,c)
    assert s.rem(num.as_expr(),D,c)==0, (expr,E)
print('SINGULAR_POINT_IDENTITY_PASS')
H=s.expand((1+u)**2*(1+v)+(1+v)**2+(1+u)-3*(1+u)*(1+v))
assert s.expand(H-(u*u-u*v+v*v+u*u*v))==0
assert s.discriminant(u*u-u*v+v*v,v)==-3*u*u
print('NODE_LOCAL_FORM_AND_DISCRIMINANT_PASS',H)
J=s.expand((1+u)**2*(1+v)+(1+v)**2+(1+u))
assert s.Poly(J-(u+v)**2-u*u*v,u,v,modulus=3).is_zero
print('CHARACTERISTIC_THREE_CUSP_FORM_PASS')
# The torus-gradient linear system has determinant 9, and its
# characteristic-three solutions force the cubic value to equal dXYZ.
B=s.Matrix([[2,0,1],[1,2,0],[0,1,2]])
assert B.det()==9
print('TORUS_GRADIENT_MATRIX_PASS',B.det())
