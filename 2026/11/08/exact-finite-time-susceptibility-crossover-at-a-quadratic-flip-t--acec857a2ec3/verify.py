#!/usr/bin/env python3
"""Reproducible finite-trajectory and exact-algebra checks; not an infinite proof."""
import math
import sympy as sp
import mpmath as mp
u,mu=sp.symbols('u mu',real=True)
f=lambda x:-(1+mu)*x+x*x
F=sp.expand(f(f(u)))
assert sp.expand(F-((1+mu)**2*u+mu*(1+mu)*u*u-2*(1+mu)*u**3+u**4))==0
assert sp.expand(sp.diff(F,u).subs(mu,0)-(1-6*u*u+4*u**3))==0
assert sp.expand(F.subs(mu,0)-(u-2*u**3+u**4))==0
mp.mp.dps=45

def dv(z,t):
    z=mp.mpf(z);t=mp.mpf(t)
    if z==0:return mp.sqrt(t/8)
    a=-mp.expm1(-2*z*t)
    V=mp.sqrt(z/a)
    return V*(1/(2*z)-t*mp.exp(-2*z*t)/a)

def S(z):return mp.quad(lambda t:dv(z,t)**2,[0,1])
assert abs(S(0)-mp.mpf(1)/16)<mp.mpf('1e-38')
eps=mp.mpf('0.0001')
assert abs((S(eps)-S(-eps))/(2*eps)-mp.mpf(1)/72)<mp.mpf('1e-8')

def finite(n,z,q):
    p=mp.mpf('0.15');x=p/q;mu=mp.mpf(z)/n;y=mp.mpf(0);tot=mp.mpf(0)
    for j in range(1,n+1):
        y=(-(1+mu)+2*q*x)*y-x
        x=-(1+mu)*x+q*x*x
        tot+=y*y
    return tot/n**2
for z in (-2,0,1,3):
    v=finite(18000,z,mp.mpf(1))
    assert abs(v-S(z))<mp.mpf('0.0007'),(z,v,S(z))
assert abs(4*S(0)-mp.mpf('0.25'))<mp.mpf('1e-30')
print('VERIFY_OK exact_second_iterate=3 susceptibility_points=4 critical_value=1/16 critical_slope=1/72')
