#!/usr/bin/env python3
"""Finite exact checks of the Fano incidence graph power-domination classification."""
from collections import Counter,deque
from itertools import combinations
from math import comb
D={0,1,3}
points=set(range(7)); lines=set(range(7,14)); universe=set(range(14))
adj=[set() for _ in range(14)]
for i in points:
    for j in range(7):
        if (j-i)%7 in D:
            adj[i].add(7+j); adj[7+j].add(i)
def success(s):
    colored=set(s)
    for v in s:colored|=adj[v]
    while 1:
        forced=set()
        for v in colored:
            u=adj[v]-colored
            if len(u)==1:forced|=u
        if not forced:return len(colored)==14
        colored|=forced

def predicted(s):
    return not any(s<=({v}|adj[v]) for v in range(14))

failed=Counter();pairs=[];all_masks=1<<14
for mask in range(all_masks):
    s={i for i in range(14) if mask & (1<<i)}
    want=predicted(s); got=success(s)
    assert want==got,(mask,want,got)
    if not got: failed[len(s)]+=1
    if got and len(s)==2:pairs.append(frozenset(s))
assert failed=={0:1,1:14,2:63,3:56,4:14},failed
assert len(pairs)==28
assert all(len(s&points)==1 and len(s&lines)==1 and not any(y in adj[x] for x in s for y in s if x!=y) for s in pairs)
assert all(len({v}|adj[v])==4 for v in range(14))
assert all(len(({u}|adj[u])&({v}|adj[v]))<=2 for u in range(14) for v in range(u+1,14))
# Single-element replacement graph on successful pairs; each is an edge of the nonincidence graph.
eig=[{i for i,b in enumerate(pairs) if i!=k and len(a&b)==1} for k,a in enumerate(pairs)]
assert all(len(x)==6 for x in eig)
diam=0
for k in range(len(pairs)):
    distance={k:0};q=deque([k])
    while q:
        x=q.popleft()
        for y in eig[x]:
            if y not in distance:
                distance[y]=distance[x]+1;q.append(y)
    assert len(distance)==28
    diam=max(diam,max(distance.values()))
assert diam==3,diam
# Counting failed subsets by size, independent from power propagation
expected=[1,14,63,56,14]+[0]*10
assert [failed[i] for i in range(15)]==expected
print('PASS geometry: 16384 subsets; failed 1,14,63,56,14; 28 optimal pairs; exchange degree 6, diameter 3, edges 84')
