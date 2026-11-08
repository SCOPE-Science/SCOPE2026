#!/usr/bin/env python3
"""Exact rational fold and nearby unstable endemic equilibria checks."""
from fractions import Fraction as Q
import sympy as s
from scipy.optimize import brentq
import numpy as np
r=s.Rational(1,6);mu=s.Rational(11,108);gamma=s.Rational(1,100)
h=s.Rational(864,11);eta=h*gamma;theta=1/(1+h*r**3)
assert mu*(1+h*r**3)==r*(1-r)
assert 3*mu*h*r**2+2*r-1==0
A=1+mu*(1-2*r)/(1-r);B=mu*r/theta;C=-3*eta*theta*r*r;D=1-gamma-eta*r**3
J=s.Matrix([[A,B],[C,D]]);assert s.factor(J.det())==s.Rational(6343,5940)
assert sorted(J.eigenvals().keys())==[1,s.Rational(6343,5940)]
assert gamma+eta<=1
print('exact_fold: mu=',mu,'gamma=',gamma,'eta=',eta,'r=',r,'theta=',theta)
print('exact_J=',J.tolist(),'eigenvalues=',list(J.eigenvals().keys()))
hf=float(h); muf=float(mu); gamf=float(gamma)
for eps in [1e-3,1e-4,1e-5]:
    he=hf*(1-eps);et=gamf*he
    F=lambda x: muf*(1+he*x**3)-x*(1-x)
    # convex positive at endpoints, negative near fold
    x1=brentq(F,1e-6,float(r))
    x2=brentq(F,float(r),.8)
    for x in [x1,x2]:
        t=1/(1+he*x**3)
        j=np.array([[1+muf*(1-2*x)/(1-x),muf*x/t],[-3*et*t*x*x,1-gamf-et*x**3]])
        eig=np.linalg.eigvals(j)
        assert max(abs(eig))>1.001,(eps,x,eig)
        print('nearby h_factor=',1-eps,'root=',round(x,8),'eig=',eig)
print('CHECK PASS')
