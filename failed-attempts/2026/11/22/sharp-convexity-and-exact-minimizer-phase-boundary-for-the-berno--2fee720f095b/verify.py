#!/usr/bin/env python3
"""Exact algebra and numerical checks for a soft-target logistic FBE curvature theorem."""
import sympy as sp
import math
p,q,gamma=sp.symbols('p q gamma',real=True)
h=p*(1-p)
g=p-q
third=h*(1-2*p)
Q=sp.expand(h+(p-q)*(1-2*p))
assert sp.simplify(Q-(-3*p**2+2*(1+q)*p-q))==0
v=sp.simplify(Q.subs(p,(1+q)/3))
assert sp.simplify(v-(q*q-q+1)/3)==0
Fcurv=sp.factor(h*(1-gamma*Q))
assert sp.expand(Fcurv-(h-gamma*(h*h+g*third)))==0
for qn in [sp.Rational(1,10),sp.Rational(1,3),sp.Rational(1,2),sp.Rational(7,10),sp.Rational(9,10)]:
 threshold=sp.factor(3/(1-qn+qn*qn))
 peak=sp.factor((1+qn)/3)
 assert sp.simplify(Fcurv.subs({q:qn,p:peak,gamma:threshold}))==0
 assert threshold>=3 and threshold<=4
 if qn!=sp.Rational(1,2):
  gm=sp.factor((threshold+4)/2)
  dis=sp.factor(1-qn+qn**2-3/gm)
  assert dis>0
  pm=(1+qn-sp.sqrt(dis))/3
  pp=(1+qn+sp.sqrt(dis))/3
  assert 0<pm<pp<1
  assert sp.simplify(Fcurv.subs({q:qn,p:(1+qn)/3,gamma:gm}))<0
  assert sp.simplify(Fcurv.subs({q:qn,p:pm,gamma:gm}))==0
  assert sp.simplify(Fcurv.subs({q:qn,p:pp,gamma:gm}))==0
  assert sp.simplify(h.subs(p,qn)*(1-gm*h.subs(p,qn)))>0
for qn in [0.03,0.1,0.2,0.3,0.49,0.5,0.51,0.8,0.9,0.97]:
 th=3/(1-qn+qn*qn)
 for k in [0.5,0.999,1,1.001,(4/th+1)/2]:
  gm=k*th
  if gm>=4: continue
  pp=(1+qn)/3
  if abs(gm-th)>1e-12:
   assert (pp*(1-pp)*(1-gm*(-3*pp*pp+2*(1+qn)*pp-qn)) < 0)==(gm>th)
print('PASS: exact curvature identity, exact sharp threshold, roots, unique minimizer, 10 numerical labels')
