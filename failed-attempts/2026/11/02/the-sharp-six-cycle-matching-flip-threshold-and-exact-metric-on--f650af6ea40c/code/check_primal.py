#!/usr/bin/env python3
"""Exact enumeration of all icosahedral perfect matchings and bounded flips.
Independent coordinates: two pentagonal rings and two poles; stdlib only.
"""
from collections import Counter, deque

V = set(range(12))
E = set()
def edge(a,b): E.add(tuple(sorted((a,b))))
for i in range(5):
    j = (i+1)%5
    edge(0, 1+i); edge(11, 6+i)
    edge(1+i, 1+j); edge(6+i, 6+j)
    edge(1+i, 6+i); edge(1+i, 6+((i-1)%5))
E = sorted(E)
assert len(E)==30 and len(V)==12
adj = {v: [] for v in V}
for idx,(a,b) in enumerate(E):
    adj[a].append((b,idx)); adj[b].append((a,idx))
assert set(len(adj[v]) for v in V)=={5}
matchings=[]
def extend(rem,mask):
    if not rem:
        matchings.append(mask);return
    v=min(rem)
    for w,j in adj[v]:
        if w in rem: extend(rem-{v,w},mask|(1<<j))
extend(V,0)
assert len(matchings)==125 and len(set(matchings))==125
A4=[set() for _ in matchings]; A6=[set() for _ in matchings]
for i,p in enumerate(matchings):
    for j in range(i):
        diff=p^matchings[j]
        touched=[k for k in range(len(E)) if (diff>>k)&1]
        n=len(touched)
        if n not in (4,6):continue
        counts=Counter(v for k in touched for v in E[k])
        # Two matchings produce disjoint alternating cycles; with n distinct
        # endpoints and degree 2 each, the difference is one n-cycle.
        if len(counts)==n and all(c==2 for c in counts.values()):
            (A4 if n==4 else A6)[i].add(j)
            (A4 if n==4 else A6)[j].add(i)
assert sum(map(len,A4))//2==300
assert sum(map(len,A6))//2==580
assert Counter(map(len,A4))=={0:5,3:20,5:60,6:40}
frozen=[i for i in range(125) if not A4[i]]
assert len(frozen)==5
assert Counter(k for i in frozen for k in range(30) if (matchings[i]>>k)&1)=={k:1 for k in range(30)}
def components(A):
    seen=set();sizes=[]
    for s in range(len(A)):
        if s in seen:continue
        todo=[s];seen.add(s);ct=0
        while todo:
            v=todo.pop();ct+=1
            for w in A[v]:
                if w not in seen:seen.add(w);todo.append(w)
        sizes.append(ct)
    return sorted(sizes)
assert components(A4)==[1]*5+[120]
A=[A4[i]|A6[i] for i in range(125)]
assert sum(map(len,A))//2==880
assert components(A)==[125]
assert Counter(map(len,A))=={8:5,11:20,14:30,15:60,18:10}
pairdist=Counter();ecc=Counter()
for s in range(125):
    dist={s:0};todo=deque([s])
    while todo:
        v=todo.popleft()
        for w in A[v]:
            if w not in dist:
                dist[w]=dist[v]+1;todo.append(w)
    assert len(dist)==125
    ecc[max(dist.values())]+=1
    pairdist.update(dist[j] for j in range(s))
assert ecc=={3:125}
# Distances among the five four-cycle-frozen configurations.
for s in frozen:
    d={s:0};q=deque([s])
    while q:
        v=q.popleft()
        for w in A[v]:
            if w not in d:d[w]=d[v]+1;q.append(w)
    assert all(d[t]==2 for t in frozen if t!=s)
assert pairdist=={1:880,2:4250,3:2620}
assert sum(pairdist.values())==125*124//2
print('ICOSAHEDRAL_PRIMAL_PAIR_DIFFERENCES_PASS')
print('perfect_matchings=125, four_cycle_edges=300, six_cycle_edges=580')
print('four_only_components=[120,1,1,1,1,1]; frozen_cover_all_30_edges')
print('four_plus_six_edges=880; degree_distribution='+str(dict(sorted(Counter(map(len,A)).items()))))
print('eccentricities='+str(dict(ecc))+'; distance_pairs='+str(dict(sorted(pairdist.items()))))
