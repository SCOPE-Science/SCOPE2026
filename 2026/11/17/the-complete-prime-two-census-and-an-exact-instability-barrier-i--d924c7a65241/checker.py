#!/usr/bin/env python3
"""Exact symbolic check for the axially symmetric prime-two classification."""
import sympy as s
b,c,p=s.symbols('b c p',real=True,nonzero=True)
q=(1+b)*(1+c)/p
mu=-c*(p*p+q*q)/(1-c*c)
z0=(p*p+c*q*q)/(1-c*c)
z1=(q*q+c*p*p)/(1-c*c)
J=lambda y,z:s.Matrix([[0,1,0],[-b,mu+z,y],[0,2*y,c]])
assert s.cancel(-b*p+mu*q+q*z0-p)==0
assert s.cancel(-b*q+mu*p+p*z1-q)==0
assert s.cancel(c*z0+q*q-z1)==0
assert s.cancel(c*z1+p*p-z0)==0
K=J(p,z1)*J(q,z0)
assert s.factor((s.eye(3)-K).det()+2*c/(1+c)*(p*p-q*q)**2)==0
bb,cc,pp=s.Rational(1,5),s.Rational(1,2),s.Rational(9,5)
subs={b:bb,c:cc,p:pp}
assert s.factor(q.subs(subs))==1
assert s.factor(mu.subs(subs)) < -2*cc*(1+bb)/(1-cc)
assert s.factor((s.eye(3)-K).det().subs(subs))<0
print('Exact orbit identities, symbolic instability barrier, and rational witness: PASS')
