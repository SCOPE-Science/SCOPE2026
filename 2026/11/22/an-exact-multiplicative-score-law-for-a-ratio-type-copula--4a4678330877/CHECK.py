"""Symbolic and numerical reproducibility for a rational copula's product law.

Requires sympy. The primary argument is written in RESULT.md.
"""
import math
import sympy as s

u,v,z,w = s.symbols('u v z w', positive=True)
C = u*v*(u+v)/(1+u*v)
assert s.simplify(C.subs(v,1)-u)==0
assert s.simplify(C.subs(u,1)-v)==0
assert s.factor(s.diff(C,u,v)-2*(u+v)/(1+u*v)**3)==0
conditional=s.factor(s.diff(C,u).subs(v,z/u))
assert s.factor(conditional-z*(2+z+z/u**2)/(1+z)**2)==0
cdf=s.factor(z+s.integrate(conditional,(u,z,1)))
assert s.factor(cdf-4*z/(1+z)**2)==0
assert s.factor(s.diff(cdf,z)-4*(1-z)/(1+z)**3)==0
assert s.factor(s.simplify(1-cdf.subs(z,s.exp(-w))-(s.exp(w)-1)**2/(s.exp(w)+1)**2))==0
assert s.simplify(1-s.tanh(w/2)**2-s.sech(w/2)**2)==0
A1=2*s.tanh(w/2)
A2=2*w*s.tanh(w/2)-4*s.log(s.cosh(w/2))
assert s.trigsimp(s.diff(A1,w)-s.sech(w/2)**2)==0
assert s.trigsimp(s.diff(A2,w)-w*s.sech(w/2)**2)==0
assert s.simplify(s.limit(A1,w,s.oo)-A1.subs(w,0)-2)==0
assert s.simplify(s.limit(A2,w,s.oo)-A2.subs(w,0)-4*s.log(2))==0
t,x = s.symbols('t x', positive=True)
H=4/(1+s.exp(-t))**2-(1+t)
assert s.factor(s.diff(H,t).subs(s.exp(-t),x)-(1-x)*(x*x+4*x-1)/(1+x)**3)==0
for zz in [0.00001,0.001,0.02,0.1,0.25,0.5,0.8,0.99]:
    ff=float(cdf.subs(z,zz))
    assert abs(ff-4*zz/(1+zz)**2)<1e-12
    assert 0<ff<1
print('PASS: 13 symbolic identities and 16 numerical/domain checks.')
print('Mean log-score = 2; variance =',float(8*s.log(2)-4))
