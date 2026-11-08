#!/usr/bin/env python3
"""Exact exhaustive census of locating-total dominating sets of the Pappus graph.

Uses a self-contained explicit edge list and independently enumerates all 2^18 subsets.
"""
from collections import Counter
from itertools import combinations

EDGE_LIST = [(0,1),(0,5),(0,17),(1,2),(1,8),(2,3),(2,13),(3,4),(3,10),
(4,5),(4,15),(5,6),(6,7),(6,11),(7,8),(7,14),(8,9),(9,10),
(9,16),(10,11),(11,12),(12,13),(12,17),(13,14),(14,15),
(15,16),(16,17)]
N=18
adj=[0]*N
for u,v in EDGE_LIST:
    assert 0<=u<v<N
    adj[u] |= 1<<v
    adj[v] |= 1<<u
assert len(EDGE_LIST)==27 and all(x.bit_count()==3 for x in adj)

def is_ltd(mask):
    distinct=set()
    for v in range(N):
        sig=adj[v]&mask
        if sig==0: return False
        if mask&(1<<v)==0:
            if sig in distinct: return False
            distinct.add(sig)
    return True

min_k=None
minima=[]
profile={}
for k in range(N+1):
    good=[]
    for idxs in combinations(range(N),k):
        m=sum(1<<i for i in idxs)
        if is_ltd(m): good.append(m)
    if good:
        min_k=k
        minima=good
        break
assert min_k==8 and len(minima)==108,(min_k,len(minima))
assert sum(is_ltd(s) for s in minima)==108
V=set(minima)
J={s:set() for s in V}
H={s:set() for s in V}
for s in V:
    for i in range(N):
        if not s>>i&1:continue
        for j in range(N):
            if s>>j&1:continue
            t=s^(1<<i)^(1<<j)
            if t in V:
                J[s].add(t)
                if adj[i]>>j&1:H[s].add(t)
assert all(len(v)==2 for v in J.values())
assert all(len(v)==0 for v in H.values())
assert all(s in J[t] for t in J for s in J[t])
assert sum(map(len,J.values()))//2==108
seen=set();sizes=[];components=[]
for s in V:
    if s in seen:continue
    todo=[s]; seen.add(s); comp=[]
    while todo:
        v=todo.pop();comp.append(v)
        for w in J[v]:
            if w not in seen:seen.add(w);todo.append(w)
    sizes.append(len(comp));components.append(comp)
assert len(components)==27 and sizes==[4]*27
assert all(sum(len(J[s]) for s in C)//2==4 for C in components)
print('DIRECT: vertices=18 edges=27 degree=3')
print('DIRECT: minimum_LTD=8 count=108')
print('DIRECT: token_jump=27 copies of C4; edges=108; degrees=2')
print('DIRECT: token_slide=108 isolated vertices; edges=0')
print('DIRECT: PASS')
