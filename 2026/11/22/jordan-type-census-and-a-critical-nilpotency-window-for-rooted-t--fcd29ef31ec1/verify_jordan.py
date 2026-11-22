#!/usr/bin/env python3
"""Exact Jordan-type census of rooted-tree adjacency operators via weighted DP."""
from collections import Counter
from itertools import product
from math import prod


def tree(b,h):
    levels=[[0]]; edges=[]; next_id=1
    for _ in range(h):
        curr=[]
        for u in levels[-1]:
            for _ in range(b):
                v=next_id;next_id+=1
                edges.append((u,v));curr.append(v)
        levels.append(curr)
    return next_id,edges,levels


def add(A,B,c=1):
    d=Counter(A)
    for k,v in B.items(): d[k]+=c*v
    return {k:v for k,v in d.items() if v}


def times(A,B):
    d=Counter()
    for x,a in A.items():
        for y,b in B.items(): d[tuple(i+j for i,j in zip(x,y))]+=a*b
    return dict(d)


def poly_pow(A,b):
    z={(0,)*len(next(iter(A))):1}
    for _ in range(b):z=times(z,A)
    return z


def census(b,h,q):
    H=[{(1,):1}]
    for height in range(1,h+1):
        prev=[{key+(0,):num for key,num in P.items()} for P in H]
        A={}
        for P in prev: A=add(A,P)
        Wprev={}
        out=[]
        B={}
        for ell in range(height+1):
            if ell>0:B=add(B,prev[ell-1],q-1)
            W=poly_pow(add(A,B),b)
            P=add(W,Wprev,-1)
            shift=[0]*(height+1);shift[ell]=1
            P={tuple(k+d for k,d in zip(v,shift)):num for v,num in P.items()}
            out.append(P);Wprev=W
        H=out
    return H


def jordan_from_rootlengths(lens):
    h=len(lens)-1
    ranks=[sum(lens)] + [sum(lens[k:]) for k in range(1,h+1)]+[0,0]
    return tuple(ranks[k-1]-2*ranks[k]+ranks[k+1] for k in range(1,h+2))


def check(b,h,q):
    n,edges,levels=tree(b,h)
    P={}
    for poly in census(b,h,q): P=add(P,poly)
    direct=Counter()
    jdirect=Counter()
    for values in product(range(q),repeat=len(edges)):
        kids=[[] for _ in range(n)]
        for (u,v),value in zip(edges,values):kids[u].append((v,value))
        rootlen=[0]*n
        for v in range(n-1,-1,-1):
            rootlen[v]=max([1+rootlen[w] for w,a in kids[v] if a]+[0])
        hist=tuple(rootlen.count(k) for k in range(h+1))
        direct[hist]+=1
        jdirect[jordan_from_rootlengths(hist)]+=1
    assert dict(direct)==P,(b,h,q,direct,P)
    jordan=Counter()
    for profile,v in P.items():jordan[jordan_from_rootlengths(profile)]+=v
    assert jordan==jdirect
    assert sum(jordan.values())==q**len(edges)
    print('PASS jordan census b=%s h=%s q=%s assignments=%s jordan_types=%s ranks=%s'%(b,h,q,q**len(edges),len(jordan),jordan))

for case in [(2,1,2),(2,2,2),(2,2,3),(2,3,2),(3,2,2)]:check(*case)
