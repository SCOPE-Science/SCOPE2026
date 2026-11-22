#!/usr/bin/env python3
"""Exact symbolic and independent numerical checks for two unequal-pulse response theorem."""
import sympy as sp
from fractions import Fraction
from math import exp,log
from scipy.integrate import quad

A,B,K,y,z = sp.symbols('A B K y z', positive=True)
D=(K+A+B)*(K+y*(A+B))+A*B*(1-y+y*y)
def R(a,b):
    return (K+a)*(K+a*y+b)/((K+a*y)*(K+(a*y+b)*z/y))
Pi=(A*y+K)*(B*y+K)*(A*z+B*y*z+K*y)*(A*y*z+B*z+K*y)
assert sp.cancel(R(A,B)-R(B,A)-K*y*(A-B)*(1-y)*(z*D-A*B*y*y)/Pi)==0
assert sp.expand(D-A*B*y - ((K+A+B)*(K+y*(A+B))+A*B*(1-y)**2))==0
# At infinite horizon the unnormalized rational numerator has strict negative factor.
L=(K+A)*(K+A*y+B)*(K+B*y)-(K+B)*(K+B*y+A)*(K+A*y)
assert sp.factor(L)==A*B*y*(A-B)*(y-1)
# At T=log(23), for A=2,B=1,K=1,k=1,tau=log(2), the exact tie occurs.
par={A:sp.Integer(2),B:sp.Integer(1),K:sp.Integer(1),y:sp.Rational(1,2)}
assert D.subs(par)==sp.Rational(23,2)
assert (A*B*y*y/D).subs(par)==sp.Rational(1,23)
for z0,sign in [(sp.Rational(1,2),1),(sp.Rational(1,23),0),(sp.Rational(1,64),-1)]:
    v=sp.factor((R(A,B)-R(B,A)).subs({**par,z:z0}))
    assert int(bool(v>0))-int(bool(v<0))==sign
# Different numerical path: quadrature of pointwise response versus logarithmic formula.
count=0
for a in [0.4,1.,2.,5.]:
 for b in [0.1,0.3]:
  if a<=b:continue
  for cap in [0.25,1.,4.]:
   for rate in [0.2,1.3]:
    for delay in [0.3,1.5]:
     for h in [delay,delay+0.2,delay+2.,delay+10.]:
      Y=exp(-rate*delay);Z=exp(-rate*h)
      def formula(x,w):return log((cap+x)*(cap+x*Y+w)/((cap+x*Y)*(cap+(x*Y+w)*Z/Y)))/rate
      def integral(x,w):
       f=lambda v:v/(cap+v)
       return quad(lambda t:f(x*exp(-rate*t)),0,delay,epsabs=2e-12)[0]+quad(lambda t:f((x*Y+w)*exp(-rate*(t-delay))),delay,h,epsabs=2e-12)[0]
      for x,w in [(a,b),(b,a)]:
       assert abs(formula(x,w)-integral(x,w))<2e-10
       count+=1
      DD=(cap+a+b)*(cap+Y*(a+b))+a*b*(1-Y+Y*Y)
      threshold=log(DD/(a*b*Y*Y))/rate
      assert threshold>delay
      d=formula(a,b)-formula(b,a)
      if h<threshold-1e-9:assert d>0
      if h>threshold+1e-9:assert d<0
print('PASS: 3 exact polynomial identities, 3 exact rational tests, '+str(count)+' independent quadrature comparisons, and all threshold/order checks.')
