#!/usr/bin/env python3
"""Numerical cross-checks for an idealized exponential-covariance spatial design theorem."""
import math
import random
import numpy as np
from scipy.optimize import brentq, minimize


def edge(u):
    return u + math.expm1(-2*u)/2.0


def interior(u):
    if abs(u)<1e-3:
        return u*u/3-u**4/45+2*u**6/945
    return u/math.tanh(u)-1


def edge_prime(u):
    return -math.expm1(-2*u)


def inter_prime(u):
    if abs(u)<1e-3:
        return 2*u/3-4*u**3/45+4*u**5/315
    return 1/math.tanh(u)-u/(math.sinh(u)**2)


def optimum(n,L):
    assert n>=2 and L>0
    def residual(d):
        a=(L-(n-1)*d)/2
        return edge_prime(a)-inter_prime(d)
    d=brentq(residual,0,L/(n-1),xtol=1e-14)
    a=(L-(n-1)*d)/2
    j=2*edge(a)+(n-1)*interior(d)
    return a,d,j


def arbitrary_objective(gaps):
    return edge(gaps[0])+edge(gaps[-1])+sum(interior(x) for x in gaps[1:-1])


def matrix_integral(n,L,coords,ngrid=3001):
    obs=np.asarray(coords)
    Q=np.exp(-np.abs(obs[:,None]-obs[None,:]))
    Qinv=np.linalg.inv(Q)
    t=np.linspace(0,L,ngrid)
    k=np.exp(-np.abs(t[:,None]-obs[None,:]))
    v=1-np.einsum('ij,jk,ik->i',k,Qinv,k)
    return float(np.trapezoid(v,t))


def main():
    rng=random.Random(211907)
    count=0
    for n in range(2,9):
        for L in [0.05,0.2,0.7,1.,3.,10.,40.]:
            a,d,j=optimum(n,L)
            assert 0<a<d and abs(2*a+(n-1)*d-L)<1e-10
            assert abs(edge_prime(a)-inter_prime(d))<1e-9
            count+=3
            if n<=5 and L<=10:
                coords=[a+i*d for i in range(n)]
                m=matrix_integral(n,L,coords)
                assert abs(m-j)<2e-6*max(1,j), (n,L,m,j)
                count+=1
            for _ in range(20):
                z=np.asarray([rng.expovariate(1) for k in range(n+1)])
                z*=L/z.sum()
                trial=arbitrary_objective(z)
                assert trial>=j-2e-10, (n,L,trial,j)
                count+=1
        # Asymptotic station gaps: edge ~= L/(3*n-1), interior ~= 3*L/(3*n-1)
        LL=1e-4
        aa,dd,jj=optimum(n,LL)
        assert abs(aa/LL-1/(3*n-1))<1e-4
        assert abs(dd/LL-3/(3*n-1))<1e-4
        count+=2
    for n in [2,3,5]:
        for L in [10.,20.,30.]:
            a,d,j=optimum(n,L)
            assert abs(d-L/(n+1)-math.log(4*L/(n+1))/(n+1))<0.15,(n,L,a,d)
            assert abs(a-L/(n+1)+(n-1)*math.log(4*L/(n+1))/(2*(n+1)))<0.15,(n,L,a,d)
            count+=2
    # Independent unconstrained nonlinear optimization for selected short domains
    for n in [2,3,4]:
        for L in [0.2,1,4]:
            a,d,j=optimum(n,L)
            def fn(y):
                # n+1 nonnegative gaps satisfying sum L, represented via softmax
                v=np.exp(np.asarray(y)-max(y)); v=L*v/v.sum()
                return arbitrary_objective(v)
            best=minimize(fn,np.zeros(n+1),method='BFGS',options={'gtol':1e-10})
            assert best.fun >= j-1e-8 and best.fun-j<1e-6,(n,L,best.fun,j)
            count+=1
    print('PASS',count,'assertions')
    for n in [2,3,5]:
        for L in [.1,1,5,20]:
            a,d,j=optimum(n,L)
            print('n,L,edge,inner,loss:',n,L,format(a,'.12f'),format(d,'.12f'),format(j,'.12f'))

if __name__=='__main__':main()
