#!/usr/bin/env python3
"""Reproducible finite diagnostics for helm-graph Kemeny optimization.

Requires numpy and scipy; finite tests corroborate but cannot replace the proofs.
"""
import math
import numpy as np
from scipy.optimize import brentq, minimize


def orbit_constant(n,a,b,c):
    assert n>=5 and a>0 and c>0 and b>=0
    A=(n-1)+(n+1)/(2*n+1)
    B=2/(2*n+1)
    modes=1-np.cos(2*np.pi*np.arange(1,n)/n)
    return A/c+B/a+2*np.sum(1/(a+2*b*modes))


def matrix_constant(n,a,b,c):
    N=2*n+1
    L=np.zeros((N,N),float)
    def edge(u,v,w):
        L[u,u]+=w;L[v,v]+=w;L[u,v]-=w;L[v,u]-=w
    for j in range(n):
        edge(0,j+1,a)
        edge(j+1,(j+1)%n+1,b)
        edge(j+1,n+j+1,c)
    e=np.linalg.eigvalsh(L)
    assert e[1]>0
    return np.sum(1/e[1:])


def optimal_c(n):
    a=1/n
    A=(n-1)+(n+1)/(2*n+1)
    modes=1-np.cos(2*np.pi*np.arange(1,n)/n)
    def d(c):
        den=a+(1-a-c)*modes
        return -A/c**2+2*np.sum(modes/den**2)
    return brentq(d,1e-12,1-a-1e-12,xtol=1e-14)


def run():
    asserts=0
    for n in list(range(5,31))+[40,50,60]:
        for frac in [0.18,0.49,0.91]:
            a=frac/n;c=(1-a)*0.24;b=(1-a-c)*0.32
            v1=orbit_constant(n,a,b,c)
            v2=matrix_constant(n,a,b,c)
            assert abs(v1-v2)<1e-7*max(v1,v2),(n,v1,v2)
            asserts+=1
    for n in range(5,51):
        a=1/n;c=optimal_c(n);b=(1-a-c)/2
        eps=max(1e-8,1e-6*c)
        f=orbit_constant(n,a,b,c)
        for dc in [-eps,eps]:
            co=c+dc
            fo=orbit_constant(n,a,(1-a-co)/2,co)
            assert fo>f-1e-8*f
            asserts+=1
        # Check that a small inward step worsens the objective while
        # maintaining zero holding at rim vertices.
        for factor in [.999,.97,.8]:
            ao=a*factor
            trial=orbit_constant(n,ao,(1-ao-c)/2,c)
            assert trial>f-1e-9*f,(n,trial,f)
            asserts+=1
        assert 0<c<1-a
        asserts+=1
        if n<=15:
            x0=[a*.8,c*.8]
            res=minimize(lambda x: orbit_constant(n,x[0],(1-x[0]-x[1])/2,x[1])
                if x[0]>0 and x[1]>0 and x[0]+x[1]<=1 else 1e15,
                x0,method='SLSQP',bounds=[(1e-9,1/n),(1e-9,1-1e-9)],
                constraints=[{'type':'ineq','fun':lambda x:1-x[0]-x[1]}],
                options={'ftol':1e-11,'maxiter':300})
            assert res.fun>=f-1e-7*max(1,f),(n,res.fun,f)
            asserts+=1
    for n in [100,500,2000,10000,40000]:
        c=optimal_c(n)
        k=orbit_constant(n,1/n,(1-1/n-c)/2,c)
        cscale=c*n**.25
        kscale=(k-math.sqrt(2)*n**1.5)/n**1.25
        # Loose checks for finite n, whose second-order convergence is slow.
        assert 0.7<cscale<1.3,(n,cscale)
        assert 0.5<kscale<2.5,(n,kscale)
        asserts+=2
        print('asymptotic',n,'leaf scale',round(cscale,7),
              'second-order value scale',round(kscale,7))
    # Check the exact maximum-degree competitor formula, including matrix cross-check.
    for n in [5,6,11,25,40]:
        k=orbit_constant(n,1/n,1/n,1/n)
        v=matrix_constant(n,1/n,1/n,1/n)
        assert math.isclose(k,v,rel_tol=1e-10)
        asserts+=1
    print('OK finite assertions:',asserts)

if __name__=='__main__':run()
