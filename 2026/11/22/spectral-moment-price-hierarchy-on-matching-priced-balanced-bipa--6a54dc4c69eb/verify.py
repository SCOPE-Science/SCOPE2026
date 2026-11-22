#!/usr/bin/env python3
"""Standalone numerical and exact sanity checks for a spectral-moment design theorem.
No external data, services, or paths are required.
"""
from fractions import Fraction
from math import isclose, log
import numpy as np
from scipy.optimize import minimize_scalar

def threshold(m, p):
    if m < 3 or p < 0: raise ValueError
    a = ((m-2)/(2*(m-1)))**p/(m-1)
    b = ((m-2)/m)**p
    return (a + 2*(m-1)/(m-2))/(a+b+1)

def moment_spectrum(m, a, b, p):
    if b <= 0 or a < 0: return float('inf')
    vals = [2*(a+(m-1)*b),m*b,2*a+(m-2)*b]
    weights = [1,m-1,m-1]
    if p == 0: return -sum(w*log(v) for w,v in zip(weights, vals))
    return sum(w*(v**(-p)) for w,v in zip(weights, vals))

def moment_matrix(m, a, b, p):
    n = 2*m
    L = np.zeros((n,n))
    for i in range(m):
        for j in range(m):
            w = a if i == j else b
            L[i,i] += w; L[m+j,m+j] += w
            L[i,m+j] -= w; L[m+j,i] -= w
    spectrum = np.linalg.eigvalsh(L)[1:]
    if p == 0: return -float(np.log(spectrum).sum())
    return float(np.sum(spectrum**(-p)))

def optimal_ratio(m,p,c):
    # Cost B=1; x is matching spend fraction.
    def objective(x):
        aa=x/(m*c); bb=(1-x)/(m*(m-1))
        return moment_spectrum(m,aa,bb,p)
    if c >= threshold(m,p):return 0.0
    result=minimize_scalar(objective,bounds=(0,1-1.e-9),method='bounded',options={'xatol':1.e-13})
    return (result.x/(m*c))/((1-result.x)/(m*(m-1)))

checks=0
for m in (3,4,5,6,9,12):
    for p in (0,.2,.5,1,1.7,2,3,6,12):
        c0=threshold(m,p)
        assert 0 < c0 < 2*(m-1)/(m-2);checks+=1
        for c in (c0*.8,c0*.999,c0,c0*1.01,c0*1.3):
            r=optimal_ratio(m,p,c)
            if c >= c0:assert r == 0
            else:assert r>0
            checks+=1
            aa = r/(m*((m-1)+c*r));bb=1/(m*(m-1+c*r))
            assert isclose(moment_spectrum(m,aa,bb,p),moment_matrix(m,aa,bb,p),rel_tol=1.e-8,abs_tol=1.e-8)
            checks+=1
        assert all(threshold(m,q+0.02)>threshold(m,q) for q in [0,0.5,1,2,4,8,20])
        checks+=1
# Verify exact rational formula for p=0,1,2 and derivative sign at a=0.
for m in range(3,30):
    M=Fraction(m)
    for p in (0,1,2):
        a=Fraction(1,2**p*(m-1)**(p+1));b=Fraction(1,m**p);d=Fraction(1,(m-2)**p)
        val=(a+Fraction(2*(m-1),m-2)*d)/(a+b+d)
        assert abs(float(val)-threshold(m,p))<1e-12
        checks+=1
    assert threshold(m,0)<threshold(m,1)<threshold(m,2);checks+=1
for p in (0,.5,1,2,4):
    for gamma in (-1,0,0.5,1.3,2.3,3.7):
        for m in (300,900):
            c=1+gamma/m
            target=max(0.,1-gamma/(p+1))
            rr=optimal_ratio(m,p,c)
            assert abs(rr-target) < .07,(m,p,gamma,rr,target)
            checks+=1
for m in (10,50,300):
    for p in (0,.2,.5,1,2,4):
        assert abs((threshold(m,p)-1)*m-(p+1)) < 20*(p+1)**2/m
        checks+=1
for alpha in (0., .1, .3, .7, 1.5, 3.):
    for m in (100,400,1000):
        cp=threshold(m,alpha*m)
        target=2/(1+np.exp(-2*alpha))
        assert abs(cp-target)<.06,(alpha,m,cp,target)
        checks+=1
print('PASS',checks,'assertions')
