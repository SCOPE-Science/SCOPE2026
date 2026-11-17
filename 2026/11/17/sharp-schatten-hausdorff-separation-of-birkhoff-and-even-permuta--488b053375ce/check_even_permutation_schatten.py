#!/usr/bin/env python3
"""Reproduce exact parity-deletion certificates and finite checks.

Requires Python 3 and numpy; cvxpy is optional for independent small-order QP.
"""
from itertools import permutations, combinations
from fractions import Fraction
import math
import numpy as np


def parity(p):
    return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2


def matrix(p):
    n=len(p)
    z=np.zeros((n,n),dtype=float)
    z[np.arange(n),list(p)]=1.0
    return z


def transposition(n,i,j):
    p=list(range(n));p[i],p[j]=p[j],p[i];return tuple(p)


def certificate(n):
    # Exact rational identity M=((n-3)/(n-1)) I + 2/(n-1) J.
    off=Fraction(2,n*(n-1))
    diag=Fraction(n-2,n)
    alpha=Fraction(n-3,n-1)
    assert diag-off==alpha
    assert off==Fraction(2,n-1)*Fraction(1,n)
    assert diag + (n-1)*off==1
    assert n*diag==n-2  # supporting hyperplane
    assert Fraction(4,n-1)==(Fraction(2,n-1)**2)*(n-1)
    return float(alpha),float(off)


def verify(n):
    alpha,off=certificate(n)
    ps=list(permutations(range(n)))
    evens=[p for p in ps if not parity(p)]
    odds=[p for p in ps if parity(p)]
    assert len(evens)==len(odds)==math.factorial(n)//2
    I=np.eye(n);U=np.ones((n,n))/n
    T=np.array([matrix(transposition(n,i,j)) for i,j in combinations(range(n),2)])
    M=T.mean(axis=0)
    assert np.allclose(M,alpha*I+2/(n-1)*U,atol=1e-14)
    assert np.allclose(M.sum(axis=0),np.ones(n))
    assert np.allclose(M.sum(axis=1),np.ones(n))
    assert abs(np.trace(M)-(n-2))<1e-12
    assert all(round(np.trace(matrix(p)))<=n-2 for p in odds)
    assert sum(round(np.trace(matrix(p)))==n-2 for p in odds)==n*(n-1)//2
    # All equality permutations are transpositions; distinct off-diagonal
    # supports certify affine independence of this exposed simplex.
    for p in odds:
        if round(np.trace(matrix(p)))==n-2:
            assert sum(p[i]!=i for i in range(n))==2
    singular=np.linalg.svd(I-M,compute_uv=False)
    assert np.allclose(singular[:n-1],np.repeat(2/(n-1),n-1),atol=1e-13)
    assert abs(singular[-1])<1e-12
    for pnorm in [1.,1.5,2.,3.,5.,float('inf')]:
        actual=np.max(singular) if pnorm==float('inf') else np.linalg.norm(singular,ord=pnorm)
        expected=2*(n-1)**((0 if pnorm==float('inf') else 1/pnorm)-1)
        assert abs(actual-expected)<1e-12,(n,pnorm,actual,expected)
    return len(evens),len(T)


def independent_projection(n):
    # Separate constrained optimization with variables for *every* even vertex.
    from scipy.optimize import minimize
    arr=np.stack([matrix(p).flatten() for p in permutations(range(n)) if not parity(p)],axis=1)
    m=arr.shape[1]; eye=matrix(transposition(n,0,1)).flatten()
    def fun(w):
        v=arr@w-eye
        return float(v@v)
    def jac(w):
        return 2*arr.T@(arr@w-eye)
    sol=minimize(fun,np.full(m,1/m),jac=jac,method='SLSQP',
        bounds=[(0,None)]*m,constraints=[{'type':'eq','fun':lambda w:np.sum(w)-1,
                                          'jac':lambda w:np.ones(m)}],
        options={'ftol':1e-11,'maxiter':500})
    assert sol.success,(n,sol.message)
    reference=4/(n-1)
    assert abs(sol.fun-reference)<1e-8,(sol.fun,reference)
    return sol.fun


if __name__=='__main__':
    profiles=[]
    for n in range(3,9):
        ev,face=verify(n)
        profiles.append((n,ev,face))
    independent=[]
    for n in [3,4,5]:
        v=independent_projection(n)
        if v is not None:independent.append((n,round(float(v),10)))
    print('EVEN_PERMUTATION_SCHATTEN_PASS exact_n=3..8',
          'simplex_sizes='+repr([x[2] for x in profiles]),
          'independent_qp='+repr(independent))
