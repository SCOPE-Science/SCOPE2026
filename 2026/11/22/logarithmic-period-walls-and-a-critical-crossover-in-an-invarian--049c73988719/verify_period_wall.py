#!/usr/bin/env python3
"""Finite algebraic and numerical checks for the boundary period asymptotics.
These are consistency checks, not an infinite-asymptotic certificate.
"""
import math
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq
x,y,p,q,r=sp.symbols('x y p q r', real=True)
A=(1-x*x)*(1+p*x); B=(1-y*y)*(1+q*y)
assert sp.simplify((x/A)*(-A*y)+(y/B)*(B*x))==0
ucrit=1/(2*(1-r))-sp.Rational(1,2)+sp.Rational(1,4)*sp.log((1-r)/(1+r))
assert sp.simplify(sp.diff(ucrit,r)-r/((1-r)**2*(1+r)))==0
assert sp.simplify(sp.diff(sp.atanh(r),r)-1/((1+r)*(1-r)))==0
checks=3
for z in [0,sp.Rational(1,2),-sp.Rational(1,2)]:
 z=float(z)
 numerical=quad(lambda s:1/((1+s)*(1+z*s)),0,1,epsabs=1e-13)[0]
 expected=(math.log(2)-math.log1p(z))/(1-z)
 assert abs(numerical-expected)<2e-13
 checks+=1
for kappa in [0.0,0.25,1.0,3.0]:
 for E in [100.0,400.0]:
  eps=kappa/E; pp=1-eps
  def pot(rr):
   if eps==0:
    return 1/(2*(1-rr))-.5+.25*math.log((1-rr)/(1+rr))
   return quad(lambda s:s/((1-s*s)*(1-pp*s)),0,rr,epsabs=1e-8,epsrel=2e-11)[0]
  delta=brentq(lambda d:pot(1-d)-E,1e-12,0.9,xtol=1e-14)
  exact_defect=2/(2-eps)*math.log((2-delta)/(eps+(1-eps)*delta))
  phi=math.log(4) if kappa==0 else math.log(2*(-math.expm1(-2*kappa))/kappa)
  assert abs(exact_defect-(math.log(E)+phi)) < (0.12 if E==100 else 0.04)
  target=0.5 if kappa==0 else kappa/math.expm1(2*kappa)
  assert abs(E*delta-target)<0.03
  checks+=2
print(f'PASS: {checks} finite algebraic/integral/scaling consistency checks')
