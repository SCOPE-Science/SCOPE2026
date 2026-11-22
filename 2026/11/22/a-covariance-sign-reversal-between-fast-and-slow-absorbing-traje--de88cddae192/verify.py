#!/usr/bin/env python3
"""Symbolic consistency checks for two-mark absorbing renewal covariance."""
import sympy as sp
b,L0,L1,s,z,t=sp.symbols('b L0 L1 s z t',positive=True)
f0=(1-b)*L0/(s+L0); f1=b*L1/(s+L1); h=1-f0-f1
F0=f0/(s*h); F1=f1/(s*h); F01=2*f0*f1/(s*h*h)
assert sp.simplify(F0+(F1) - (f0+f1)/(s*h))==0
# Short-time analytic coefficients from expansion at s=infinity.
T=[]
for F in (F0,F1,F01):
    Q=sp.series(F.subs(s,1/z),z,0,7).removeO().expand()
    T.append(sp.expand(sum(Q.coeff(z,k)*t**(k-1)/sp.factorial(k-1) for k in range(1,7))))
C=sp.expand(T[2]-T[0]*T[1]); c3=sp.factor(C.coeff(t,3))
c3_expected=b*(1-b)*L0*L1*(2*b-1)*(L0-L1)/6
assert sp.simplify(c3-c3_expected)==0
assert sp.simplify(C.coeff(t,2))==0
# Large-time coefficients: rational transforms have only poles at 0 and -c.
a0=sp.simplify(sp.limit(s*s*F0,s,0))
a1=sp.simplify(sp.limit(s*s*F1,s,0))
d0=sp.simplify(sp.limit(sp.diff(s*s*F0,s),s,0))
d1=sp.simplify(sp.limit(sp.diff(s*s*F1,s),s,0))
j=sp.simplify(sp.limit(sp.diff(s**3*F01,s),s,0))
slope=sp.factor(j-a0*d1-a1*d0)
c=b*L0+(1-b)*L1
expected=b*(1-b)*L0*L1*(L1-L0)*((1-b)*L1-b*L0)/c**3
assert sp.simplify(slope-expected)==0
print('small-time cubic coefficient =',c3)
print('long-time covariance slope =',slope)
print('large-time mean rates =',a0,a1)
assert sp.simplify(sp.limit(s**3*F01,s,0)/2-a0*a1)==0
# Explicit numerical example inside strict reversal wedge.
parms={b:sp.Rational(7,10),L0:1,L1:5}
means=[sp.inverse_laplace_transform(sp.apart(F.subs(parms),s),s,t) for F in (F0,F1,F01)]
Cexact=means[2]-means[0]*means[1]
for tt in [sp.Rational(1,20),sp.Rational(1,10),1,3,10]:
 print('time',tt,'covariance',float(Cexact.subs(t,tt).evalf(30)))
assert float(Cexact.subs(t,sp.Rational(1,20)).evalf(30))<0
assert float(Cexact.subs(t,10).evalf(30))>0
print('PASS: expansions, exact transforms, and strict finite-time sign reversal')
