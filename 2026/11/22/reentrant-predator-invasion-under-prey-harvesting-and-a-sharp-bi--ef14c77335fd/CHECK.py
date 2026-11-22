"""Exact algebra and local equilibrium tests for a two-threshold predator invasion theorem.

Requires Python 3 and SymPy. The symbolic identities certify formulas; local
numerical tests are consistency checks, not substitutes for the proof.
"""
import sympy as s

x,y,h=s.symbols('x y h')
r,K,q,k,P,B,A,d,v,m=s.symbols('r K q k P B A d v m', positive=True)
f = x*(r*(1-x/K)/(1+k*y)-h/(1+q*x))-P*x*y/(1+B*x)
G = A*x/(1+B*x)-d-v*x
z = y*(G-m*y)
H = r*(1-x/K)*(1+q*x)
assert s.cancel(f.subs({y:0,h:H}))==0
fx = s.factor(s.diff(f,x).subs({y:0,h:H}))
fy = s.factor(s.diff(f,y).subs({y:0,h:H}))
assert s.cancel(fx - r*x*(q*(K-2*x)-1)/(K*(1+q*x)))==0
assert s.cancel(fy + r*k*x*(1-x/K)+P*x/(1+B*x))==0
assert s.cancel(s.diff(G,x)-(A/(1+B*x)**2-v))==0

vals={r:s.Integer(2), K:s.Integer(5), q:s.Rational(1,10), k:s.Rational(1,5),
      P:s.Rational(3,4), B:s.Rational(1,2), A:s.Rational(3,8),
      d:s.Rational(3,20), v:s.Rational(1,10), m:s.Rational(1,100)}
g=s.factor(G.subs(vals)); hh=s.factor(H.subs(vals))
assert s.cancel((1+B*x).subs(vals)*g+(x-1)*(x-3)/s.Integer(20))==0
assert hh.subs(x,3)==s.Rational(26,25)
assert hh.subs(x,1)==s.Rational(44,25)
assert s.factor(s.diff(hh,x).subs(x,3))==-s.Rational(11,25)
assert s.factor(s.diff(hh,x).subs(x,1))==-s.Rational(7,25)

fxv=fx.subs(vals); fyv=fy.subs(vals); gv=s.diff(g,x)
Q=lambda xx: s.factor(-vals[m]-gv.subs(x,xx)*(fyv/fxv).subs(x,xx))
assert Q(3)==s.Rational(61,1375)
assert Q(1)==-s.Rational(118,525)
critical=s.factor(-gv.subs(x,3)*(fyv/fxv).subs(x,3))
assert critical==s.Rational(299,5500)
# Slopes of positive branches: -lambda_h/Q, lambda_h = G_x/H_x.
low_slope=s.factor(-(gv.subs(x,3)/s.diff(hh,x).subs(x,3))/Q(3))
high_slope=s.factor(-(gv.subs(x,1)/s.diff(hh,x).subs(x,1))/Q(1))
assert low_slope==-s.Rational(125,61)
assert high_slope==-s.Rational(125,118)

fv=f.subs(vals); zv=z.subs(vals)
Jac=s.Matrix([fv,zv]).jacobian([x,y]);
# Check local branch existence on the predicted side and Jacobian stability.
for ht,guess,pred_sign in [(s.Rational(26,25)-s.Rational(1,10000),(3,.0002),-1),
                            (s.Rational(44,25)-s.Rational(1,10000),(1,.0001),1)]:
    root=s.nsolve([fv.subs(h,ht),zv],[x,y],guess, tol=1e-26,prec=50)
    xx=float(root[0]); yy=float(root[1]); assert xx>0 and yy>0
    jj=Jac.subs({x:root[0],y:root[1],h:ht}).evalf(40)
    det=float(jj.det()); trace=float(s.trace(jj))
    assert (det>0)-(det<0)==pred_sign
    if pred_sign==1:assert trace<0
    print('harvest',ht,'coexistence',tuple(map(str,root)),'trace',trace,'det',det)
print('symbolic identities, thresholds, bifurcation directions and local equilibria: PASS')
