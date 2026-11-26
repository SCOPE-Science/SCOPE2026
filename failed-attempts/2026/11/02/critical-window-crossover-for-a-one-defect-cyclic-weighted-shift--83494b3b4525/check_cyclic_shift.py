#!/usr/bin/env python3
"""Numerical and exact small-size checks for one-bond cyclic-shift radii.
No floating-point calculation is used as an infinite-dimensional proof.
Requires Python 3, numpy, scipy, sympy, mpmath.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.optimize import brentq
import sympy as sp
import mpmath as mp

checks=0
x,r=sp.symbols('x r')
for n in range(3,11):
    B=sp.zeros(n)
    for j in range(n-1): B[j,j+1]=B[j+1,j]=1
    B[n-1,0]=B[0,n-1]=r
    U=[sp.Integer(1),x]
    for j in range(2,n+1):U.append(sp.expand(x*U[-1]-U[-2]))
    characteristic=sp.expand(B.charpoly(x).as_expr())
    assert sp.expand(characteristic-(U[n]-2*r-r*r*U[n-2]))==0
    assert sp.expand(U[n-1]**2-U[n]*U[n-2]-1)==0
    assert sp.expand((U[n]-r*(U[n-1]+1))*(U[n]+r*(U[n-1]-1))-U[n]*characteristic)==0
    checks+=3
for n in range(3,28):
    for rval in [0.0,0.1,0.5,0.91,0.999,1.0,1.001,1.2,1.75,3.0]:
        B=np.zeros((n,n))
        for j in range(n-1):B[j,j+1]=B[j+1,j]=1
        B[0,-1]=B[-1,0]=rval
        measured=np.linalg.eigvalsh(B)[-1]/2
        if rval<1:
            angle=(math.pi/(n+1) if rval==0 else brentq(lambda x:math.cos((n+1)*x/2)-rval*math.cos((n-1)*x/2),1e-15,math.pi/(n+1)+1e-12))
            exact=math.cos(angle)
        elif rval==1:exact=1.0
        else:
            angle=brentq(lambda x:math.cosh((n+1)*x/2)/math.cosh((n-1)*x/2)-rval,1e-15,math.log(rval)+1)
            exact=math.cosh(angle)
        assert abs(measured-exact)<3e-12,(n,rval,measured,exact)
        checks+=1
# High-precision finite-size crossover checks; evaluate n^2 (w-1).
mp.mp.dps=70
for a in [-7,-2,-0.1,0,0.1,2,7]:
    if a<0:
        z=mp.findroot(lambda t:t*mp.tan(t/2)+a,(mp.mpf('.01'),mp.mpf('3.12')),solver='bisect',tol=mp.mpf('1e-45'),maxsteps=200)
        limit=-z*z/2
    elif a>0:
        y=mp.findroot(lambda t:t*mp.tanh(t/2)-a,(mp.mpf('1e-15'),mp.mpf(max(10,a+3))),solver='bisect',tol=mp.mpf('1e-45'),maxsteps=200)
        limit=y*y/2
    else:limit=mp.mpf('0')
    for n in [400,1200]:
        r=1+mp.mpf(a)/n
        if a<0:
            f=lambda t:mp.cos((n+1)*t/(2*n))/mp.cos((n-1)*t/(2*n))-r
            t=mp.findroot(f,(z*mp.mpf('.8'),z*mp.mpf('1.2')))
            numerical=n*n*(mp.cos(t/n)-1)
        elif a>0:
            f=lambda t:mp.cosh((n+1)*t/(2*n))/mp.cosh((n-1)*t/(2*n))-r
            t=mp.findroot(f,(y*mp.mpf('.8'),y*mp.mpf('1.2')))
            numerical=n*n*(mp.cosh(t/n)-1)
        else:numerical=mp.mpf(0)
        assert abs(numerical-limit)<mp.mpf('1.2')/(n/400), (a,n,numerical,limit)
        checks+=1
print(f'CHECK_OK spectral_and_critical_window_tests={checks} dimensions=3..27')
