#!/usr/bin/env python3
"""Finite diagnostic for projection-angle trace-norm identities and Chebyshev Wronskians.
Analytic proofs, not numerical tests, establish the general result.
"""
import math
import random

rng=random.Random(261119)
count=0

def det(a):
    a=[list(map(float,row)) for row in a]
    n=len(a); out=1.0
    for i in range(n):
        pivot=max(range(i,n),key=lambda j:abs(a[j][i]))
        if pivot!=i:
            a[pivot],a[i]=a[i],a[pivot]
            out=-out
        v=a[i][i]
        out*=v
        if abs(v)<1.e-15: return 0.0
        for j in range(i+1,n):
            c=a[j][i]/v
            for h in range(i+1,n):
                a[j][h]-=c*a[i][h]
    return out

for _ in range(500):
    a=rng.random(); t=rng.random()
    s=math.sqrt(a*(1-a))
    x=1-t*a; y=-t*s; z=-t*(1-a)
    eigen_hi=(x+z+math.hypot(x-z,2*y))/2
    eigen_lo=(x+z-math.hypot(x-z,2*y))/2
    got=abs(eigen_hi)+abs(eigen_lo)
    want=math.sqrt((1+t)**2-4*t*a)
    assert math.isclose(got,want,rel_tol=3.e-14,abs_tol=3.e-14)
    count+=1
for m in range(1,6):
    for _ in range(90):
        qs=sorted(rng.uniform(0.07,0.87) for _ in range(m))
        u=rng.random()
        coeff=1.0; w=[]
        for ell in range(m):
            if ell: coeff*=ell-0.5
            w.append([coeff* (q**ell) / ((1-q*u)**(ell+0.5)) for q in qs])
        lhs=det(w)
        vs=[q/(1-q*u) for q in qs]
        rhs=1.0;coeff=1.0
        for ell in range(m):
            if ell: coeff*=ell-0.5
            rhs*=coeff
        for q in qs: rhs*=(1-q*u)**(-0.5)
        for i in range(m):
            for j in range(i+1,m):rhs*=vs[j]-vs[i]
        assert rhs>0
        assert math.isclose(lhs,rhs,rel_tol=5.e-6,abs_tol=3.e-12), (m,lhs,rhs)
        count+=1
print('PROJECTION_TRACE_TOMOGRAPHY_DIAGNOSTIC_OK',count)
