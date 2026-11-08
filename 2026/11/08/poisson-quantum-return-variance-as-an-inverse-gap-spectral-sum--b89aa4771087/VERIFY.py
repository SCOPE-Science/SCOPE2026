#!/usr/bin/env python3
"""Exact operator and independent numerical checks for Poisson quantum return statistics.

Usage: python VERIFY.py
Requires: numpy, scipy, sympy.
All calculations here use only the stated finite-dimensional Hamiltonian and sampling law.
"""
import math
import numpy as np
import sympy as sp
from scipy.linalg import null_space

checks = 0

def verify_exact(energies, rate):
    global checks
    E=[sp.Rational(x) for x in energies]
    r=sp.Rational(rate); n=len(E)
    I=sp.eye(n); one=sp.ones(n,1)
    P=one*one.T/n; Q=I-P
    ss=[sum((1/(E[j]-E[k]) for k in range(n) if k!=j),sp.S.Zero) for j in range(n)]
    a=[-r*s/n for s in ss]
    Z=sp.zeros(n);Y=sp.zeros(n)
    for j in range(n):
        for k in range(n):
            if j!=k:
                delta=E[j]-E[k]
                Z[j,k]=-1+sp.I*(a[j]-a[k])
                Y[j,k]=sp.expand(Z[j,k]*(1-sp.I*r/delta))
    for j in range(n):Y[j,j]=-sum(Y[j,k] for k in range(n) if k!=j)
    phi=lambda X:sp.Matrix(n,n,lambda j,k:sp.expand(X[j,k]*r/(r+sp.I*(E[j]-E[k]))))
    assert sp.simplify(Y-Y.H)==sp.zeros(n);checks+=1
    assert sp.simplify(Y*one)==sp.zeros(n,1);checks+=1
    assert sp.simplify(Q*(Y-phi(Y))*Q-Q)==sp.zeros(n);checks+=1
    expected=n*(n-1)+sp.Rational(4,n)*r*r*sum(1/(E[j]-E[k])**2 for j in range(n) for k in range(j+1,n))
    assert sp.simplify(sp.trace(Y)-expected)==0;checks+=1


def direct_moments(E,p,r):
    E=np.asarray(E,dtype=float)
    p=np.asarray(p,dtype=float)
    n=len(E);psi=np.sqrt(p).reshape(n,1)
    V=null_space(psi.conj().T)
    m=n-1
    phi=lambda X:X*r/(r+1j*(E[:,None]-E[None,:]))
    P=psi@psi.T
    B=V.conj().T@phi(P)@V
    T=np.zeros((m*m,m*m),dtype=complex)
    for j in range(m):
        for k in range(m):
            unit=np.zeros((m,m),dtype=complex);unit[j,k]=1
            T[:,j*m+k]=(V.conj().T@phi(V@unit@V.conj().T)@V).reshape(-1)
    solved=np.linalg.solve(np.eye(m*m)-T,B.reshape(-1))
    solved_twice=np.linalg.solve(np.eye(m*m)-T,solved)
    mean=1+np.trace(solved.reshape(m,m)).real
    second=mean+2*np.trace(solved_twice.reshape(m,m)).real
    return mean,second-mean**2


def check_numeric():
    global checks
    rng=np.random.default_rng(20241103)
    for n in range(2,7):
        for _ in range(12):
            E=np.cumsum(np.r_[0,rng.uniform(.4,3,n-1)])
            r=float(rng.uniform(.25,4))
            mean,var=direct_moments(E,np.full(n,1/n),r)
            target=n*(n-1)+8*r*r/n*sum(1/(E[j]-E[k])**2 for j in range(n) for k in range(j+1,n))
            assert abs(mean-n)<1.e-7,(n,mean)
            assert abs(var-target)<1.e-6*max(1,target),(n,var,target)
            checks+=2
    for alpha in [.07,.2,.3,.49,.8,1.12]:
        for r in [.25,.7,2.6]:
            E=-2*np.cos(alpha+2*np.pi*np.arange(3)/3)
            mean,var=direct_moments(E,[1/3]*3,r)
            target=6+2*r*r/np.sin(3*alpha)**2
            assert abs(mean-3)<1e-7 and abs(var-target)<1.e-6*max(1,target)
            checks+=1
    for r in [.3,1,3,7]:
        mean,var=direct_moments([-2.,1.],[1/3,2/3],r)
        assert abs(mean-2)<1e-9 and abs(var-(2.5+.5*r*r))<1e-8
        checks+=1

if __name__=='__main__':
    for E,r in [([0,1],sp.Rational(1,3)),([0,1,4],sp.Rational(5,4)),([0,2,5,11],sp.Rational(3,2)),([0,3,7,9,16],sp.Rational(7,5))]:
        verify_exact(E,r)
    check_numeric()
    print(f'PASS: {checks} exact and independent numerical assertions')
