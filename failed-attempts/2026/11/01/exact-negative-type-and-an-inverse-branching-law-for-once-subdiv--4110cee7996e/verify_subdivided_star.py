#!/usr/bin/env python3
"""Independent finite arithmetic and spectral tests for once-subdivided metric stars.
All indices are constructed by BFS from the actual graph; analytic sign proofs
are in the accompanying mathematical result, not inferred from these tests.
"""
from fractions import Fraction as F
from collections import deque
from math import log, sqrt
import numpy as np

def graph_distances(q):
    n = 2*q+1
    adj=[[] for _ in range(n)]
    for i in range(q):
        a,b=1+i,1+q+i
        adj[0].append(a); adj[a].append(0)
        adj[a].append(b); adj[b].append(a)
    D=[]
    for start in range(n):
        ds=[-1]*n;ds[start]=0; todo=deque([start])
        while todo:
            i=todo.popleft()
            for j in adj[i]:
                if ds[j]<0: ds[j]=ds[i]+1;todo.append(j)
        assert all(v>=0 for v in ds)
        D.append(ds)
    return D

def direct_quadratic(D,coeff,p):
    return sum(coeff[i]*coeff[j]*D[i][j]**p for i in range(len(D)) for j in range(len(D)))

def decomposition(q,aa,bb,p):
    x=F(2)**p;y=F(3)**p
    u=sum(aa)/q;v=sum(bb)/q
    z=-q*(u+v)
    A=2*q-(q-1)*x
    C=q*(1+x)-1-(q-1)*y
    rad=-q*(A*u*u+2*C*u*v+x*A*v*v)
    fluct=-sum(x*(aa[i]-u)**2+2*(y-1)*(aa[i]-u)*(bb[i]-v)+x*x*(bb[i]-v)**2 for i in range(q))
    return z,rad+fluct

# exact rational p=1,2,3 for arbitrary test states: independent pairwise sums
for q in range(2,9):
    D=graph_distances(q)
    for k in range(12):
        aa=[F((2*i+3*k)%11-5, (i%3)+1) for i in range(q)]
        bb=[F((5*i+7*k)%13-6, (i%4)+1) for i in range(q)]
        for p in (1,2,3):
            z,Q=decomposition(q,aa,bb,p)
            coeff=[z]+aa+bb
            assert sum(coeff)==0
            assert direct_quadratic(D,coeff,p)==Q, (q,k,p)
print('EXACT_DECOMPOSITION_OK q=2..8 states=12 exponents=1,2,3')

def f(q,p):
    return q*(1+2**(p/2))**2-1-(q-1)*(3**p+2**(3*p/2))
def bisect(q):
    a,b=1.0,2.0
    assert f(q,a)>0
    assert f(q,b)<0 or abs(f(q,b))<1e-10
    for _ in range(90):
        c=(a+b)/2
        if f(q,c)>0:a=c
        else:b=c
    return (a+b)/2

def inertia(q,p):
    d=np.array(graph_distances(q),float)
    n=len(d);J=np.eye(n)-np.ones((n,n))/n
    B=-(J@(d**p)@J)/2
    eig=np.linalg.eigvalsh(B)
    thr=2e-9
    return (int(np.sum(eig>thr)),int(np.sum(abs(eig)<=thr)),int(np.sum(eig<-thr))),eig

for q in range(3,17):
    root=bisect(q)
    assert 1<root<log(2*q/(q-1),2)
    assert inertia(q,1)[0]==(2*q,1,0)
    assert inertia(q,root)[0]==(2*q-1,2,0), (q,root,inertia(q,root)[0])
    assert inertia(q,(root+min(2,root+0.1))/2)[0][-1]==1
    print(f'INERTIA_OK arms={q} threshold={root:.12f} rank_endpoint={2*q-1}')
assert abs(bisect(2)-2)<1e-9
for q in (20,50,100,500,1000):
    root=bisect(q)
    print('ASYMPTOTIC_DIAGNOSTIC q=',q,'q*(root-1)=',round(q*(root-1),12))
print('ALL_ONCE_SUBDIVIDED_STAR_TESTS_OK')
