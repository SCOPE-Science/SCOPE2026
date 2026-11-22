#!/usr/bin/env python3
"""Finite exact checks for single-arrow random-map cycle transitions (standard library only)."""
from fractions import Fraction as Q
from itertools import product
from math import comb, factorial, exp, lgamma, log, sqrt, pi


def component_cycles(a):
    n=len(a); visited=set(); count=0
    for v in range(n):
        if v in visited: continue
        path=set();w=v
        while w not in visited and w not in path:
            path.add(w);w=a[w]
        if w in path: count+=1
        visited.update(path)
    return count


def ancestral_set(g,v=0):
    n=len(g); B=set()
    for i in range(n):
        x=i;vis=set()
        while x!=v and x not in vis:
            vis.add(x);x=g[x]
        if x==v: B.add(i)
    return B


def pmass(n,k):
    count=comb(n-1,k-1)*(k**(k-2) if k>1 else 1)*((n-k)**(n-k) if k<n else 1)
    return Q(count,n**(n-1))


def heightmass(k,h):
    if h==0:return Q(1,k)
    ff=1
    for i in range(h):ff*=k-1-i
    return Q((h+1)*ff,k**(h+1))


def enum(n):
    counts={}
    for rest in product(range(n),repeat=n-1):
        g=(0,)+rest
        B=ancestral_set(g)
        k=len(B)
        counts[('B',k)]=counts.get(('B',k),0)+1
        for a in range(n):
            f=(a,)+rest;c=component_cycles(f)
            for b in range(n):
                f2=(b,)+rest;delta=component_cycles(f2)-c
                assert delta==(int(b in B)-int(a in B))
                if delta:
                    x=b if delta==1 else a
                    h=0;y=x
                    while y!=0:
                        y=g[y];h+=1
                        assert h<=n
                    t=(delta,k,h)
                    counts[t]=counts.get(t,0)+1
    tot=n**(n+1)
    for k in range(1,n+1):
        assert Q(counts.get(('B',k),0),n**(n-1))==pmass(n,k)
        assert sum(heightmass(k,h) for h in range(k))==1
        for s in [-1,1]:
            for h in range(k):
                a=Q(counts.get((s,k,h),0),tot)
                b=pmass(n,k)*Q(k*(n-k),n*n)*heightmass(k,h)
                assert a==b,(n,k,s,h,a,b)
    print('exact enumeration passed n=',n,' n^n+1=',tot)

for n in range(2,6):enum(n)

# Hand-coded Prufer tree to check the Cayley height law, independently of random mappings.
def tree_from_prufer(seq,k):
    degree=[1]*k
    for x in seq:degree[x]+=1
    adj=[[] for _ in range(k)]
    for x in seq:
        leaf=min(i for i in range(k) if degree[i]==1)
        adj[leaf].append(x);adj[x].append(leaf)
        degree[leaf]-=1;degree[x]-=1
    u,v=[i for i in range(k) if degree[i]==1]
    adj[u].append(v);adj[v].append(u)
    return adj

for k in range(2,7):
    d=[0]*k
    for seq in product(range(k),repeat=k-2):
        adj=tree_from_prufer(seq,k)
        seen={0};front=[0];dep={0:0}
        for v in front:
            for w in adj[v]:
                if w not in seen:
                    seen.add(w);dep[w]=dep[v]+1;front.append(w)
        for h in dep.values():d[h]+=1
    for h,count in enumerate(d):assert Q(count,k**(k-1))==heightmass(k,h),(k,h,count)
    print('Cayley root depth passed k=',k,'trees',k**(k-2))

# Asymptotic intensity and conditional beta mean, via log-gamma stable finite sums.
for n in (100,1000,10000):
    weights=[]
    for k in range(1,n):
        logpm=lgamma(n)-lgamma(k)-lgamma(n-k+1)+(k-2)*log(k)+(n-k)*log(n-k)-(n-1)*log(n)
        weights.append(exp(logpm)*k*(n-k)/n**2)
    rate=sum(weights)
    beta_mean=sum(weights[k-1]*k/n for k in range(1,n))/rate
    print('n',n,'sqrt(n)*Pbirth',rate*sqrt(n),'target',sqrt(pi/8),'conditional basin mean',beta_mean,'target',0.25)
    assert abs(beta_mean-.25)<.05 and abs(rate*sqrt(n)-sqrt(pi/8))<.07
print('All checks passed.')
