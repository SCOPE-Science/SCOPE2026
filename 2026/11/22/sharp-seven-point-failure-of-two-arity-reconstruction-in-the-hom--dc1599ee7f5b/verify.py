#!/usr/bin/env python3
"""Exact enumeration of triangle-free base graphs for an orbit-count collision claim.
Python 3 standard library only. No graph-database dependency.
"""
from itertools import combinations, permutations, product
from collections import defaultdict

def bits(n, edges):
    adj=[0]*n
    for u,v in edges:
        adj[u]|=1<<v
        adj[v]|=1<<u
    return tuple(adj)

def enc(adj, order):
    n=len(adj); value=0; bit=0
    for i in range(n):
        for j in range(i+1,n):
            value |= (((adj[order[i]]>>order[j])&1)<<bit)
            bit+=1
    return value

def decode(n,code):
    adj=[0]*n;bit=0
    for i in range(n):
        for j in range(i+1,n):
            if (code>>bit)&1:
                adj[i]|=1<<j;adj[j]|=1<<i
            bit+=1
    return tuple(adj)

def canonical_code(adj):
    n=len(adj)
    groups=defaultdict(list)
    for v,mask in enumerate(adj):groups[mask.bit_count()].append(v)
    levels=[groups[d] for d in sorted(groups)]
    return min(enc(adj,order) for parts in product(*(permutations(level) for level in levels)) for order in (sum((tuple(g) for g in parts),()),))

def independent_masks(adj):
    n=len(adj);out=[]
    for mask in range(1<<n):
        if all(not (adj[v]&mask) for v in range(n) if (mask>>v)&1):out.append(mask)
    return out

def extend(adj, neighborhood):
    n=len(adj)
    return tuple(adj[v] | (((neighborhood>>v)&1)<<n) for v in range(n)) + (neighborhood,)

def enumerator(nmax=7):
    graphs={0:[()]}
    for n in range(nmax):
        seen=set()
        for adj in graphs[n]:
            for neigh in independent_masks(adj):
                seen.add(canonical_code(extend(adj,neigh)))
        graphs[n+1]=[decode(n+1,code) for code in sorted(seen)]
    return graphs

def signature(adj):
    indep=independent_masks(adj)
    I=len(indep)
    C=sum((s&t)==0 for s in indep for t in indep)
    return I,C

def triple(adj):
    indep=independent_masks(adj); I=len(indep)
    C=sum((s&t)==0 for s in indep for t in indep)
    J=sum(sum((s&t)==0 for t in indep)**2 for s in indep)
    return I**3+3*I*C+3*J,J

def edges(adj):
    return tuple((i,j) for i in range(len(adj)) for j in range(i+1,len(adj)) if (adj[i]>>j)&1)

def main():
    graphs=enumerator()
    assert [len(graphs[n]) for n in range(8)]==[1,1,2,3,7,14,38,107], [len(graphs[n]) for n in range(8)]
    for n in range(8):
        by=defaultdict(list)
        for adj in graphs[n]:by[signature(adj)].append(adj)
        collisions=[(sig,rs) for sig,rs in by.items() if len(rs)>1]
        print('N',n,'CLASSES',len(graphs[n]),'COLLISIONS',len(collisions))
        if n<7:assert not collisions
        else:
            assert len(collisions)==1
            (I,C),pair=collisions[0]
            assert (I,C)==(36,597) and len(pair)==2
            pair=sorted(pair,key=lambda a:sum(bool(x) for x in a))
            assert [triple(a) for a in pair] == [(145767,11545),(145689,11519)] or [triple(a) for a in pair]==[(145689,11519),(145767,11545)]
            for a in pair:
                print(' WITNESS',edges(a),'DEGREES',sorted(x.bit_count() for x in a),'SIGNATURE',signature(a),'THIRD',triple(a))
    print('EXHAUSTIVE_FRAISSE_COLLISION_OK')
if __name__=='__main__':main()
