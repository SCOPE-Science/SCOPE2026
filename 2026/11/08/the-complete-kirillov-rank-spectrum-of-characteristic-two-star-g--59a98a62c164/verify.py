#!/usr/bin/env python3
"""Exact finite characteristic-two Kirillov-rank checks for three-step star Lie algebras."""
from collections import Counter
from itertools import combinations,product
from math import prod

def gf_mul(a,b,q):
    if q==2: return a & b
    assert q==4
    v=0
    while b:
        if b&1:v^=a
        a<<=1
        if a&4:a^=7
        b>>=1
    return v

def gf_inv(a,q):
    return next(b for b in range(1,q) if gf_mul(a,b,q)==1)

def rank(rows,q):
    a=[list(row) for row in rows];n=len(a);m=len(a[0]) if n else 0;i=0
    for c in range(m):
        k=next((j for j in range(i,n) if a[j][c]),None)
        if k is None: continue
        a[k],a[i]=a[i],a[k]
        inv=gf_inv(a[i][c],q)
        a[i]=[gf_mul(v,inv,q) for v in a[i]]
        for j in range(n):
            if j!=i and a[j][c]:
                t=a[j][c];a[j]=[v^gf_mul(t,w,q) for v,w in zip(a[j],a[i])]
        i+=1
        if i==n:break
    return i

def gaussian(n,k,q):
    if k<0 or k>n:return 0
    v=1
    for i in range(k):
        v=v*(q**(n-i)-1)//(q**(k-i)-1) if False else v
    a=prod(q**(n-i)-1 for i in range(k))
    b=prod(q**(k-i)-1 for i in range(k))
    return a//b

def predicted(m,q):
    # Distribution of ranks of the full alternating Kirillov matrix, including free dual coordinates.
    n=1+2*m+m*(m-1)//2
    d=Counter()
    for k in range(m//2+1):
        h=gaussian(m,2*k,q)*q**(k*(k-1))*prod(q**(2*i-1)-1 for i in range(1,k+1))
        d[4*k]+=q**(m+1)*h*q**(2*k)
        if 2*k<m:d[4*k+2]+=q**(m+1)*h*(q**m-q**(2*k))
    assert sum(d.values())==q**n,(m,q,d,n)
    return dict(sorted(d.items()))

def matrix(m,q,alpha,beta,full=False):
    pairs=list(combinations(range(m),2))
    B=[[0]*m for _ in range(m)]
    for (i,j),v in zip(pairs,beta):B[i][j]=v;B[j][i]=v
    C=[[alpha[i]]+B[i] for i in range(m)]
    if not full:return C
    # Order of basis: c,x_1,...,x_m,a_1,...,a_m, then central z_ij.
    d=1+2*m+len(pairs);K=[[0]*d for _ in range(d)]
    for i in range(m):
        K[0][1+i]=alpha[i];K[1+i][0]=alpha[i]
        for j in range(m):
            K[1+i][1+m+j]=B[i][j];K[1+m+j][1+i]=B[i][j]
    return K

def direct(m,q):
    size=m+m*(m-1)//2
    totals=Counter();full_cases=0
    for coeff in product(range(q),repeat=size):
        alpha=coeff[:m];beta=coeff[m:]
        r=rank(matrix(m,q,alpha,beta),q)
        totals[2*r]+=1
        if (m<=3) or (full_cases<300 and sum(coeff)%7==0):
            assert rank(matrix(m,q,alpha,beta,True),q)==2*r,(m,q,coeff)
            full_cases+=1
    free=q**(m+1)
    got={r:v*free for r,v in sorted(totals.items())}
    expected=predicted(m,q)
    assert got==expected,(m,q,got,expected)
    return got,full_cases,q**size

if __name__=='__main__':
    for m,q in [(2,2),(2,4),(3,2),(3,4),(4,2),(5,2)]:
        counts,full,parameters=direct(m,q)
        print(f'm={m} q={q} parameter_assignments={parameters} full_matrix_checks={full} spectrum={counts}')
    print('VERIFY_OK exhaustive_configurations=6')
