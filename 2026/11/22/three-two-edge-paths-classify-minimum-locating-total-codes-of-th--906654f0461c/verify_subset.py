#!/usr/bin/env python3
"""Exact LTD census on the Petersen line graph, using set arithmetic.
All vertex labels are the 2-subsets of {0,1,2,3,4} in lexicographic order.
No external dependencies.
"""
import itertools
from collections import Counter, deque

points = tuple(itertools.combinations(range(5), 2))
original_edges = tuple((i,j) for i in range(10) for j in range(i+1,10)
                       if not set(points[i]).intersection(points[j]))
assert len(original_edges) == 15
neigh = [frozenset(j for j,(c,d) in enumerate(original_edges)
                   if j != i and (a in (c,d) or b in (c,d)))
         for i,(a,b) in enumerate(original_edges)]
assert all(len(n)==4 for n in neigh)

def ltd(selected):
    chosen = set(selected)
    if any(not neigh[i].intersection(chosen) for i in range(15)):
        return False
    outside = [i for i in range(15) if i not in chosen]
    signatures = [frozenset(neigh[i].intersection(chosen)) for i in outside]
    return len(signatures) == len(set(signatures))

def path_factor(selected):
    deg=[0]*10
    sub=[set() for _ in range(10)]
    for i in selected:
        a,b=original_edges[i];deg[a]+=1;deg[b]+=1;sub[a].add(b);sub[b].add(a)
    if sorted(deg) != [0,1,1,1,1,1,1,2,2,2]:
        return False
    visited=set(); shapes=[]
    for v in range(10):
        if v in visited: continue
        stack=[v];visited.add(v);component=set()
        while stack:
            w=stack.pop();component.add(w)
            for z in sub[w]:
                if z not in visited: visited.add(z);stack.append(z)
        shapes.append((len(component),sum(deg[w] for w in component)//2))
    return sorted(shapes)==[(1,0),(3,2),(3,2),(3,2)]

C = {k:set() for k in range(16)}
for k in range(16):
    for tup in itertools.combinations(range(15),k):
        if ltd(tup):
            C[k].add(frozenset(tup))
assert [len(C[k]) for k in range(16)] == [0,0,0,0,0,0,110,1590,3810,4150,2838,1350,455,105,15,1]
opt=C[6]
# The P3-factor classification is an iff over every six-subset, not merely necessity.
for tup in itertools.combinations(range(15), 6):
    assert (frozenset(tup) in opt) == path_factor(tup)

# Natural S5 action on the original vertices induces the full order-120 action.
edge_index={e:i for i,e in enumerate(original_edges)}
pt_index={p:i for i,p in enumerate(points)}
actions=[]
for p in itertools.permutations(range(5)):
    vertex_map=[pt_index[tuple(sorted((p[a],p[b])))] for a,b in points]
    actions.append(tuple(edge_index[tuple(sorted((vertex_map[a],vertex_map[b])))]
                         for a,b in original_edges))
def move(tup, act): return frozenset(act[i] for i in tup)
remaining=set(opt); orbits=[]
while remaining:
    s=min(remaining,key=lambda t:tuple(sorted(t)))
    orb={move(s,p) for p in actions}
    assert orb <= opt
    orbits.append((len(orb),s))
    remaining-=orb
assert sorted(size for size,s in orbits) == [10,40,60]

# Graph edges are all one-selected-edge swaps that remain optimum.
index={s:i for i,s in enumerate(sorted(opt,key=lambda t:tuple(sorted(t))))}
ids=list(index)
adj=[set() for _ in ids]
for i,s in enumerate(ids):
    for x in s:
        for y in range(15):
            if y not in s:
                t=frozenset((s-{x})|{y})
                j=index.get(t)
                if j is not None: adj[i].add(j)
assert all(i in adj[j] for i,ni in enumerate(adj) for j in ni)
assert sum(map(len,adj))//2==210
assert Counter(map(len,adj))==Counter({4:60,3:40,6:10})
all_dist=[]
for i in range(len(ids)):
    d={i:0}; q=deque([i])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v not in d:d[v]=d[u]+1;q.append(v)
    assert len(d)==110
    all_dist.append(d)
assert Counter(max(d.values()) for d in all_dist)==Counter({6:60,7:50})
assert min(max(d.values()) for d in all_dist)==6
assert max(max(d.values()) for d in all_dist)==7
profiles={}
for size,rep in orbits:
    i=index[rep]; d=all_dist[i]
    profiles[size]=(len(adj[i]),tuple(Counter(d.values()).get(t,0) for t in range(max(d.values())+1)))
assert profiles=={
 10:(6,(1,6,12,18,28,24,18,3)),
 40:(3,(1,3,9,21,32,36,6,2)),
 60:(4,(1,4,10,21,32,27,15))}
# Uniform count for every choice of the sole uncovered Petersen vertex.
counts=Counter()
for code in opt:
    covered={v for j in code for v in original_edges[j]}
    assert len(covered)==9
    counts[next(iter(set(range(10))-covered))]+=1
assert counts==Counter({i:11 for i in range(10)})
print('PASS_PETERSEN_LINE_LTD_SET_32768')
print('COUNTS', [len(C[k]) for k in range(16)])
print('ORBIT_PROFILES',profiles)
print('EXCHANGE_VERTICES_EDGES_RADIUS_DIAMETER',len(ids),sum(map(len,adj))//2,6,7)
