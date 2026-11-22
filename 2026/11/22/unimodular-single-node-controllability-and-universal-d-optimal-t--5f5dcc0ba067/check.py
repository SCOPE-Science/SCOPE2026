"""Reproducibility checks for path single-actuator controllability-volume identities.
Run: python check.py
Uses sympy and mpmath; no network access or external files.
"""
from math import gcd, pi
import sympy as s
import mpmath as mp

checks=0
for n in range(2,19):
    L=s.zeros(n)
    for k in range(n-1):
        L[k,k]+=1; L[k+1,k+1]+=1
        L[k,k+1]-=1; L[k+1,k]-=1
    E=s.eye(n)
    for j in range(n):
        v=E[:,j]; columns=[]
        for k in range(n):
            columns.append(v)
            v=-L*v
        K=s.Matrix.hstack(*columns)
        actual=int(K.det(method='domain-ge'))
        assert (actual!=0)==(gcd(2*j+1,n)==1), (n,j,actual)
        assert abs(actual) in (0,1), (n,j,actual)
        checks+=2

mp.mp.dps=65
for n in range(2,10):
    for mu,T in [(0,mp.mpf('0.2')),(mp.mpf('0.7'),mp.mpf('1.5')),(mp.mpf('2'),mp.mpf('3'))]:
        lam=[2-2*mp.cos(k*mp.pi/n) for k in range(n)]
        C=mp.matrix(n,n)
        for k in range(n):
            for ell in range(n):
                ss=2*mu+lam[k]+lam[ell]
                C[k,ell]=T if abs(ss)<mp.mpf('1e-48') else -mp.expm1(-ss*T)/ss
        detC=mp.det(C)
        assert detC>0,(n,mu,T,detC)
        for j in range(1,n+1):
            v=[mp.mpf(1)/mp.sqrt(n)]+[mp.sqrt(mp.mpf(2)/n)*mp.cos(mp.pi*k*(j-mp.mpf('.5'))/n) for k in range(1,n)]
            # Build matrix directly in physical coordinates from normalized eigensystem.
            # For singular sites use a high-precision near-zero comparison, not signs.
            if gcd(2*j-1,n)!=1:
                continue
            eigprod=mp.fprod(x*x for x in v)
            assert mp.almosteq(eigprod,mp.mpf(1)/(2*n)**(n-1),rel_eps=mp.mpf('1e-51')),(n,j,eigprod)
            Wmodal=mp.matrix(n,n)
            for k in range(n):
                for ell in range(n): Wmodal[k,ell]=v[k]*C[k,ell]*v[ell]
            assert mp.almosteq(mp.det(Wmodal),detC/(2*n)**(n-1),rel_eps=mp.mpf('1e-44')),(n,j,mu,T)
            checks+=2
        checks+=1

# Independent high-precision matrix-exponential quadrature to evaluate a physical Gramian.
# Gauss integration is not proof; checks are supplementary.
import numpy as np
from scipy.linalg import expm
from numpy.polynomial.legendre import leggauss
for n in range(2,8):
    LL=np.zeros((n,n))
    for k in range(n-1):
        LL[k,k]+=1;LL[k+1,k+1]+=1;LL[k,k+1]-=1;LL[k+1,k]-=1
    mu=0.7;T=2.0
    nodes,weights=leggauss(240)
    x=(nodes+1)*T/2;weight=weights*T/2
    direct=[]
    for j in range(n):
        W=np.zeros((n,n))
        for t,w in zip(x,weight):
            vec=expm(-t*(LL+mu*np.eye(n)))[:,j]
            W+=w*np.outer(vec,vec)
        direct.append(np.linalg.det(W))
    endpoint=direct[0]
    assert endpoint>0
    for j in range(n):
        if gcd(2*j+1,n)==1:
            assert abs(direct[j]/endpoint-1)<2e-5,(n,j,direct,endpoint)
            checks+=1
print('PASS',checks,'checks; exact integer determinants 2<=n<=18, high-precision spectral Gramian and independent quadrature')
