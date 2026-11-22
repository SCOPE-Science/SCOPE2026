#!/usr/bin/env python3
"""Exact reverse-complement-closed cross-bifix-free codebook census.

Usage: python verify_exhaustive.py
Standard-library only. All outputs are produced from source-word overlap tests.
"""
from itertools import product
from collections import Counter
import json

EXPECTED = {
    1:(2,1), 2:(1,2), 3:(0,1), 4:(1,2), 5:(0,1), 6:(2,2),
    7:(0,1), 8:(5,2), 9:(2,4), 10:(14,6), 11:(10,96), 12:(42,1134),
}

def rc(w):
    return ''.join('1' if x=='0' else '0' for x in reversed(w))

def overlap(u,v):
    n=len(u)
    return any(u[:k]==v[-k:] or v[:k]==u[-k:] for k in range(1,n))

def graph(n):
    words=[''.join(w) for w in product('01',repeat=n)]
    seen=set();orbits=[]
    for w in words:
        if w in seen:continue
        pair=tuple(sorted({w,rc(w)}))
        seen.update(pair)
        if any(overlap(u,v) for u in pair for v in pair):continue
        orbits.append(pair)
    m=len(orbits)
    compatible=[]
    for i,x in enumerate(orbits):
        bits=0
        for j,y in enumerate(orbits):
            if j!=i and all(not overlap(u,v) for u in x for v in y):bits|=1<<j
        compatible.append(bits)
    return orbits,compatible

def exact(n):
    if n==1:return dict(length=1, orbits=1, maximum=2, optimizers=1, nodes=1, witness=['0','1'])
    orbits,adj=graph(n);m=len(orbits);wt=list(map(len,orbits))
    best=-1;optimizers=0;nodes=0;witness=[];types=Counter()
    def rec(selected,P,X,total):
        nonlocal best,optimizers,nodes,witness,types
        nodes+=1
        if not P and not X:
            if total>best:
                best=total;optimizers=0;witness=[];types=Counter()
            if total==best:
                optimizers+=1
                types[sum(wt[i]==2 for i in selected)]+=1
                if not witness:witness=sorted(w for i in selected for w in orbits[i])
            return
        if total+sum(wt[i] for i in range(m) if P&(1<<i))<best:return
        while P:
            b=P&-P;i=b.bit_length()-1
            rec(selected+(i,),P&adj[i],X&adj[i],total+wt[i])
            P-=b;X|=b
    rec((),(1<<m)-1,0,0)
    # Independent complete check of the displayed codebook's constraints.
    assert len(witness)==best and all(rc(w) in witness for w in witness)
    assert all(not overlap(u,v) for u in witness for v in witness)
    return dict(length=n,orbits=m,maximum=best,optimizers=optimizers,nodes=nodes,
                pair_distribution=dict(sorted(types.items())),witness=witness)

if __name__=='__main__':
    reports=[]
    for n in range(1,13):
        result=exact(n)
        assert (result['maximum'],result['optimizers'])==EXPECTED[n], result
        reports.append(result)
        print(f"n={n:2d} orbits={result['orbits']:2d} M={result['maximum']:2d} "
              f"N={result['optimizers']:4d} nodes={result['nodes']:8d} "
              f"pairs={result.get('pair_distribution',{})}",flush=True)
    print('PASS: all exact maxima, optimizer counts and witness checks')
