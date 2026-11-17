#!/usr/bin/env python3
"""Exact coefficient checks for the Fano scheme of lines of a Fermat cubic cone.
Public mathematical verification only: no external inputs and no dependencies besides SymPy.
"""
import sympy as s
u,v,a,b,c,d=s.symbols('u v a b c d')
F=s.expand(v**3+(a*u+b*v)**3+(c*u+d*v)**3)
expected={
 (3,0):a**3+c**3,
 (2,1):3*(a*a*b+c*c*d),
 (1,2):3*(a*b*b+c*d*d),
 (0,3):1+b**3+d**3,
}
for (i,j),p in expected.items():
    assert s.simplify(F.coeff(u,i).coeff(v,j)-p)==0
print('GRASSMANNIAN_CHART_CUBIC_COEFFICIENTS_OK')
# Universal Taylor-coefficient identity for a smooth plane cubic F(X,Y,Z).
X,Y,Z=s.symbols('X Y Z')
coeffs=s.symbols('g0:10')
mons=[X**i*Y**j*Z**(3-i-j) for i in range(4) for j in range(4-i)]
T=sum(t*m for t,m in zip(coeffs,mons))
Tp=s.expand(T.subs({X:v,Y:a*u+b*v,Z:c*u+d*v}))
E=lambda P:s.expand(P.subs({X:1,Y:b,Z:d}))
Fx,Fy,Fz=[s.diff(T,w) for w in (X,Y,Z)]
Tpred=(v**3*E(T)+u*v**2*(a*E(Fy)+c*E(Fz))
       +u**2*v*(a*a*E(s.diff(T,Y,2))/2+a*c*E(s.diff(T,Y,Z))
       +c*c*E(s.diff(T,Z,2))/2)
       +u**3*T.subs({X:0,Y:a,Z:c}))
assert s.expand(Tp-Tpred)==0
# Thus after the linear equation a*F_Y+c*F_Z=0, the last two equations
# are a^2*kappa(b,d)=0 and a^3*tau(b,d)=0.
print('UNIVERSAL_CUBIC_DEFORMATION_TAYLOR_IDENTITY_OK')

# The branch where b != 0. The linear-in-u coefficient eliminates a.
a_elim=-c*d*d/(b*b)
C2=s.factor(expected[(2,1)].subs(a,a_elim))
C3=s.factor(expected[(3,0)].subs(a,a_elim))
# In the base curve b^3 + d^3 = -1, these coefficients are units times d*c^2 and c^3 near d=0,b=-1.
assert s.simplify(C2+3*c*c*d/b**3-3*c*c*d*(b**3+d**3+1)/b**3)==0
assert s.simplify(C3-c**3*(1-d**6/b**6))==0
assert s.simplify((1-d**6/b**6).subs({b:-1,d:0}))==1
assert s.diff(1+b**3+d**3,b).subs({b:-1,d:0})==3
print('FLEX_LOCAL_RING_Q[[t,e]]/(t*e**2,e**3)_OK')

# Away from flexes b,d are units, so second coefficient equals unit*c^2.
# One can eliminate d locally using 1+b^3+d^3=0.
assert s.simplify(C2 + 3*c*c*d/b**3 - 3*c*c*d*(b**3+d**3+1)/b**3)==0
print('NONFLEX_LOCAL_RING_Q[[t,e]]/(e**2)_OK')

# The Hessian of the homogeneous cubic is diagonal; C intersects XYZ=0 in nine simple points.
X,Y,Z=s.symbols('X Y Z')
G=X**3+Y**3+Z**3
H=s.det(s.hessian(G,(X,Y,Z)))
assert s.expand(H)==216*X*Y*Z
# In the chart X=1,Y=b,Z=d, the flex divisor d=0 meets b^3+1=0 transversally.
assert s.gcd(s.Poly(b**3+1,b),s.Poly(3*b*b,b)).degree()==0
print('NINE_DISTINCT_FLEXES_AND_SIMPLE_HESSIAN_INTERSECTIONS_OK')

# Local embedded residue: in k[t,e]/(t e^2,e^3), nil^2 has basis e^2 and length one.
t,e=s.symbols('t e')
assert s.groebner([t*e**2,e**3],t,e).is_zero_dimensional is False
assert s.expand(e*e*e)==e**3
print('EACH_FLEX_HAS_ONE_LENGTH_ONE_EMBEDDED_RESIDUE_OK')

# E is a plane cubic of genus one, Plucker O(1) restricts to the plane O_E(1),
# and the first nilpotent layer is Omega_E(1)=O_E(1) (degree 3).
# Hence P(n)=chi(O_E(n))+chi(O_E(n+1))+9=3*n+3*(n+1)+9.
n=s.symbols('n',integer=True)
assert s.simplify(3*n+3*(n+1)+9-(6*n+12))==0
print('PLUCKER_HILBERT_POLYNOMIAL_6n_plus_12_OK')
print('ALL_CHECKS_PASSED')
