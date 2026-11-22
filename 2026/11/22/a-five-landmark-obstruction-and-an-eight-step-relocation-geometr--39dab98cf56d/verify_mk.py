#!/usr/bin/env python3
"""Exhaustive, standalone verification of edge landmark census on GP(8,3).
Only Python 3 standard library required. No precomputed feasible-set input.
"""
from collections import Counter, deque
from itertools import combinations

N=16
neighbors=[set() for _ in range(N)]
def join(a,b):
    neighbors[a].add(b); neighbors[b].add(a)
for i in range(8):
    join(i,(i+1)%8)
    join(i,8+i)
    join(8+i,8+(i+3)%8)
E=sorted((a,b) for a in range(N) for b in neighbors[a] if a<b)
assert len(E)==24 and all(len(v)==3 for v in neighbors)
# Breadth-first vertex distance, from the explicit adjacency graph.
d=[]
for src in range(N):
    dis=[-1]*N;dis[src]=0;q=deque([src])
    while q:
        x=q.popleft()
        for y in neighbors[x]:
            if dis[y]<0:
                dis[y]=dis[x]+1;q.append(y)
    assert -1 not in dis
    d.append(dis)
edge_distance=[[min(d[v][a],d[v][b]) for a,b in E] for v in range(N)]
# Each bit represents an edge dominated by vertex v.
cover=[]
for v in range(N):
    mask=0
    for j,(a,b) in enumerate(E):
        if v in ({a,b}|neighbors[a]|neighbors[b]):mask|=1<<j
    cover.append(mask)
all_edges=(1<<24)-1

def ve_dom(S):
    total=0
    for v in S:total|=cover[v]
    return total==all_edges

def resolve(S):
    labels=[tuple(edge_distance[v][j] for v in S) for j in range(24)]
    return len(set(labels))==24

V=Counter();R=Counter();J=Counter();minimum=[]
# Check all 65,536 subsets, including empty and all vertices.
for mask in range(1<<N):
    S=[i for i in range(N) if mask>>i&1]
    v=ve_dom(S)
    r=resolve(S)
    if v:V[len(S)]+=1
    if r:R[len(S)]+=1
    if v and r:
        J[len(S)]+=1
        if len(S)==5:minimum.append(mask)
assert V[4]==128 and sum(V[k] for k in range(4))==0
assert R[4]==368 and sum(R[k] for k in range(4))==0
assert J[4]==0 and J[5]==512 and sum(J.values())==50363
assert len(minimum)==512
assert [J[k] for k in range(17)]==[0,0,0,0,0,512,3432,8560,11790,11200,7984,4368,1820,560,120,16,1]
print('COUNTS_OK',dict(sorted(J.items())))

minimum.sort(); idx={s:i for i,s in enumerate(minimum)}
def reconfig(only_edges):
    graph=[set() for _ in minimum]
    for p,mask in enumerate(minimum):
        for a in range(N):
            if not ((mask>>a)&1):continue
            candidates=neighbors[a] if only_edges else range(N)
            for b in candidates:
                if mask>>b&1:continue
                q=idx.get(mask^(1<<a)^(1<<b))
                if q is not None:graph[p].add(q)
    assert all(p in graph[q] for p, adj in enumerate(graph) for q in adj)
    degree=Counter(map(len,graph))
    ecc=[]
    for start in range(len(graph)):
        dist=[-1]*len(graph);dist[start]=0;queue=deque([start])
        while queue:
            x=queue.popleft()
            for y in graph[x]:
                if dist[y]<0:dist[y]=dist[x]+1;queue.append(y)
        assert -1 not in dist
        ecc.append(max(dist))
    return sum(map(len,graph))//2, degree, Counter(ecc)
slide=reconfig(True); jump=reconfig(False)
assert slide==(1320,Counter({2:96,4:144,5:96,6:32,7:96,11:48}),Counter({8:512}))
assert jump==(3616,Counter({10:96,11:96,13:176,15:48,23:96}),Counter({5:368,6:144}))
print('DISTANCES_OK',slide,jump)

# All graph automorphisms, with arbitrary source->image assignments explored.
# Adjacent/nonadjacent consistency to every already-assigned vertex is enforced.
def automorphisms():
    maps=[-1]*N; used=[False]*N
    def rec(k):
        if k==N:
            yield tuple(maps)
            return
        # Choose the unassigned vertex with most previously assigned neighbors.
        candidates=[i for i in range(N) if maps[i]<0]
        source=max(candidates,key=lambda a:sum(maps[t]>=0 for t in neighbors[a]))
        for target in range(N):
            if used[target]:continue
            if any(((b in neighbors[source]) != (maps[b] in neighbors[target])) for b in range(N) if maps[b]>=0):continue
            maps[source]=target;used[target]=True
            yield from rec(k+1)
            used[target]=False;maps[source]=-1
    return list(rec(0))

perms=automorphisms()
assert len(perms)==96
unseen=set(minimum);orbits=[]
while unseen:
    mask=min(unseen)
    orbit={sum(1<<p[v] for v in range(N) if mask>>v&1) for p in perms}
    assert orbit <= set(minimum)
    assert orbit <= unseen
    unseen -= orbit
    orbits.append((len(orbit),mask))
assert sorted(orbits)==sorted([(48,0x1aa),(48,0x354),(48,0x394),(48,0x52a),(32,0x54a),(96,0x18e),(96,0x1a6),(96,0x34c)])
print('SYMMETRY_OK',len(perms),orbits)
print('MK_EDGE_LANDMARK_VERIFY_OK')
