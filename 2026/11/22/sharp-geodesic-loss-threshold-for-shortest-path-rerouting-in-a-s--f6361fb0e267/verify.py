#!/usr/bin/env python3
"""Standalone finite checks of a punctured-hypercube geodesic rerouting theorem.

Run: python3 verify.py
All graph distances are reconstructed by BFS on explicitly generated admissible
permutations. Finite checks are not a substitute for the mathematical proof.
"""
from itertools import permutations
from collections import deque, Counter
from math import factorial


def kendall(p, q):
    pos = {v: i for i, v in enumerate(p)}
    return sum(pos[q[i]] > pos[q[j]] for i in range(len(q)) for j in range(i + 1, len(q)))


def witness(n, k):
    A = list(range(k)); B = list(range(k, n))
    a, ap = A[-2:]; b, bp = B[:2]
    u = A[:-2]; v = B[2:]
    trace = [
        (a, b, ap, bp),
        (b, a, ap, bp),
        (b, ap, a, bp),
        (b, ap, bp, a),
        (ap, b, bp, a),
        (ap, bp, b, a),
        (ap, bp, a, b),
    ]
    return [tuple(u + list(w) + v) for w in trace]


def check(n, k, full_pairs=False):
    A = set(range(k))
    P = [p for p in permutations(range(n)) if set(p[:k]) != A]
    index = {p: i for i, p in enumerate(P)}
    m = len(P)
    assert m == factorial(n)-factorial(k)*factorial(n-k)
    neighbors = [[] for _ in P]
    for idx,p in enumerate(P):
        for j in range(n-1):
            q = list(p); q[j],q[j+1] = q[j+1],q[j]
            if tuple(q) in index:
                neighbors[idx].append(index[tuple(q)])
    degree = Counter(map(len,neighbors))
    F = factorial(k)*factorial(n-k)
    assert degree[n-2] == F or (n==2 and degree[n-2]==F)
    assert degree[n-1] == m-F
    edges = sum(map(len,neighbors))//2
    assert edges == ((n-1)*factorial(n)-n*F)//2

    def bfs(start):
        D = [-1]*m
        D[start]=0
        Q=deque([start])
        while Q:
            j = Q.popleft()
            for t in neighbors[j]:
                if D[t]<0:
                    D[t]=D[j]+1; Q.append(t)
        return D

    d0 = bfs(0)
    assert all(d>=0 for d in d0), (n,k,'disconnected')
    if full_pairs:
        for i,p in enumerate(P):
            ds=bfs(i)
            if k in (1,n-1):
                for j,q in enumerate(P):
                    assert ds[j]==kendall(p,q), (n,k,p,q,ds[j],kendall(p,q))
    if 2<=k<=n-2:
        path=witness(n,k)
        assert all(p in index for p in path)
        assert all(sum(x!=y for x,y in zip(p,q))==2 for p,q in zip(path,path[1:]))
        assert kendall(path[0],path[-1])==4
        assert len(path)-1==6
        ds = bfs(index[path[0]])
        assert ds[index[path[-1]]]==6, (n,k,ds[index[path[-1]]])
    return m,edges,dict(sorted(degree.items()))



def check_cube_interpretation(n, k):
    """Build rerouting edges directly from shortest-path vertex sequences."""
    A = set(range(k))
    forbidden = sum(1 << a for a in A)
    words = []
    buckets = {}
    for p in permutations(range(n)):
        seq = [0]
        state = 0
        for bit in p:
            state |= 1 << bit
            seq.append(state)
        if forbidden in seq:
            continue
        idx = len(words)
        words.append(p)
        for i in range(1,n):
            key = tuple(seq[:i] + seq[i+1:])
            buckets.setdefault(key, []).append(idx)
    edges = set()
    for ids in buckets.values():
        assert len(ids) <= 2
        if len(ids)==2:
            edges.add(tuple(sorted(ids)))
    direct = set()
    loc = {p:i for i,p in enumerate(words)}
    for i,p in enumerate(words):
        for j in range(n-1):
            q=list(p);q[j],q[j+1]=q[j+1],q[j]
            t=loc.get(tuple(q))
            if t is not None:
                direct.add(tuple(sorted((i,t))))
    assert edges == direct, (n,k)
    return len(words),len(edges)

def main():
    count=0
    for n in range(2,9):
        for k in range(1,n):
            m,e,d=check(n,k,full_pairs=n<=6)
            count+=1
            print(f'n={n} k={k} vertices={m} edges={e} degree_counts={d}')
    for n in range(2,7):
        for k in range(1,n):
            count_cube = check_cube_interpretation(n,k)
    print(f'PASS: {count} graph instances; all-pairs extremal geodesic checks n<=6;')
    print('      connectivity/counts/degrees and exact interior-six-move witness n<=8;')
    print('      direct cube-path versus permutation-edge reconciliation for n<=6.')

if __name__=='__main__': main()
