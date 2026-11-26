"""Exact algebraic checks for the two-patch cubic Allee equilibrium classification.
Run: python verification.py. Not a substitute for the accompanying proof.
"""
import sympy as S
s,d,m,u,x,y=S.symbols('s d m u x y', real=True)
f=lambda z:z*(z-S.Rational(1,2))*(1-z)
F=f(x)+m*(y-x); G=f(y)+m*(x-y)
U=S.expand((F+G)/2).subs({x:S.Rational(1,2)+s,y:S.Rational(1,2)-s+d}) if False else None
Fsd=S.expand(F.subs({x:S.Rational(1,2)+s+d,y:S.Rational(1,2)+s-d}))
Gsd=S.expand(G.subs({x:S.Rational(1,2)+s+d,y:S.Rational(1,2)+s-d}))
Su=S.factor((Fsd+Gsd)/2)
Dd=S.factor((Fsd-Gsd)/2)
assert S.simplify(Su+s*(3*d*d+s*s-S.Rational(1,4)))==0
assert S.simplify(Dd+d*(d*d+3*s*s+2*m-S.Rational(1,4)))==0
J=S.Matrix([Su,Dd]).jacobian([s,d])
assert S.simplify(J[0,0].subs(s,0).subs(d*d,S.Rational(1,4)-2*m)-(6*m-S.Rational(1,2)))==0
assert S.simplify(J[1,1].subs(s,0).subs(d*d,S.Rational(1,4)-2*m)-(4*m-S.Rational(1,2)))==0
assert S.factor(J[0,1].subs(s,0))==S.factor(J[1,0].subs(s,0))==0
assert S.factor(J.det().subs({s*s:(1-12*m)/16,d*d:(1+4*m)/16}))==-(1-12*m)*(1+4*m)/8
# At m = 1/12, the nonhyperbolic asymmetric points have a repelling cubic centre drift.
d0=S.sqrt(S.Rational(1,12)); c=-3/(2*d0)
h=d0+c*s*s
assert S.simplify(S.limit(Su.subs({m:S.Rational(1,12),d:h})/s**3,s,0)-8)==0
assert S.simplify(S.limit(Dd.subs({m:S.Rational(1,12),d:h})/s**2,s,0))==0
for mm in [S.Rational(1,100),S.Rational(1,24),S.Rational(1,16),S.Rational(1,12),S.Rational(1,10),S.Rational(1,8),S.Rational(1,6)]:
 eqs=[(S.Rational(0),S.Rational(0)),(S.Rational(1,2),S.Rational(1,2)),(S.Rational(1),S.Rational(1))]
 if mm<S.Rational(1,8):
  val=S.sqrt(S.Rational(1,4)-2*mm)
  eqs.extend([(S.Rational(1,2)+val,S.Rational(1,2)-val),(S.Rational(1,2)-val,S.Rational(1,2)+val)])
 if mm<S.Rational(1,12):
  for ss in [+S.sqrt(1-12*mm)/4,-S.sqrt(1-12*mm)/4]:
   for dd in [+S.sqrt(1+4*mm)/4,-S.sqrt(1+4*mm)/4]:
    eqs.append((S.Rational(1,2)+ss+dd,S.Rational(1,2)+ss-dd))
 for xx,yy in eqs:
  assert S.simplify(F.subs({m:mm,x:xx,y:yy}))==0
  assert S.simplify(G.subs({m:mm,x:xx,y:yy}))==0
  assert 0<=xx<=1 and 0<=yy<=1
 expected=9 if mm<S.Rational(1,12) else (5 if mm<S.Rational(1,8) else 3)
 assert len(eqs)==expected,(mm,len(eqs),expected)
 print('m=',mm,'equilibria=',len(eqs))
# Gradient energy and strict decay identity, valid throughout the positive invariant square
W=(x*x*(1-x)**2+y*y*(1-y)**2)/4+m*(x-y)**2/2
assert S.factor(S.diff(W,x)+F)==0
assert S.factor(S.diff(W,y)+G)==0
print('All symbolic and exact-rational checks passed.')
