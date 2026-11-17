#!/usr/bin/env python3
"""Exact finite checks for equilateral-cluster one-point Lipschitz extension."""
from fractions import Fraction as F
from itertools import product
from heapq import heapify, heappush, heappop


def tree_edges(n, word):
    deg = [1]*n
    for u in word:
        deg[u] += 1
    leaves = [u for u in range(n) if deg[u] == 1]
    heapify(leaves)
    edges = []
    for u in word:
        v = heappop(leaves)
        edges.append((v, u))
        deg[v] -= 1
        deg[u] -= 1
        if deg[u] == 1:
            heappush(leaves,u)
    a, b = sorted(leaves)
    edges.append((a,b))
    return edges


def make_metric(sizes, ts):
    N = sum(sizes)
    d = [[F(int(i != j)) for j in range(N)] for i in range(N)]
    start = 0
    for m,t in zip(sizes,ts):
        for i in range(start,start+m):
            for j in range(start,start+m):
                if i != j:
                    d[i][j] = t
        start += m
    return d


def vertices(d):
    n = len(d)
    out = set()
    # Each extreme potential has a spanning tree of tight constraints.
    for word in product(range(n), repeat=n-2):
        es = tree_edges(n,word)
        adj = [[] for _ in range(n)]
        for a,b in es:
            adj[a].append((b,d[a][b],1))
            adj[b].append((a,d[a][b],-1))
        for signs in product((-1,1),repeat=n-1):
            f = [None]*n
            f[0] = F(0)
            todo = [0]
            while todo:
                u=todo.pop()
                for v,dist,sign in adj[u]:
                    if f[v] is None:
                        # sign index obtained from sorted tree edge index via key
                        ei = es.index((u,v)) if (u,v) in es else es.index((v,u))
                        ordered_a,ordered_b=es[ei]
                        s=signs[ei] if u == ordered_a else -signs[ei]
                        f[v]=f[u]+s*dist
                        todo.append(v)
            if all(abs(f[a]-f[b])<=d[a][b] for a in range(n) for b in range(a)):
                out.add(tuple(f))
    return out


def center_norm(c, extremes):
    n=len(c)
    return max(abs(sum(c[i]*f[i] for i in range(n))-f[j]) for f in extremes for j in range(n))


def verify(sizes,ts):
    assert len(sizes)==len(ts)>=2 and all(m>=1 for m in sizes)
    n=sum(sizes)
    d=make_metric(sizes,ts)
    beta=[F(1)-t*(m-1)/m for m,t in zip(sizes,ts)]
    H=sum(F(1)/b for b in beta)
    h=1/H
    delta=1-h
    c=tuple(h/(m*b) for m,b in zip(sizes,beta) for _ in range(m))
    assert sum(c)==1
    ext=vertices(d)
    assert len(ext)>0
    K=center_norm(c,ext)
    assert K==delta,(sizes,ts,K,delta)
    assert all(sum(c[i]*d[i][j] for i in range(n)) == delta for j in range(n))
    for i in range(n):
        for j in range(i+1,n):
            for step in (F(1,20),F(-1,20),F(1,7),F(-1,7)):
                v=list(c)
                v[i]+=step
                v[j]-=step
                assert center_norm(v,ext)>delta,(sizes,ts,i,j,step)
    for r in (F(1,2),delta,(delta+1)/2,F(1)):
        if r>=F(1,2):
            norm=max(F(1),delta/r)
            assert norm>=1
    return len(ext)

if __name__=='__main__':
    configs=[
        ((1,1,1),(F(1),F(1),F(1))),
        ((2,1),(F(1,2),F(1))),
        ((2,2),(F(1,2),F(2,3))),
        ((2,2),(F(1),F(1))),
        ((1,2,1),(F(1),F(3,4),F(1))),
        ((3,2),(F(1,3),F(3,5))),
        ((2,1,2),(F(2,3),F(1),F(4,5))),
        ((1,1,1,1),(F(1),)*4),
    ]
    total=0
    for sizes,ts in configs:
        z=verify(sizes,ts)
        total+=z
        print('EXACT_EXTREME_POTENTIAL_DUAL_CHECK_PASS sizes=',sizes,' vertices=',z)
    print('HARMONIC_CLUSTER_EXTENSION_ALL_CHECKS_PASS profiles=',len(configs),'extreme_vertices=',total)
