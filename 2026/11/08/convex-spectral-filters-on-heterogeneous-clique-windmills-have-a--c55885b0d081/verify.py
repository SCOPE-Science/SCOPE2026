#!/usr/bin/env python3
"""Exact-rational checks of convex-filter identities on clique-block stars."""
from fractions import Fraction as F
from math import factorial
from itertools import product

def compositions(n):
    if n == 0:
        yield ()
    else:
        for k in range(1, n+1):
            for rest in compositions(n-k):
                yield (k,)+rest

def graph(parts):
    N=sum(parts); n=N+1
    L=[[F(0) for _ in range(n)] for _ in range(n)]
    for v in range(1,n):
        L[0][0]+=1;L[v][v]+=1
        L[0][v]-=1;L[v][0]-=1
    begin=1
    for p in parts:
        for i in range(begin,begin+p):
            for j in range(i+1,begin+p):
                L[i][i]+=1;L[j][j]+=1;L[i][j]-=1;L[j][i]-=1
        begin+=p
    return L

def multiply(A,B):
    n=len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(n)),F(0)) for j in range(n)] for i in range(n)]

def approx(L,p,h):
    n=len(L);P=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    S=[[x for x in row] for row in P]
    for k in range(1,p+1):
        P=multiply(P,L)
        coef=(-h)**k/F(factorial(k))
        for i in range(n):
            for j in range(n):S[i][j]+=coef*P[i][j]
    return S

def f(p,x):return sum(((-x)**k/F(factorial(k)) for k in range(p+1)),F(0))

def formula(parts,p,h):
    n=1+sum(parts);N=n-1
    a=f(p,h);c=f(p,n*h)
    E=(1-c)/n;d=(N+c-n*a)/F(n*N)
    T=[[F(0) for _ in range(n)] for _ in range(n)]
    T[0][0]=(1+N*c)/n
    for j in range(1,n):T[0][j]=T[j][0]=E
    v=1
    for part in parts:
        b=f(p,(part+1)*h)
        z=d+(a-b)/part
        for u in range(v,v+part):
            T[u][u]=z+b
            for w in range(1,n):
                if w!=u:T[u][w]=z if v<=w<v+part else d
        v+=part
    return T

def verify():
    items=0;entries=0;ineq=0
    for N in range(1,8):
        for parts in compositions(N):
            n=N+1;L=graph(parts)
            for p in (2,4,6,8):
                for x in (F(1,2),F(1),F(2),F(5,2),F(3),F(4),F(6)):
                    h=x/n
                    actual=approx(L,p,h);expected=formula(parts,p,h)
                    target=(f(p,x)<=1)
                    for i in range(n):
                        assert sum(actual[i])==1, ('row-sum',parts,p,x,i)
                        for j in range(n):
                            assert actual[i][j]==expected[i][j], ('formula',parts,p,x,i,j)
                            if target: assert actual[i][j]>=0, ('positivity',parts,p,x,i,j)
                            entries+=1
                    assert (min(min(row) for row in actual)>=0)==target, ('iff',parts,p,x)
                    items+=1;ineq+=1
    print('PASS: exact full-matrix instances',items,'entry identities',entries,'iff-threshold cases',ineq)
if __name__=='__main__':verify()
