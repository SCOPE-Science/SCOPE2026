#!/usr/bin/env python3
"""Independent geodesic-count exhaustive certificate using a planar dodecahedron labeling."""
from collections import Counter,deque
from itertools import combinations

N=20
E=[(0,1),(0,10),(0,19),(1,2),(1,8),(2,3),(2,6),(3,4),(3,19),(4,5),
   (4,17),(5,6),(5,15),(6,7),(7,8),(7,14),(8,9),(9,10),(9,13),(10,11),
   (11,12),(11,18),(12,13),(12,16),(13,14),(14,15),(15,16),(16,17),(17,18),(18,19)]
assert len(E)==30
# Explicit isomorphism: GP(10,2) vertices 0..9,10..19 map to this planar labeling.
MAP=[0,1,8,7,14,15,16,17,18,19,10,2,9,6,13,5,12,4,11,3]
gp_edges={tuple(sorted((MAP[a],MAP[b]))) for i in range(10) for a,b in
          ((i,(i+1)%10),(i,10+i),(10+i,10+(i+2)%10))}
assert gp_edges==set(E)
A=[[] for _ in range(N)]
for a,b in E:A[a].append(b);A[b].append(a)

def bfs(start):
    dist=[-1]*N;ways=[0]*N;dist[start]=0;ways[start]=1;Q=deque([start])
    while Q:
        a=Q.popleft()
        for b in A[a]:
            if dist[b]<0:dist[b]=dist[a]+1;Q.append(b)
            if dist[b]==dist[a]+1:ways[b]+=ways[a]
    return dist,ways
D=[];P=[]
for i in range(N):
    d,p=bfs(i);D.append(d);P.append(p)
assert all(min(d)>=0 for d in D)
cover={}
for s,t in combinations(range(N),2):
    mask=0
    for k,(a,b) in enumerate(E):
        passes=0
        if D[s][a]+1+D[b][t]==D[s][t]:passes+=P[s][a]*P[b][t]
        if D[s][b]+1+D[a][t]==D[s][t]:passes+=P[s][b]*P[a][t]
        if passes==P[s][t]:mask|=1<<k
    cover[s,t]=mask

def is_meg(vertices):
    mask=0
    for p in combinations(vertices,2):mask|=cover[p]
    return mask==(1<<30)-1

assert sum(is_meg(s) for s in combinations(range(N),7))==0
sets=[frozenset(s) for s in combinations(range(N),8) if is_meg(s)]
assert len(sets)==25
ind=[s for s in sets if not any(a in s and b in s for a,b in E)]
non=[s for s in sets if s not in ind]
assert len(ind)==5 and len(non)==20
assert all(sum(a in s and b in s for a,b in E)==3 for s in non)
assert all(len({v for a,b in E if a in s and b in s for v in (a,b)})==6 for s in non)
counts=Counter();nbrs={s:set() for s in sets}
for s,t in combinations(sets,2):
    shared=len(s&t);counts[shared]+=1
    if shared>=5:nbrs[s].add(t);nbrs[t].add(s)
assert sum(counts.values())==300
assert counts=={0:30,2:80,3:60,4:90,5:40}
assert all(len(nbrs[s])==8 for s in ind)
assert all(len(nbrs[s])==2 and nbrs[s]<=set(ind) for s in non)
assert len({frozenset(nbrs[s]) for s in non})==10
assert Counter(frozenset(nbrs[s]) for s in non)=={frozenset(p):2 for p in combinations(ind,2)}
# Distances in the graph of moves exchanging exactly three selected vertices.
ecc={}
for source in sets:
    paths={source:0};q=deque([source])
    while q:
        a=q.popleft()
        for b in nbrs[a]:
            if b not in paths:paths[b]=paths[a]+1;q.append(b)
    assert len(paths)==25
    ecc[source]=max(paths.values())
assert Counter(ecc.values())=={3:5,4:20}
print('PASS planar labeling: independently checked 7-sets, 8-sets, shortest-path counts, pair-intersection profile, doubled K5 incidence and eccentricities')
