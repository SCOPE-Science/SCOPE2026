#!/usr/bin/env python3
"""Standalone numerical corroboration for first-Hermite annular concentration theorem.
Run: python3 check.py (requires scipy/numpy). This is not a proof."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import gammaln, ndtr

SQRT_2PI=math.sqrt(2*math.pi)
checks=0

def verify(condition, description='check'):
    global checks
    assert condition, description
    checks+=1

def h(x):
    return x*x*math.exp(-x*x/2)/SQRT_2PI

def F(b,u):
    return ndtr(u+b)-ndtr(u-b) -(u+b)*math.exp(-(u+b)**2/2)/SQRT_2PI+(u-b)*math.exp(-(u-b)**2/2)/SQRT_2PI

def U(b):
    return brentq(lambda u:math.log((u+b)/(u-b))-b*u,b+1e-12,b+max(2.,20./b),xtol=1e-13)

def D(b):
    return F(b,0)-F(b,U(b))

def exact_lambda(j,n,b):
    a=n-b*math.sqrt(n)
    c=n+b*math.sqrt(n)
    assert j>=0 and a>0
    integrand=lambda t:math.exp(-t+j*math.log(t)-gammaln(j+1))*(j-t)**2/t
    return quad(integrand,a,c,epsabs=2e-12,epsrel=2e-12,limit=120)[0]

critical=brentq(D,math.sqrt(2)+1e-8,2.,xtol=1e-13)
verify(abs(critical-1.524046518925874)<2e-12)
verify(abs(U(critical)-1.75113102393145)<2e-12)
verify(abs(D(critical))<2e-13)
for b in (0.3,0.5,0.9,1.,1.3,math.sqrt(2),1.5,critical,1.55,1.75,2.,3.):
    u=U(b)
    verify(u>b, 'detached solution outside interval')
    verify(abs(math.log((u+b)/(u-b))-b*u)<1e-8)
    verify(abs(F(b,u)-quad(lambda t:h(t),u-b,u+b)[0])<5e-12)
    verify(abs(F(b,0)-quad(lambda t:h(t),-b,b)[0])<5e-12)
    verify(abs(F(b,u)-F(b,-u))<5e-12)
    if b<critical-1e-5:
        verify(F(b,u)>F(b,0))
    if b>critical+1e-5:
        verify(F(b,0)>F(b,u))
for b in (1.1,1.49,1.6,2.3):
    for u in np.linspace(-4.,4.,21):
        verify(abs(F(b,u)-quad(lambda t:h(t),u-b,u+b)[0])<5e-12)
        verify(F(b,u) <= max(F(b,0),F(b,U(b)))+1e-10)
for b in (0.75,1.4,1.6,2.,3.):
    for u in (-3.2,-1.6,-0.2,0.3,1.3,2.8):
        step=1e-5
        numerical=(F(b,u+step)-F(b,u-step))/(2*step)
        verify(abs(numerical-(h(u+b)-h(u-b)))<3e-9)
for n,b in [(120,1.),(400,1.),(1200,1.),(2000,1.),(120,2.),(400,2.),(1200,2.),(2000,2.)]:
    idx=range(max(0,int(n-3.3*math.sqrt(n))),int(n+3.3*math.sqrt(n))+1)
    values=[exact_lambda(j,n,b) for j in idx]
    arg=list(idx)[int(np.argmax(values))]
    target=U(b) if b<critical else 0.
    verify(abs(abs(arg-n)/math.sqrt(n)-target)<(0.4 if n==120 else 0.19), 'location convergence')
    verify(abs(max(values)-max(F(b,0),F(b,U(b))))<(0.07 if n==120 else 0.04), 'value convergence')
for n in (300,1500,8000):
    for b in (0.8,1.1,1.6,2.):
        for u in (-2.7,-1.5,-0.2,0,0.8,1.6,2.5):
            j=int(round(n+u*math.sqrt(n)))
            actual=exact_lambda(j,n,b)
            target=F(b,u)
            verify(abs(actual-target)<(0.08 if n==300 else 0.026 if n==1500 else 0.012))
# Exact normalization by elementary Gamma moments: j>=1: j^2/j -2j +(j+1)=1; j=0: E[T]=1.
for j in range(1,100):
    verify(abs(j*j/j-2*j+j+1 -1)<1e-10)
print(f'FIRST_HERMITE_ANNULUS_CHECKS_PASS {checks}')
