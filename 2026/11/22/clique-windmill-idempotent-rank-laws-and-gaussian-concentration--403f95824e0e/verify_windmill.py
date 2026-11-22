#!/usr/bin/env python3
"""Independent exhaustive check for rank-counted idempotent graph-continuous partial maps."""
from itertools import product
from collections import Counter
from math import comb


def add(a,b):
    n=max(len(a),len(b))
    return [((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)) for i in range(n)]

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def polypow(a,k):
    out=[1]
    for _ in range(k):out=mul(out,a)
    return out

def expected(sizes):
    bs=[]
    for s in sizes:
        b=[comb(s,k) for k in range(s+1)]
        b[1]+=s*(s-1)
        bs.append(b)
    p=[1]
    for b in bs:p=mul(p,b)
    out=p[:]
    for i,s in enumerate(sizes):
        p=[0,s]
        for j,b in enumerate(bs):
            if i!=j:p=mul(p,b)
        out=add(out,p)
    S=sum(sizes)
    out=add(out,[0]+[comb(S,k) for k in range(S+1)])
    out=add(out,[0,S])
    return out


def verify(sizes):
    n=1+sum(sizes)
    edges=set()
    a=1
    for s in sizes:
        block=list(range(a,a+s));a+=s
        for v in block:edges.add((0,v))
        for i in range(len(block)):
            for j in range(i+1,len(block)):
                edges.add((block[i],block[j]))
    cells=[(v,) for v in range(n)]+list(edges)
    def isface(verts):
        return len(verts)<=1 or (len(verts)==2 and tuple(sorted(verts)) in edges)
    counts=Counter(); scanned=0
    for f in product(range(-1,n),repeat=n):
        scanned+=1
        # composition-idempotent iff every defined image point is a fixed point
        if any(f[w]!=w for w in f if w>=0):continue
        # continuity of all singleton and edge inverse images
        if any(not isface([u for u in range(n) if f[u] in cell]) for cell in cells):continue
        counts[len({w for w in f if w>=0})]+=1
    exp=expected(sizes)
    assert [counts.get(k,0) for k in range(n+1)]==exp, (sizes, counts, exp)
    print('PASS',sizes,'vertices',n,'partial_maps_scanned',scanned,'rank_counts',exp,'total_idempotents',sum(exp))

if __name__=='__main__':
    for sizes in [(1,), (2,), (1,1), (2,1), (2,2), (1,1,1), (3,1), (2,2,1), (2,3)]:
        verify(sizes)
    print('VERIFY_OK')
