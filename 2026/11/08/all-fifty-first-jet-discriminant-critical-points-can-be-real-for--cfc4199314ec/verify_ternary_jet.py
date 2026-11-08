#!/usr/bin/env python3
"""Exact symbolic checks for a real ternary-cubic first-jet critical-point construction.

Run: python verify_ternary_jet.py
Requirements: Python 3, SymPy. This checks the finite identities and local
nondegeneracy data used in a separate analytic implicit-function argument.
"""
import sympy as S
u,c,b,L=S.symbols('u c b L', real=True)
x,y,z=S.symbols('x y z', real=True)
F=x**3-3*x*y**2+b*z*(x*x+y*y)+L*z**3
D=S.expand(-2*F**2+S.Rational(1,3)*sum(S.diff(F,w)**2 for w in [x,y,z]))
N=(c+b*u+L*u**3)**2+S.Rational(1,3)*(b+(3*L-2*b)*u**2-3*u*c)**2+3*(1-c*c)*(1+u*u)
# In meridian coordinates x=A/sqrt(1+u^2), y=B/sqrt(1+u^2),
# z=u/sqrt(1+u^2), A^2+B^2=1.  This explicitly verifies the reduction.
A,B=S.symbols('A B', real=True)
Fscale=F.subs({x:A,y:B,z:u})
Nfrom=S.expand(-2*Fscale**2+(1+u*u)*S.Rational(1,3)*sum(S.diff(F,w).subs({x:A,y:B,z:u})**2 for w in (x,y,z)))
triple=A**3-3*A*B**2
assert S.rem(S.expand(Nfrom-N.subs(c,triple)),A*A+B*B-1,A)==0
Pc=S.factor(S.diff(N,c))
Pu=S.factor((1+u*u)*S.diff(N,u)-6*u*N)
assert S.expand(Pc-4*((b-L)*u**3-c))==0
assert S.simplify(Pu.subs({b:0,L:2})-12*u*(c*c+2*c*u**3-2*c*u+3*u*u-1))==0
Dbase=S.factor(N.subs({b:0,L:2})/(1+u*u)**3)
Duc=S.diff(Dbase,u,c)
Duu=S.diff(Dbase,u,2)
Dcc=S.diff(Dbase,c,2)
Dc=S.diff(Dbase,c)
def det_hessian(U,C):
  # D_theta=-3*sin(3theta)*D_c, (sin 3theta)^2 = 1-C^2.
  a=S.simplify(Duu.subs({u:U,c:C}))
  cross2=S.simplify(9*(1-C*C)*Duc.subs({u:U,c:C})**2)
  d=S.simplify((-9*C*Dc+9*(1-c*c)*Dcc).subs({u:U,c:C}))
  return S.factor(a*d-cross2)
classes=[(0,0,6,S.Integer(432)),
         (-2,1,3,S.Rational(5184,3125)),
         (S.Rational(1,2),1,3,S.Rational(442368,3125)),
         (2,-1,3,S.Rational(5184,3125)),
         (-S.Rational(1,2),-1,3,S.Rational(442368,3125)),
         (S.Rational(1,2),-S.Rational(1,4),6,-S.Rational(663552,3125)),
         (-S.Rational(1,2),S.Rational(1,4),6,-S.Rational(663552,3125))]
assert sum(k for _,_,k,_ in classes)==30
for U,C,count,expected in classes:
  assert S.simplify(Pu.subs({u:U,c:C,b:0,L:2}))==0,(U,C,'u')
  assert (abs(C)==1 or S.simplify(Pc.subs({u:U,c:C,b:0,L:2}))==0),(U,C,'c')
  actual=det_hessian(U,C)
  assert actual==expected,(U,C,actual,expected)
# Each six-fold equatorial boundary point at u=0,c=+/-1 has radial
# gradient P(u,c,b)=u*(8b+O(b**2)-24c*u+O(u**2,b*u)); the second radial
# root tends to u=b/(3c), while u=0 remains a root.
for C in (-1,1):
  Q=S.factor((Pu/u).subs({c:C,L:2}))
  assert S.simplify(Q.subs(u,0)-(8*b-S.Rational(8,3)*b*b))==0
  assert S.diff(Q,u).subs({u:0,b:0})==-24*C
  assert S.diff(Q,b).subs({u:0,b:0})==8
  # Angular second derivative at the limiting point is +36.
  assert S.simplify((-9*c*Dc).subs({u:0,c:C}))==36
# At the two poles, rescale x=eps X,y=eps Y, b=-eps, z=+-sqrt(1-eps^2 R^2).
eps,X,Y=S.symbols('eps X Y',real=True)
R2=X*X+Y*Y
for sg in (1,-1):
  zz=sg*S.sqrt(1-eps**2*R2)
  local=D.subs({x:eps*X,y:eps*Y,z:zz,b:-eps,L:2})
  coefficient=S.factor(S.series(local,eps,0,4).removeO().expand().coeff(eps,3))
  expected=4*R2-8*sg*(X**3-3*X*Y**2)
  assert S.simplify(coefficient-expected)==0,(sg,coefficient)
  assert S.simplify(local.subs(eps,0)-4)==0
  # The limit polynomial has origin (positive Hessian) plus three saddles.
  H=S.hessian(expected,(X,Y))
  assert S.simplify(H.det().subs({X:0,Y:0}))==64
  stationary=[(sg*S.Rational(1,3),0),
             (-sg*S.Rational(1,6),S.sqrt(3)/6),
             (-sg*S.Rational(1,6),-S.sqrt(3)/6)]
  for px,py in stationary:
     assert S.diff(expected,X).subs({X:px,Y:py}).simplify()==0
     assert S.diff(expected,Y).subs({X:px,Y:py}).simplify()==0
     assert H.det().subs({X:px,Y:py}).simplify()==-192
print('VERIFY_OK: N/gradients, 30 simple finite points, 6 two-point splittings, 8 pole points; total 50')
