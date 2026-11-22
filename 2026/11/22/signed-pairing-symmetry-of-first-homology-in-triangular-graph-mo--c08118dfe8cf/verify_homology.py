#!/usr/bin/env python3
"""Compute integral Euler and mod-2 homology of the explicit position complex."""
from itertools import combinations
from math import comb

def gf2_rank(columns):
    piv={}
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p in piv:x^=piv[p]
            else:piv[p]=x;break
    return len(piv)

def one(n):
    E=list(combinations(range(n),2));q=len(E)
    simplices={frozenset()}
    for k in range(1,3):simplices.update(map(frozenset,combinations(range(q),k)))
    for v in range(n):
        star=[j for j,e in enumerate(E) if v in e]
        for k in range(3,len(star)+1):simplices.update(map(frozenset,combinations(star,k)))
    for a,b,c in combinations(range(n),3):
        simplices.add(frozenset((E.index((a,b)),E.index((a,c)),E.index((b,c)))))
    dim=max(len(a) for a in simplices)-1
    levels=[[s for s in simplices if len(s)==k+1] for k in range(dim+1)]
    ranks=[]
    for k in range(1,len(levels)):
        prev={frozenset(x):i for i,x in enumerate(levels[k-1])}
        cols=[]
        for s in levels[k]:
            col=0
            for x in s:col^=1<<prev[s-{x}]
            cols.append(col)
        ranks.append(gf2_rank(cols))
    betti=[]
    for k,L in enumerate(levels):
        d_prev=ranks[k-1] if k else 0
        d_next=ranks[k] if k<len(ranks) else 0
        betti.append(len(L)-d_prev-d_next)
    expected=[1,3*comb(n,4),comb(n-1,3)]+[0]*(max(0,len(betti)-3))
    assert betti==expected,(n,betti,expected)
    print('n',n,'f-vector',[len(L) for L in levels],'GF2 Betti',betti)

if __name__=='__main__':
    for n in range(4,8):one(n)
    print('HOMOLOGY_OK')
