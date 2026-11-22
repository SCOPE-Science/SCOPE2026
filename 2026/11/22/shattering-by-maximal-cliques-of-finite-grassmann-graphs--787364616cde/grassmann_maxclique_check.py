#!/usr/bin/env python3
"""Independent finite-field enumeration of maximal-clique shattering in small Grassmann graphs.

Run: python3 grassmann_maxclique_check.py
Requires Python 3 (standard library only). Maximal cliques are enumerated by a
Bron--Kerbosch search on adjacency, without invoking star/top formulas.
"""
import itertools
import math
import random


def prime_vector_space(n, q):
    return list(itertools.product(range(q), repeat=n))


def span(vectors, q):
    n = len(vectors[0])
    return frozenset(tuple(sum(c*v[i] for c,v in zip(coeffs,vectors)) % q
                          for i in range(n))
                     for coeffs in itertools.product(range(q), repeat=len(vectors)))


def subspaces(n, k, q):
    zero=(0,)*n
    vs=[v for v in prime_vector_space(n,q) if v!=zero]
    out=set()
    for basis in itertools.combinations(vs,k):
        S=span(basis,q)
        if len(S)==q**k:
            out.add(S)
    return sorted(out,key=lambda s:sorted(s))


def gaussian(n,k,q):
    if k<0 or k>n:return 0
    a=b=1
    for j in range(k):
        a*=q**(n-j)-1
        b*=q**(k-j)-1
    return a//b


def predicted(n,k,q):
    size=gaussian(n,k,q)
    line=lambda r:(q**r-1)//(q-1)
    def noncollinear(r):
        return math.comb(line(r),3)-gaussian(r,2,q)*math.comb(q+1,3)
    return (1,size,size*q*line(k)*line(n-k)//2,
            gaussian(n,k-1,q)*noncollinear(n-k+1)+gaussian(n,k+1,q)*noncollinear(k+1))


def graph_and_cliques(n,k,q):
    vertices=subspaces(n,k,q)
    N=len(vertices)
    adj=[set() for _ in range(N)]
    for i,j in itertools.combinations(range(N),2):
        if len(vertices[i]&vertices[j])==q**(k-1):
            adj[i].add(j)
            adj[j].add(i)

    def bronk(R,P,X):
        if not P and not X:
            yield R
            return
        pivot=max(P|X,key=lambda u:len(P&adj[u]))
        for v in list(P-adj[pivot]):
            yield from bronk(R+(v,),P&adj[v],X&adj[v])
            P.remove(v)
            X.add(v)

    maximal=list(bronk(tuple(),set(range(N)),set()))
    return adj,maximal


def traces(concepts, S):
    patterns=set()
    for c in concepts:
        t=0
        for i,v in enumerate(S):
            if v in c:t|=1<<i
        patterns.add(t)
    return patterns


def test(n,k,q, all_triples=True):
    adj,cliques=graph_and_cliques(n,k,q)
    N=len(adj)
    expected=predicted(n,k,q)
    assert len(cliques)==gaussian(n,k-1,q)+gaussian(n,k+1,q)
    # A separate graph-theoretic test of the proposed support criterion.
    C=[set(s) for s in cliques]
    coeffs=[1,0,0,0]
    for s in range(1,4):
        if s==3 and not all_triples:
            continue
        for S in itertools.combinations(range(N),s):
            if len(traces(C,S))==(1<<s):
                coeffs[s]+=1
                assert all(v in adj[u] for u,v in itertools.combinations(S,2))
            elif s==2:
                assert not S[1] in adj[S[0]]
        assert coeffs[s]==expected[s],(n,k,q,s,coeffs[s],expected[s])
    # Check that every clique-edge is shattered and no four-support is shattered.
    if N<=40:
        for S in itertools.combinations(range(N),4):
            assert len(traces(C,S))<16,S
    else:
        rng=random.Random(2914+n*100+k*10+q)
        for _ in range(10000):
            S=tuple(sorted(rng.sample(range(N),4)))
            assert len(traces(C,S))<16,S
    print('PASS', f'GF({q}) n={n} k={k} vertices={N} maximal_cliques={len(cliques)}',
          f'faces={expected} fully_checked_triples={all_triples}',flush=True)

if __name__=='__main__':
    test(4,2,2)
    test(4,2,3)
    # Additional randomly sampled higher ambient dimension, with a fixed seed.
    n,k,q=5,2,2
    adj,cliques=graph_and_cliques(n,k,q)
    assert len(adj)==155 and len(cliques)==186
    rng=random.Random(181)
    for s in (2,3,4):
        for _ in range(2000):
            sample=rng.sample(range(len(adj)),s)
            observed=len(traces([set(c) for c in cliques],sample))==(1<<s)
            if s==2:
                assert observed==(sample[1] in adj[sample[0]])
            elif s==3:
                triangle=all(sample[j] in adj[sample[i]]
                             for i in range(3) for j in range(i+1,3))
                # A nonpencil triangle belongs to exactly one maximal clique.
                containing=sum(all(v in C for v in sample) for C in cliques)
                assert observed==(triangle and containing==1)
            else:
                assert not observed
    print('PASS GF(2) n=5 k=2 sampled 2000 supports of sizes 2,3,4',flush=True)
    print('GRASSMANN_MAXCLIQUE_SHATTER_PASS',flush=True)
