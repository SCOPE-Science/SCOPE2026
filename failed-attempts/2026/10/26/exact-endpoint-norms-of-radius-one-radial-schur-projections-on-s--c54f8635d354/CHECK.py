#!/usr/bin/env python3
"""Exact rational checks of the algebraic certificates in the star Schur norm theorem.

The finite checks are supplemental; the accompanying proof handles all integers n>=1.
"""
from fractions import Fraction as F


def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [list(row) for row in zip(*A)]


def verify(n):
    assert isinstance(n,int) and n >= 1
    N=n+1
    den=3*n+1
    t=F(5*n-1, den)
    d=t-1
    b=2-t
    M=[[F(int(i==j or i==0 or j==0)) for j in range(N)] for i in range(N)]
    A=[[t if i==j else b if i==0 or j==0 else d for j in range(N)] for i in range(N)]
    w=[F(1)]+[F(-1)]*n
    r=[F(2*n)]+[F(n+1)]*n
    P=[[F(0) if i==0 or j==0 else F(int(i==j))-F(1,n)
         for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            assert A[i][j]-M[i][j]==d*w[i]*w[j]
            assert A[i][j]+M[i][j]==2*P[i][j]+F(2,n*den)*r[i]*r[j]
    assert matmul(P,P)==P and transpose(P)==P
    # Exact eigenvalues of the two-dimensional compression of diag(x) M diag(x).
    a2=F(n+1,den)
    b2=F(2,den)
    lam_plus=F(2*(n+1),den)
    lam_minus=-F(n-1,den)
    assert a2+n*b2==1
    assert a2+b2 == lam_plus+lam_minus
    assert a2*b2*(1-n) == lam_plus*lam_minus
    # The other n-1 eigenvalues are b2.
    assert lam_plus+(n-1)*b2+abs(lam_minus)==t
    assert t == F(5*n-1,3*n+1)
    assert F(5,3)-t==F(8,3*den)
    return t


if __name__=='__main__':
    ns=list(range(1,25))+[32,48]
    results=[verify(n) for n in ns]
    assert results[0] == 1 and results[1] == F(9,7)
    assert all(results[i]<results[i+1] for i in range(len(results)-1))
    print(f'PASS: {len(ns)} exact rational certificates; n=2 norm {results[1]}, limit 5/3')
