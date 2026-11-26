"""Reproducible checks for the weighted-wheel spectral-gap classification.

Analytical arguments establish all-order statements. This script checks finite
instances exactly where algebraic eigenvalues are rational, and numerically
checks independent unsymmetrized edge weights.
"""
from fractions import Fraction
import math
import numpy as np
import sympy as sp


def wheel_laplacian(n, spokes, rims, dtype=float):
    size=n+1
    L=np.zeros((size,size),dtype=dtype) if dtype is not object else sp.zeros(size,size)
    for j in range(n):
        for u,v,w in [(0,j+1,spokes[j]),(j+1,(j+1)%n+1,rims[j])]:
            L[u,u]+=w
            L[v,v]+=w
            L[u,v]-=w
            L[v,u]-=w
    return L


def theoretical(n,t,B=1):
    c=4*math.sin(math.pi/n)**2
    if t<c:
        a=B*c/(n*(c+n*t))
        b=B/(c+n*t)
        value=(n+1)*a
    else:
        a=B/n;b=0.0;value=B/n
    return a,b,value,c


def validate():
    assertions=0
    for n in (3,4,6):
        c={3:sp.Integer(3),4:sp.Integer(2),6:sp.Integer(1)}[n]
        for t in (sp.Rational(1,5),sp.Rational(1,2),sp.Integer(1),sp.Integer(2),sp.Integer(3),sp.Integer(5)):
            B=sp.Integer(7)
            if t < c:
                a=B*c/(n*(c+n*t)); b=B/(c+n*t); gap=(n+1)*a
            else:
                a=B/n; b=sp.Integer(0); gap=B/n
            L=wheel_laplacian(n,[a]*n,[b]*n,dtype=object)
            eig=L.eigenvals()
            eigenvalues=sorted((val for val,m in eig.items() for _ in range(m)),key=lambda z:float(z))
            assert eigenvalues[0]==0 and sp.simplify(eigenvalues[1]-gap)==0
            assertions+=1
            assert sp.simplify(n*a+n*t*b-B)==0
            assertions+=1
            # Exact two-dimensional lowest Fourier subspace trace.
            if n in (3,4,6):
                cs=[sp.cos(2*sp.pi*j/n) for j in range(n)]
                sn=[sp.sin(2*sp.pi*j/n) for j in range(n)]
                cosv=sp.Matrix([0]+cs)
                sinv=sp.Matrix([0]+sn)
                e1=sp.simplify((cosv.T*L*cosv)[0]/(cosv.T*cosv)[0])
                e2=sp.simplify((sinv.T*L*sinv)[0]/(sinv.T*sinv)[0])
                assert sp.simplify(e1-a-c*b)==0
                assert sp.simplify(e2-a-c*b)==0
                assertions+=2
    # Exact critical-line multiple optimizers.
    for n,c in ((3,sp.Integer(3)),(4,sp.Integer(2)),(6,sp.Integer(1))):
        B=sp.Integer(7)
        for k in (0,1,2,3,4):
            # b ranges from 0 to B/((n+1)c).
            b=sp.Rational(k,4)*B/((n+1)*c)
            a=B/n-c*b
            L=wheel_laplacian(n,[a]*n,[b]*n,dtype=object)
            es=sorted((ev for ev,m in L.eigenvals().items() for _ in range(m)),key=lambda z:float(z))
            assert sp.simplify(es[1]-B/n)==0
            assertions+=1
    rng=np.random.default_rng(29042)
    # Independent full-matrix optimization tests; no symmetry imposed.
    for n in range(3,13):
        for multiplier in (.15,.5,1,2,6):
            a,b,val,c=theoretical(n, multiplier*4*math.sin(math.pi/n)**2, 1)
            t=multiplier*c
            LL=wheel_laplacian(n,[a]*n,[b]*n)
            assert abs(np.linalg.eigvalsh(LL)[1]-val)<1e-10
            assertions+=1
            for _ in range(20):
                weights=rng.uniform(.01,1,size=2*n)
                budget=sum(weights[:n])+t*sum(weights[n:])
                weights/=budget
                L=wheel_laplacian(n,weights[:n],weights[n:])
                obtained=np.linalg.eigvalsh(L)[1]
                upper=min((sum(weights[:n])+c*sum(weights[n:]))/n,
                          (n+1)*sum(weights[:n])/n)
                assert obtained <= upper+1e-10
                assert obtained <= val+1e-10
                assertions+=2
    # A critical segment beyond its upper endpoint must lose optimality.
    for n in (3,4,6,8):
        c=4*math.sin(math.pi/n)**2
        B=1
        beyond=.5*(B/((n+1)*c)+B/(n*c))
        aa=B/n-c*beyond
        L=wheel_laplacian(n,[aa]*n,[beyond]*n)
        assert np.linalg.eigvalsh(L)[1] < B/n-1e-10
        assertions+=1
    print(f'PASS {assertions} symbolic, exact and numerical checks')


if __name__=='__main__':
    validate()
