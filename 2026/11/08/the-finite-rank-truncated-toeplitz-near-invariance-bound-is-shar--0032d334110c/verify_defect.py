#!/usr/bin/env python3
"""Exact finite-matrix check for finite-rank perturbations of truncated Toeplitz operators."""
from sympy import zeros, eye, Matrix

def run(n):
    k = 2*n + 2
    r = 3*n + 4
    N = k+r
    A = zeros(N,N)
    R = zeros(N,N)
    U = zeros(N,n)
    Q = zeros(n,N)
    Sstar = zeros(N,N)
    G = zeros(N,k)
    for i in range(N):
        if i+k<N: A[i+k,i]=1
        if i>=1: Sstar[i-1,i]=1
    for j in range(1,n+1):
        U[3*j,j-1]=1
        Q[j-1,r+2*j]=1
    for a in range(k):G[r+a,a]=1
    R=A*U*Q
    B=A-R
    assert Q*U == zeros(n,n)
    assert (eye(N)-U*Q)*(eye(N)+U*Q)==eye(N)
    assert R.rank()==n
    M=(eye(N)+U*Q)*G
    assert B*M==zeros(N,k)
    assert M.rank()==k==N-B.rank()
    assert M[0,:]==zeros(1,k)
    assert Matrix.hstack(M,Sstar*M).rank()-M.rank()==2*n+1
    W=Matrix.hstack(*[Matrix.eye(N)[:,i] for i in [r-1]+[3*j for j in range(1,n+1)]+[3*j-1 for j in range(1,n+1)]])
    assert Matrix.hstack(M,W).rank()==k+2*n+1
    return N,k,2*n+1
if __name__=='__main__':
    for n in range(1,9):print('rank',n,'N,k,defect',run(n))
    print('TRUNCATED_TOEPLITZ_SHARP_DEFECT_EXACT_OK 8')
