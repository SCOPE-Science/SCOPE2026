#!/usr/bin/env python3
"""Optional independent direct Euclidean QP check (needs NumPy and SciPy)."""
from fractions import Fraction
from random import Random
import numpy as np
from scipy.optimize import minimize
N=16;n=15
C=[sum(((((a&v).bit_count()&1)<<(v-1))) for v in range(1,N)) for a in range(N)]
M=np.array([[(c>>i)&1 for i in range(n)] for c in C],dtype=float).T
rng=Random(2026)
samples=[0,(1<<n)-1]+rng.sample(range(1<<n),35)
for x in samples:
    xv=np.array([(x>>i)&1 for i in range(n)],float)
    sol=minimize(lambda a: np.dot(M@a-xv,M@a-xv),np.ones(N)/N,
        jac=lambda a:2*M.T@(M@a-xv),method='SLSQP',
        bounds=[(0,None)]*N,
        constraints=[{'type':'eq','fun':lambda a:sum(a)-1,
                      'jac':lambda a:np.ones(N)}],
        options={'ftol':1e-11,'maxiter':2000})
    b=[N-2*(c.bit_count()+x.bit_count())+4*(c&x).bit_count() for c in C]
    z=sorted(b,reverse=True)
    for k in range(1,N+1):
        t=Fraction(sum(z[:k])-N,k)
        if z[k-1]>t and (k==N or z[k]<=t):break
    d=sum((max(Fraction(0),v-t)-v)**2 for v in b)/(4*N)
    assert sol.success and abs(sol.fun-float(d))<1e-8,(x,sol.fun,float(d))
print('SIMPLEX15_QP_PASS samples=37')
