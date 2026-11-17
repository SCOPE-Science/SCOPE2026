#!/usr/bin/env python3
"""Standalone finite checks for cyclic fixed-locus universality in digraph complexes."""
from itertools import combinations
from math import gcd, prod

PRIMES=(2,3,5,7,11,13,17,19)

def all_subsets(items):
    items=list(items)
    for k in range(len(items)+1):
        yield from combinations(items,k)

def closure(facets):
    return {frozenset(t) for f in facets for t in all_subsets(f)}

def fast_strong(N,steps):
    # Exact criterion (independently checked by BFS below).
    g=N
    for s in steps:g=gcd(g,s)
    return g==1

def bfs_strong(N,steps):
    if not steps:return N==1
    reached={0}; stack=[0]
    while stack:
        x=stack.pop()
        for s in steps:
            y=(x+s)%N
            if y not in reached:
                reached.add(y);stack.append(y)
    return len(reached)==N

def rank_mod2(columns):
    piv={}; rank=0
    for c in columns:
        while c:
            p=c.bit_length()-1
            if p not in piv:
                piv[p]=c;rank+=1;break
            c^=piv[p]
    return rank

def reduced_betti_mod2(faces):
    bydim={}
    for f in faces: bydim.setdefault(len(f)-1,[]).append(tuple(sorted(f)))
    bydim={k:sorted(v) for k,v in bydim.items()}
    ranks={}
    for d in range(0,max(bydim)+1):
        rows={x:i for i,x in enumerate(bydim.get(d-1,[]))}
        cols=[]
        for f in bydim.get(d,[]):
            c=0
            for t in combinations(f,len(f)-1):
                c^=1<<rows[t]
            cols.append(c)
        ranks[d]=rank_mod2(cols)
    return {d:len(bydim[d])-ranks[d]-ranks.get(d+1,0)
            for d in bydim if d>=0 and len(bydim[d])-ranks[d]-ranks.get(d+1,0)}

def case(label,r,facets,expected_betti):
    facets=[frozenset(f) for f in facets]
    L=closure(facets)
    # Exactly r actual vertices; all listed explicitly in facets.
    assert {i for f in facets for i in f}==set(range(r))
    primes=PRIMES[:r]; q=PRIMES[r]
    N=q*prod(primes)
    ds=sorted({prod(primes[i] for i in f) for f in facets})
    S=[1,-1]+[s for d in ds for s in (d,-d)]
    assert len(S)==len(set(s%N for s in S))
    K={frozenset(t) for t in all_subsets(S) if not fast_strong(N,t)}
    for t in all_subsets(S):
        if N<=2310 and len(S)<=10:
            assert fast_strong(N,t)==bfs_strong(N,t), (label,t)
    # cover by all prime-divisibility simplices
    sigma=[{s for s in S if s%p==0} for p in primes]
    union={frozenset(t) for v in sigma for t in all_subsets(v)}
    assert K==union,(label,'prime cover')
    nerve={frozenset(I) for I in all_subsets(range(r))
           if not I or set.intersection(*(sigma[i] for i in I))}
    assert nerve==L,(label,'nerve')
    betti=reduced_betti_mod2(K)
    assert betti==expected_betti,(label,betti,expected_betti)
    print('CASE',label,'order',N,'arc steps',len(S),'fixed vertices',len(S)-2,
          'nonempty fixed faces',len(K)-1,'nerve faces',len(L)-1,
          'reduced_mod2_betti',sorted(betti.items()))

case('one-simplex',3,[{0,1,2}],{})
case('disconnected-edge-and-point',3,[{0,1},{2}],{0:1})
case('triangle-boundary',3,[{0,1},{1,2},{0,2}],{1:1})
case('tetrahedron-boundary',4,[{0,1,2},{0,1,3},{0,2,3},{1,2,3}],{2:1})
case('four-cycle',4,[{0,1},{1,2},{2,3},{0,3}],{1:1})
print('UNIVERSAL_CYCLIC_FIXED_NSC_PASS')
