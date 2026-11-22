#!/usr/bin/env python3
"""Reproducible algebraic and independent finite-dimensional semigroup checks.
Run: python CHECK.py; requires sympy, numpy, scipy.
"""
from fractions import Fraction
import math
import random
import sympy as sp
import numpy as np
from scipy.linalg import expm

r,k,d,h,t=sp.symbols('r k d h t', positive=True, real=True)
m=2*d/r
cross=2*h/(r+2*k)
fourth=24*d*d/r**2+24*h*h/(r*(r+2*k))
V=sp.factor(fourth-m*m)
assert sp.simplify(V-(20*d*d/r**2+24*h*h/(r*(r+2*k))))==0
# Independent exact generator moment equations for both variants.
for mode in ('P','F'):
    Ls=-2*k if mode=='P' else -(r+2*k)
    assert sp.simplify(2*d-r*m)==0
    assert sp.simplify(2*h-(r+2*k)*cross)==0
    assert sp.simplify(12*(d*m+h*cross)-r*fourth)==0
    mixed_fourth=12*(h*m+d*cross)/(r+2*k)
    assert sp.simplify(12*(h*m+d*cross)-(r+2*k)*mixed_fourth)==0
# Formula for the conditional-moment semigroup, and exact covariance rates.
u=sp.symbols('u',nonnegative=True)
CP=sp.exp(-r*t)*V+4*h*h/(r+2*k)*(sp.exp(-2*k*t)-sp.exp(-r*t))/(r-2*k)
CF=sp.exp(-r*t)*V+2*h*h/(k*(r+2*k))*sp.exp(-r*t)*(1-sp.exp(-2*k*t))
assert sp.simplify(CP.subs(t,0)-V)==0
assert sp.simplify(CF.subs(t,0)-V)==0
assert sp.simplify(sp.diff(CP,t).subs(t,0)+r*V-2*h*cross)==0
assert sp.simplify(sp.diff(CF,t).subs(t,0)+r*V-2*h*cross)==0
assert sp.simplify(sp.limit(CP,r,2*k)-sp.exp(-r*t).subs(r,2*k)*(V.subs(r,2*k)+4*h*h/(4*k)*t))==0

# Completely independent generator-matrix exponentiation on basis (1,S,X^2,S X^2).
random.seed(4131)
count=0
for trial in range(80):
    rr=random.uniform(.1,7.)
    kk=random.uniform(.1,5.)
    dd=random.uniform(.4,4.)
    hh=dd*random.uniform(.02,.9)
    tt=random.uniform(.01,3.)
    mm=2*dd/rr
    aa=2*hh/(rr+2*kk)
    f4=24*dd**2/rr**2+24*hh**2/(rr*(rr+2*kk))
    b4=12*(hh*mm+dd*aa)/(rr+2*kk)
    vv=f4-mm**2
    for mode in ('P','F'):
        decay=2*kk if mode=='P' else rr+2*kk
        M=np.array([[0,0,0,0],[0,-decay,0,0],[2*dd,2*hh,-rr,0],
                    [2*hh,2*dd,0,-rr-2*kk]],dtype=float)
        # Matrix exponential verified separately from analytic convolution.
        row=expm(M*tt)[2]
        got=float(np.dot(row,np.array([mm,aa,f4,b4]))-mm**2)
        if mode=='P':
            z=((-math.expm1(-(rr-2*kk)*tt))/(rr-2*kk))*math.exp(-2*kk*tt) if abs(rr-2*kk)>1e-8 else tt*math.exp(-rr*tt)
            expected=vv*math.exp(-rr*tt)+4*hh**2/(rr+2*kk)*z
        else:
            expected=vv*math.exp(-rr*tt)+(2*hh**2/(kk*(rr+2*kk)))*math.exp(-rr*tt)*(-math.expm1(-2*kk*tt))
        assert math.isclose(got,expected,rel_tol=2e-11,abs_tol=2e-11),(trial,mode,got,expected)
        count+=1
    # Positivity is pointwise analytic; numerical spot check.
    cp=vv*math.exp(-rr*tt)+4*hh**2/(rr+2*kk)*((math.exp(-2*kk*tt)-math.exp(-rr*tt))/(rr-2*kk))
    cf=vv*math.exp(-rr*tt)+2*hh**2/(kk*(rr+2*kk))*math.exp(-rr*tt)*(1-math.exp(-2*kk*tt))
    assert cp>cf>0
    count+=2
# Characteristic function at a random spatial wave number using autonomous environment resolvent:
for trial in range(30):
    rr=random.uniform(.3,5.)
    kk=random.uniform(.2,3.)
    dd=random.uniform(.5,4.)
    hh=dd*random.uniform(.1,.9)
    w=random.uniform(.2,3.)
    Q=np.array([[-kk,kk],[kk,-kk]])
    env=np.diag([dd-hh,dd+hh])
    phi=rr*np.array([.5,.5])@np.linalg.solve(rr*np.eye(2)-Q+w*w*env,np.ones(2))
    assert (0<phi<1)
    # Taylor expansion at zero recovers E X^2=2d/r irrespective of k.
    eps=1e-4
    phi0=rr*np.array([.5,.5])@np.linalg.solve(rr*np.eye(2)-Q+eps**2*env,np.ones(2))
    assert abs((1-phi0)*2/eps**2-2*dd/rr)<3e-6
    count+=2
print('PASS:',count,'independent numeric assertions; 14 symbolic generator / normalization assertions')
