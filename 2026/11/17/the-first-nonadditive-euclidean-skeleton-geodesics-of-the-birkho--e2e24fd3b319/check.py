"""Finite, independently executable checks for the weighted Birkhoff skeleton theorem.
Usage: python check.py (n=6); optional python check.py 7. Requires only Python's standard library.
"""
from itertools import combinations, permutations
from math import sqrt
from heapq import heappush, heappop
from collections import Counter
import sys


def cycles(n):
    identity = tuple(range(n))
    out=[]
    for k in range(2,n+1):
        for subset in combinations(range(n),k):
            for tail in permutations(subset[1:]):
                cyc=(subset[0],)+tail
                g=list(identity)
                for j in range(k):
                    g[cyc[j]]=cyc[(j+1)%k]
                out.append((tuple(g),k))
    return out


def cyctype(p):
    seen=set(); sizes=[]
    for start in range(len(p)):
        if start not in seen:
            t=start; length=0
            while t not in seen:
                seen.add(t); length+=1; t=p[t]
            if length>1: sizes.append(length)
    return tuple(sorted(sizes))


def composition(a,b):
    return tuple(a[b[j]] for j in range(len(a)))


def run(n):
    assert 6<=n<=7
    identity=tuple(range(n))
    v=list(permutations(range(n)))
    index={p:i for i,p in enumerate(v)}
    generators=cycles(n)
    dist=[float('inf')]*len(v)
    dist[index[identity]]=0.
    heap=[(0.,index[identity])]
    while heap:
        d,i=heappop(heap)
        if d>dist[i]+1e-10:continue
        p=v[i]
        for g,k in generators:
            q=composition(p,g)
            j=index[q]
            newd=d+sqrt(2*k)
            if newd<dist[j]-1e-10:
                dist[j]=newd
                heappush(heap,(newd,j))
    checked=0
    for p,d in zip(v,dist):
        t=cyctype(p)
        if sum(t)<=5:
            expected=sum(sqrt(2*k) for k in t)
            assert abs(expected-d)<1e-9,(p,t,d,expected)
            checked+=1
        if t==(2,2,2):
            assert abs(d-(sqrt(6)+sqrt(12)))<1e-9,(p,t,d)
            checked+=1
    target=list(identity)
    for a in range(0,6,2):
        target[a],target[a+1]=target[a+1],target[a]
    target=tuple(target)
    counts=Counter()
    for a,k in generators:
        if k not in (3,6):continue
        for b,l in generators:
            if k+l!=9:continue
            if composition(a,b)==target:
                counts[(k,l)]+=1
    assert counts=={(3,6):16,(6,3):16},counts
    print('BIRKHOFF_WEIGHTED_METRIC_PASS', 'n=',n,'vertices=',len(v),
          'validated_pairs=',checked,'ordered_geodesics=',sum(counts.values()))

if __name__=='__main__':
    run(int(sys.argv[1]) if len(sys.argv)>1 else 6)
