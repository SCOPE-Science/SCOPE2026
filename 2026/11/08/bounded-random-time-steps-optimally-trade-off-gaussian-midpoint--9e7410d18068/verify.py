#!/usr/bin/env python3
"""Exact algebra and finite-case checks of the bounded random-step OU phase law.

Requires SymPy. Finite checks are supplementary to the analytic convex-envelope proof.
"""
import random
from fractions import Fraction
import sympy as sp

u, B, m = sp.symbols('u B m', positive=True)
r=lambda z: (1-z)/(1+z)
f=lambda z: r(z)**2
assert sp.factor(sp.diff(r(u),u,2)-4/(u+1)**3)==0
assert sp.factor(sp.diff(f(u),u,2)-8*(2-u)/(u+1)**4)==0

t=1+2/B
ell=(B**2*u-B**2-B+1)/(B+1)**3
assert sp.factor(ell.subs(u,t)-f(t))==0
assert sp.factor(sp.diff(f(u),u).subs(u,t)-sp.diff(ell,u))==0
assert sp.factor(ell.subs(u,B)-f(B))==0
assert sp.factor(f(u)-ell - (B-u)*(B*u-B-2)**2/((B+1)**3*(1+u)**2))==0
assert sp.factor(f(m)-ell.subs(u,m) - (B-m)*(B*m-B-2)**2/((B+1)**3*(1+m)**2))==0

assert sp.factor(f(sp.Rational(6,5))-sp.Rational(1,121))==0
assert sp.factor(f(sp.Integer(10))-sp.Rational(81,121))==0
q2=sp.Rational(25,44)*f(sp.Rational(6,5))+sp.Rational(19,44)*f(sp.Integer(10))
q1=sp.Rational(25,44)*r(sp.Rational(6,5))+sp.Rational(19,44)*r(sp.Integer(10))
assert sp.simplify(q2-sp.Rational(391,1331))==0
assert sp.simplify(q1+sp.Rational(49,121))==0
assert sp.simplify((1+q2)/(1-q2)-sp.Rational(861,470))==0
assert sp.simplify((1+q1)/(1-q1)-sp.Rational(36,85))==0
assert sp.simplify((1+f(sp.Integer(sp.Integer(5))))/(1-f(sp.Integer(sp.Integer(5))))-sp.Rational(13,5))==0
assert sp.simplify((1+r(sp.Integer(5)))/(1-r(sp.Integer(5)))-sp.Rational(1,5))==0

# Exact finite rational tests of all branch formulas on admissible grid means.
checks=0
for maxu in (Fraction(1,2),Fraction(1),Fraction(2),Fraction(5,2),Fraction(3),Fraction(4),Fraction(10),Fraction(20)):
  tangent=1+Fraction(2,1)/maxu if maxu>2 else maxu
  for j in range(1,20):
    mean=maxu*Fraction(j,20)
    if mean<=tangent:
      qstar=f(mean)
    else:
      qstar=(maxu*maxu*mean-maxu*maxu-maxu+1)/(maxu+1)**3
    assert 0<=qstar<=1
    assert qstar<=f(mean)
    # Sample families of competing two-atom laws with the prescribed mean.
    for ai in range(0,10):
      a=maxu*Fraction(ai,20)
      if a>mean: continue
      for bi in range(10,21):
        b=maxu*Fraction(bi,20)
        if b<mean or b==a:continue
        p=(b-mean)/(b-a)
        q=p*f(a)+(1-p)*f(b)
        assert q>=qstar,(maxu,mean,a,b,q,qstar)
        rbar=p*r(a)+(1-p)*r(b)
        assert rbar>=r(mean)
        checks+=1
print('symbolic identities: PASS')
print('rational two-atom comparison cases:',checks,'PASS')
print('example (B,m)=(10,5): q2_opt=',q2,'q1_opt=',q1)
print('quadratic IACT deterministic=',sp.Rational(13,5),'optimal=',sp.Rational(861,470))
print('linear IACT deterministic=',sp.Rational(1,5),'quadratic-optimized law=',sp.Rational(36,85))
