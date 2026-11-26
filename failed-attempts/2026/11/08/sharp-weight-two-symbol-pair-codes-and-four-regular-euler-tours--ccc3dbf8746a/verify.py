#!/usr/bin/env python3
"""Standalone checks for the weight-two symbol-pair-distance-seven theorem.

The mathematical proof is in RESULT.md. This program checks small exact
instances exhaustively and arbitrary-size graph-based witnesses directly.
"""
from itertools import combinations


def pair_distance(n, a, b):
    aa, bb = set(a), set(b)
    return sum(((i in aa), ((i+1) % n in aa)) !=
               ((i in bb), ((i+1) % n in bb)) for i in range(n))


def expected(n):
    assert n >= 2
    return (1 if n <= 6 else 2 if n <= 8 else 3 if n == 9
            else n // 2)


def euler_labels(k):
    assert k >= 5
    # Simple connected 4-regular circulant graph with offsets +/-1,+/-2.
    edges = sorted({tuple(sorted((a,(a+d) % k)))
                    for a in range(k) for d in (1,2)})
    assert len(edges) == 2*k
    adj = [[] for _ in range(k)]
    for j,(u,v) in enumerate(edges):
        adj[u].append((j,v)); adj[v].append((j,u))
    for arr in adj:
        arr.sort(reverse=True)
        assert len(arr) == 4
    used = [False] * len(edges)
    stack = [0]
    circuit = []
    while stack:
        v=stack[-1]
        while adj[v] and used[adj[v][-1][0]]:
            adj[v].pop()
        if not adj[v]:
            circuit.append(stack.pop())
        else:
            j,w=adj[v].pop()
            if not used[j]:
                used[j]=True; stack.append(w)
    assert all(used) and len(circuit) == 2*k+1
    assert circuit[0] == circuit[-1]
    labels = circuit[:-1]
    assert sorted(labels).count(0)==2
    assert all(labels.count(v)==2 for v in range(k))
    assert len({tuple(sorted((labels[j],labels[(j+1)%(2*k)])))
                for j in range(2*k)}) == 2*k
    return labels


def construction(n):
    if n <= 6:
        return [(0,1)]
    if n in (7,8):
        return [(0,1),(3,5)]
    if n == 9:
        return [(0,2),(3,7),(5,8)]
    k=n//2
    labels=euler_labels(k)
    if n % 2:
        labels = labels[:1]+[-1]+labels[1:]
    return [tuple(j for j,v in enumerate(labels) if v==i)
            for i in range(k)]


def all_codes_have_distance(n, C):
    assert all(len(a)==2 and all(0<=i<n for i in a) for a in C)
    assert len(set(C))==len(C)
    return all(pair_distance(n,a,b)>=7 for a,b in combinations(C,2))


def small_exhaustive(n, target):
    pool=list(combinations(range(n),2))
    # If a code strictly larger than target exists, a (target+1)-subset exists.
    m=target+1
    for I in combinations(range(len(pool)),m):
        if all(pair_distance(n,pool[i],pool[j])>=7
               for i,j in combinations(I,2)):
            raise AssertionError((n,'unexpected larger code',[pool[i] for i in I]))


def main():
    for n in range(2,10):
        C=construction(n)
        assert len(C)==expected(n) and all_codes_have_distance(n,C),n
        small_exhaustive(n, expected(n))
    for n in range(10,151):
        C=construction(n)
        assert len(C)==expected(n) and all_codes_have_distance(n,C),n
        # Even-length sharp codes have 4-regular simple transition graphs.
        if n%2==0:
            labels=[None]*n
            for a,positions in enumerate(C):
                for p in positions: labels[p]=a
            assert all(v is not None for v in labels)
            E=[tuple(sorted((labels[i],labels[(i+1)%n])))
               for i in range(n)]
            assert len(set(E))==n and all(u!=v for u,v in E)
    print('VERIFY_OK exhaustive_sizes=2..9 graph_witness_sizes=10..150')
    print('n=10 witness:',construction(10))


if __name__=='__main__':main()
