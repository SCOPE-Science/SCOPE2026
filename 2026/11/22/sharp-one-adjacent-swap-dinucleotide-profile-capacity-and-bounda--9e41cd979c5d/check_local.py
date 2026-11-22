#!/usr/bin/env python3
"""Exhaustive finite-support certificate for local adjacent-swap profile changes."""
from itertools import product, combinations
from collections import Counter
from math import comb

def delta(block, q):
    a,b,c,d=block
    z=[0]*(q*q)
    for u,v in ((a,b),(b,c),(c,d)):
        z[u*q+v]-=1
    for u,v in ((a,c),(c,b),(b,d)):
        z[u*q+v]+=1
    return tuple(z)

def support(vec,q):
    s=set()
    for i,t in enumerate(vec):
        if t:
            s.add(i//q);s.add(i%q)
    return frozenset(s)

def classify(q):
    vals={delta(x,q) for x in product(range(q),repeat=4) if x[1]!=x[2]}
    parts=Counter(map(lambda v:len(support(v,q)),vals))
    for m in range(2,min(q,4)+1):
        for s in combinations(range(q),m):
            number=sum(support(v,q)==frozenset(s) for v in vals)
            assert number=={2:2,3:14,4:24}[m], (q,m,s,number)
    assert parts == {k:v for k,v in {0:1,2:2*comb(q,2),3:14*comb(q,3),4:24*comb(q,4)}.items() if v}
    assert len(vals)==1+2*comb(q,2)+14*comb(q,3)+24*comb(q,4)
    return parts,len(vals)

for q in range(2,9):
    counts,total=classify(q)
    print('alphabet',q,'support-classes',dict(sorted(counts.items())),'interior-distinct',total,'max',total+2)
print('PASS local signed-difference support classification for q=2..8')
