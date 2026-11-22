#!/usr/bin/env python3
"""Finite and symbolic reproductions of the axial pedal curvature theorem.
The finite parameter grid is diagnostic, not a proof of all-parameter assertions.
"""
import sympy as s
import numpy as np
A,B,D,t=s.symbols('A B D t',positive=True,real=True)
c=s.cos(t)
q=s.sqrt(A*A*c*c+B*B*s.sin(t)**2)
p=q-D*c
N=s.expand(p*p+2*s.diff(p,t)**2-p*s.diff(p,t,2))
e=1-B*B/A**2
x=A*c/q
z=D/A
poly=A*A*(1-2*e+2*z*z+3*e*x*x-z*x*(3+e*x*x))
assert s.simplify(s.factor(N-poly))==0
print('SYMBOLIC_CURVATURE_POLYNOMIAL_OK')
rng=np.random.default_rng(417)
for _ in range(300):
    a=rng.uniform(1.001,12.0)
    b=1.0
    d=rng.uniform(0,a*0.9999)
    ecc=1-1/a**2
    lower=a*np.sqrt((a*a-2)/(a*a-1)) if a>np.sqrt(2) else 0.0
    upper=a-1/(2*a)
    ss=np.linspace(0,1,4000)
    vals=a*a*(1-2*ecc+2*(d/a)**2+3*ecc*ss**2-(d/a)*ss*(3+ecc*ss**2))
    predicted=(lower<=d<=upper)
    computed=(np.min(vals)>=-1e-9*a*a)
    assert predicted==computed,(a,d,lower,upper,np.min(vals))
print('300_AXIAL_THRESHOLD_COMPARISONS_OK')
u,E=s.symbols('u E',real=True,positive=True)
zz=2*E*u/(1+E*u*u)
F=1-2*E+2*zz*zz+3*E*u*u-zz*u*(3+E*u*u)
assert s.simplify(F-(E*u*u-1)**2*(E*u*u-2*E+1)/(1+E*u*u)**2)==0
print('STATIONARY_FACTORIZATION_OK')
w=s.symbols('w',positive=True)
width=1-w/2-s.sqrt((1-2*w)/(1-w))
assert s.simplify(s.limit(width/w**2,w,0))==s.Rational(5,8)
print('THIN_ELLIPSE_WIDTH_CONSTANT_OK')
