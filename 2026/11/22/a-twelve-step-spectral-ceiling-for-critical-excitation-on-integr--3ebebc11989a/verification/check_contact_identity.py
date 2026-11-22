#!/usr/bin/env python3
"""Direct test of the critical contact identity on small recurrent orbits.
Uses an independent integer-encoding state iterator and exact adjacency sums.
"""

def graph_cycle(n,offset=0):
    return [{offset+(j-1)%n,offset+(j+1)%n} for j in range(n)]

def graph_disjoint_cycles(*ns):
    res=[]
    for n in ns:
        res+=graph_cycle(n,len(res))
    return res

def graph_octahedron():
    return [{j for j in range(6) if j//2 != i//2} for i in range(6)]

def step(x,g,r):
    y=[]
    for i,xi in enumerate(x):
        y.append(2 if xi==1 else 0 if xi==2 else (1 if sum(x[j]==1 for j in g[i])>=r else 0))
    return tuple(y)

def check(g,r):
    n=len(g)
    assert all(len(ns)==2*r for ns in g)
    periods=0
    for k in range(3**n):
        a=[];v=k
        for _ in range(n):
            a.append(v%3);v//=3
        x=tuple(a)
        seen={};seq=[]
        while x not in seen:
            seen[x]=len(seq);seq.append(x)
            x=step(x,g,r)
        orbit=seq[seen[x]:]
        L=len(orbit)
        for t in range(L):
            previous=orbit[(t-1)%L]
            now=orbit[t]
            nxt=orbit[(t+1)%L]
            for i,nb in enumerate(g):
                lhs=sum(now[j]==1 for j in nb)
                rhs=r*((previous[i]==1)+(nxt[i]==1))
                assert lhs==rhs,(n,r,orbit,t,i,lhs,rhs)
        periods+=1
    return periods

for name,g,r in [('C3',graph_cycle(3),1),('C4',graph_cycle(4),1),('C3_disjoint_C4',graph_disjoint_cycles(3,4),1),('octahedron',graph_octahedron(),2)]:
    n=check(g,r)
    print(name,'checked recurrent-orbit contact identity across',n,'initial states')
