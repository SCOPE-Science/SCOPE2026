#!/usr/bin/env python3
"""Exact polynomial certificates for the generalized Legendre flex theorem.
Requires SymPy: python3 -m pip install sympy
Run: python3 verify_symbolic.py
"""
import sympy as s
x,t,Y,Z,X,z=s.symbols('x t Y Z X z')
g=x*(x-1)*(x-t)
Q=3*x**4-4*(t+1)*x**3+(4*t*t+2*t+4)*x*x-4*t*(t+1)*x+3*t*t
hom=Q.subs(x,X/Z)*Z**4
F=Y**4-X*Z*(X-Z)*(X-t*Z)
assert s.factor(s.hessian(F,(X,Y,Z)).det()+36*Y**2*hom)==0
assert s.factor(s.discriminant(Q,x)-4096*t*t*(t-1)**2*(t+1)**2*(t-2)**2*(2*t-1)**2)==0
assert s.factor(s.resultant(Q,g,x)-27*t**4*(t-1)**4)==0
ops=[(t/x,x,t**2),((x-t)/(x-1),x-1,(t-1)**2),(t*(x-1)/(x-t),x-t,t**2*(t-1)**2)]
for func,den,mul in ops:
    assert s.cancel(den**4*Q.subs(x,func)-mul*Q)==0
    assert s.cancel(den**4*g.subs(x,func)-mul*g)==0
fixed=[x*x-t,(x-1)**2-(1-t),(x-t)**2-t*(t-1)]
expected=[16*t*t*(t-1)**2*(t+1)**2,16*t*t*(t-1)**2*(t-2)**2,16*t*t*(t-1)**2*(2*t-1)**2]
for eq,goal in zip(fixed,expected):
    assert s.factor(s.resultant(Q,eq,x)-goal)==0
b=-4*(t+1)/3
c=(4*t*t+2*t+4)/3
d=-4*t*(t+1)/3
e=t*t
res=z**3-c*z*z+(b*d-4*e)*z+4*c*e-d*d-b*b*e
zvals=[2*t,2*t*(2*t-1)/3,(4-2*t)/3]
D=[-(t-2)*(2*t-1),(t-2)*(t+1),-(t+1)*(2*t-1)]
assert s.factor(res-s.prod(z-v for v in zvals))==0
for v,val in zip(zvals,D):
    assert s.factor((b*b-4*(c-v))*s.Rational(9,16)-val)==0
assert s.expand(Q.subs({x:1-x,t:1-t},simultaneous=True)-Q)==0
assert s.expand(g.subs({x:1-x,t:1-t},simultaneous=True)+g)==0
print('GENERALIZED_LEGENDRE_EXACT_POLYNOMIAL_CERTIFICATES_VERIFIED')
