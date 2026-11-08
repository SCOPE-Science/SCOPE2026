#!/usr/bin/env python3
"""Reproducible algebra and independent finite-dimensional tests for two-stage renewal quantum resetting."""
import sympy as sp
import numpy as np
from fractions import Fraction
from math import isclose

A,B,Q,W=sp.symbols('a b q omega', positive=True, real=True)
I=sp.I
mu=(B+A*Q)/(A*B)
z=(1- (A/(A+I*W))*((1-Q)+Q*B/(B+I*W)))/(I*W*mu)
zc=A*B*(B+A*Q+I*W)/((B+A*Q)*(A+I*W)*(B+I*W))
assert sp.simplify(z-zc)==0
D=sp.factor(sp.expand_complex(zc*sp.conjugate(zc))-sp.re(sp.expand_complex(zc)))
K=A*A*B*Q*(A*Q-A+B)/(A*Q+B)**2
kernel=W*W/((A*A+W*W)*(B*B+W*W))
assert sp.simplify(D-K*kernel)==0
cv2=(1/A**2+Q*(2-Q)/B**2)/mu**2
assert sp.simplify(K-A*B*(1-cv2)/2)==0
assert sp.simplify(sp.diff(kernel,W).subs(W,sp.sqrt(A*B)))==0
assert sp.simplify(kernel.subs(W,sp.sqrt(A*B))-1/(A+B)**2)==0
# Rate mixtures (decreasing hazard), serial exponentials (increasing hazard), and exponential threshold
assert sp.simplify(D.subs(Q,1)-A*A*B*B*kernel/(A+B)**2)==0
assert sp.simplify(D.subs(Q,0))==0
assert sp.simplify(D.subs(Q,1-B/A))==0
print('symbolic identities: 9 PASS')

rng=np.random.default_rng(705341)
n=0
for a,b,q in [(3.,1.,0.2),(3.,1.,0.8),(2.,1.,0.5),(1.,2.,0.5),(.75,1.7,1.),(3.,1.,1.),(3.,1.,0.),(3.,1.,2/3)]:
    for dimension in (2,3,5):
        E=np.sort(rng.uniform(-3,3,size=dimension))
        X=rng.normal(size=(dimension,dimension))+1j*rng.normal(size=(dimension,dimension))
        R=X@X.conj().T
        R=R/np.trace(R).real
        omega=E[:,None]-E[None,:]
        muv=1/a+q/b
        z=(a*b)*(b+a*q+1j*omega)/((b+a*q)*(a+1j*omega)*(b+1j*omega))
        Rstar=R*z
        p=np.trace(Rstar@Rstar).real
        f=np.trace(Rstar@R).real
        predicted=(a*a*b*q*(a*q-a+b)/(a*q+b)**2*np.sum(np.abs(R)**2*omega**2/((a*a+omega**2)*(b*b+omega**2))))
        assert abs(p-f-predicted)<3e-13,(a,b,q,dimension,p,f,predicted)
        # independent computation: direct stationary equilibrium age integral using quadrature
        import scipy.integrate as si
        def survival(t):
            if abs(a-b)<1e-9:
                return np.exp(-a*t)*(1+q*a*t)
            return (1-q)*np.exp(-a*t)+q*(a*np.exp(-b*t)-b*np.exp(-a*t))/(a-b)
        # independent numerical integration of rho matrix elements, using survival and complex oscillation
        M=np.zeros((dimension,dimension),dtype=complex)
        for j in range(dimension):
            for k in range(dimension):
                ww=E[j]-E[k]
                re=si.quad(lambda t:survival(t)*np.cos(ww*t)/muv,0,np.inf,epsabs=1e-11)[0]
                im=si.quad(lambda t:-survival(t)*np.sin(ww*t)/muv,0,np.inf,epsabs=1e-11)[0]
                M[j,k]=R[j,k]*(re+1j*im)
        assert np.max(np.abs(M-Rstar))<1e-9
        n+=1
print('matrix and independent quadrature checks:',n,'PASS')

# exact-rational arithmetic for 2x2 balanced qubit no floating point
for aa,bb,qq,ww in [(3,1,sp.Rational(1,3),2),(3,1,sp.Rational(4,5),sp.Rational(3,2)),(1,3,sp.Rational(1,2),2),(3,1,sp.Rational(2,3),3),(3,1,0,1),(3,1,1,2),(1,1,1,1)]:
    zz=sp.simplify(zc.subs({A:aa,B:bb,Q:qq,W:ww}))
    # stationary state of equal-superposition qubit with Hamiltonian diag(0,omega)
    rho=sp.Matrix([[sp.Rational(1,2),sp.Rational(1,2)*zz],[sp.Rational(1,2)*sp.conjugate(zz),sp.Rational(1,2)]])
    rho0=sp.ones(2)/2
    gap=sp.simplify(sp.trace(rho*rho)-sp.trace(rho*rho0))
    expected=sp.simplify((K*kernel/2).subs({A:aa,B:bb,Q:qq,W:ww}))
    assert sp.simplify(gap-expected)==0
print('exact-rational balanced qubit checks: 7 PASS')
print('PASS ALL')
