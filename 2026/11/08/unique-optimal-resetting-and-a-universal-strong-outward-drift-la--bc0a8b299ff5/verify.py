#!/usr/bin/env python3
"""Exact algebra checks and numerical sanity tests for the stated theorem."""
import math
import sympy as s
from scipy.optimize import brentq

y,a,b=s.symbols('y a b', positive=True)
q=b+y
h=s.expand((q*q-b*b)*(a+q+1)-2*q*(a+q))
assert s.expand(h-(y**3+(a+3*b-1)*y**2+2*(a+b)*(b-1)*y-2*b*(a+b)))==0
k=h+2*a*(b+y)*s.exp(-2*b-y)
assert s.simplify(s.diff(k,y,2)-(6*y+2*(a+3*b-1)+2*a*s.exp(-2*b-y)*(b+y-2)))==0
for B in [1,2,5,10,20,40,80]:
 for eta in [.2,1.,3.,20.]:
  A=eta*B
  def root_fn(t):
   return float(h.subs({a:A,b:B,y:t}))+2*A*(B+t)*math.exp(-2*B-t)
  star=brentq(root_fn,1e-10,7)
  assert root_fn(star-1e-6)<0<root_fn(star+1e-6)
  if B>=10:
   correction=0.5-1/(1+eta)
   assert abs(B*(star-1)-correction)<0.65
   assert abs((2*B*star+star*star)-(2*B+2*eta/(1+eta)))<2.0
print('PASS: polynomial and curvature identities, 28 numerical optimum checks')
