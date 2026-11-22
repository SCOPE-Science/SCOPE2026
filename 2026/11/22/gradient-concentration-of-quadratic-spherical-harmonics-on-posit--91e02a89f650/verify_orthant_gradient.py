#!/usr/bin/env python3
"""Independent monomial-moment verification of quadratic orthant gradient spectra.

Rebuilds each full Gram matrix without using incidence spectral blocks.
Requires numpy; the proof of the all-dimensional theorem is analytic.
"""
import math
import numpy as np
from functools import lru_cache


def full_basis(d):
    # Euclidean-orthonormal coordinates in the trace-zero diagonal hyperplane.
    columns=[]
    for i in range(d-1):
        u=np.zeros(d)
        u[:i+1]=1/math.sqrt((i+1)*(i+2))
        u[i+1]=-(i+1)/math.sqrt((i+1)*(i+2))
        Q=np.diag(u/math.sqrt(2.0))
        columns.append(Q)
    for i in range(d):
        for j in range(i+1,d):
            Q=np.zeros((d,d))
            Q[i,j]=Q[j,i]=0.5
            columns.append(Q)
    return columns


def from_moments(d):
    Q=full_basis(d)
    n=len(Q)
    a=2/math.pi
    S2=np.full((d,d),a/d)
    np.fill_diagonal(S2,1/d)
    @lru_cache(None)
    def mom4(i,j,k,l):
        ct=[0]*d
        for v in (i,j,k,l):ct[v]+=1
        return math.exp(math.lgamma(d/2)-math.lgamma((d+4)/2)+
             sum(math.lgamma((e+1)/2)-math.lgamma(.5) for e in ct))
    F4=np.empty((d,d,d,d))
    for i in range(d):
        for j in range(d):
            for k in range(d):
                for l in range(d):F4[i,j,k,l]=mom4(i,j,k,l)
    out=np.empty((n,n))
    for i,A in enumerate(Q):
        for j,B in enumerate(Q):
            q1=np.sum((A@B)*S2.T)
            q2=np.einsum('ab,cd,abcd->',A,B,F4)
            out[i,j]=2*(d+2)*(q1-q2)
    return 0.5*(out+out.T)


def prediction(d):
    a=2/math.pi
    alpha=(1-a)*(1+2*a/d)
    beta=a*(d-2+4*a)/(2*d)
    gamma=-2*a*a/d
    constant=alpha+2*(d-1)*beta+math.comb(d,2)*gamma
    M=np.array([[1,a*math.sqrt((d-2)/2)],
                [a*math.sqrt((d-2)/2),alpha+(d-2)*beta]])
    mminus,mplus=np.linalg.eigvalsh(M)
    vals=[mminus]*(d-1)+[constant]+[mplus]*(d-1)+[alpha]*(d*(d-3)//2)
    return sorted(vals),(mminus,alpha,constant,mplus)


def main():
    count=0
    for d in range(3,11):
        direct=np.linalg.eigvalsh(from_moments(d))
        expected, ordered=prediction(d)
        assert len(direct)==len(expected)==(d-1)*(d+2)//2
        assert np.allclose(direct,expected,rtol=2e-11,atol=1e-11),(d,direct,expected)
        assert all(0<x<y for x,y in zip(ordered,ordered[1:])),(d,ordered)
        assert abs(sum(direct)-len(direct))<3e-10
        count+=len(direct)+4
    for d in (100,1000,10000):
        _,(lo,_,_,hi)=prediction(d)
        assert abs((hi/lo)/d-1/(math.pi-2))<10/d
        count+=1
    print('ORTHANT_GRADIENT_SPECTRUM_CHECKS_PASS',count)

if __name__=='__main__':main()
