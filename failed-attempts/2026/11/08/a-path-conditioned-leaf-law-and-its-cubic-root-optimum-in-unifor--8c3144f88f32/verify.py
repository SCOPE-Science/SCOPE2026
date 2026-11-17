#!/usr/bin/env python3
"""Exact finite checks for a distance-conditioned leaf law in labeled trees."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, exp, sqrt, e

checks=0

def verify(a,b,tag):
    global checks
    checks += 1
    if a != b:
        raise AssertionError((tag,a,b))

def trees(n):
    for code in product(range(n), repeat=n-2):
        degrees=[1]*n
        for v in code:degrees[v]+=1
        edges=[]
        for v in code:
            u=next(j for j in range(n) if degrees[j]==1)
            edges.append((u,v))
            degrees[u]-=1;degrees[v]-=1
        a,b=[j for j in range(n) if degrees[j]==1]
        edges.append((a,b))
        yield edges

def root_path(adjacency):
    parents={0:-1}
    fringe=[0]
    for a in fringe:
        if 1 in parents:break
        for b in adjacency[a]:
            if b not in parents:
                parents[b]=a;fringe.append(b)
    current=1
    route={current}
    while current!=0:
        current=parents[current];route.add(current)
    return route

def mean_prediction(n,d):
    if d==n-1:return Fraction(2)
    m=n-d-1
    return (Fraction(m)+Fraction(2*d,d+1))*Fraction(n-1,n)**(m-1)

def moment_prediction(n,d,r,s):
    k=d+1;m=n-k
    if m==0: return Fraction(comb(2,s) if r==0 else 0)
    if s>k:return Fraction(0)
    return Fraction(comb(m,r)*comb(2,s)*(k-s),k)*Fraction(n-r-s,n)**(m-1)

for n in range(3,9):
    tables=defaultdict(lambda:defaultdict(int))
    for edges in trees(n):
        adj=[set() for _ in range(n)]
        for a,b in edges:
            adj[a].add(b);adj[b].add(a)
        p=root_path(adj)
        d=len(p)-1
        X=sum(len(adj[v])==1 for v in range(n) if v not in p)
        Y=sum(len(adj[v])==1 for v in (0,1))
        tables[d][(X,Y)]+=1
    verify(sum(sum(z.values()) for z in tables.values()),n**(n-2),('tree-total',n))
    for d in range(1,n):
        counts=tables[d]
        den=sum(counts.values())
        verify(den>0,True,('distance-found',n,d))
        mean=Fraction(sum((X+Y)*c for (X,Y),c in counts.items()),den)
        verify(mean,mean_prediction(n,d),('conditional-mean',n,d))
        for r in range(n-d):
            for s in range(3):
                observed=Fraction(sum(c*comb(X,r)*comb(Y,s) for (X,Y),c in counts.items()),den)
                verify(observed,moment_prediction(n,d,r,s),('joint-factorial-moment',n,d,r,s))
    print('exhaustive Pruefer n=',n,'total=',n**(n-2))

for n in range(3,75):
    seq=[mean_prediction(n,d) for d in range(1,n)]
    for d in range(1,n-2):
        q=Fraction(n-1,n)
        difference=q**(n-d-3)*Fraction(2*(n-1)-d*(d+1)**2,n*(d+1)*(d+2))
        verify(seq[d]-seq[d-1],difference,('finite-difference',n,d))
    peaks=[d for d,mu in enumerate(seq,1) if mu==max(seq)]
    approximate=[d for d in range(1,n) if (d==1 or seq[d-1]>=seq[d-2]) and (d==n-1 or seq[d-1]>=seq[d])]
    verify(peaks,approximate,('peak',n))
    verify(len(peaks)<=2 and max(peaks)-min(peaks)<=1,True,('unimodality',n))

for n in (10000,100000,1000000):
    for z in (.5,1,2,3):
        d=max(1,int(z*sqrt(n)))
        observed=float(mean_prediction(n,d))-n/e
        expected=(5-z*z)/(2*e)
        if n==1000000:
            verify(abs(observed-expected)<0.025,True,('rayleigh-scale-numerical',n,z))
print('ALL VERIFIED: ', checks, ' exact/controlled checks')
