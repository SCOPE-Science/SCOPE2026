#!/usr/bin/env python3
"""Independent finite tests for exact-cardinality cut shattering."""
from itertools import combinations, product
from math import comb, factorial
from collections import Counter

def parts(n):
    if n == 0:
        yield ()
    else:
        yield from recparts(n,1)
def recparts(n,mn):
    if n==0:
        yield ()
    for t in range(mn,n+1):
        for tail in recparts(n-t,t):
            yield (t,)+tail

def criterion(n,k,edges):
    p=list(range(n))
    def root(v):
        while p[v]!=v:
            p[v]=p[p[v]];v=p[v]
        return v
    for u,v in edges:
        a,b=root(u),root(v)
        if a==b: return False
        p[a]=b
    groups={}
    for i in range(n):groups.setdefault(root(i),0);groups[root(i)]+=1
    sizes=list(groups.values())
    nons=[t for t in sizes if t>=2]
    isolated=len(sizes)-len(nons)
    for a in product(*(range(t//2+1) for t in nons)):
        totals={0}
        for t,b in zip(nons,a):
            totals={v+w for v in totals for w in (b,t-b)}
        if not any(0<=k-v<=isolated for v in totals):return False
    return True

def brute(n,k,edges):
    observed=set(); target=1<<len(edges)
    for A in combinations(range(n),k):
        A=set(A)
        observed.add(sum((((u in A) != (v in A)) << i) for i,(u,v) in enumerate(edges)))
        if len(observed)==target:return True
    return False

def countpart(n,part):
    cc=Counter(part)
    den=1
    for t,m in cc.items():
        den*=factorial(t)**m*factorial(m)
    treeprod=1
    for t in part:
        if t>=2:treeprod*=t**(t-2)
    return factorial(n)*treeprod//den

def size_good(n,k,part):
    # One fixed forest of each component size realizes the same traces.
    edges=[];at=0
    for t in part:
        edges +=[(at,at+i) for i in range(1,t)]
        at+=t
    return criterion(n,k,edges)

checks=0
for n in range(2,7):
    edges=list(combinations(range(n),2)); polynomial=Counter()
    for mask in range(1<<len(edges)):
        S=[e for i,e in enumerate(edges) if mask>>i&1]
        for k in range(1,n):
            a=criterion(n,k,S);b=brute(n,k,S)
            assert a==b,(n,k,S,a,b)
            if a: polynomial[k,len(S)]+=1
            checks+=1
    for k in range(1,n):
        predicted=Counter()
        for part in parts(n):
            if size_good(n,k,part):predicted[n-len(part)]+=countpart(n,part)
        assert all(polynomial[k,s]==predicted[s] for s in set(predicted)|{s for j,s in polynomial if j==k}), (n,k,polynomial,predicted)
        r=min(k,n-k)
        if n>=3*r+1:
            assert max(s for j,s in polynomial if j==k)==2*r, (n,k)
print('BALANCED_CUT_FOREST_CRITERION_PASS',checks,'independent support-cardinality cases, partitions checked through n=6')
