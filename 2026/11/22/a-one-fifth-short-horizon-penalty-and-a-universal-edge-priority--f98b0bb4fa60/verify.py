#!/usr/bin/env python3
"""Standalone finite checks for a path heat-trace conductance theorem.

Analytic arguments for all sizes and all times are in RESULT.md.  These
finite tests are reproducibility checks, not replacements for proofs.
Requires Python 3, NumPy, SciPy and SymPy.
"""
from fractions import Fraction as F
import math
import numpy as np
import sympy as sp
from scipy.optimize import minimize

checks = 0

def require(ok, message):
    global checks
    assert ok, message
    checks += 1

def rational_short(n):
    # Solve 4y_i+y_(i-1)+y_(i+1)=1 with y_0=y_n=0.
    m=n-1
    A=sp.diag(*([4]*m))
    for i in range(m-1):
        A[i,i+1] = A[i+1,i] = 1
    y=A.inv()*sp.ones(m,1)
    return [sp.Rational(v) for v in y]

def long_weights(n):
    return [sp.Rational(6*i*(n-i),n*(n*n-1)) for i in range(1,n)]

def lap(w):
    n=len(w)+1
    L=sp.zeros(n,n)
    for i,a in enumerate(w):
        L[i,i]+=a; L[i+1,i+1]+=a
        L[i,i+1]-=a; L[i+1,i]-=a
    return L

def quadratic(w):
    return 4*sum(x*x for x in w)+2*sum(x*y for x,y in zip(w[:-1],w[1:]))

rho=2-math.sqrt(3)
for n in range(4,43):
    y=rational_short(n)
    a=[v/sum(y) for v in y]
    b=long_weights(n)
    require(all(v>0 for v in a+b),f'positivity n={n}')
    require(sum(a)==1 and sum(b)==1,f'budget n={n}')
    require(a[0]>a[1] and b[0]<b[1],f'edge priority n={n}')
    for i,v in enumerate(y,1):
        formula=(1-((-rho)**i+(-rho)**(n-i))/(1+(-rho)**n))/6
        require(abs(float(v)-formula)<1e-12,f'closed short n={n},i={i}')
    La=lap(a); Lb=lap(b)
    require(sp.trace(La**2)==quadratic(a),f'moment n={n}')
    require(sp.trace(Lb**2)==quadratic(b),f'moment long n={n}')
    x=sp.Matrix([sp.Rational(2*i-n-1,2) for i in range(1,n+1)])
    gap=sp.Rational(12,n*(n*n-1))
    require(Lb*x==gap*x, f'linear eigen n={n}')

for n in range(4,12):
    b=long_weights(n)
    M=lap(b)
    vals=sorted(M.eigenvals().keys())
    target=[sp.Rational(6*k*(k+1),n*(n*n-1)) for k in range(n)]
    require(vals==target,f'long spectrum n={n}')

for n in (30,100,1000,10000):
    i=np.arange(1,n,dtype=float)
    y=(1-((-rho)**i+(-rho)**(n-i))/(1+(-rho)**n))/6
    a=y/y.sum()
    b=6*i*(n-i)/(n*(n*n-1))
    Q=lambda w:4*np.dot(w,w)+2*np.dot(w[:-1],w[1:])
    ratio=Q(b)/Q(a)
    require(1<ratio<1.2, f'ratio n={n}')
    print('quadratic-ratio',n,format(ratio,'.12f'))
require(abs(ratio-1.2)<0.0001,'one-fifth penalty limit sample')

for n in (4,5,6,7):
    m=n-1
    a=np.asarray([float(z/sum(rational_short(n))) for z in rational_short(n)])
    b=np.asarray([float(z) for z in long_weights(n)])
    def vals(w):
        L=np.zeros((n,n))
        for i,z in enumerate(w):
            L[i,i]+=z;L[i+1,i+1]+=z;L[i,i+1]-=z;L[i+1,i]-=z
        return np.linalg.eigvalsh(L)
    for t in (0.01,0.5,5,40):
        fn=lambda w:float(np.exp(-t*vals(w)).sum())
        sol=minimize(fn, a, method='SLSQP',bounds=[(0,1)]*m,
            constraints={'type':'eq','fun':lambda w:np.sum(w)-1},
            options={'ftol':1e-12,'maxiter':400})
        require(sol.success,f'numeric optimizer n={n},t={t}: {sol.message}')
        require(abs(sum(sol.x)-1)<1e-9, 'numeric budget')
        require(sol.fun <= min(fn(a),fn(b))+1e-9,'optimal objective bound')
        if t==0.01:
            require(np.max(abs(sol.x-a))<0.001,'short limit numeric')
        print('numerical-minimum',n,t,'first-two',*[round(float(v),8) for v in sol.x[:2]])
print('PASS',checks,'finite checks')
