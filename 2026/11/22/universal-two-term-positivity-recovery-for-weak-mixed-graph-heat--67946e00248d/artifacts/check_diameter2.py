#!/usr/bin/env python3
"""Finite numerical sanity checks for mixed heat on diameter-two weighted graphs.
Uses direct matrix exponentials, not used as proof of one-crossing assertions.
"""
import random
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq


def dist2(A):
    n=len(A)
    E=A>0
    E2=(E.astype(int)@E.astype(int))>0
    np.fill_diagonal(E2,True)
    return np.all(E|E2)


def check(A,eta):
    n=len(A)
    L=np.diag(A.sum(axis=1))-A
    Q=L+eta*L@L
    E=A>0
    pair=[(i,j) for i in range(n) for j in range(i+1,n) if not E[i,j]]
    if not pair:return None
    L2=L@L; L3=L2@L
    assert all(L2[i,j]>0 for i,j in pair)
    roots=[]
    for i,j in pair:
        f=lambda u:expm(-eta*u*Q)[i,j]
        a,b=1.1,3.0
        assert f(a)<0 and f(b)>0, (i,j,eta,f(a),f(b))
        u=brentq(f,a,b,xtol=1e-12)
        target=2-(8/3)*L3[i,j]/L2[i,j]*eta
        roots.append((u,target))
        assert abs(u-target)<3e4*eta*eta, (eta,u,target)
    T=eta*max(x[0] for x in roots)
    for u in (0.05,0.5,1.4,3,5,20,100):
        t=eta*u
        S=expm(-t*Q)
        if u<=1.4:assert np.min(S)<-1e-12
        elif u>=3:assert np.min(S)>-1e-11,(eta,u,np.min(S))
        assert abs(S.sum(axis=1)-1).max()<1e-10
    return len(pair), T, roots


def generate():
    rng=random.Random(314159265)
    for n in range(3,10):
        made=0;trials=0
        while made<16 and trials<100000:
            trials+=1
            A=np.zeros((n,n))
            for i in range(n):
              for j in range(i+1,n):
                if rng.random()<.7:
                    A[i,j]=A[j,i]=rng.choice([.5,1.,1.5,2.5,4.])
            if np.count_nonzero(A)==n*(n-1):continue
            if not dist2(A):continue
            made+=1
            yield A

def exact_integer_example():
    edges=[(0,1),(0,4),(0,5),(1,2),(2,3),(3,4),(3,5)]
    A=np.zeros((6,6),dtype=int)
    for i,j in edges:A[i,j]=A[j,i]=1
    L=np.diag(A.sum(axis=1))-A
    L2=L@L;L3=L2@L
    expected={(0,2):(1,5),(0,3):(2,15),(1,3):(1,5),(1,4):(1,6),
              (1,5):(1,6),(2,4):(1,6),(2,5):(1,6),(4,5):(2,14)}
    assert all((int(L2[i,j]),int(L3[i,j]))==v for (i,j),v in expected.items())
    assert dist2(A)
    assert min(L3[i,j]/L2[i,j] for i,j in expected)==5
    print('integer example: 8 exact nonedge matrix-product comparisons')

if __name__=='__main__':
    exact_integer_example()
    graphs=list(generate())
    cnt=0;nonedges=0
    for A in graphs:
      for eta in (.0005,.001,.002):
        k,_,_=check(A,eta)
        cnt+=1;nonedges+=k
    print('weighted diameter-two graph/time checks:',cnt)
    print('nonedge root checks:',nonedges)
    # Three explicitly different graph families with weighted edges.
    for n in (5,7):
      A=np.zeros((n,n))
      for i in range(n):A[0,i]=A[i,0]=1
      A[0,0]=0
      print('star',n,check(A,.001)[1])
