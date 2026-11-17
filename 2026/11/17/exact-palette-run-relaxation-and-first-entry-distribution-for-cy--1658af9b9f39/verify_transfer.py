#!/usr/bin/env python3
"""Exact polynomial matrix transfer and independent support subset census."""
from itertools import combinations
from math import comb,factorial

def mul(a,b,deg):
    out=[0]*(deg+1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:deg-i+1]):
                out[i+j]+=x*y
    return out

def matrix_mul(A,B,deg):
    d=len(A); C=[[[0]*(deg+1) for j in range(d)] for i in range(d)]
    for i in range(d):
        for k in range(d):
            if any(A[i][k]):
                for j in range(d):
                    if any(B[k][j]):
                        t=mul(A[i][k],B[k][j],deg)
                        C[i][j]=[u+v for u,v in zip(C[i][j],t)]
    return C

def transfer(q,r):
    d=r+1
    A=[[[0]*(q+1) for j in range(d)] for i in range(d)]
    for i in range(d):
        A[i][0][0]=1 # append an absent color
        if i<r:A[i][i+1][1]=1 # append an occupied color
    B=[[[int(i==j)]+[0]*q for j in range(d)] for i in range(d)]
    for _ in range(q):B=matrix_mul(B,A,q)
    return [sum(B[i][i][k] for i in range(d)) for k in range(q+1)]

def surj(n,k):
    return sum((-1)**j * comb(k,j)*(k-j)**n for j in range(k+1))

def subset_count(q,r):
    tally=[0]*(q+1)
    for mask in range(1<<q):
        s={i for i in range(q) if mask>>i&1};k=len(s)
        if k==q:continue
        longest=0
        for c in s:
            if (c-1)%q not in s:
                t=0
                while (c+t)%q in s:t+=1
                longest=max(longest,t)
        if longest<=r:tally[k]+=1
    return tally

cases=0
for q in range(4,10):
    for r in range(1,q):
        tr=transfer(q,r)
        sub=subset_count(q,r)
        assert tr==sub,(q,r,tr,sub)
        for n in range(2,10):
            total=sum(tr[k]*surj(n,k) for k in range(1,q))
            if r==q-1:assert total+surj(n,q)==q**n,(q,r,n)
            if r==q-1:
                prev=transfer(q,r-1)
                diff=sum((tr[k]-prev[k])*surj(n,k) for k in range(1,q))
                assert diff==q*surj(n,q-1),(q,n,diff)
        cases+=1
        print(f'q={q} cutoff_run={r} subset_coefficients={tr}')
print(f'PASS transfer comparisons={cases}')
