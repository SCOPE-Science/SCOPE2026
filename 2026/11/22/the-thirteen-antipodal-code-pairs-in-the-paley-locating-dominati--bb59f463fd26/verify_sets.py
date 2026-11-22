#!/usr/bin/env python3
"""Independent exhaustive proof checker: edge-list, immutable sets, Floyd-Warshall distances."""
from itertools import combinations
from collections import Counter, deque
p=13
edges=set()
for i in range(p):
    for j in range(i+1,p):
        if any((j-i)%p==(r*r)%p for r in range(1,p)):
            edges.add((i,j))
def edge(i,j):return (min(i,j),max(i,j)) in edges if i!=j else False
assert len(edges)==39

def ld(code):
    remaining=[v for v in range(p) if v not in code]
    witnesses=[]
    for v in remaining:
        pattern=tuple(x for x in code if edge(x,v))
        if not pattern:return False
        witnesses.append(pattern)
    return len(set(witnesses))==len(remaining)

def ic(code):
    patt=[]
    for v in range(p):
        patt.append(tuple(x for x in code if x==v or edge(x,v)))
    return all(patt) and len(set(patt))==p

minsets=[]
for k in range(5):
    level=[t for t in combinations(range(p),k) if ld(t)]
    if k<4:assert not level
    else:minsets=level
assert len(minsets)==247
assert sum(ic(t) for t in minsets)==26

def compare(local):
    index={s:i for i,s in enumerate(minsets)}
    adj=[set() for _ in minsets]
    for i,s in enumerate(minsets):
        for t in minsets[i+1:]:
            lost=list(set(s)-set(t));gained=list(set(t)-set(s))
            if len(lost)!=1:continue
            if (not local) or edge(lost[0],gained[0]):
                adj[i].add(index[t]);adj[index[t]].add(i)
    dists={};ecc=[]
    for a in range(len(minsets)):
        D={a:0};q=deque([a])
        while q:
            v=q.popleft()
            for w in adj[v]:
                if w not in D:D[w]=D[v]+1;q.append(w)
        assert len(D)==247
        ecc.append(max(D.values()))
        for b in range(a+1,len(minsets)):dists[(a,b)]=D[b]
    return sum(map(len,adj))//2,Counter(len(x) for x in adj),Counter(ecc),Counter(dists.values()),ecc
J=compare(False);T=compare(True)
assert J[0]==1599 and J[2]==Counter({4:247})
assert T[0]==858 and T[2]==Counter({5:221,6:26})
assert T[1]==Counter({6:117,8:39,10:39,3:26,9:26})
assert all((T[4][i]==6)==ic(s) for i,s in enumerate(minsets))
# Independent all-pairs BFS identifies the thirteen antipodal pairs.
index={s:i for i,s in enumerate(minsets)}
neighbor=[set() for _ in minsets]
for i,s in enumerate(minsets):
    for j,t in enumerate(minsets[i+1:],start=i+1):
        out=set(s)-set(t);incoming=set(t)-set(s)
        if len(out)==1 and edge(next(iter(out)),next(iter(incoming))):
            neighbor[i].add(j);neighbor[j].add(i)
far=set()
for i in range(len(minsets)):
    d={i:0};q=deque([i])
    while q:
        u=q.popleft()
        for v in neighbor[u]:
            if v not in d:d[v]=d[u]+1;q.append(v)
    for j in range(i+1,len(minsets)):
        if d[j]==6:far.add(frozenset((minsets[i],minsets[j])))
a=(0,1,3,9);b=(0,4,10,12)
assert far=={frozenset((tuple(sorted((x+t)%p for x in a)),tuple(sorted((x+t)%p for x in b)))) for t in range(p)}
assert len(far)==13
print('PASS tuple/edge-list; min=247 identifier=26; jumping=1599 sliding=858')
print('jump_distance_hist',dict(sorted(J[3].items())))
print('slide_distance_hist',dict(sorted(T[3].items())))
