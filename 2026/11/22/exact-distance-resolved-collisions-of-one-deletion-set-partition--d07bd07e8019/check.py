#!/usr/bin/env python3
"""Reproducibility checks for one-point deletion collisions in set partitions.
Pure Python 3, standard library only; no network or external datasets.
"""
from collections import defaultdict
from itertools import combinations
from random import Random


def canonical(labels):
    ranks = {}
    return tuple(ranks.setdefault(v, len(ranks)) for v in labels)


def partitions(n):
    if n == 0:
        yield ()
        return
    def walk(prefix, top):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for value in range(top+2):
            yield from walk(prefix + [value], max(top, value))
    yield from walk([0], 0)


def deletion(p, i):
    return canonical(p[:i]+p[i+1:])


def periodic_isolated(p, i, j):
    segment = p[i:j+1]
    d = len(set(segment))
    if d < 2:
        return False
    if len(set(segment[:d])) != d:
        return False
    if any(segment[t] != segment[t%d] for t in range(len(segment))):
        return False
    return not (set(segment) & set(p[:i]+p[j+1:]))


def structural(p, i, j):
    return len(set(p[i:j+1])) == 1 or periodic_isolated(p, i, j)


def stirling(N):
    S=[[0]*(N+1) for _ in range(N+1)]
    S[0][0]=1
    for n in range(1,N+1):
        for k in range(1,n+1):
            S[n][k]=k*S[n-1][k]+S[n-1][k-1]
    return S


def run():
    N=9
    S=stirling(N)
    B=[sum(row) for row in S]
    pair_cases=0
    for n in range(2,N+1):
        actual=defaultdict(int)
        for p in partitions(n):
            deck=[deletion(p,i) for i in range(n)]
            k=len(set(p))
            for i,j in combinations(range(n),2):
                equal=deck[i]==deck[j]
                assert equal == structural(p,i,j), (n,p,i,j)
                if equal:
                    actual[(k,j-i+1)]+=1
                pair_cases+=1
        for k in range(1,n+1):
            for ell in range(2,n+1):
                fixed=S[n-ell+1][k] + sum(
                    S[n-ell][k-d] for d in range(2,ell+1)
                    if 0 <= k-d <= n-ell)
                assert actual[(k,ell)] == (n-ell+1)*fixed, (
                    n,k,ell, actual[(k,ell)],fixed)
        collapsed=sum(actual[(k,ell)] for k in range(1,n+1)
                      for ell in range(2,n+1))
        closed=sum((n-ell+1)*(B[n-ell+1]+(ell-1)*B[n-ell])
                   for ell in range(2,n+1))
        assert collapsed==closed, (n,collapsed,closed)
        print('n=',n,'Bell=',B[n],'collision-pairs=',collapsed,'OK')
    # A second representation tests invariant under arbitrary block relabeling.
    rng=Random(314159)
    for n in range(2,61):
        for _ in range(200):
            p=tuple(rng.randrange(max(2,n//3)) for _ in range(n))
            i,j=sorted(rng.sample(range(n),2))
            assert (deletion(p,i)==deletion(p,j))==structural(p,i,j)
    print('VERIFY_OK; exhaustive-pair-cases=',pair_cases,
          'random-large-pair-cases=',59*200)

if __name__=='__main__':
    run()
