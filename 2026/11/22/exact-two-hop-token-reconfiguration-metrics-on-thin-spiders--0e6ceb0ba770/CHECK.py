#!/usr/bin/env python3
"""Exact independent checks for two-hop independent-set reconfiguration on thin spiders.

No dependencies beyond Python's standard library. Run: python3 CHECK.py
"""
from itertools import combinations
from collections import deque, Counter
from math import comb


def base(r):
    # Cliques 0..r-1; their pendant vertices r..2r-1.
    g = [set() for _ in range(2*r)]
    for i in range(r):
        for j in range(i):
            g[i].add(j)
            g[j].add(i)
        g[i].add(r+i)
        g[r+i].add(i)
    dists = []
    for a in range(2*r):
        d = {a: 0}
        q = deque([a])
        while q:
            v = q.popleft()
            for w in g[v]:
                if w not in d:
                    d[w] = d[v]+1
                    q.append(w)
        assert len(d) == 2*r
        dists.append(d)
    return g, dists


def formula(a, b, k):
    # Node P = ('P', leaf-index tuple), M = ('M', clique-index, leaf-index tuple).
    if a[0] == 'P' and b[0] == 'P':
        return 2*(k-len(set(a[1]) & set(b[1])))
    if a[0] == 'M' and b[0] == 'M':
        if a[2] == b[2]:
            return int(a[1] != b[1])
        return 2*(k-1-len(set(a[2]) & set(b[2])))
    p, m = (a,b) if a[0] == 'P' else (b,a)
    return 2*(k-1-len(set(p[1]) & set(m[2])))+1


def check(r, k):
    g, d = base(r)
    nodes = []
    for cc in combinations(range(2*r), k):
        if all(j not in g[i] for ii,i in enumerate(cc) for j in cc[ii+1:]):
            c = [u for u in cc if u < r]
            leaves = tuple(u-r for u in cc if u >= r)
            assert len(c) <= 1
            nodes.append(('M',c[0],leaves) if c else ('P',leaves))
    assert len(nodes) == (k+1)*comb(r,k)
    graph = {x:set() for x in nodes}
    def occupied(x):
        return set(u+r for u in x[1]) if x[0]=='P' else {x[1]} | set(u+r for u in x[2])
    O = {x:occupied(x) for x in nodes}
    for ii,a in enumerate(nodes):
        for b in nodes[ii+1:]:
            diffa = O[a]-O[b]
            diffb = O[b]-O[a]
            if len(diffa)==len(diffb)==1:
                if d[next(iter(diffa))][next(iter(diffb))] <= 2:
                    graph[a].add(b)
                    graph[b].add(a)
    pure = sum(a[0]=='P' for a in nodes)
    assert pure == comb(r,k)
    mixed = len(nodes)-pure
    assert mixed == k*comb(r,k)
    total_edges = sum(len(v) for v in graph.values())//2
    expected_edges = k*(r-k+1)*comb(r,k)+comb(r,k-1)*comb(r-k+1,2)
    assert total_edges == expected_edges, (r,k,total_edges,expected_edges)
    for a in nodes:
        expected_degree = k*(r-k+1) if a[0]=='P' else 2*(r-k)+1
        assert len(graph[a]) == expected_degree, (r,k,a,len(graph[a]),expected_degree)
    observed_diameter = 0
    for a in nodes:
        shortest = {a:0}
        q = deque([a])
        while q:
            b = q.popleft()
            for c in graph[b]:
                if c not in shortest:
                    shortest[c] = shortest[b]+1
                    q.append(c)
        assert len(shortest) == len(nodes), (r,k,'disconnected')
        for b in nodes:
            assert shortest[b] == formula(a,b,k), (r,k,a,b,shortest[b],formula(a,b,k))
        observed_diameter = max(observed_diameter,max(shortest.values()))
    proposed = min(2*k,2*(r-k+1),r)
    assert observed_diameter == proposed, (r,k,observed_diameter,proposed)
    return (r,k,len(nodes),total_edges,observed_diameter)


def main():
    checked = 0
    for r in range(2,9):
        for k in range(1,r+1):
            result = check(r,k)
            checked += 1
            print('PASS: r=%d k=%d states=%d edges=%d diameter=%d' % result)
    for r in range(2,201):
        for k in range(1,r+1):
            vals = [2*min(k,r-k), 2*min(k-1,r-k)+1,
                    2*min(k-1,r-k+1)]
            if k==1: vals.append(1)
            assert max(vals) == min(2*k,2*(r-k+1),r)
    print('PASS:',checked,'independent graph-and-distance tests; 20099 algebraic parameter tests')

if __name__=='__main__':
    main()
