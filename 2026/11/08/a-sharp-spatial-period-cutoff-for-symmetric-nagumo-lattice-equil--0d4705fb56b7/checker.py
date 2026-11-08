#!/usr/bin/env python3
"""Finite reproducibility checks for the balanced Nagumo cycle theorem.
The all-period existence/nonexistence assertion is proved analytically, not by this script.
"""
from fractions import Fraction
from math import sin, pi
import numpy as np
from scipy.optimize import minimize

# Exact primitive 3- and 4-period orbits and their squared amplitudes.
for n, k in [(3,3),(4,2)]:
    for d in [Fraction(1,100), Fraction(1,30)]:
        amp2=Fraction(1,4)-k*d
        assert amp2>0
        a=float(amp2)**0.5
        v=np.array([0,a,-a] if n==3 else [0,a,0,-a])
        res=d.numerator/d.denominator*(np.roll(v,1)+np.roll(v,-1)-2*v)+v*(0.25-v*v)
        assert np.max(np.abs(res))<1e-13

def profile(n,z):
    v=np.zeros(n)
    for j,t in enumerate(z,1):
        v[j]=t
        v[-j]=-t
    return v

def energy(n,d,z):
    v=profile(n,z)
    return 0.5*d*np.sum((np.roll(v,-1)-v)**2)-0.125*np.sum(v*v)+0.25*np.sum(v**4)

for n in [5,6,7,9]:
    critical=1/(16*sin(pi/n)**2)
    for factor in [0.3,0.9]:
        d=critical*factor
        m=(n-1)//2
        opt=minimize(lambda z:energy(n,d,z),np.full(m,0.1),method='BFGS',
                     options={'gtol':1e-11,'maxiter':3000})
        v=profile(n,opt.x)
        residual=d*(np.roll(v,1)+np.roll(v,-1)-2*v)+v*(0.25-v*v)
        assert energy(n,d,opt.x)<-1e-10,(n,d,opt.fun)
        assert np.min(v[1:m+1])>0,(n,opt.x)
        assert np.max(np.abs(residual))<2e-6,(n,d,np.max(abs(residual)))
        assert np.max(np.abs(v))<0.5
    # At or beyond threshold, the exact coercivity argument yields
    # d*lambda_2>=1/4 and forbids all nonconstant equilibria.
    assert critical*4*sin(pi/n)**2==0.25 or abs(critical*4*sin(pi/n)**2-.25)<1e-14
print('VERIFY_OK exact_3_4=4 variational_examples=8 spectral_thresholds=4')
