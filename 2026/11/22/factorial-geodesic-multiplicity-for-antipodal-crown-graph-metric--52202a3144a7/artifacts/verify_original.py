#!/usr/bin/env python3
"""Exhaustive checks directly on crown graphs and resolving sets."""
from collections import deque
from itertools import combinations
from math import comb, factorial


def graph(n):
    V=range(2*n)
    adj=[set() for _ in V]
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    return adj


def dists(adj):
    out=[]
    for s in range(len(adj)):
        d={s:0}; q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if v not in d:
                    d[v]=d[u]+1; q.append(v)
        out.append([d[v] for v in range(len(adj))])
    return out


def vertex_resolves(S,ds):
    return len({tuple(ds[s][v] for s in S) for v in range(len(ds))})==len(ds)


def edge_resolves(S,ds,adj):
    E=[(i,j) for i in range(len(adj)) for j in adj[i] if i<j]
    return len({tuple(min(ds[s][i],ds[s][j]) for s in S) for i,j in E})==len(E)


def enumerate_bases(n):
    adj=graph(n); ds=dists(adj)
    assert all(not vertex_resolves(S,ds) for k in range(n-1) for S in combinations(range(2*n),k))
    assert all(not edge_resolves(S,ds,adj) for k in range(n-1) for S in combinations(range(2*n),k))
    V={frozenset(S) for S in combinations(range(2*n),n-1) if vertex_resolves(S,ds)}
    E={frozenset(S) for S in combinations(range(2*n),n-1) if edge_resolves(S,ds,adj)}
    expected={frozenset((n+i if bit&(1<<i) else i) for i in range(n) if i!=hole) for hole in range(n) for bit in range(1<<n) if not(bit&(1<<hole))}
    assert V==E==expected, (n,len(V),len(E),len(expected))
    return adj,V


def count_paths(n,adj,bases):
    origin=frozenset(range(1,n))
    target=frozenset(range(n+1,2*n))
    q=deque([origin]); dist={origin:0}; count={origin:1}
    while q:
        S=q.popleft()
        for u in S:
            for v in adj[u]-S:
                T=(S-{u})|{v}
                T=frozenset(T)
                if T not in bases:
                    continue
                if T not in dist:
                    dist[T]=dist[S]+1; count[T]=0; q.append(T)
                if dist[T]==dist[S]+1:
                    count[T]+=count[S]
    assert len(dist)==len(bases)
    return dist[target],count[target]


def main():
    for n in range(3,8):
        adj,bases=enumerate_bases(n)
        d,count=count_paths(n,adj,bases)
        expected=factorial(n-1)*comb(n,3)
        assert (d,count)==(n+3,expected),(n,d,count,expected)
        print(f'original-graph n={n} bases={len(bases)} geodesic_length={d} shortest_paths={count} PASS')
    print('DIRECT_GRAPH_AND_DISTANCES_OK')

if __name__=='__main__':main()
