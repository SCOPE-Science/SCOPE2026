#!/usr/bin/env python3
"""Exact edge-failure monitoring census for GP(10,2), Python standard library only."""
from collections import Counter, deque
from itertools import combinations

N=20
EDGES=sorted({tuple(sorted(pair)) for i in range(10) for pair in
    ((i,(i+1)%10),(i,10+i),(10+i,10+(i+2)%10))})
assert len(EDGES)==30

def distances(omit=None):
    adj=[[] for _ in range(N)]
    for ei,(u,v) in enumerate(EDGES):
        if ei!=omit:adj[u].append(v);adj[v].append(u)
    rows=[]
    for source in range(N):
        d=[N+1]*N;d[source]=0;q=deque([source])
        while q:
            v=q.popleft()
            for w in adj[v]:
                if d[w]>d[v]+1:d[w]=d[v]+1;q.append(w)
        rows.append(d)
    return rows

baseline=distances()
edge_deletions=[distances(ei) for ei in range(30)]
coverage=[[0]*N for _ in range(N)]
for i,j in combinations(range(N),2):
    for k,after in enumerate(edge_deletions):
        if after[i][j]>baseline[i][j]:coverage[i][j] |= 1<<k
        coverage[j][i]=coverage[i][j]

FULL=(1<<30)-1

def monitored(vertices):
    mask=0
    for i,j in combinations(vertices,2):mask|=coverage[i][j]
    return mask==FULL

assert sum(map(monitored,combinations(range(N),7)))==0
solutions=[frozenset(s) for s in combinations(range(N),8) if monitored(s)]
assert len(solutions)==25
independent=[s for s in solutions if all((u not in s or v not in s) for u,v in EDGES)]
others=[s for s in solutions if s not in independent]
assert (len(independent),len(others))==(5,20)
assert Counter(sum(u in s and v in s for u,v in EDGES) for s in others)=={3:20}
assert all(len({x for u,v in EDGES if u in s and v in s for x in (u,v)})==6 for s in others)
assert Counter(len(a&b) for a,b in combinations(solutions,2))=={0:30,2:80,3:60,4:90,5:40}
# For three-sensor simultaneous exchanges, exactly five vertices remain fixed.
adj={s:set() for s in solutions}
for s,t in combinations(solutions,2):
    if len(s&t)>=5:adj[s].add(t);adj[t].add(s)
assert Counter(map(len,adj.values()))=={8:5,2:20}
assert all(set(adj[s])<=set(independent) for s in others)
assert Counter(tuple(sorted(independent.index(a) for a in adj[s])) for s in others)=={
    pair:2 for pair in combinations(range(5),2)}
assert sum(len(v) for v in adj.values())//2==40

def all_eccentricities():
    out=[]
    for source in solutions:
        distance={source:0};queue=deque([source])
        while queue:
            v=queue.popleft()
            for w in adj[v]:
                if w not in distance:distance[w]=distance[v]+1;queue.append(w)
        assert len(distance)==25
        out.append(max(distance.values()))
    return Counter(out)
assert all_eccentricities()=={3:5,4:20}
print('PASS GP(10,2): meg=8, optima=25, classes=5+20, no <=2 exchanges, 3-exchange doubled K5 incidence, 40 edges, radius=3, diameter=4')
