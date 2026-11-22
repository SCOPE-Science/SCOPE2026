#!/usr/bin/env python3
"""Exhaustive finite-field checks of endomorphism ranks of model filiform Lie algebras.
Usage: python check_filiform.py
Only prime fields are required for the enumerator: the proof works over all finite fields.
"""
from itertools import product
from collections import Counter

def bracket(u,v,p):
    n=len(u)
    w=[0]*n
    for j in range(2,n):
        w[j]=(u[0]*v[j-1]-v[0]*u[j-1])%p
    return tuple(w)

def rank(columns,p):
    if not columns: return 0
    a=[list(row) for row in zip(*columns)]
    h=len(a); w=len(a[0]); piv=0
    for j in range(w):
        k=next((k for k in range(piv,h) if a[k][j]%p),None)
        if k is None: continue
        a[piv],a[k]=a[k],a[piv]
        inv=pow(a[piv][j]%p,-1,p)
        for z in range(j,w): a[piv][z]=(a[piv][z]*inv)%p
        for k2 in range(h):
            if k2!=piv and (v:=a[k2][j]%p):
                for z in range(j,w):a[k2][z]=(a[k2][z]-v*a[piv][z])%p
        piv+=1
        if piv==h: break
    return piv

def predicted(n,q):
    c=Counter()
    c[0]=1
    c[1]=(q**(n-1)-1)*(q+1)+2*(q-1)*q**(n-1)+(q-1)**2*q**(n-1)
    c[2]=(q**(n-1)-1)*(q**(n-1)-q)+2*(q-1)**2*q**(n-1)+(q-1)**3*q**(n-1)
    c[3]=2*(q-1)**2*q**n+(q-1)**3*q**n
    for r in range(2,n+1): c[r]+=(q-1)**2*q**(n+r-3) if r>=4 else 0
    # The rank-2 and rank-3 terms from the a!=0, A=0 branch are already included above.
    assert sum(c.values())==q**(2*n-1)+(q-1)*q**(n+2),(n,q,c)
    return c

def check(n,p):
    c=Counter()
    vecs=list(product(range(p), repeat=n))
    for u in vecs:
        for v in vecs:
            w=bracket(u,v,p)
            columns=[u,v,w]
            while len(columns)<n:
                columns.append(bracket(u,columns[-1],p))
            good=all(bracket(columns[i],columns[j],p)==tuple(0 for _ in range(n)) for i in range(1,n) for j in range(i+1,n))
            # Remaining presentation relations [e1,ej]=e(j+1) and [e1,en]=0 follow by construction.
            good &= bracket(u,columns[-1],p)==tuple(0 for _ in range(n))
            if good: c[rank(columns,p)]+=1
    expected=predicted(n,p)
    assert c==expected,(n,p,c,expected)
    print(f'PASS n={n} q={p}: endomorphisms={sum(c.values())} rank_counts={dict(sorted(c.items()))}')

if __name__=='__main__':
    for n,p in ((4,2),(5,2),(6,2),(7,2),(4,3),(5,3),(4,5)):
        check(n,p)
    print('All exhaustive checks passed.')
