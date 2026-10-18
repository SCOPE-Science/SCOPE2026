#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, product
from collections import deque

def connected_bipartite(p,q,edges):
    if not edges:
        return False
    N=p+q
    adj=[[] for _ in range(N)]
    for a,b in edges:
        u=a
        v=p+b
        adj[u].append(v); adj[v].append(u)
    seen={0}
    dq=deque([0])
    while dq:
        u=dq.popleft()
        for v in adj[u]:
            if v not in seen:
                seen.add(v); dq.append(v)
    return len(seen)==N

def hall_ok(p,q,edges):
    neigh=[set() for _ in range(p)]
    for a,b in edges:
        neigh[a].add(b)
    for mask in range(1<<p):
        X=[a for a in range(p) if (mask>>a)&1]
        NX=set()
        for a in X:
            NX |= neigh[a]
        if p*len(NX) < q*len(X):
            return False
    return True

def maxflow_ok(p,q,edges):
    # Integer scaling: each A needs q, each B has capacity p.
    N=2+p+q
    s=p+q
    t=s+1
    cap=[[0]*N for _ in range(N)]
    for a in range(p):
        cap[s][a]=q
    for a,b in edges:
        cap[a][p+b]=p*q
    for b in range(q):
        cap[p+b][t]=p

    flow=0
    while True:
        par=[-1]*N
        par[s]=s
        dq=deque([s])
        while dq and par[t]<0:
            u=dq.popleft()
            for v in range(N):
                if par[v]<0 and cap[u][v]>0:
                    par[v]=u
                    dq.append(v)
        if par[t]<0:
            break
        aug=10**9
        v=t
        while v!=s:
            u=par[v]
            aug=min(aug,cap[u][v])
            v=u
        v=t
        while v!=s:
            u=par[v]
            cap[u][v]-=aug
            cap[v][u]+=aug
            v=u
        flow+=aug
    return flow==p*q

def sphere_formula_standard(p,q,edges):
    # Center is (-1/p on A, +1/q on B).
    c=[-Fraction(1,p)]*p+[Fraction(1,q)]*q
    want=Fraction(2,1)-Fraction(1,p)-Fraction(1,q)
    for a,b in edges:
        v=[Fraction(0)]*(p+q)
        v[a]=-1
        v[p+b]=1
        d2=sum((v[i]-c[i])**2 for i in range(p+q))
        assert d2==want
    return want

# Exhaustive small standard bipartite graphs.
families=0
for p in range(1,5):
    for q in range(1,5):
        all_edges=[(a,b) for a in range(p) for b in range(q)]
        # Full exhaustive range is still small through 4x4 only if restricted by edge count.
        # Check all graphs for pq<=9; for 4x4 use all connected graphs with 8..10 edges plus complete.
        masks=[]
        if p*q<=9:
            masks=range(1,1<<(p*q))
        else:
            selected=[]
            for r in range(max(p+q-1,8),11):
                for comb in combinations(range(p*q),r):
                    m=0
                    for z in comb: m|=1<<z
                    selected.append(m)
            selected.append((1<<(p*q))-1)
            masks=selected
        for mask in masks:
            edges=[all_edges[i] for i in range(p*q) if (mask>>i)&1]
            if not connected_bipartite(p,q,edges):
                continue
            assert hall_ok(p,q,edges)==maxflow_ok(p,q,edges)
            sphere_formula_standard(p,q,edges)
            families+=1

# Multi-layer semi-balanced examples: every edge increases the supplied layer by one.
examples=[
    ([0,1,2], [(0,1),(1,2)]),
    ([0,0,1,1,2], [(0,2),(0,3),(1,2),(2,4),(3,4)]),
    ([0,1,1,2,2,3], [(0,1),(0,2),(1,3),(2,4),(3,5),(4,5)]),
]
for ell,edges in examples:
    n=len(ell)
    mean=Fraction(sum(ell),n)
    ell0=[Fraction(x)-mean for x in ell]
    s=sum(x*x for x in ell0)
    c=[x/s for x in ell0]
    want=Fraction(2,1)-1/s
    for t,h in edges:
        assert ell[h]-ell[t]==1
        v=[Fraction(0)]*n
        v[h]=1; v[t]=-1
        assert sum(v)==0
        assert sum(Fraction(ell[i])*v[i] for i in range(n))==1
        d2=sum((v[i]-c[i])**2 for i in range(n))
        assert d2==want

print(f"VERIFY_OK semibalanced-root-sphere bipartite_families={families} layered_examples={len(examples)} exact=yes")
