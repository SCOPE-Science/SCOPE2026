#!/usr/bin/env python3
"""Exact algebraic checks for a three-step double-base expanding map."""
import sympy as s
b=s.symbols('b', positive=True)
Q=1+b+b*b
D=1+2*b+3*b*b
assert s.factor((1-b)*Q-(1-b**3))==0
R=s.Matrix([[1/Q,b/Q,b*b/Q],[1,0,0],[0,1,0]])
pi=s.Matrix([[Q/D,b*(1+b)/D,b*b/D]])
assert all(s.factor(v)==0 for v in pi*R-pi)
assert all(s.factor(sum(R.row(i))-1)==0 for i in range(3))
h0=Q/(b*D);h1=(1+b)/(b*D);h2=1/(b*D)
assert s.factor(b*h0+b*b*h1+b**3*h2-1)==0
assert s.factor(h0-h0/Q-b*h1)==0
assert s.factor(h1-h0/Q-b*h2)==0
assert s.factor(h2-h0/Q)==0
g=s.Matrix([0,1,1]);p=s.factor((pi*g)[0])
assert s.factor(p-b*(1+2*b)/D)==0
C=lambda n:s.factor((pi*s.diag(*g)*R**n*g)[0]-p*p)
C0=C(0);C1=C(1)
assert s.factor(C0-p*(1-p))==0
assert s.factor(C1+b**3*(b+2)/D**2)==0
A=b*(1+b)/Q;B=b*b/Q
for n in range(8):
    assert s.factor(C(n+2)+A*C(n+1)+B*C(n))==0
z=s.symbols('z')
assert s.factor(R.charpoly(z).as_expr()-(z-1)*(z*z+A*z+B))==0
assert s.factor(A*A-4*B+b*b*(3+2*b+3*b*b)/Q**2)==0
sig=b*Q*(1+4*b+b*b)/D**3
sumcov=(C0+C1+A*C0)/(1+A+B)
assert s.factor(C0+2*(sumcov-C0)-sig)==0
assert s.factor(p*(1-p)-sig-6*b**3*(1+b)*Q/D**3)==0
H=3*b**6+26*b**5+39*b**4+40*b**3+7*b*b-6*b-1
assert s.factor(s.diff(sig,b)+H/D**4)==0
lam,t=s.symbols('lam t')
F=lam**3-lam**2/Q-b*s.exp(t)*lam/Q-b*b*s.exp(2*t)/Q
assert s.factor(F.subs({lam:1,t:0}))==0
lp=s.factor((-s.diff(F,t)/s.diff(F,lam)).subs({lam:1,t:0}))
lpp=s.factor((-(s.diff(F,lam,2)*lp**2+2*s.diff(F,lam,t)*lp+s.diff(F,t,2))/s.diff(F,lam)).subs({lam:1,t:0}))
assert s.factor(lp-p)==0
assert s.factor(lpp-lp**2-sig)==0
for x in [s.Rational(1,4),s.Rational(1,3),s.Rational(1,2),s.Rational(2,3),s.Rational(3,4)]:
    assert float(sig.subs(b,x))>0
    assert float((p*(1-p)-sig).subs(b,x))>0
    assert all(abs(float((pi*R-pi)[j].subs(b,x)))<1e-12 for j in range(3))
print('VERIFY_OK exact_stationarity=3 invariant_density=4 covariance_recurrences=8 pressure_derivatives=2 sample_parameters=5')
