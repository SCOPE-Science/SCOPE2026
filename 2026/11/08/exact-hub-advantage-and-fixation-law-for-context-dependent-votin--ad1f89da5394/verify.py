#!/usr/bin/env python3
"""Independent exact-arithmetic checks for context-dependent adoption on stars.
This file is a reproducibility aid; the theorem has a separate analytic proof.
"""
from fractions import Fraction as F
from itertools import product


def closed(m, r, hub, leaves):
    r = F(r)
    q = (m*r + 1)/(r*(m+r))
    d = 1/(q**m+(r/m)*sum((q**j for j in range(1,m+1)),F(0)))
    f = (r/m)*sum((q**j for j in range(1,leaves+1)),F(0))*d
    return f+(q**leaves)*d if hub else f


def solve(A,b):
    n=len(b)
    for j in range(n):
        pivot=next(k for k in range(j,n) if A[k][j]);A[j],A[pivot]=A[pivot],A[j];b[j],b[pivot]=b[pivot],b[j]
        c=A[j][j]
        for z in range(j,n):A[j][z]/=c
        b[j]/=c
        for i in range(n):
            if i==j:continue
            c=A[i][j]
            if c:
                for z in range(j,n): A[i][z]-=c*A[j][z]
                b[i]-=c*b[j]
    return b


def brute(m, up, down):
    n=m+1;M=1<<n;allones=M-1
    states=list(range(1,allones));idx={s:i for i,s in enumerate(states)}
    A=[[F(0) for _ in states] for _ in states];b=[F(0) for _ in states]
    for s in states:
        i=idx[s];hub=s&1
        for v in range(n):
            sv=(s>>v)&1
            neigh=list(range(1,n)) if v==0 else [0]
            for j in neigh:
                sj=(s>>j)&1
                if sv==sj:continue
                rate= (up if sj else down)/len(neigh)
                t=s^(1<<v)
                A[i][i]+=rate
                if t==allones:b[i]+=rate
                elif t!=0:A[i][idx[t]]-=rate
    return solve(A,b),states


def run():
    n=0
    for m in range(1,7):
        for up,down in [(F(1,2),F(1,4)),(F(1,3),F(2,3)),(F(1),F(1)),(F(2,5),F(3,7))]:
            r=up/down
            sol,states=brute(m,up,down)
            for s,p in zip(states,sol):
                hub=s&1;leaves=(s>>1).bit_count()
                pred=closed(m,r,hub,leaves)
                assert p==pred, (m,r,s,p,pred)
                n+=1
            for k in range(1,m+1):
                assert closed(m,r,1,k-1)>closed(m,r,0,k) or m==1
                n+=1
            assert closed(m,r,0,0)==0
            assert closed(m,r,1,m)==1
            n+=2
    print('PASS',n,'exact rational checks on full Markov chains and hub-optimal comparisons')

if __name__=='__main__':run()
