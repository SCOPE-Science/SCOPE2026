#!/usr/bin/env python3
"""Independent finite checks for idempotent homomorphisms of Heisenberg Lie algebras."""
from itertools import product
from collections import Counter

def rank(cols,n):
    pivot={}
    for c in cols:
        v=c
        while v:
            p=v.bit_length()-1
            if p in pivot: v^=pivot[p]
            else: pivot[p]=v; break
    return len(pivot)

def dot(a,b):return (a&b).bit_count()%2

def symp(a,b,m):
    # indices first m x_i, last m y_i
    low=(1<<m)-1
    return dot(a&low,b>>m)^dot(a>>m,b&low)

def mul(A,v):
    x=0
    for i,a in enumerate(A):
        if v>>i&1:x^=a
    return x

def classify(m):
    n=2*m
    tbl=Counter()
    projs=set()
    for C in product(range(1<<n),repeat=n):
        if any(mul(C,c)!=c for c in C):continue
        if any(symp(C[i],C[j],m) for i in range(n) for j in range(i)):
            continue
        r=rank(C,n)
        # kernel basis by enumeration of vectors; needed rank of restricted symplectic form
        K=[v for v in range(1<<n) if mul(C,v)==0]
        B=[]
        for v in K:
            if rank(B+[v],n)>len(B):B.append(v)
        assert len(B)==n-r
        restrict=[sum(symp(B[i],B[j],m)<<j for j in range(len(B))) for i in range(len(B))]
        t=rank(restrict,len(B))
        assert t%2==0 and t>=2*(m-r)
        s=(t-2*(m-r))//2
        tbl[(r,s)]+=1<<r
        projs.add(C)
    tbl[(n,0)]+=1 # identity, has different central action
    return tbl,projs

def iso_count(m,r,q):
    from fractions import Fraction
    ans=Fraction(1)
    for i in range(r):ans*=Fraction(q**(2*m-i)-q**i,q**r-q**i)
    assert ans.denominator==1
    return int(ans)

def alt_count(r,s,q):
    # enumerate all alternating matrices for r <=2 in this checker
    count=0
    for vals in product(range(q),repeat=r*(r-1)//2):
        A=[[0]*r for _ in range(r)]
        k=0
        for i in range(r):
            for j in range(i+1,r):
                A[i][j]=vals[k];A[j][i]=-vals[k]%q;k+=1
        # rank mod q
        b=[row[:] for row in A]; z=0
        for j in range(r):
            hit=next((i for i in range(z,r) if b[i][j]),None)
            if hit is None:continue
            b[z],b[hit]=b[hit],b[z]
            inv=pow(b[z][j],-1,q)
            b[z]=[(t*inv)%q for t in b[z]]
            for i in range(r):
                if i!=z:
                    a=b[i][j]
                    b[i]=[(b[i][k]-a*b[z][k])%q for k in range(r)]
            z+=1
        if z==2*s:count+=1
    return count

def expected(m,q):
    return {(r,s):iso_count(m,r,q)*q**(r+2*r*(m-r)+r*(r+1)//2)*alt_count(r,s,q) for r in range(m+1) for s in range(r//2+1)} | {(2*m,0):1}

for m in (1,2):
    tbl,projs=classify(m)
    exp=expected(m,2)
    assert tbl==exp,(m,tbl,exp)
    print('F2_H',2*m+1,'direct_idempotent_retraction_by_(r,s)',dict(sorted(tbl.items())))
    print('F2_H',2*m+1,'total',sum(tbl.values()))
print('VERIFY_OK')
