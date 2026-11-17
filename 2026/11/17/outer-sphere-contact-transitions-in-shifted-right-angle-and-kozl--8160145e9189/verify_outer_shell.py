#!/usr/bin/env python3
"""Exact finite checks of right-angle Minkowski-sum Euclidean outer spheres.

Run: python3 verify_outer_shell.py. Uses only the Python standard library.
No finite enumeration is used as a substitute for the general proof.
"""
from itertools import combinations_with_replacement, product
from math import comb

checks = 0
cases = 0

def require(pred, explanation):
    global checks
    checks += 1
    if not pred:
        raise AssertionError(explanation)

def binom(n,k):
    return comb(n,k) if 0<=k<=n else 0

def v(a,k,d,size):
    x=[0]*size
    for j in range(1,k+1): x[d+j]=a[j-1]
    return x

def total(a,ks,ds):
    size=max(ds)+len(a)+1
    return tuple(sum(v(a,k,d,size)[j] for k,d in zip(ks,ds)) for j in range(size))

def norm2(x,y):
    return sum((u-w)**2 for u,w in zip(x,y))

def sphere_norm4(x,L,U):
    return sum((2*t-l-u)**2 for t,l,u in zip(x,L,U))

def blocks(n, ds):
    out=[]
    for d in sorted(ds):
        p,q=d+2,d+n
        if out and p<=out[-1][1]:
            out[-1]=(out[-1][0],max(q,out[-1][1]))
        else: out.append((p,q))
    return out

def verify(a,ds):
    global cases
    n=len(a); r=len(ds)
    L=total(a,(1,)*r,ds); U=total(a,(n,)*r,ds)
    D2=norm2(L,U)
    pts=sorted({total(a,ks,ds) for ks in product(range(1,n+1),repeat=r)})
    bl=blocks(n,ds)
    predicted_contacts=1
    for lo,hi in bl: predicted_contacts*=hi-lo+2
    contacts=sum(sphere_norm4(x,L,U)==D2 for x in pts)
    require(contacts==predicted_contacts,(a,ds,'contacts',contacts,predicted_contacts))
    require(all(sphere_norm4(x,L,U)<=D2 for x in pts),(a,ds,'containment'))
    pairs=0; farthest=0
    for i,x in enumerate(pts):
        for y in pts[i+1:]:
            d=norm2(x,y)
            farthest=max(farthest,d)
            pairs+=(d==D2)
    require(farthest==D2,(a,ds,'diameter'))
    require(pairs==2**(len(bl)-1),(a,ds,'diametral pairs',pairs,len(bl)))
    require(all(L[j]<=x[j]<=U[j] for x in pts for j in range(len(L))),(a,ds,'box'))
    predicted_D2=sum((sum(a[j-d-1] for d in ds if 2<=j-d<=n))**2
                     for j in range(max(ds)+n+1))
    require(D2==predicted_D2,(a,ds,'diameter formula'))
    if all(a[j-1]==comb(n,j) for j in range(1,n+1)):
        corr=lambda h: binom(2*n,n+h)-binom(n,h)-n*binom(n,h+1)
        require(D2==sum(corr(abs(p-q)) for p in ds for q in ds),(a,ds,'binomial autocorrelation'))
    cases+=1

if __name__=='__main__':
    for n in range(2,7):
        legs=[tuple(comb(n,j) for j in range(1,n+1)),
              tuple(j*j+1 for j in range(1,n+1)),
              tuple(n+2-j for j in range(1,n+1))]
        for r in (1,2,3):
            for ds in combinations_with_replacement(range(6),r):
                for a in legs: verify(a,ds)
    for n in range(2,80):
        w=[comb(n,j) for j in range(2,n+1)]
        for h in range(n+3):
            direct=sum(w[j]*w[j+h] for j in range(len(w)-h)) if h<len(w) else 0
            formula=binom(2*n,n+h)-binom(n,h)-n*binom(n,h+1)
            require(direct==formula,(n,h,'correlation identity'))
    print('PASS: %d exact instances and %d assertions'%(cases,checks))
