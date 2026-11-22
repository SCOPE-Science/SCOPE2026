#!/usr/bin/env python3
"""Finite independent certificate for intrinsic-volume forest decomposition.
Reconstruct all edge subsets and their connected components, then compare
with closed expressions; no external files or dependencies.
"""
from itertools import combinations
from math import comb, factorial, sqrt, isclose

def exact_formula(q):
    D=[0.]*(q+2)
    C=[0.]*(q+2)
    for a in range(q+1):
        for b in range(q+1-a):
            k=a+b
            D[k]+=factorial(q)/factorial(a)/factorial(b)/factorial(q-k)*sqrt((a+1)*(b+1))
    for k in range(2,q+2):
        C[k]=q*comb(q-1,k-2)*2**(k-2)*sqrt(k+1)
    return D,C

def det_bareiss(M):
    n=len(M)
    if not n: return 1
    a=[row[:] for row in M]
    den=1
    sign=1
    for k in range(n-1):
        if a[k][k]==0:
            i=next((i for i in range(k+1,n) if a[i][k]),None)
            if i is None:return 0
            a[i],a[k]=a[k],a[i]
            sign=-sign
        piv=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*piv-a[i][k]*a[k][j]
                assert num%den==0
                a[i][j]=num//den
        for i in range(k+1,n): a[i][k]=0
        den=piv
    return sign*a[-1][-1]

def enumerate_forests(q):
    n=q+2
    edges=[(u,2+j) for u in range(2) for j in range(q)]
    D=[0.]*(q+2);C=[0.]*(q+2)
    count=0
    for mask in range(1<<len(edges)):
        k=mask.bit_count()
        if k>q+1: continue
        parent=list(range(n)); size=[1]*n
        def find(x):
            while x!=parent[x]: x=parent[x]
            return x
        ok=True
        selected=[]
        for t,(u,v) in enumerate(edges):
            if not (mask>>t)&1:continue
            selected.append((u,v))
            a,b=find(u),find(v)
            if a==b:
                ok=False;break
            parent[b]=a;size[a]+=size[b]
        if not ok:continue
        count+=1
        roots={find(x) for x in range(n)}
        product=1
        for rt in roots:product*=size[rt]
        if q<=6:
            gram=[[int(u==x)-int(u==y)-int(v==x)+int(v==y)
                   for x,y in selected] for u,v in selected]
            assert det_bareiss(gram)==product,(q,selected,product)
        (C if find(0)==find(1) else D)[k]+=sqrt(product)
    return D,C,count

for q in range(1,8):
    eD,eC,cnt=enumerate_forests(q)
    fD,fC=exact_formula(q)
    for k in range(q+2):
        assert isclose(eD[k],fD[k],rel_tol=3e-12,abs_tol=3e-12),(q,k,'disconnected',eD[k],fD[k])
        assert isclose(eC[k],fC[k],rel_tol=3e-12,abs_tol=3e-12),(q,k,'connected',eC[k],fC[k])
    assert isclose(eC[-1],q*2**(q-1)*sqrt(q+2))
    print('q',q,'forests',cnt,'Vtop',round(eC[-1],8),'fraction connected',round(sum(eC)/(sum(eD)+sum(eC)),8))
print('K2Q_INTRINSIC_PASS q=1..7')
