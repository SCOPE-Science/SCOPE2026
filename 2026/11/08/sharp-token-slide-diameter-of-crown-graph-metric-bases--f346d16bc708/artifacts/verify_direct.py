#!/usr/bin/env python3
"""Independently verify crown-graph ordinary vertex metric bases and token slides."""
from collections import deque
from itertools import combinations


def instance(n):
    V = range(2*n)
    adj = [set() for _ in V]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    D = []
    for v in V:
        d = [-1]*(2*n)
        d[v] = 0
        q = deque([v])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if d[w] < 0:
                    d[w] = d[u]+1
                    q.append(w)
        assert min(d)>=0
        D.append(d)
    return adj, D


def resolving(S, D):
    vectors = [tuple(D[s][v] for s in S) for v in range(len(D))]
    return len(set(vectors)) == len(D)


def candidate(S,n):
    seen = [0]*n
    for v in S:
        seen[v%n] += 1
    return sum(c == 0 for c in seen) == 1 and all(c < 2 for c in seen)


def check(n):
    adj,D=instance(n)
    allbases=set()
    tested=0
    for k in range(n):
        for S in combinations(range(2*n),k):
            got=resolving(S,D)
            tested+=1
            if k<n-1:
                assert not got, (n,S)
            else:
                assert got == candidate(S,n), (n,S)
                if got:
                    allbases.add(frozenset(S))
    assert len(allbases)==n*2**(n-1)
    edges=set()
    for S in allbases:
        legal=0
        for u in S:
            for v in adj[u]-S:
                T=frozenset((S-{u})|{v})
                if T in allbases:
                    edges.add(frozenset((S,T)))
                    legal+=1
        assert legal == n-1, (n,S,legal)
    assert len(edges)==len(allbases)*(n-1)//2
    return tested,len(allbases),len(edges)

if __name__=='__main__':
    for n in range(3,8):
        tested,states,edges=check(n)
        print(f'n={n} tested_subsets={tested} bases={states} slide_edges={edges} PASS')
    print('DIRECT_VERIFY_PASS n=3..7')
