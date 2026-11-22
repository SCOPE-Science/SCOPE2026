#!/usr/bin/env python3
"""Exact algebraic checks and finite rational-grid diagnostics for a two-node kernel quadrature theorem."""
from fractions import Fraction
import sympy as sp

x,y,eta,u,d=sp.symbols('x y eta u d', real=True)
K11=x*(1-x)+eta
K22=y*(1-y)+eta
K12=x*(1-y)
k1=x*(1-x)/2
k2=y*(1-y)/2
det=sp.expand(K11*K22-K12**2)
R=sp.factor((K22*k1**2+K11*k2**2-2*K12*k1*k2)/det)
change={x:(1+u-d)/2,y:(1+u+d)/2}
Rs=sp.factor(R.subs(change, simultaneous=True))
Ds=sp.factor(det.subs(change, simultaneous=True))
F=d*(u**2-(1-d)**2)+2*eta*(3*d**2+u**2-1)
claimed_du=u*(d*(1-d)+2*eta)*((1-d)**2-u**2+4*eta)*F/(128*Ds**2)
assert sp.cancel(sp.diff(Rs,u)-claimed_du)==0
center=sp.factor(Rs.subs(u,0))
assert sp.cancel(center-(1-d**2)**2/(16*(1+2*eta-d)))==0
q=3*d**2-(4+8*eta)*d+1
assert sp.cancel(sp.diff(center,d)-(1-d**2)*q/(16*(1+2*eta-d)**2))==0
assert sp.cancel((center-d*(1-d**2)/4).subs(eta,((1-d)*(1-3*d))/(8*d)))==0

# For nonnegative noise the boundary observation at an endpoint carries no
# information, and the maximum one-observation reduction is attained at 1/2.
t=sp.symbols('t', real=True)
Rone=(t*(1-t)/2)**2/(t*(1-t)+eta)
assert sp.factor(Rone.subs(t,sp.Rational(1,2))-1/(16*(1+4*eta)))==0

# Independent exact rational-grid diagnostic; not a proof of the continuum theorem.
def rational_R(a,b,e):
  h=lambda t:t*(1-t)/2
  aa=a*(1-a)+e;bb=b*(1-b)+e;cc=a*(1-b)
  DD=aa*bb-cc*cc
  return (bb*h(a)**2+aa*h(b)**2-2*cc*h(a)*h(b))/DD

checks=0
for e in (sp.Rational(1,100),sp.Rational(1,10),sp.Rational(1,2),sp.Rational(1),sp.Rational(5)):
    root=(2+4*e-sp.sqrt(16*e**2+16*e+1))/3
    best=sp.N(root*(1-root**2)/4,60)
    for i in range(17):
        for j in range(i,17):
            a=sp.Rational(i,16);b=sp.Rational(j,16)
            qv=rational_R(a,b,e)
            assert sp.N(qv,60)<=best+sp.Float('1e-50',60),(a,b,e,qv,best)
            checks+=1
print('PASS: 5 exact symbolic identities; %d rational location/noise comparisons' % checks)
for e in [sp.Rational(1,100),sp.Rational(1,10),sp.Rational(1),sp.Rational(5)]:
    r=(2+4*e-sp.sqrt(16*e**2+16*e+1))/3
    print('eta=%s: nodes=(%.12f, %.12f), posterior_variance=%.12f' %
        (e,float((1-r)/2),float((1+r)/2),float(sp.Rational(1,12)-r*(1-r*r)/4)))
