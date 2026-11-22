#!/usr/bin/env python3
"""Coefficient check by independently grouping run-parameter families (not string matching)."""
from collections import Counter,defaultdict
from math import comb

def grouped(n):
    out=Counter()
    for b in range(1,(n-2)+1):
        for a in range(b+1):
            c=n-2-b-a
            if 0<=c<=b:
                q=2+int(a==b)+int(c==b)
                out[(b+1,q)]+=1
    for m in range(1,n-1):
        for b in range(m):
            r=n-2-m-b
            if r<0 or r>m: continue
            if r<m: out[(m+b+2,1)]+=2
            else: out[(m+b+2,2)]+=1
    if n==2:out[(1,2)]+=1
    return out

def direct_param(n):
    d=Counter()
    for a in range(n-1):
        for b in range(n-1-a):
            c=n-2-a-b;m=max(a,c)
            if m>b:
                d[(b+m+2,2 if a==c else 1)]+=1
            elif b==0:
                d[(1,2)]+=1
            else:
                d[(b+1,2+int(a==b)+int(c==b))]+=1
    return d

def q_only_closed(n):
    # independent rational-function coefficients, from 1/(1-z^j) geometric sums.
    A=0; B=0; D=int(n>=5 and (n-5)%3==0)
    for j in range(1,n-1):
        # A: b>=1, 0<=a,c<b
        x=n-2-j
        if x>=0:
            A+=max(0,min(j-1,x)-max(0,x-j+1)+1)
        # B: m>=1, b in [0,m-1], 2m+b+2=n
        b=n-2-2*j
        B+=int(0<=b<j)
    return {1:2*A,2:A+B+int(n==2),3:2*B,4:D}

for n in range(2,181):
    d=grouped(n)
    p=direct_param(n)
    assert d==p,(n,d-p,p-d)
    totals={k:sum(v for (L,q),v in d.items() if q==k) for k in (1,2,3,4)}
    q=q_only_closed(n)
    assert totals==q,(n,totals,q)
    assert sum(totals.values())==comb(n,2)
    if n in (2,5,10,20,100,180): print('n=',n,'counts=',totals)
print('PASS: independent run-family joint coefficients, 179 lengths, n=2..180')
