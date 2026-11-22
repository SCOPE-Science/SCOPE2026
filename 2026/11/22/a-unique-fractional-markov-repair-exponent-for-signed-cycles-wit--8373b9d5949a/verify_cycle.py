#!/usr/bin/env python3
"""Reproducible finite diagnostics for a signed path-closure Laplacian.
All infinite-dimensional or all-parameter claims require the accompanying proof.
Requires Python 3, NumPy and SciPy for the spectral checks.
"""
from fractions import Fraction as Q
from math import isclose
import numpy as np
from scipy.linalg import eigh
from scipy.optimize import brentq


def signed_path(n, a):
    L = [[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(n-1):
        L[i][i] += 1
        L[i+1][i+1] += 1
        L[i][i+1] -= 1
        L[i+1][i] -= 1
    L[0][0] -= a
    L[-1][-1] -= a
    L[0][-1] += a
    L[-1][0] += a
    return L


def inverse_rational(A):
    n=len(A)
    b=[list(row)+[Q(i==j) for j in range(n)] for i,row in enumerate(A)]
    for k in range(n):
        p=next(i for i in range(k,n) if b[i][k])
        b[k],b[p]=b[p],b[k]
        den=b[k][k]
        b[k]=[x/den for x in b[k]]
        for i in range(n):
            if i==k: continue
            mul=b[i][k]
            b[i]=[x-mul*y for x,y in zip(b[i],b[k])]
    return [row[n:] for row in b]


def U(k,x):
    if k==0: return Q(1)
    v0,v1=Q(1),2*x
    for j in range(1,k):
        v0,v1=v1,2*x*v1-v0
    return v1


def rational_checks():
    checks=0
    for n in range(3,9):
        for s in [Q(1,5),Q(1),Q(7,3)]:
            x=1+s/2
            D=s*U(n-1,x)
            p=U(n-1,x)-U(n-2,x)
            r=2*(p-1)/D
            G=inverse_rational([[Q(i==j)*s+v for j,v in enumerate(row)] for i,row in enumerate(signed_path(n,Q(0)))])
            assert G[0][-1] == 1/D
            checks+=1
            assert G[0][0]==p/D
            checks+=1
            assert p*p-1 == D*U(n-2,x)
            checks+=1
            for num,den in [(1,10),(1,2),(9,10)]:
                a=Q(num,den*(n-1))
                R=inverse_rational([[Q(i==j)*s+v for j,v in enumerate(row)] for i,row in enumerate(signed_path(n,a))])
                expect=(1-a*U(n-2,x))/(D*(1-a*r))
                assert R[0][-1]==expect
                checks+=1
                for i in range(n):
                    for j in range(i+1,n):
                        assert R[i][j] >= expect
                        checks+=1
                        if (i,j)!=(0,n-1):
                            assert R[i][j]>expect
                            checks+=1
    return checks


def spectral_checks():
    checks=0
    for n in [3,4,5,8,12,20]:
        for rho in [0.1,0.5,0.9]:
            a=rho/(n-1)
            L=np.array(signed_path(n,Q(str(a))),dtype=float)
            eig,V=eigh(L)
            eig=np.maximum(eig,0.0)
            assert eig[1]>1e-10 and abs(eig[0])<1e-9
            eig[0]=0.0  # exact known constant-vector zero eigenvalue
            checks+=1
            def power(alpha):
                return (V*eig**alpha)@V.T
            def endpoint(alpha):
                return power(alpha)[0,-1]
            root=brentq(endpoint,0.001,0.999,xtol=1e-13)
            assert 0<root<1 and abs(endpoint(root))<1e-10
            checks+=1
            for alpha in [0.05,root*0.6,root,root+(1-root)*0.4,0.95]:
                F=power(alpha)
                ep=F[0,-1]
                assert np.max(np.abs(F-F.T))<1e-12
                checks+=1
                assert np.max(np.abs(F.sum(axis=0)))<1e-11
                checks+=1
                for i in range(n):
                    for j in range(i+1,n):
                        if (i,j)!=(0,n-1):
                            assert F[i,j] < ep+2e-9, (n,rho,alpha,i,j,F[i,j],ep)
                            checks+=1
                if alpha<root-1e-10: assert ep<0
                if alpha>root+1e-10: assert ep>0
                checks+=1
    return checks

if __name__=='__main__':
    a=rational_checks()
    b=spectral_checks()
    print(f'VERIFICATION_OK rational={a} spectral={b} total={a+b}')
