"""Exact normal form and finite-orbit cross-check for a quadratic predator--prey Euler map.
Run with: python verify_ns_euler.py (requires SymPy; NumPy for optional orbit check).
"""
import sympy as S

x,y,h,u,v=S.symbols('x y h u v',real=True)
fx=x+h*x*(1-x-y)
fy=y+h*y*(x-S.Rational(1,4)-y/S.Integer(2))
p=S.Matrix([fx,fy]); pe=S.Matrix([S.Rational(1,2),S.Rational(1,2)])
assert all(S.simplify((p-pe)[i].subs({x:S.Rational(1,2), y:S.Rational(1,2)}))==0 for i in range(2))
J=p.jacobian([x,y]);
Jc=S.simplify(J.subs({x:S.Rational(1,2),y:S.Rational(1,2)}))
assert Jc==S.Matrix([[1-h/S.Integer(2),-h/S.Integer(2)], [h/S.Integer(2),1-h/S.Integer(4)]])
assert S.expand(Jc.det())==1-S.Rational(3,4)*h+S.Rational(3,8)*h*h
A=S.simplify(Jc.subs(h,2)); assert A==S.Matrix([[0,-1],[1,S.Rational(1,2)]])
R=S.sqrt(15); lam=(1+S.I*R)/4
q=S.Matrix([1,-lam]); qb=S.conjugate(q)
assert S.simplify(A*q-lam*q)==S.zeros(2,1)
assert S.simplify(lam*S.conjugate(lam)-1)==0
assert all(S.simplify(lam**j-1)!=0 for j in [1,2,3,4])
Q=S.Matrix.hstack(q,qb); ell=S.simplify(Q.inv()[0,:]);
assert S.simplify((ell*q)[0]-1)==0
assert S.simplify((ell*qb)[0])==0

P2=S.expand((p-pe).subs({x:u+S.Rational(1,2),y:v+S.Rational(1,2),h:2}))
assert S.simplify(P2-A*S.Matrix([u,v])-S.Matrix([-2*u*u-2*u*v,2*u*v-v*v]))==S.zeros(2,1)

def B(a,b):
 return S.Matrix([-4*a[0]*b[0]-2*(a[0]*b[1]+a[1]*b[0]),
                   2*(a[0]*b[1]+a[1]*b[0])-2*a[1]*b[1]])
assert S.expand(B(S.Matrix([u,v]),S.Matrix([u,v]))/2)==S.Matrix([-2*u*u-2*u*v, 2*u*v-v*v])

h11=S.simplify((S.eye(2)-A).inv()*B(q,qb));
h20=S.simplify((lam*lam*S.eye(2)-A).inv()*B(q,q));
assert h11==S.Matrix([1,-4]);
assert S.simplify((S.eye(2)-A)*h11-B(q,qb))==S.zeros(2,1)
assert S.simplify((lam**2*S.eye(2)-A)*h20-B(q,q))==S.zeros(2,1)
resonant=S.simplify(S.expand_complex((ell*(B(q,h11)+S.Rational(1,2)*B(qb,h20)))[0]))
assert S.simplify(resonant-(S.Rational(23,6)-S.Rational(25,18)*S.I*R))==0
first_lyap=S.simplify(S.re(S.conjugate(lam)*resonant))
assert first_lyap==-S.Rational(17,4)
assert S.diff(S.sqrt(Jc.det()),h).subs(h,2)==S.Rational(3,8)
assert S.simplify(S.Rational(3,8)/(-first_lyap))==S.Rational(3,34)

# Finite numerical trajectories support, but are not a proof of, the invariant-circle result.
try:
 import math
 for step in [2.001,2.003,2.01]:
  xx,yy=.503,.497
  xs=[]; ys=[]
  for n in range(20000):
   xx,yy=xx+step*xx*(1-xx-yy),yy+step*yy*(xx-.25-.5*yy)
   if n>=19000: xs.append(xx);ys.append(yy)
  assert min(xs+ys)>0
  actual=max(abs(xx-.5) for xx in xs)
  expected=2*math.sqrt(3*(step-2)/34)
  assert abs(actual/expected-1)<.04, (step,actual,expected)
 print('VERIFY_OK exact_jacobian=1 eigenpair=1 nonresonance=1 quadratic_jet=1 resolvent_identities=2 exact_cubic_coefficient=-17/4 radial_slope=3/34 numerical_curves=3')
except ImportError:
 print('VERIFY_OK exact_jacobian=1 eigenpair=1 nonresonance=1 quadratic_jet=1 resolvent_identities=2 exact_cubic_coefficient=-17/4 radial_slope=3/34 numerical_curves=not_run')
