#!/usr/bin/env python3
"""Standalone algebraic and numerical checks for cardinal cubic-spline BV gain."""
import math
import random
import sympy as sp
import numpy as np
from scipy.interpolate import CubicSpline

q=2-sp.sqrt(3)
E=sp.sqrt(3)*(1+q)
t=sp.symbols('t',real=True)
r=sp.sqrt(q)
tstar=(1-r)/(1+q)
F=sp.expand(E* t*(1-t)*((2-q)-(1+q)*t)/6)
h=sp.simplify(F.subs(t,tstar))
C=sp.simplify(1+4*h/(1-q))
assert sp.simplify(q*q-4*q+1)==0
assert sp.simplify(E-(3*sp.sqrt(3)-3))==0
assert sp.simplify(sp.diff(F,t).subs(t,tstar))==0
assert 0<float(tstar)<1
assert float(sp.diff(F,t).subs(t,0))>0 and float(sp.diff(F,t).subs(t,1))<0
assert float(E)<6
assert abs(float(C)-1.58910899599299)<1e-12
assert sp.simplify(81*C**4-216*C**3+18*C**2+312*C-191)==0
print('EXACT_GEOMETRIC_GREEN_AND_CRITICAL_POINT_PASS')
print('ALGEBRAIC_NORM_MINPOLY_PASS',sp.minpoly(C))

# Evaluate exact total variation of finite natural-cubic interpolants, using
# all derivative roots, not a grid of sampled function values.
def tv_curve(y):
    x=np.arange(len(y),dtype=float)
    s=CubicSpline(x,np.array(y,dtype=float), bc_type='natural',extrapolate=False)
    knots=list(x)
    roots=s.derivative().roots(extrapolate=False)
    nodes=sorted(set([*knots,*[float(z) for z in roots if np.isfinite(z) and 0<z<x[-1]]]))
    vals=s(nodes)
    return sum(abs(float(b-a)) for a,b in zip(vals,vals[1:]))

for n in (12,20,40,80,160):
    y=[0.0]*n+[1.0]*n
    got=tv_curve(y)
    assert got<C+1e-8 and abs(got-float(C))<0.005 if n>=12 else True
    print('FINITE_NATURAL_STEP_APPROX',n,round(got,12))

random.seed(20261113)
for trial in range(60):
    increments=[random.randrange(-4,5) for _ in range(20)]
    y=[0.0]*35
    for z in increments:y.append(y[-1]+z)
    y += [y[-1]]*35
    dy=sum(abs(y[i]-y[i-1]) for i in range(1,len(y)))
    gain=tv_curve(y)
    assert gain <= float(C)*dy+1e-7, (trial,gain,dy)
print('RANDOM_FINITE_SPLINE_VARIATION_INEQUALITIES_PASS',60)

# Independent direct formula checks for a number of plateau cells. 
from math import sqrt
qf=float(q);Ef=float(E)
for j in range(1,15):
    m1=(-qf)**(j-1)*(-Ef)
    m2=(-qf)**j*(-Ef)
    xs=np.linspace(0,1,7001)
    v=-(xs*(1-xs)/6)*(m1*(2-xs)+m2*(1+xs))
    target=float(h)*qf**(j-1)
    assert abs(max(abs(v))-target)<2e-7
print('GEOMETRIC_PLATEAU_HUMPS_PASS',14)
print('ALL_CARDINAL_CUBIC_VARIATION_CHECKS_PASS',str(sp.N(C,16)))
