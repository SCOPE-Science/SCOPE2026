#!/usr/bin/env python3
"""Exact symbolic checks for the coupled-logistic invariant-ray theorem."""
from fractions import Fraction
import sympy as s

r, e, t, z, D = s.symbols('r e t z D', real=True)
d = 1 + e**2
k = (1-e)/(1+e)
x = (1+e)*t/d
y = k*x + z
Fx = r*x*(1-x+e*y)
Fy = r*y*(1-y-e*x)
t_next = s.factor(d*Fx/(1+e))
z_next = s.factor(Fy-k*Fx)
assert s.factor(t_next-r*t*(1-t+e*z)) == 0
assert s.factor(z_next-r*z*(1-2*t/d-z)) == 0

# Jacobian in the coordinate chart, restricted to the invariant ray.
J=s.Matrix([t_next,z_next]).jacobian([t,z]).subs(z,0)
Jexpected=s.Matrix([[r*(1-2*t), r*e*t],[0, r*(1-2*t/d)]])
assert all(s.factor(x)==0 for x in (J-Jexpected))

tplus=(r+1+s.sqrt((r-3)*(r+1)))/(2*r)
tminus=(r+1-s.sqrt((r-3)*(r+1)))/(2*r)
assert s.simplify(tplus+tminus-(r+1)/r)==0
assert s.simplify(tplus*tminus-(r+1)/r**2)==0
assert s.simplify(r*tplus*(1-tplus)-tminus)==0
assert s.simplify(r*tminus*(1-tminus)-tplus)==0
Lpar=s.simplify(r**2*(1-2*tplus)*(1-2*tminus))
assert s.factor(Lpar-(-r**2+2*r+4))==0
Ltrans=s.simplify(r**2*(1-2*tplus/D)*(1-2*tminus/D))
Lform=r**2-2*r*(r+1)/D+4*(r+1)/D**2
assert s.factor(Ltrans-Lform)==0
assert s.factor(s.diff(Lform,D)-2*(r+1)*(r*D-4)/D**3)==0
assert s.factor(Lform.subs(D,4/r)-r**2*(3-r)/4)==0
Q=s.expand(D**2*(Lform+1))
Qexpected=(r**2+1)*D**2-2*r*(r+1)*D+4*(r+1)
assert s.factor(Q-Qexpected)==0
assert s.factor(s.discriminant(Q,D)-4*(r+1)*(r**3-3*r**2-4))==0
assert s.factor(Lform.subs(D,2)-1)==0
assert s.factor(Lform.subs(D,1)-Lpar)==0

# Fully exact physical and Floquet witnesses, with no floating-point sign tests.
rr=s.Rational(17,5)
assert s.simplify(tplus.subs(r,rr)-(11+s.sqrt(11))/17)==0
assert Lpar.subs(r,rr)==-s.Rational(19,25)
witnesses={s.Rational(1,10):-s.Rational(206711,255025),
           s.Rational(1,4):-s.Rational(1459,1445),
           s.Rational(3,5):-s.Rational(6679,7225)}
for eps,want in witnesses.items():
    got=s.factor(Lform.subs({r:rr,D:1+eps**2}))
    assert got==want,(eps,got,want)
    # Coordinates for both cycle states are strictly positive and below one.
    factor=(1+eps)/(1+eps**2)
    assert s.Rational(0)<eps<s.Rational(1)
    assert factor<=s.Rational(20,17)
    assert s.Rational(20,17)*(11+s.Rational(10,3))/17<s.Rational(1)
    for pt in [tplus.subs(r,rr),tminus.subs(r,rr)]:
        xpt=s.factor((1+eps)/(1+eps**2)*pt)
        ypt=s.factor((1-eps)/(1+eps**2)*pt)
        assert s.N(xpt,25)>0 and s.N(xpt,25)<1
        assert s.N(ypt,25)>0 and s.N(ypt,25)<1
        # Direct evaluation of the original two-coordinate polynomial map.
        xnew=s.factor(rr*xpt*(1-xpt+eps*ypt))
        ynew=s.factor(rr*ypt*(1-ypt-eps*xpt))
        other=tminus.subs(r,rr) if pt==tplus.subs(r,rr) else tplus.subs(r,rr)
        assert s.simplify(xnew-(1+eps)/(1+eps**2)*other)==0
        assert s.simplify(ynew-(1-eps)/(1+eps**2)*other)==0
assert -1<witnesses[s.Rational(1,10)]<1
assert witnesses[s.Rational(1,4)]<-1
assert -1<witnesses[s.Rational(3,5)]<1
assert s.Rational(11)<s.Rational(100,9) # sqrt(11)<10/3
print('VERIFY_OK exact_map=2 exact_multipliers=2 cusp=1 witnesses=3')
