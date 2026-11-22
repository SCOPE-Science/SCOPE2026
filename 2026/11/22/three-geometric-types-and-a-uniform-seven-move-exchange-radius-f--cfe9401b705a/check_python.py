#!/usr/bin/env python3
"""Exhaustive independent distance-code checker for G(8,3). Requires networkx 3.x for orbit computation."""
import itertools
from collections import Counter, deque
import networkx as nx

N=16
G=nx.Graph();G.add_nodes_from(range(N))
for i in range(8):
    G.add_edge(i,(i+1)%8)
    G.add_edge(i,8+i)
    G.add_edge(8+i,8+(i+3)%8)
assert G.number_of_edges()==24 and all(d==3 for _,d in G.degree()) and nx.is_connected(G)
dist=dict(nx.all_pairs_shortest_path_length(G))

def wtr(s):
    W=[i for i in range(N) if s & 1<<i]
    code={i:tuple(dist[i][w] for w in W) for i in range(N)}
    if len(set(code.values()))!=N:return False
    for v in W:
        for u in range(N):
            if s>>u&1:continue
            if sum(code[u][j]!=code[v][j] for j in range(len(W))) <2:return False
    return True

def fault_tolerant(s):
    W=[i for i in range(N) if s & 1<<i]
    if not W:return False
    return all(all(sum(dist[u][w]!=dist[v][w] for w in W if w!=removed)>0
         for u in range(N) for v in range(u+1,N)) for removed in W)

# Pure weak-total condition omits distinguishing pairs of two unselected vertices.
def pure_wtr(s):
    W=[i for i in range(N) if s>>i&1]
    return all(any(dist[v][z]!=dist[u][z] for z in W if z!=v)
               for v in W for u in range(N) if not s>>u&1)
assert sum(pure_wtr(s) for s in range(1<<N) if s.bit_count()==1)==0
assert sum(pure_wtr(s) for s in range(1<<N) if s.bit_count()==2)==8

allgood={s for s in range(1<<N) if wtr(s)}
counts=Counter(s.bit_count() for s in allgood)
assert dict(sorted(counts.items()))=={5:192,6:2712,7:8288,8:11966,9:11328,10:8008,11:4368,12:1820,13:560,14:120,15:16,16:1}
minimal={s for s in allgood if not any(s^(1<<i) in allgood for i in range(N) if s>>i&1)}
assert dict(sorted(Counter(s.bit_count() for s in minimal).items()))=={5:192,6:1080,7:192,8:2}
opt={s for s in allgood if s.bit_count()==5}
assert len(opt)==192
ft=[s for s in range(1<<N) if s.bit_count()<=6 and fault_tolerant(s)]
assert len(ft)==336 and all(s.bit_count()==6 for s in ft)

# Independent graph-isomorphism enumeration validates all orbit memberships.
autos=list(nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter())
assert len(autos)==96
remaining=set(opt);orbits=[]
while remaining:
    s=min(remaining)
    orb={sum(1<<a[i] for i in range(N) if s>>i&1) for a in autos}
    assert orb<=opt
    remaining-=orb
    rep=[i for i in range(N) if s>>i&1]
    deg=tuple(sorted(d for _,d in G.subgraph(rep).degree()))
    orbits.append((len(orb),rep,deg))
assert sorted((size,deg) for size,rep,deg in orbits)==[(48,(0,0,0,0,0)),(48,(0,0,1,1,2)),(96,(1,1,1,1,2))]

# Single-token replacement, with every intermediate set remaining an optimum.
neighbor={s:set() for s in opt}
for s in opt:
    for i in range(N):
        if not (s>>i&1):continue
        for j in range(N):
            if s>>j&1:continue
            t=s^(1<<i)^(1<<j)
            if t in opt:neighbor[s].add(t)
assert {len(x) for x in neighbor.values()}=={5}
profiles=set()
for s in opt:
    queue=deque([s]); d={s:0}
    while queue:
        q=queue.popleft()
        for t in neighbor[q]:
            if t not in d:d[t]=d[q]+1;queue.append(t)
    assert len(d)==len(opt)
    profiles.add(tuple(Counter(d.values())[k] for k in range(8)))
assert profiles=={(1,5,14,40,74,42,14,2)}
print('PASS: 65536 masks, WTR polynomial',dict(sorted(counts.items())))
print('PASS: minimal spectrum',dict(sorted(Counter(s.bit_count() for s in minimal).items())))
print('PASS: FTR size-six count',len(ft),'pure WTR two-set count 8')
print('PASS: automorphisms',len(autos),'orbits',sorted(orbits))
print('PASS: optimum exchange degree 5, diameter 7, common distance profile',profiles.pop())
