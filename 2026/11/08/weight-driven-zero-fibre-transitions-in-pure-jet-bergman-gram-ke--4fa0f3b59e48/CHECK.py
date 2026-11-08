#!/usr/bin/env python3
"""Independent finite checks for weighted pure-jet Bergman-kernel zero migration.
Run: python CHECK.py  (requires numpy, scipy, sympy).
"""
from math import comb, sqrt, factorial
import numpy as np
import sympy as sp
from scipy.special import roots_jacobi, roots_laguerre
from scipy.optimize import brentq

checks = 0
def require(test, message):
    global checks
    checks += 1
    if not bool(test):
        raise AssertionError(message)

t, beta = sp.symbols('t beta')
for m in range(0, 11):
    for b in (sp.Rational(1, 2), 1, 2, 3, 7):
        q = sum(sp.binomial(m, j) * sp.binomial(m+b, j) * t**j for j in range(m+1))
        transformed = sp.cancel((1-t)**m * sp.jacobi(m, 0, b, (1+t)/(1-t)))
        require(sp.expand(q - transformed) == 0, ('Jacobi transform',m,b))
        if m:
            Jroots = np.sort(roots_jacobi(m,0,float(b))[0])
            qroots = np.sort(np.array([(x-1)/(x+1) for x in Jroots]))
            numerical = np.sort(np.roots([float(sp.expand(q).coeff(t,j)) for j in range(m,-1,-1)]).real)
            require(np.max(np.abs(qroots - numerical)) < 2e-5*(1+max(abs(qroots))), ('roots',m,b))
            require(all(x < 0 for x in qroots), ('negativity',m,b))
            require(sum(x>0 for x in Jroots) >= (m+1)//2, ('minimum count',m,b))

for m in range(1, 7):
    z,w=sp.symbols('z w')
    for b in (1,2,3):
        alpha=b+1
        symbolic=sp.diff((1-z*w)**(-alpha),z,m,w,m) / factorial(m)**2
        q=sum(sp.binomial(m,j)*sp.binomial(m+b,j)*(z*w)**j for j in range(m+1))
        predicted=sp.rf(alpha,m)/factorial(m)*q/(1-z*w)**(alpha+2*m)
        require(sp.cancel(symbolic-predicted)==0, ('derivative',m,b))

for m in range(2,14):
    T=sp.Poly(sum((-1)**j*sp.binomial(m,j)*(sp.prod(m+beta-r for r in range(j))/sp.factorial(j)) for j in range(m+1)),beta)
    roots=sp.nroots(T, maxsteps=150)
    positive=sorted(float(sp.re(r)) for r in roots if abs(float(sp.im(r)))<1e-7 and float(sp.re(r))>1e-8)
    require(len(positive)==m//2, ('transition count',m,positive))
    require(all(positive[i+1]-positive[i]>1e-5 for i in range(len(positive)-1)), ('separation',m))
    for B in (0.01, 0.5, 1.0, 2.0, 4.0, 10.0, 20.0, 80.0):
        zcount=int(sum(roots_jacobi(m,0,B)[0]>0))
        predicted=(m+1)//2+sum(B>th for th in positive)
        require(zcount==predicted, ('phase count',m,B,zcount,predicted))

for m in (2,3,4,8,16,32):
    for b in (0.5,2,6,15,40):
        n=np.arange(m,dtype=float)
        diag=b*b/((2*n+b)*(2*n+b+2))
        k=np.arange(1,m,dtype=float)
        off=2*k*(k+b)/((2*k+b)*np.sqrt((2*k+b)**2-1))
        jacobimat=np.diag(diag)+np.diag(off,1)+np.diag(off,-1)
        require(np.max(np.abs(np.linalg.eigvalsh(jacobimat)-roots_jacobi(m,0,b)[0]))<1e-10,('Jacobi matrix',m,b))

critical=2+2*sqrt(2)
for m in (40,80,160):
    threshold=brentq(lambda b:roots_jacobi(m,0,b)[0][0],0.1,6*m)
    require(0<threshold/m<critical, ('threshold sign',m))
    if m==160:
        require(critical-threshold/m<0.35,('critical trend',m,threshold/m))
for m in range(1,7):
    B=500.0
    jacobiroots=roots_jacobi(m,0,B)[0]
    rescaled=np.sort(-B*(jacobiroots-1)/(jacobiroots+1))
    lag=np.sort(roots_laguerre(m)[0])
    require(np.max(abs(rescaled-lag))<0.2,('Laguerre scale',m))

print(f'CHECK_OK {checks} assertions; sharp scaling constant = {critical:.12f}')
