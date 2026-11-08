#!/usr/bin/env python3
"""Finite consistency checks for the finite-atomic stationary Kaczmarz theorem.
Requires NumPy and SymPy. Not a substitute for the proof of the universal claims.
"""
import numpy as np
import sympy as sp

checks=0
def check(assertion,msg):
    global checks
    if not assertion:
        raise AssertionError(msg)
    checks+=1

# Exact two-atom characteristic coefficient and closed-form contraction.
p=sp.Rational(3,7)
wa,wb=sp.Integer(1),-sp.Integer(1)
t=sp.Symbol('t')
R=sp.expand(p*(t-wb)+(1-p)*(t-wa))
check(sp.expand(R-(t-sp.Rational(1,7)))==0,'two-atom exact polynomial')
check(sp.expand((sp.Rational(1,7))**2-(1-4*p*(1-p)))==0,'two-atom exact norm')

for m in range(2,9):
    for trial in range(10):
        rng=np.random.default_rng(1000*m+trial)
        if trial==0:
            points=np.exp(2j*np.pi*(np.arange(m)+0.137)/m)
            weights=np.full(m,1/m)
        else:
            points=np.exp(2j*np.pi*rng.uniform(0,1,m))
            weights=rng.uniform(0.1,1.1,m)
            weights/=weights.sum()
        u=np.sqrt(weights)
        U=np.diag(points)
        Q=np.eye(m)-np.outer(u,u)
        _,_,Vh=np.linalg.svd(u[np.newaxis,:],full_matrices=True)
        V=Vh[1:].conjugate().T
        B=V.conjugate().T@U.conjugate().T@V
        nodes=points.conjugate()
        R=np.zeros(m,dtype=complex)
        for j in range(m):
            R+=weights[j]*np.poly(np.delete(nodes,j))
        check(np.linalg.norm(np.poly(B)-R)<1e-7,(m,trial,'minor polynomial'))
        check(max(abs(np.linalg.eigvals(B)))<1+1e-8,(m,trial,'spectral disk'))
        for N in range(0,9):
            E=np.eye(m,dtype=complex)
            for k in range(N+1):
                ek=(points**k)*u
                E=(np.eye(m)-np.outer(ek,ek.conjugate()))@E
            expected=np.linalg.matrix_power(U,N)@V@np.linalg.matrix_power(B,N)@V.conjugate().T@Q
            check(np.linalg.norm(E-expected)<1e-8,(m,trial,N,'product identity'))
            check(abs(np.linalg.norm(E,ord=2)-np.linalg.norm(np.linalg.matrix_power(B,N),ord=2))<1e-8,(m,trial,N,'norm identity'))
        if trial==0:
            check(np.linalg.norm(np.linalg.matrix_power(B,m-1))<1e-6,(m,'regular nilpotence'))
        else:
            check(max(abs(np.linalg.eigvals(B)))>1e-8,(m,'nonregular nonnilpotence'))

print('PASS',checks,'exact and finite-dimensional diagnostic checks')
