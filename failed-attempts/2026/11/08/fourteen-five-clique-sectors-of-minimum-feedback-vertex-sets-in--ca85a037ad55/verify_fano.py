#!/usr/bin/env python3
"""Independent finite check using incidence bitsets and a disjoint-set forest test."""
from itertools import combinations
from collections import Counter

N = 14
lines = [{i, (i+1)%7, (i+3)%7} for i in range(7)]
edges = [(p, 7+j) for j,L in enumerate(lines) for p in L]
adj = [0]*N
for u,v in edges:
    adj[u] |= 1<<v; adj[v] |= 1<<u

def is_forest(S):
    parent = list(range(N))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u,v in edges:
        if (S >> u) & 1 or (S >> v) & 1:
            continue
        a,b = find(u),find(v)
        if a == b: return False
        parent[a] = b
    return True

F_by_size = {k:{sum(1<<j for j in c) for c in combinations(range(N),k) if is_forest(sum(1<<j for j in c))} for k in range(5)}
assert [len(F_by_size[k]) for k in range(4)] == [0,0,0,0]
F = F_by_size[4]
assert len(F) == 70
blocks=[]
for j,L in enumerate(lines):
    Q=set(range(7))-L
    blocks.append(Q|{j+7})
for p in range(7):
    blocks.append({p}|{j+7 for j,L in enumerate(lines) if p not in L})
assert len(blocks)==14 and all(len(b)==5 for b in blocks)
assert all(all((adj[u]>>v)&1 == 0 for u,v in combinations(sorted(b),2)) for b in blocks)
classified={sum(1<<v for v in B if v!=o) for B in blocks for o in B}
assert F==classified and len(classified)==70
f=sorted(F); index={s:i for i,s in enumerate(f)}
J=[set() for _ in f]; T=[set() for _ in f]
for i,s in enumerate(f):
    for u in range(N):
        if not (s>>u)&1:continue
        for v in range(N):
            if (s>>v)&1:continue
            t=s^(1<<u)^(1<<v)
            if t in index:
                j=index[t];J[i].add(j)
                if (adj[u]>>v)&1:T[i].add(j)
def components(graph):
    unseen=set(range(len(graph))); sizes=[]
    while unseen:
        root=min(unseen);queue=[root];unseen.remove(root)
        for u in queue:
            for v in graph[u]:
                if v in unseen:unseen.remove(v);queue.append(v)
        sizes.append(len(queue))
    return Counter(sizes)
assert all(len(x)==4 for x in J)
assert sum(map(len,J))//2 == 140
assert components(J)==Counter({5:14})
assert sum(map(len,T)) == 0
assert components(T)==Counter({1:70})
assert all(len(set.intersection(*[set(B) for B in [b1,b2]])) <= 2 for b1,b2 in combinations(blocks,2))
print('FANO_VERIFY_OK; minimum=4; fvs_count=70; blocks=14; all_blocks_size=5; jump_edges=140; jump_components=14*K5; slide_edges=0; slide_components=70*K1')
