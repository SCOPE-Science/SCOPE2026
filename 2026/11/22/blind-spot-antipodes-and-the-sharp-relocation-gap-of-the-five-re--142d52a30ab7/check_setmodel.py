#!/usr/bin/env python3
"""Independent standard-library check using the empty/singleton/pair model.

Vertices: the empty set, five singleton sets, and ten two-element subsets of [5].
Adjacency: empty-singleton, singleton-pair incidence, and disjointness of pairs.
"""
from itertools import combinations
from collections import Counter,deque

A=(1,2,3,4,5)
V=(frozenset(),)+tuple(frozenset((i,)) for i in A)+tuple(frozenset(p) for p in combinations(A,2))
assert len(V)==16

def linked(x,y):
    if x==y:return False
    lx,ly=len(x),len(y)
    if {lx,ly}=={0,1}:return True
    if {lx,ly}=={1,2}:return (x<=y or y<=x)
    return lx==ly==2 and not (x&y)

N={x:{y for y in V if linked(x,y)} for x in V}
assert all(len(N[x])==5 for x in V)
assert all(linked(x,y)==linked(y,x) for x in V for y in V)

def closure(s):
    marked=set(s)
    for x in s: marked|=N[x]
    while True:
        ready=set()
        for x in marked:
            z=N[x]-marked
            if len(z)==1:ready|=z
        if not ready:return marked
        marked|=ready

def ok(s):return len(closure(s))==16
for k in (1,2):assert all(not ok(p) for p in combinations(V,k))
S={frozenset(p) for p in combinations(V,3) if ok(p)}
assert len(S)==320
kind=lambda p:sum(linked(x,y) for x,y in combinations(p,2))
assert Counter(kind(p) for p in S)=={0:160,2:160}
assert all(ok(p)==(kind(p)!=1) for p in combinations(V,3))

# Separate graph construction: compare pairs of configurations directly, without swaps.
configs=sorted(S,key=lambda p:tuple(sorted((tuple(sorted(x)) for x in p))))
ids={p:i for i,p in enumerate(configs)}
J=[set() for _ in configs];T=[set() for _ in configs]
for i in range(len(configs)):
    for j in range(i+1,len(configs)):
        s,t=configs[i],configs[j]
        if len(s&t)!=2:continue
        J[i].add(j);J[j].add(i)
        a=next(iter(s-t));b=next(iter(t-s))
        if linked(a,b):T[i].add(j);T[j].add(i)
assert sum(len(a) for a in J)//2==3360
assert sum(len(a) for a in T)//2==1120
assert Counter((kind(configs[i]),len(T[i])) for i in range(320)) == {(0,9):160,(2,5):160}

def BFS(adj,root):
    dist={root:0}; Q=deque([root])
    while Q:
        i=Q.popleft()
        for j in adj[i]:
            if j not in dist:dist[j]=dist[i]+1;Q.append(j)
    return dist

hJ=Counter();hT=Counter();hD=Counter()
for i,s in enumerate(configs):
    a=BFS(J,i);b=BFS(T,i)
    assert len(a)==len(b)==320
    assert max(a.values())==3 and max(b.values())==6
    unseen=frozenset(set(V)-set().union(*(N[v]|{v} for v in s)))
    assert len(unseen)==3 and unseen in S and kind(s)+kind(unseen)==2
    assert [j for j in b if b[j]==6]==[ids[unseen]]
    assert a[ids[unseen]]==3
    for j in range(i+1,320):
        hJ[a[j]]+=1;hT[b[j]]+=1;hD[b[j]-a[j]]+=1
assert hJ==Counter({1:3360,2:20160,3:27520})
assert hT==Counter({1:1120,2:5840,3:18400,4:20720,5:4800,6:160})
assert hD==Counter({0:12560,1:27520,2:10800,3:160})
print('PASS set-system construction, 320 minimum configurations, both complete shortest-path matrices')
print('jump distance histogram',sorted(hJ.items()))
print('slide distance histogram',sorted(hT.items()))
print('additional local slides',sorted(hD.items()))
