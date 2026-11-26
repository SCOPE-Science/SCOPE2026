#!/usr/bin/env python3
"""Reproduce commutator fibers and graph-coloring reductions over prime fields."""
from itertools import product
from collections import Counter
from functools import lru_cache

def chromatic(n, edges, colors):
    c=0
    for labels in product(range(colors),repeat=n):
        if all(labels[u]!=labels[v] for u,v in edges): c+=1
    return c

def contractions_chromatic(n, S, T, q):
    p=list(range(n))
    def root(x):
        while p[x]!=x: x=p[x]
        return x
    for a,b in T:
        ra,rb=root(a),root(b);p[ra]=rb
    parts={root(i) for i in range(n)}
    index={t:k for k,t in enumerate(sorted(parts))}
    transformed=[(index[root(a)],index[root(b)]) for a,b in S]
    if any(a==b for a,b in transformed):return 0
    return chromatic(len(parts),transformed,q*q)

def predicted(n,edges,q,support):
    M=len(edges); rest=[i for i in range(M) if i not in support]
    total=0
    for mask in range(1<<len(rest)):
        T=[edges[rest[i]] for i in range(len(rest)) if mask>>i&1]
        S=[edges[i] for i in support]
        total+=(q-1)**len(T)*contractions_chromatic(n,S,T,q)
    return (q**M)*total

def direct(n,edges,q):
    m=len(edges)
    out=Counter()
    # directly enumerate full algebra ordered pairs, with products computed by diagonal-arrow equations
    for vx in product(range(q),repeat=n):
      for vy in product(range(q),repeat=n):
        diffs=[((vx[a]-vx[b])%q,(vy[a]-vy[b])%q) for a,b in edges]
        for u in product(range(q),repeat=m):
          for w in product(range(q),repeat=m):
            value=tuple((d1*w[i]-d2*u[i])%q for i,(d1,d2) in enumerate(diffs))
            out[value]+=1
    return out

def test(n,edges,q):
    out=direct(n,edges,q);m=len(edges)
    assert sum(out.values()) == q**(2*(n+m))
    for z in product(range(q),repeat=m):
      supp=frozenset(i for i,v in enumerate(z) if v)
      p=predicted(n,edges,q,supp)
      assert out[z]==p,(n,edges,q,z,out[z],p)
    print('case',n,edges,q,'pairs',q**(2*(n+m)),'zero',out[(0,)*m], 'fiber types',len(set(out.values())),flush=True)

def width(n,edges,q):
    r=0
    while True:
      if chromatic(n,edges,q**(2*r)):
        return r
      r+=1

def k5_witness():
    # q=2: four labels cannot color K5, while 16 labels do
    edges=[(i,j) for i in range(5) for j in range(i+1,5)]
    assert not chromatic(5,edges,4)
    assert chromatic(5,edges,16)>0
    assert width(5,edges,2)==2
    # explicit decomposition of all-one target with 2 commutators
    # vertices given distinct 4-bit labels, two pairs of binary coordinates
    color=[0,1,2,3,4]; groups=[[(v>>(2*h))&3 for v in color] for h in (0,1)]
    vals=[ [0]*len(edges) for _ in range(2)]
    for k,(a,b) in enumerate(edges):
      h=0 if groups[0][a]!=groups[0][b] else 1
      alpha=groups[h][a]&1; beta=(groups[h][a]>>1)&1
      da=alpha^(groups[h][b]&1);db=beta^((groups[h][b]>>1)&1)
      # equation da*w - db*u = 1 in F2
      vals[h][k]=(1 if da else 2)
      assert da or db
    for k,(a,b) in enumerate(edges):
      total=0
      for h in range(2):
        da=(groups[h][a]&1)^(groups[h][b]&1)
        db=((groups[h][a]>>1)&1)^((groups[h][b]>>1)&1)
        if vals[h][k]==1: total^=da
        if vals[h][k]==2: total^=db
      assert total==1
    print('K5 q2 all-arrow commutator length exactly 2',flush=True)

if __name__=='__main__':
    test(2,[(0,1)],2)
    test(3,[(0,1),(1,2)],2)
    test(3,[(0,1),(1,2),(0,2)],2)
    test(2,[(0,1)],3)
    test(3,[(0,1),(1,2)],3)
    test(2,[(0,1),(0,1)],2)
    k5_witness()
    print('VERIFY_OK')
