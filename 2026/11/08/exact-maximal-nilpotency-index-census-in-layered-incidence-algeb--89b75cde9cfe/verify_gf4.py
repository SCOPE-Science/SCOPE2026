#!/usr/bin/env python3
"""Finite-field extension checks in GF(4)=GF(2)[t]/(t^2+t+1)."""
from itertools import product
from collections import Counter

Q=4

def add(a,b):return a^b

def mul(a,b):
    v=0
    for i in range(2):
        if (b>>i)&1:v^=a<<i
    if v&8:v^=0b1100  # t^3=t^2+t
    if v&4:v^=0b111   # t^2=t+1
    return v

def inv(a):
    if not a:raise ZeroDivisionError
    return next(b for b in (1,2,3) if mul(a,b)==1)

def rank(a):
    a=[row[:] for row in a]
    piv=0;ncol=len(a[0])
    for col in range(ncol):
        row=next((j for j in range(piv,len(a)) if a[j][col]),None)
        if row is None:continue
        a[row],a[piv]=a[piv],a[row]
        v=inv(a[piv][col]);a[piv]=[mul(v,x) for x in a[piv]]
        for j in range(len(a)):
            if j!=piv and a[j][col]:
                f=a[j][col]
                a[j]=[add(u,mul(f,w)) for u,w in zip(a[j],a[piv])]
        piv+=1
        if piv==len(a):break
    return piv

def mulmat(a,b):
    return [[__import__('functools').reduce(add,(mul(x,y) for x,y in zip(row,col)),0) for col in zip(*b)] for row in a]

def predict(ws):
    ranks={ws[0]:1}
    def choose(n,k):
        from math import prod
        return prod(4**(n-i)-1 for i in range(k))//prod(4**(k-i)-1 for i in range(k))
    for olddim,newdim in zip(ws[:-1],ws[1:]):
        nxt=Counter()
        for r,num in ranks.items():
            for s in range(min(r,newdim)+1):
                ways=choose(r,s)
                for j in range(s):ways*=4**newdim-4**j
                nxt[s]+=num*ways*4**((olddim-r)*newdim)
        ranks=dict(nxt)
    return ranks

def direct(ws,full):
    offsets=[sum(ws[:i]) for i in range(len(ws))]
    edges=[(offsets[i]+a,offsets[j]+b) for i in range(len(ws)) for j in range(i+1,len(ws)) if full or j==i+1 for a in range(ws[i]) for b in range(ws[j])]
    N=sum(ws); h=len(ws)
    hist=Counter()
    for vals in product(range(4),repeat=len(edges)):
        A=[[0]*N for _ in range(N)]
        for (i,j),v in zip(edges,vals):A[i][j]=v
        power=A
        for i in range(h-2):power=mulmat(power,A)
        hist[rank(power)]+=1
    far=sum(ws[i]*ws[j] for i in range(len(ws)) for j in range(i+2,len(ws))) if full else 0
    expected={i:cnt*4**far for i,cnt in predict(ws).items()}
    assert dict(hist)==expected,(ws,full,hist,expected)
    print('GF4',ws,'full',full,'total',4**len(edges),'ranks',dict(sorted(hist.items())))

if __name__=='__main__':
    for w,f in [((1,2,1),True),((2,1,2),True),((2,2,2),False)]:direct(w,f)
    print('LAYERED_INCIDENCE_GF4_EXTENSION_PASS')
