#!/usr/bin/env python3
"""Direct numerical and exact-arithmetic checks for crown-graph mixing rigidity.

Run: python verify.py

Numerical tests are finite corroboration; the infinite-family conclusions are
proved algebraically in RESULT.md.
"""
from fractions import Fraction as F
import itertools
import math
import random
import numpy as np


def make_P(n, W):
    W=np.asarray(W,dtype=float)
    assert W.shape == (n,n)
    assert np.max(abs(np.diag(W))) < 1e-12
    assert np.min(W) >= -1e-12
    row=W.sum(axis=1); col=W.sum(axis=0)
    assert max(row.max(),col.max()) <= 1+1e-10
    P=np.zeros((2*n,2*n),dtype=float)
    P[:n,:n]=np.diag(1-row)
    P[n:,n:]=np.diag(1-col)
    P[:n,n:]=W
    P[n:,:n]=W.T
    return P


def slem(P):
    n=P.shape[0]
    return np.linalg.norm(P-np.ones_like(P)/n,ord=2)


def exact_formulas(n):
    p=F(2,3*n-4); m=F(n,3*n-4)
    assert p>0 and 1-(n-1)*p>=0
    e_partition=1-2*(n-1)*p
    e_sym=1-n*p
    e_anti=1-(n-2)*p
    assert e_partition == -m and e_anti==m and abs(e_sym)<=m
    s=n*(n-1)*p
    assert F(n,1)*(1+m)/2==s
    assert F(n*(n-1),n-2)*(1-m)==s
    assert F(n-1,1)-F(n-2,n)*s == (n-1)*m
    return p,m


def trace_U(P,n):
    W=P[:n,n:]
    Q=np.eye(n)-np.ones((n,n))/n
    U=np.vstack([Q,-Q])/math.sqrt(2)
    return float(np.trace(U.T@P@U))


def check():
    rng=random.Random(521431)
    cases=0
    exact=0
    for n in range(3,20):
        p,m=exact_formulas(n); exact+=7
        W=np.ones((n,n))*float(p); np.fill_diagonal(W,0)
        P=make_P(n,W)
        assert np.allclose(np.sum(P,axis=1),1)
        assert abs(slem(P)-float(m))<2e-12
        ev=np.sort(np.linalg.eigvalsh(P))
        expected=sorted([-float(m)]+[float(1-n*p)]*(n-1)+[float(m)]*(n-1)+[1.])
        assert np.max(np.abs(ev-expected))<2e-12
        cases+=1
    for n in range(3,11):
        p,m=exact_formulas(n)
        for z in range(320):
            W=np.zeros((n,n))
            # Scale a random nonnegative cross-weight matrix to meet all
            # row and column stochasticity constraints.
            for i in range(n):
                for j in range(n):
                    if i!=j:W[i,j]=rng.randrange(0,21)/20
            scale=0.99/max(W.sum(axis=1).max(),W.sum(axis=0).max(),0.01)
            W*=scale
            P=make_P(n,W)
            mu=slem(P); delta=mu-float(m)
            assert delta >= -5e-12,(n,z,delta)
            s=W.sum()
            tr=(n-1)-(n-2)*s/n
            assert abs(tr-trace_U(P,n)) < 5e-11
            assert s <= n*(1+mu)/2+5e-11
            assert s >= n*(n-1)*(1-mu)/(n-2)-5e-11
            bound=6*math.sqrt(max(0,mu*(3*n-4)*max(0,delta)))+max(0,delta)/(n-2)
            assert np.max(np.abs(W-(float(p)*(np.ones((n,n))-np.eye(n))))) <= bound+1e-9
            cases+=1
    print(f'PASS: {cases} full-matrix spectral/feasibility cases, {exact} exact rational identities; trace and stability corroborated')

if __name__=='__main__': check()
