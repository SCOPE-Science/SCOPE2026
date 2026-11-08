#!/usr/bin/env python3
"""Independent finite exhaustive checker: minimum domination and reconfiguration."""
from itertools import combinations
from collections import Counter

def neigh(n):
    ans=[]
    for a in range(2*n):
        i=a%n; row=a//n
        ans.append(sum(1<<b for b in {a, n*(1-row)+i, n*row+(i-1)%n, n*row+(i+1)%n}))
    return ans

def graph(n):
    nb=neigh(n); allv=(1<<(2*n))-1
    lower=(n+1)//2
    ff=set()
    for comb in combinations(range(2*n),lower):
        m=0; cov=0
        for v in comb:m|=1<<v;cov|=nb[v]
        if cov==allv:ff.add(m)
    assert ff,('no minimum domination found',n)
    AJ={s:set() for s in ff}; AS={s:set() for s in ff}
    for s in ff:
        for a in range(2*n):
            if not s>>a&1:continue
            for b in range(2*n):
                if s>>b&1:continue
                t=s^(1<<a)^(1<<b)
                if t in ff:
                    AJ[s].add(t)
                    if nb[a]>>b&1:AS[s].add(t)
    return ff, AS, AJ

def shape(A):
    seen=set(); parts=[]
    for s in A:
        if s in seen:continue
        q=[s];seen.add(s)
        for z in q:
            for t in A[z]:
                if t not in seen:seen.add(t);q.append(t)
        parts.append((len(q),Counter(len(A[t]) for t in q)))
    return Counter(x[0] for x in parts),Counter(len(ns) for ns in A.values()),sum(map(len,A.values()))//2

for n in range(3,13):
    if n%4==2:continue
    ff,slides,jumps=graph(n)
    cs,ds,es=shape(slides);cj,dj,ej=shape(jumps)
    if n==3:
        assert len(ff)==9 and (cs,ds,es)==(Counter({9:1}),Counter({4:9}),18)
        assert (cj,dj,ej)==(cs,ds,es)
    elif n%4==0:
        assert len(ff)==4 and (cs,ds,es)==(Counter({1:4}),Counter({0:4}),0)
        assert (cj,dj,ej)==(cs,ds,es)
    elif n%4==1:
        assert len(ff)==2*n and (cs,ds,es)==(Counter({1:2*n}),Counter({0:2*n}),0)
        assert (cj,dj,ej)==(Counter({2*n:1}),Counter({2:2*n}),2*n)
    else:
        assert len(ff)==2*n and (cs,ds,es)==(Counter({2*n:1}),Counter({2:2*n}),2*n)
        assert (cj,dj,ej)==(cs,ds,es)
    print('PASS n={} minima={} TS_edges={} TS_components={} TJ_edges={} TJ_components={}'.format(n,len(ff),es,dict(cs),ej,dict(cj)))
print('PASS: all checks completed')
