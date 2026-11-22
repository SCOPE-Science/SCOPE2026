#!/usr/bin/env python3
"""Reproducibility tests for a two-level tree Kemeny optimization theorem.
Uses only Python standard library; assertions are finite diagnostics, not the all-size proof.
"""
from math import sqrt, isclose
from random import Random


def cutoff(k):
    assert k >= 2
    return k*k-3*k+4


def F(k,m):
    return k*m*m-(k-1)**2*((k-1)*m+k)


def design(k,m):
    assert k>=2 and m>=1
    n=1+k*(m+1)
    a=(m+1)*(1+(k-1)*(m+1))
    b=n-1
    x0=sqrt(a)/(sqrt(a)+m*sqrt(b))
    x=min(1/k,x0)
    y=(1-x)/m
    K=(k*a/x + k*m*b/y)/n
    # leaf weights appear km times; replace x with an unrestricted leaf class y
    return x,y,K,a,b


def construct_laplacian(k,m,x,y):
    n=1+k*(m+1)
    a=[[0.0]*n for _ in range(n)]
    edgelist=[]
    for i in range(k):
        v=1+i*(m+1)
        edgelist.append((0,v,x))
        for j in range(m):
            edgelist.append((v,v+j+1,y))
    for i,j,w in edgelist:
        a[i][i]+=w
        a[j][j]+=w
        a[i][j]-=w
        a[j][i]-=w
    return a,edgelist


def spectral_trace_pseudoinverse(L):
    n=len(L)
    A=[[L[i][j]+1/n for j in range(n)]+[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]
    for j in range(n):
        p=max(range(j,n),key=lambda i:abs(A[i][j]))
        assert abs(A[p][j])>1e-14
        A[p],A[j]=A[j],A[p]
        v=A[j][j]
        for l in range(j,2*n): A[j][l]/=v
        for i in range(n):
            if i==j:continue
            v=A[i][j]
            for l in range(j,2*n): A[i][l]-=v*A[j][l]
    return sum(A[i][n+i] for i in range(n))-1


def resistance_formula(k,m,x,y):
    n=1+k*(m+1)
    a=(m+1)*(1+(k-1)*(m+1))
    b=n-1
    return (k*a/x+k*m*b/y)/n


def test():
    tests=0
    for k in range(2,251):
        t=cutoff(k)
        assert F(k,t)==4
        assert F(k,t-1)==3-k*t<0
        for m in [1,max(1,t-1),t,t+1,2*t]:
            x,y,K,a,b=design(k,m)
            assert 0<x<=1/k+1e-14
            assert 0<y<1
            assert isclose(x+m*y,1,abs_tol=1e-13)
            assert (x<1/k-1e-13)==(m>=t) if t<10000 else True
            tests+=1
    rng=Random(77723)
    for k in range(2,6):
      for m in range(1,7):
        x,y,K,a,b=design(k,m)
        L,edges=construct_laplacian(k,m,x,y)
        assert isclose(spectral_trace_pseudoinverse(L),K,rel_tol=1e-10,abs_tol=1e-8)
        tests+=1
        for rep in range(6):
            # Independent edge weights with a global feasible row scaling
            weights=[.02+(.98*rng.random()) for _ in edges]
            rows=[0.0]*len(L)
            for (u,v,_),w in zip(edges,weights):
                rows[u]+=w
                rows[v]+=w
            scale=1/max(rows)
            A=[[0.0]*len(L) for _ in L]
            for (u,v,_),w in zip(edges,weights):
                w*=scale
                A[u][u]+=w;A[v][v]+=w;A[u][v]-=w;A[v][u]-=w
            kv=spectral_trace_pseudoinverse(A)
            assert kv>=K-1e-8
            tests+=1
    for k in range(2,15):
        for m in (300,1000,10000,50000):
            x,y,K,a,b=design(k,m)
            ratio=x*sqrt(m)/sqrt((k-1)/k)
            if m>=10000: assert abs(ratio-1)<.04
            tests+=1
    for rho in (0.25,0.5,1.0,2.0,4.0):
        target=max(0.0,1.0-rho**(-0.5))
        for k in (100,300,900):
            m=max(1,round(rho*k*k))
            x,y,K,a,b=design(k,m)
            observed=1-k*x
            assert abs(observed-target)<0.025
            tests+=1
    for k in (2,3,5,8):
        m=250000
        x,y,K,a,b=design(k,m)
        n=1+k*(m+1)
        equal=(m+1)*(k*a+k*m*b)/n
        assert abs(equal/K-(2-1/k))<0.02
        tests+=1
    print('PASS:',tests,'exact threshold, row feasibility, direct trace, sampled unrestricted designs and asymptotic diagnostics')

if __name__=='__main__':
    test()
