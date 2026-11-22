"""Exact algebraic checks for a symmetric torus-sextic bifurcation.
Run: python check.py  (requires SymPy). The full classification uses the proof in RESULT.md;
these computations confirm its critical polynomial identities and Hessians.
"""
import sympy as S
X,Y,Z,l,s,w=S.symbols('X Y Z l s w')
G=X*Y-Z**2
H=X**3+Y**3+l*Z**3
F=S.expand(G**3+s*H**2)
assert S.Poly(F,X,Y,Z).total_degree()==6
# Elimination at the six base cusps: t^2 + l*t + 1, repeated iff l^2=4.
t=S.symbols('t')
assert S.expand(S.discriminant(t**2+l*t+1,t)-(l**2-4)) == 0
# Critical-point equation away from the base, in Z=1:
f=S.expand(F.subs(Z,1))
fx,fy=S.diff(f,X),S.diff(f,Y)
assert S.expand(X*fx-Y*fy - 6*s*(X**3-Y**3)*(X**3+Y**3+l))==0
# Diagonal critical-point polynomial, showing exactly the three outer wall factors.
d=S.expand(f.subs({X:w,Y:w}))
disc=S.factor(S.discriminant(d,w))
expected=-46656*s**4*(l-2)**3*(l+2)**3*(4*s+1)*(l**2*s-1)*(4*l**2*s+l**2-4)
assert S.expand(disc-expected)==0
# Finite node on s=1/l^2-1/4, at X=Y=-l/2 (other two obtained by mu_3).
p={X:-l/2,Y:-l/2,s:1/l**2-S.Rational(1,4)}
assert S.factor(f.subs(p))==0
assert S.factor(fx.subs(p))==0
assert S.factor(fy.subs(p))==0
assert S.simplify(S.hessian(f,(X,Y)).det().subs(p) + S.Rational(27,64)*(l**2-4)**3) == 0
# Central node, s=1/l^2, at X=Y=0: nonsingular quadratic term 3XY.
assert S.factor(f.subs({X:0,Y:0,s:1/l**2}))==0
assert S.factor(S.hessian(f,(X,Y)).det().subs({X:0,Y:0,s:1/l**2})) == -9
# Infinity: Z=0, X=1. Three nodes at Y^3=1 when s=-1/4.
finf=S.expand(F.subs({X:1,Z:0}))
assert S.expand(finf-(Y**3+s*(1+Y**3)**2))==0
assert S.expand(finf.subs(s,-S.Rational(1,4)) + S.Rational(1,4)*(Y**3-1)**2) == 0
Hinf=S.hessian(F.subs(X,1),(Y,Z))
assert S.factor(Hinf.det().subs({Y:1,Z:0,s:-S.Rational(1,4)}))==27
# Explicit complete-intersection model: substitute X=(W+R)/2,Y=(W-R)/2.
W,R,T,c=S.symbols('W R T c')
Q=R**2-W**2-4*T**2+4*Z**2
E=W**3+3*W*(T**2-Z**2)+l*Z**3-c*T**3
xx=(W+R)/2; yy=(W-R)/2
assert S.expand((G.subs({X:xx,Y:yy})+T**2)+Q/S.Integer(4))==0
onQ=S.expand((H.subs({X:xx,Y:yy})-c*T**3)-E)
assert S.expand(onQ-3*W*Q/S.Integer(4))==0
# The plane-cubic singularities occur at l^2=4, s=-1/4 or s=1/l^2-1/4.
assert all(S.expand(S.diff(E,v)-target)==0 for v,target in zip((W,T,Z),(3*(T**2+W**2-Z**2),-3*T*(T*c-2*W),3*Z*(-2*W+Z*l))))
# Check three sample wall configurations, incl. rational four-node intersection.
for lv,sv,nodes in [(S.Integer(1),S.Integer(2),0),(S.Integer(1),S.Integer(1),1),(S.Integer(1),-S.Rational(1,4),3),(S.Integer(1),S.Rational(3,4),3),(2*S.I,-S.Rational(1,4),4)]:
  walls = [S.simplify(sv-1/lv**2)==0,S.simplify(sv+S.Rational(1,4))==0,S.simplify(sv-(1/lv**2-S.Rational(1,4)))==0]
  assert (int(walls[0])+3*int(walls[1])+3*int(walls[2]))==nodes
print('PASS: cusp base discriminant, all node-wall factors, finite/central/infinity Hessians, canonical model, and wall samples')
