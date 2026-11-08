"""Supplementary finite tests for positive Fourier tight-frame cardinalities.
The general result follows from a mathematical proof, not this finite test.
Requires numpy and scipy.
"""
from itertools import combinations
from math import gcd
import random
import numpy as np
from scipy.optimize import linprog


def diffset(p, A):
    return {(a-b) % p for a in A for b in A}


def quadrature(p, A):
    D = diffset(p,A)
    rows = [np.ones(p)]
    for d in sorted(D - {0}):
        if (p-d) in D and d > p-d:
            continue
        theta = 2*np.pi*d*np.arange(p)/p
        rows.append(np.cos(theta))
        if d != p-d:
            rows.append(np.sin(theta))
    B=np.vstack(rows)
    assert B.shape[0]==len(D)
    rhs=np.zeros(len(D));rhs[0]=1
    r=linprog(np.zeros(p),A_eq=B,b_eq=rhs,bounds=(0,None),method='highs')
    assert r.success,r.message
    w=r.x
    S=np.where(w>1e-7)[0]
    assert len(S)==len(D),(p,A,len(S),len(D),w)
    assert w[S].min()>1e-7
    assert np.max(np.abs(B@w-rhs))<2e-8
    V=np.exp(2j*np.pi*np.outer(np.array(A),np.arange(p))/p)
    G=(V*w[None,:])@V.conj().T
    assert np.max(np.abs(G-np.eye(len(A))))<2e-8
    return len(S)


def check():
    rng=random.Random(365)
    count=0
    for p in [2,3,5,7,11,13,17,19]:
        families=[]
        if p<=7:
            families=[C for n in range(1,p+1) for C in combinations(range(p),n)]
        else:
            families=[tuple(range(k)) for k in range(1,p+1)]
            for k in range(2,p):
                for _ in range(4):
                    families.append(tuple(sorted(rng.sample(range(p),k))))
        for A in families:
            quadrature(p,A)
            count+=1
        for k in range(1,p+1):
            Ap=tuple(range(k))
            assert len(diffset(p,Ap))==min(p,2*k-1)
    print('CHECK_OK prime_sizes=[2,3,5,7,11,13,17,19] configurations=',count)

if __name__=='__main__':check()
