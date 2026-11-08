#!/usr/bin/env python3
"""Finite independent checks for split-saturation queries on set partitions.

A query is an unordered split S|S^c; the oracle returns 1 iff each block
is contained in one shore.  This code checks full trace shattering against
private crossing-pair witnesses and Cayley's count of top faces.
"""
import itertools
from collections import Counter
from functools import lru_cache
from math import comb

def partitions(n):
    if n == 0:
        yield ()
        return
    def gen(a, highest):
        if len(a) == n:
            yield tuple(a)
            return
        for k in range(highest+2):
            yield from gen(a+[k],max(highest,k))
    yield from gen([0],0)

def splits(n):
    # Choose the shore NOT containing distinguished vertex n-1.
    return tuple(s for s in range(1,1<<(n-1)))

def saturated(p,s):
    bits={}
    for x,c in enumerate(p):
        b=(s>>x)&1
        if c in bits and bits[c]!=b:
            return 0
        bits[c]=b
    return 1

def private_witness(s,other,n):
    other=tuple(other)
    for x in range(n):
        for y in range(x+1,n):
            if bool((s>>x)&1)==bool((s>>y)&1):
                continue
            if all(bool((t>>x)&1)==bool((t>>y)&1) for t in other):
                return (x,y)
    return None

def direct_shatter(support,patterns):
    sub=set()
    for pat in patterns:
        key=0
        for i, s in enumerate(support):
            if pat[s]: key |= 1<<i
        sub.add(key)
        if len(sub)==1<<len(support):
            return True
    return len(sub)==1<<len(support)

def predicted(support,n):
    return all(private_witness(s,(t for t in support if t!=s),n) is not None for s in support)

def prufer_trees(n):
    if n==1:
        yield frozenset()
        return
    for word in itertools.product(range(n),repeat=n-2):
        degree=[1]*n
        for v in word: degree[v]+=1
        edges=[]
        for v in word:
            u=next(k for k in range(n) if degree[k]==1)
            edges.append(tuple(sorted((u,v))))
            degree[u]-=1;degree[v]-=1
        a,b=(k for k in range(n) if degree[k]==1)
        edges.append(tuple(sorted((a,b))))
        yield frozenset(edges)

def cuts_of_tree(n,edges):
    cuts=[]
    for x,y in edges:
        adj=[[] for _ in range(n)]
        for a,b in edges:
            if (a,b)==(x,y): continue
            adj[a].append(b);adj[b].append(a)
        reached={x};stack=[x]
        while stack:
            u=stack.pop()
            for v in adj[u]:
                if v not in reached:
                    reached.add(v);stack.append(v)
        shore=sum(1<<k for k in reached)
        if shore>>(n-1)&1:shore^=(1<<n)-1
        cuts.append(shore)
    return frozenset(cuts)


def main():
    for n in range(1,6):
        ss=splits(n)
        pp=list(partitions(n))
        patterns=[{s:saturated(p,s) for s in ss} for p in pp]
        counts=Counter(); shattered=set(); all_supports=0
        for m in range(len(ss)+1):
            for support in itertools.combinations(ss,m):
                all_supports+=1
                theory=predicted(support,n)
                actual=direct_shatter(support,patterns)
                assert theory==actual,(n,support,theory,actual)
                if actual:
                    counts[m]+=1
                    shattered.add(frozenset(support))
        top=frozenset(s for s in shattered if len(s)==n-1)
        trees=set(cuts_of_tree(n,E) for E in prufer_trees(n))
        assert top==trees,(n,len(top),len(trees))
        assert len(top)==(n**(n-2) if n>=2 else 1)
        assert counts[1]==len(ss) if n>=2 else counts[1]==0
        if n>=2:assert counts[2]==comb(len(ss),2)
        facets=[s for s in shattered if not any(s<t for t in shattered)]
        sizes=dict(sorted(Counter(map(len,facets)).items()))
        print('n=%d Bell=%d splits=%d supports=%d Phi=%s top=%d tree=%d facet_sizes=%s'
          %(n,len(pp),len(ss),all_supports, [counts[k] for k in range(n)],len(top),len(trees),sizes))
        if n==4:
            short=next(s for s in facets if len(s)==2)
            print('nonpure_example_n4=',sorted(short))

    # Exact Littlestone dimensions for n up to four via bitmasked concept families.
    for n in range(1,5):
        ss=splits(n);pp=list(partitions(n))
        allc=(1<<len(pp))-1
        q1=[]
        for s in ss:
            mask=sum(1<<i for i,p in enumerate(pp) if saturated(p,s))
            q1.append(mask)
        @lru_cache(None)
        def ldim(C):
            d=0
            for mask in q1:
                yes=C&mask; no=C&~mask
                if yes and no:
                    d=max(d,1+min(ldim(yes),ldim(no)))
            return d
        val=ldim(allc)
        assert val==n-1,(n,val)
        print('Ldim n=%d: %d, memoized=%d'%(n,val,ldim.cache_info().currsize))
    print('PARTITION_SPLITS_PASS')

if __name__=='__main__':main()
