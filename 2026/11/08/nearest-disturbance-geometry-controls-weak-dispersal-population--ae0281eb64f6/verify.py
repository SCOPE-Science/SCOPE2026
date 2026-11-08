#!/usr/bin/env python3
"""Exact formal Lyapunov-series checks for localized spatial forcing.
Requires only the Python 3 standard library. The analytic all-graph proof
is in RESULT.md; these are finite, exact regression checks.
"""
from fractions import Fraction as F
from math import factorial
from collections import deque

def matmul(a,b):
    n=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def add(a,b):
    return [[a[i][j]+b[i][j] for j in range(len(a))] for i in range(len(a))]

def laplacian(n,edges):
    L=[[F(0) for _ in range(n)] for _ in range(n)]
    W=[[F(0) for _ in range(n)] for _ in range(n)]
    for u,v,w in edges:
        w=F(w)
        assert u!=v and w>0 and W[u][v]==0
        W[u][v]=W[v][u]=w
        L[u][u]+=w;L[v][v]+=w
        L[u][v]-=w;L[v][u]-=w
    return L,W

def lengths_weights(W,source):
    n=len(W);d=[None]*n;P=[F(0)]*n
    d[source]=0;P[source]=F(1); todo=deque([source])
    while todo:
        u=todo.popleft()
        for v in range(n):
            if W[u][v]==0:continue
            if d[v] is None:
                d[v]=d[u]+1;todo.append(v)
            if d[v]==d[u]+1:P[v]+=P[u]*W[u][v]
    assert all(z is not None for z in d)
    return d,P

def leading(L,W,noise,lam):
    n=len(L)
    geometry={s:lengths_weights(W,s) for s in noise}
    r=[min(geometry[s][0][i] for s in noise) for i in range(n)]
    near=[{s for s in noise if geometry[s][0][i]==r[i]} for i in range(n)]
    # Exact first nonzero coefficient of every covariance entry.
    v=[]; c={}; order={}
    for i in range(n):
        z=r[i]
        a=sum(noise[s]*geometry[s][1][i]**2 for s in near[i])
        v.append(F(factorial(2*z),factorial(z)**2)*a/(2*lam)**(2*z+1))
    for i in range(n):
        for j in range(n):
            m=min(geometry[s][0][i]+geometry[s][0][j] for s in noise)
            z=F(0)
            for s in noise:
                di=geometry[s][0][i];dj=geometry[s][0][j]
                if di+dj==m:
                    z+=noise[s]*geometry[s][1][i]*geometry[s][1][j]*F(factorial(m),factorial(di)*factorial(dj))
            order[i,j]=m
            c[i,j]=z/(2*lam)**(m+1)
    return r,near,v,c,order

def formal(L,noise,lam,K):
    n=len(L)
    C=[[[F(0) for _ in range(n)] for _ in range(n)] for _ in range(K+1)]
    for s,z in noise.items():C[0][s][s]=z/(2*lam)
    for k in range(1,K+1):
        D=add(matmul(L,C[k-1]),matmul(C[k-1],L))
        C[k]=[[-D[i][j]/(2*lam) for j in range(n)] for i in range(n)]
    return C

examples=[
 ('path3_single',3,[(0,1,1),(1,2,1)],{0:F(1)},F(1)),
 ('diamond_multi',4,[(0,1,2),(0,2,1),(1,3,3),(2,3,5)],{0:F(2),3:F(3)},F(2)),
 ('path5_multi',5,[(0,1,2),(1,2,3),(2,3,1),(3,4,2)],{0:F(1),4:F(5)},F(1)),
 ('two_shortest_paths',5,[(0,1,1),(0,2,2),(1,3,3),(2,3,1),(3,4,4)],{0:F(7)},F(3)),
]
checks=0; zero_pairs=0;positive_pairs=0
for label,n,edges,noise,lam in examples:
    L,W=laplacian(n,edges)
    r,near,V,C,order=leading(L,W,noise,lam)
    K=max(order.values())
    coeffs=formal(L,noise,lam,K)
    for i in range(n):
        assert V[i]>0
        assert all(coeffs[k][i][i]==0 for k in range(2*r[i]))
        assert coeffs[2*r[i]][i][i]==V[i],(label,i,coeffs[2*r[i]][i][i],V[i])
        checks+=1
        for j in range(i+1,n):
            target=order[i,j]
            assert target >=r[i]+r[j]
            assert (target==r[i]+r[j]) == bool(near[i].intersection(near[j]))
            assert all(coeffs[k][i][j]==0 for k in range(target))
            assert C[i,j]>0
            assert coeffs[target][i][j]==C[i,j],(label,i,j,coeffs[target][i][j],C[i,j])
            checks+=1
            if near[i].isdisjoint(near[j]):zero_pairs+=1
            else:positive_pairs+=1
    if label=='path3_single':
        assert r==[0,1,2]
        # Corr(1,2)=6/sqrt(2!4!)=sqrt(3)/2.
        assert C[1,2]**2*4==3*V[1]*V[2]
        assert C[0,1]**2*2==V[0]*V[1]
        assert C[0,2]**2*6==V[0]*V[2]
    print(label,'vertices',n,'source_count',len(noise),'formal_checks',n*(n+1)//2)
assert zero_pairs>0 and positive_pairs>0
print('PASS exact formal-coefficient checks:',checks,
      'pairs shared nearest source:',positive_pairs,
      'pairs no shared nearest source:',zero_pairs)
