#!/usr/bin/env python3
"""Exhaustive, standard-library verifier for vertex-landmark reconfiguration.

Graph labels and edges are fixed in EDGES. No external data or packages required.
"""
from collections import Counter, deque
from itertools import combinations
import json

N = 12
EDGES = [
    (0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),(2,3),
    (2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),(5,10),
    (5,11),(6,10),(6,11),(7,8),(7,11),(8,10),(9,10),(9,11),
]
ADJ = [set() for _ in range(N)]
for u,v in EDGES:
    ADJ[u].add(v)
    ADJ[v].add(u)
assert len(EDGES)==24 and all(len(q)==4 for q in ADJ)


def distances(start, neighbors):
    d = {start:0}
    queue=deque([start])
    while queue:
        u=queue.popleft()
        for v in neighbors(u):
            if v not in d:
                d[v]=d[u]+1
                queue.append(v)
    return d

D=[distances(v,lambda u: ADJ[u]) for v in range(N)]
assert all(len(row)==N and max(row.values())==2 for row in D)

def resolves(subset):
    return len({tuple(D[v][landmark] for landmark in subset) for v in range(N)})==N

for size in range(4):
    assert not any(resolves(c) for c in combinations(range(N),size))
BASES=set(tuple(c) for c in combinations(range(N),4) if resolves(c))
assert len(BASES)==146


def network(slide):
    graph={s:set() for s in BASES}
    for s in BASES:
        for a in s:
            for b in (ADJ[a] if slide else range(N)):
                if b not in s:
                    t=tuple(sorted((set(s)-{a})|{b}))
                    if t in BASES: graph[s].add(t)
    assert all(s in graph[t] for t,L in graph.items() for s in L)
    assert all(t != s for s,L in graph.items() for t in L)
    return graph


def census(graph):
    degrees=Counter(len(v) for v in graph.values())
    edges=sum(len(v) for v in graph.values())//2
    shells=Counter()
    ecc=Counter()
    excess=Counter()
    centers=[]
    for s in sorted(graph):
        d=distances(s,lambda u:graph[u])
        assert len(d)==len(graph)
        e=max(d.values());ecc[e]+=1
        if e==min([4,5,6] if graph is slidegraph else [4]):
            centers.append(s)
        for t,length in d.items():
            if s < t:
                shells[length]+=1
                excess[length-(4-len(set(s)&set(t)))]+=1
    return {'states':len(graph),'edges':edges,
        'degrees':dict(sorted(degrees.items())), 'eccentricities':dict(sorted(ecc.items())),
        'distance_histogram_unordered':dict(sorted(shells.items())),
        'excess_over_exchange_lower_bound':dict(sorted(excess.items())),
        'radius':min(ecc),'diameter':max(ecc),
        'centers':centers if graph is slidegraph else 'all states'}

jumpgraph=network(False)
slidegraph=network(True)
jump=census(jumpgraph)
slide=census(slidegraph)
assert jump['edges']==928
assert jump['radius']==jump['diameter']==4
assert jump['excess_over_exchange_lower_bound']=={0:10367,1:218}
assert slide['edges']==452 and slide['eccentricities']=={4:2,5:104,6:40}
assert slide['centers']==[(2,8,9,11),(3,6,7,10)]
assert slide['excess_over_exchange_lower_bound']=={0:4463,1:4944,2:1070,3:92,4:16}
assert sum(slide['distance_histogram_unordered'].values())==146*145//2
print(json.dumps({'graph':'Chvatal vertex-metric-basis relocation', 'TJ':jump,'TS':slide},sort_keys=True))
