#!/usr/bin/env python3
"""Standalone exact-rational algebra tests for PoiTG canonical jump sequence.

This code checks formulas and examples, not the universal k-quantifier,
which is proved in RESULT.md by an analytic beta-density inequality.
"""
from fractions import Fraction as F
import sympy as s
z,q,a,L=s.symbols('z q a L',real=True)
r=q*(q+a)/(1+a*q)
pgf_mix=(1-a)*(1-q)/(1-q*z)+a*(1-q*q)/(1-q*q*z)
assert s.factor(pgf_mix-(1-q)*(1+a*q)*(1-r*z)/((1-q*z)*(1-q*q*z)))==0
assert s.factor(1-r-(1-q*q)/(1+a*q))==0
assert s.simplify(r-q*q-a*q*(1-q*q)/(1+a*q))==0
assert s.simplify(q-r-q*(1-q)*(1-a)/(1+a*q))==0
assert s.factor(pgf_mix.subs(z,0)-(1-q)*(1+a*q))==0
for Q in (F(1,5),F(1,2),F(3,4),F(9,10),F(99,100)):
 for A in (F(0),F(1,10),F(1,2),F(9,10),F(1)):
  R=Q*(Q+A)/(1+A*Q)
  assert Q*Q<=R<=Q
  B=lambda k:Q**k+Q**(2*k)-R**k
  assert B(1)>0
  assert all(B(k)>B(k+1)>0 for k in range(1,90))
  for lam in (F(0),F(1,3),F(2)):
   jump1=lam+B(1)
   assert jump1>B(2)
# A generic, equally weighted two-geometric mixture lacks the property.
lo,hi=F(1,6),F(5,6)
R=(lo*(1-hi)+hi*(1-lo))/((1-lo)+(1-hi))
assert R==F(13,18)
B=lambda k:lo**k+hi**k-R**k
assert B(3)-B(2)==F(35,5832)>0
# First three power coefficients of logarithmic PGF at a rational parameter.
Q,A=F(3,4),F(2,5)
R=Q*(Q+A)/(1+A*Q)
for k in range(1,6):
 zz=s.symbols('zz')
 P=((1-Q)*(1+A*Q)*(1-R*zz)/((1-Q*zz)*(1-Q*Q*zz)))
 formal=s.diff(s.log(P),zz,k).subs(zz,0)/s.factorial(k)
 assert s.simplify(formal-(Q**k+Q**(2*k)-R**k)/k)==0
print('PASS: exact rational PGF, canonical jumps, strict DSD checks, and a counterexample for unrelated geometric rates')
