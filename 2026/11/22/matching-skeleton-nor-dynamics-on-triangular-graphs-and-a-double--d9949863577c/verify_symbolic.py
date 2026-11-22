#!/usr/bin/env python3
"""Exact combinatorial basin verification for simultaneous open NOR on L(K_n)."""
from itertools import combinations
from collections import Counter
from math import comb, factorial


def component_clean_counts(N):
    # Exponential formula: exp(-z-z*z/2) sum_n 2^C(n,2)z^n/n!.
    # Solve A'' relation equivalently by component inclusion-exclusion.
    # A(z)=G(z) exp(-z-z²/2), therefore A'(z)=G'(z)e^...-(1+z)A(z).
    # Coefficient recurrence: a_n = g_n - sum_{i>=1} binom(n,i) b_i a_{n-i}
    # where exp(z+z²/2) coefficient b_i counts set partitions into singletons and pairs.
    b = [0]*(N+1); b[0]=1
    for k in range(1,N+1):
        b[k]=b[k-1]+(k-1)*b[k-2] if k>=2 else 1
    a=[0]*(N+1)
    for n in range(N+1):
        a[n]=2**comb(n,2)-sum(comb(n,j)*b[j]*a[n-j] for j in range(1,n+1))
    assert a[:7]==[1,0,0,4,38,728,26864],a
    return a


def theoretical(n, a):
    edges=list(combinations(range(n),2)); ei={e:i for i,e in enumerate(edges)}
    complete=lambda V:sum(1<<ei[e] for e in combinations(sorted(V),2))
    out={}
    def walk(M, used, start):
        if start==n:
            m=len(M); R=tuple(i for i in range(n) if i not in used);r=len(R)
            mm=sum(1<<ei[e] for e in M)
            if r<=1:
                out[(mm,mm)]=m+1 if r==0 else 1
            elif r>=3:
                z=mm | complete(R); out[tuple(sorted((mm,z)))]=1+(m+1)*a[r]+r*a[r-1]
                pivot=R[0]
                for k in range(3,r-2):
                    for subset in combinations(R[1:],k-1):
                        A=(pivot,)+subset;B=tuple(v for v in R if v not in A)
                        if len(B)>=3:
                            out[tuple(sorted((mm|complete(A),mm|complete(B))))]=a[len(A)]+a[len(B)]
            return
        # Enumerate each partial matching exactly once via decisions on the least unmatched vertex.
        if start in used:
            walk(M,used,start+1);return
        walk(M,used,start+1)
        for j in range(start+1,n):
            if j not in used:walk(M+[(start,j)],used | {start,j},start+1)
    walk([],set(),0)
    return out


def observed(n):
    edges=list(combinations(range(n),2)); k=len(edges)
    out=Counter()
    for s in range(1<<k):
        degrees=[0]*n
        for j,(u,v) in enumerate(edges):
            if s>>j&1:degrees[u]+=1;degrees[v]+=1
        # Direct local NOR: no distinct adjacent active edge.
        t=0
        for j,(u,v) in enumerate(edges):
            if all(not(s>>h&1) or h==j or (u not in ab and v not in ab)
                   for h,ab in enumerate(edges)):
                t|=1<<j
        # Independent second update through edge occupancy, not reusing local NOR loop.
        deg=[0]*n
        for j,(u,v) in enumerate(edges):
            if t>>j&1:deg[u]+=1;deg[v]+=1
        q=sum(1<<j for j,(u,v) in enumerate(edges)
              if deg[u]-(t>>j&1)==0 and deg[v]-(t>>j&1)==0)
        out[tuple(sorted((t,q)))]+=1
    return out

if __name__=='__main__':
    a=component_clean_counts(8)
    for n in range(3,7):
        expected=theoretical(n,a);actual=observed(n)
        assert expected==actual,(n,len(expected),len(actual),(expected-actual).most_common(4),(actual-expected).most_common(4))
        fixed=sum(x==y for x,y in expected);cycles=len(expected)-fixed
        top=max(expected.values());dist=expected[(0,(1<<comb(n,2))-1)]
        print(f'PASS n={n} states={1<<comb(n,2)} fixed={fixed} two_cycles={cycles} distinguished_basin={dist} maximum_basin={top}')
