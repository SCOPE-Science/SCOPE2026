#!/usr/bin/env python3
"""Exact paired-domination and reconfiguration census for the icosahedral graph.
Run with Python 3 standard library: python3 check_ring.py
"""
from itertools import combinations
from collections import Counter, deque
import json

N = 12
adj = [set() for _ in range(N)]
def edge(a, b):
    adj[a].add(b)
    adj[b].add(a)
for i in range(5):
    u, v = 1 + i, 6 + i
    for x, y in ((0, u), (11, v), (u, 1+(i+1)%5),
                 (v, 6+(i+1)%5), (u,v), (u,6+(i-1)%5)):
        edge(x,y)
assert sum(map(len,adj)) == 60

def distances(a):
    dist = {a: 0}
    Q=deque([a])
    while Q:
        u=Q.popleft()
        for v in adj[u]:
            if v not in dist:
                dist[v] = dist[u]+1
                Q.append(v)
    return dist
D = [distances(v) for v in range(N)]
ant = {v: next(w for w in range(N) if D[v][w] == 3) for v in range(N)}
assert all(ant[ant[v]] == v for v in range(N))
assert len({tuple(sorted((v,w))) for v,w in ant.items()}) == 6

def matched(S):
    a,b,c,d=sorted(S)
    return ((b in adj[a] and d in adj[c]) or
            (c in adj[a] and d in adj[b]) or
            (d in adj[a] and c in adj[b]))

def dominating(S):
    return all(u in S or bool(adj[u].intersection(S)) for u in range(N))

assert not any(dominating(set(S)) and (list(S)[1] in adj[list(S)[0]])
               for S in combinations(range(N),2))
states = [sum(1<<v for v in S) for S in combinations(range(N),4)
          if dominating(set(S)) and matched(set(S))]
assert len(states) == 135
# Every pair of opposite vertices dominates: their closed neighborhoods partition V.
for u in range(N):
    assert {u,*adj[u]}.isdisjoint({ant[u],*adj[ant[u]]})
    assert len({u,*adj[u]} | {ant[u],*adj[ant[u]]}) == N
# Every paired four-set contains an opposite pair; the edge-pair exhaustive
# check uses every disjoint pair from the 30 graph edges, not sampled orbits.
host_edges=[(u,v) for u in range(N) for v in adj[u] if u<v]
counts=[]; witnesses=set()
for a,b in host_edges:
    usable=[]
    for c,d in host_edges:
        if len({a,b,c,d})==4 and dominating({a,b,c,d}):
            usable.append((c,d))
            W={a,b,c,d}
            assert any(ant[x] in W for x in W)
            witnesses.add(sum(1<<x for x in W))
    counts.append(len(usable))
assert counts == [9]*30
assert witnesses == set(states)
# Explicit construction: one antipodal pair plus a neighbor of each endpoint.
by_opposite=set()
for u in range(N):
    w=ant[u]
    for v in adj[u]:
        for z in adj[w]:
            by_opposite.add(sum(1<<x for x in (u,w,v,z)))
assert by_opposite == set(states)
index = {s:i for i,s in enumerate(states)}
types = Counter()
for mask in states:
    S={v for v in range(N) if mask>>v&1}
    pairs=sum(ant[v] in S for v in S)//2
    induced=sum(len(adj[v].intersection(S)) for v in S)//2
    types[(pairs,induced)]+=1
    assert pairs >= 1
    assert any({u,ant[u]} <= S and
               any(v in adj[u] and w in adj[ant[u]]
                   for v,w in ((list(S-{u,ant[u]})[0],list(S-{u,ant[u]})[1]),
                               (list(S-{u,ant[u]})[1],list(S-{u,ant[u]})[0])))
               for u in S)
assert types == Counter({(1,2):60,(1,3):60,(2,2):15})

result={'order':N,'edges':30,'minimum_paired_domination':4,'states':len(states),
        'antipodal_pair_types':{'one_pair_two_edges':60,'one_pair_three_edges':60,'two_pairs':15}}
for mode in ('slide','jump'):
    graph=[set() for _ in states]
    for i,mask in enumerate(states):
        for u in range(N):
            if mask>>u&1:
                for v in range(N):
                    if not(mask>>v&1) and (mode == 'jump' or v in adj[u]):
                        new=mask^(1<<u)^(1<<v)
                        if new in index:graph[i].add(index[new])
    assert all(i in graph[j] for i,vs in enumerate(graph) for j in vs)
    comps=[]; unseen=set(range(len(states)))
    while unseen:
        Q=[min(unseen)];unseen.remove(Q[0])
        for x in Q:
            for y in graph[x]:
                if y in unseen:unseen.remove(y);Q.append(y)
        comps.append(Q)
    assert len(comps)==1
    ecc=[]
    for root in range(len(states)):
        dist={root:0};Q=deque([root])
        while Q:
            x=Q.popleft()
            for y in graph[x]:
                if y not in dist:dist[y]=dist[x]+1;Q.append(y)
        assert len(dist)==len(states)
        ecc.append(max(dist.values()))
    r={'edges':sum(map(len,graph))//2,'components':len(comps),
       'degree_counts':dict(sorted(Counter(map(len,graph)).items())),
       'radius':min(ecc),'diameter':max(ecc),
       'eccentricity_counts':dict(sorted(Counter(ecc).items()))}
    result[mode]=r
assert result['slide'] == {'edges':360,'components':1,'degree_counts':{4:60,6:60,8:15},'radius':6,'diameter':6,'eccentricity_counts':{6:135}}
assert result['jump'] == {'edges':720,'components':1,'degree_counts':{10:120,16:15},'radius':4,'diameter':4,'eccentricity_counts':{4:135}}
print(json.dumps(result,sort_keys=True,indent=2))
