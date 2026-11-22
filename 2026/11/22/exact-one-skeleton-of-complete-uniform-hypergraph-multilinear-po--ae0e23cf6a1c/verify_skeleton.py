#!/usr/bin/env python3
"""Exact finite midpoint-collision cross-check for the full skeleton theorem.

No third-party dependencies. For small n, every pair of lifted Boolean vertices
is checked against all other pairs for an identical midpoint. A collision proves
nonadjacency; absence of collision corroborates (but does not establish) an edge.
The proof in RESULT.md, not this finite program, establishes every n and r.
"""
from itertools import combinations
from math import comb

def bit_count(v): return v.bit_count()

def predicted_edge(s,t,r):
    if max(bit_count(s),bit_count(t)) >= r:
        return True
    d=bit_count(s^t)
    return d==1 or (bit_count(s)==bit_count(t)==r-1 and d==2)

def stats(n,r):
    N=1<<n
    M=sum(comb(n,j) for j in range(r,n+1))
    low=N-M
    E=comb(M,2)+M*low+n*sum(comb(n-1,j) for j in range(r-1)) + comb(n,r-1)*(r-1)*(n-r+1)//2
    return M,E

def check(n,r):
    allsets=tuple(combinations(range(n),r))
    masks=[sum(1<<i for i in F) for F in allsets]
    verts=[]
    for s in range(1<<n):
        verts.append(bytes([((s>>i)&1) for i in range(n)]+[int((s&m)==m) for m in masks]))
    midpoint_first={}
    pairs=[]
    for s in range(1<<n):
        for t in range(s+1,1<<n):
            sig=bytes(a+b for a,b in zip(verts[s],verts[t]))
            collision=sig in midpoint_first
            if not collision:
                midpoint_first[sig]=(s,t)
            pairs.append((s,t,sig,collision))
    multiplicities={}
    for s,t,sig,_ in pairs:
        multiplicities[sig]=multiplicities.get(sig,0)+1
    degrees=[0]*(1<<n)
    edges=0
    for s,t,sig,_ in pairs:
        pred=predicted_edge(s,t,r)
        collides=multiplicities[sig]>1
        assert pred != collides, f'counterexample n={n},r={r}, pair={s},{t}, collision={collides}'
        if pred:
            edges+=1
            degrees[s]+=1
            degrees[t]+=1
    M,E=stats(n,r)
    assert edges==E, (n,r,edges,E)
    for s,d in enumerate(degrees):
        k=s.bit_count()
        expected=((1<<n)-1 if k>=r else M+n if k<=r-2 else M+(r-1)*(n-r+2))
        assert d==expected,(n,r,s,d,expected)
    assert (min(degrees)>0)
    return f'n={n},r={r}: vertices={1<<n}, edges={edges}, maximum_degree={(1<<n)-1}, exact midpoint classifications={len(pairs)}'

if __name__=='__main__':
    total=0
    for n in range(2,8):
        for r in range(2,n+1):
            print(check(n,r)); total+=1
    print(check(8,4)); total+=1
    print(f'PASS: {total} finite instances, exact integer signatures and closed-form graph counts')
