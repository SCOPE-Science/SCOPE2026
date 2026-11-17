"""Exact identities and numerical checks for two-phase implicit cusp stability.

Requires Python 3 and SymPy. Checks reproduce finite algebraic certificates,
not an independent mathematical audit or a proof of general inequalities.
"""
import sympy as S
z, p, m, d = S.symbols('z p m d', real=True)
B0=S.Matrix([[p,-1],[-S.Rational(3,2)*z,1]])
B1=S.Matrix([[p,-1],[-2*z,1]])
J0=B0.inv()*S.diag(1,S.Rational(1,2))
J1=B1.inv()*S.diag(1,S.Rational(1,3))
M=S.simplify(J1*J0)
D=3*(p-2*z)*(2*p-3*z)
N=p*p+9*z+6
assert S.simplify(S.trace(M)-N/D)==0
assert S.simplify(M.det()-1/D)==0
p_outer=1-3*z-4*z*z
D0=S.factor(D.subs(p,p_outer))
N0=S.factor(N.subs(p,p_outer))
assert S.expand(D0-3*(4*z*z+5*z-1)*(8*z*z+9*z-2))==0
assert S.expand(D0-N0+1-2*z*(2*z+3)*(20*z*z+21*z-10))==0
assert S.expand(D0+N0+1-2*(56*z**4+126*z**3+44*z*z-27*z+7))==0
z_star=(-S.Integer(21)+S.sqrt(1241))/40
assert S.simplify(20*z_star*z_star+21*z_star-10)==0
assert 0.35<float(z_star)<0.36
b_star=S.expand(-3*z_star-z_star*z_star)
for bz,should_stabilize in [(-S.Rational(1,2),False),(-S.Rational(1),False),(-S.Rational(2),True),(-S.Rational(3),True)]:
 zz=(-3+S.sqrt(9-4*bz))/2
 PP=p_outer.subs(z,zz)
 MM=M.subs({p:PP,z:zz})
 eigen=[complex(ev.evalf()) for ev in MM.eigenvals()]
 assert (max(abs(e) for e in eigen)<1)==should_stabilize
 # Exact orbit residual at t=+sqrt(zz), a=0 and b=bz.
 t=S.sqrt(zz)
 assert S.simplify(bz*t+3*t**3+t**5)==0
# Symmetry-breaking sheet after eliminating the auxiliary coordinates.
u=m+d;v=m-d
B=2-S.Rational(12,5)*(u*u+u*v+v*v) -(u**4+u**3*v+u*u*v*v+u*v**3+v**4)
B_expected=2-S.Rational(36,5)*m*m-S.Rational(12,5)*d*d-5*m**4-10*m*m*d*d-d**4
assert S.expand(B-B_expected)==0
H=S.expand(5*B*(u+v)+16*u**3+14*v**3+5*(u**5+v**5))
assert S.simplify(H.subs(d,0)-2*m*(10-21*m*m-20*m**4))==0
assert S.simplify(S.diff(H,d).subs(d,0)-6*m*m)==0
assert abs(float(S.diff(H,m).subs({d:0,m:S.sqrt(z_star)})))>10
assert abs(float(S.diff(B,m).subs({d:0,m:S.sqrt(z_star)})))>1
print('VERIFY_OK exact_matrix_trace_determinant=2 exact_jury_factorizations=3')
print('VERIFY_OK exact_symmetry_breaking_identities=3 numerical_stability_cases=4')
print('z_star=',S.N(z_star,17),'b_star=',S.N(b_star,17))
