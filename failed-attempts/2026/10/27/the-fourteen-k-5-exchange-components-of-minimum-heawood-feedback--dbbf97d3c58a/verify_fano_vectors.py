#!/usr/bin/env python3
"""Independent exhaustive verification using binary Fano incidence."""
from itertools import combinations
from collections import deque

POINTS = tuple(range(7))
LINES = tuple(range(7,14))
def inner(x,y):
    return ((x & y).bit_count() % 2) == 0

adj = [set() for _ in range(14)]
for i in POINTS:
    for j in range(7):
        if inner(i+1,j+1):
            adj[i].add(j+7)
            adj[j+7].add(i)
assert all(len(a)==3 for a in adj)
# A 3-regular graph is 3-vertex-connected when deletion of fewer than
# three vertices always leaves a connected graph.
for k_removed in range(3):
    for removed in combinations(range(14),k_removed):
        kept=set(range(14))-set(removed)
        reached={next(iter(kept))};frontier=list(reached)
        while frontier:
            for v in adj[frontier.pop()]&kept:
                if v not in reached:
                    reached.add(v);frontier.append(v)
        assert reached==kept, (k_removed,removed)

def is_forest_after(S):
    remain = set(range(14))-set(S)
    edges = sum(len(adj[u] & remain) for u in remain)//2
    # Connected components: a forest has edges = vertices - components.
    seen=set(); components=0
    for root in remain:
        if root in seen: continue
        components+=1; stack=[root]; seen.add(root)
        while stack:
            for v in adj[stack.pop()] & remain:
                if v not in seen:
                    seen.add(v);stack.append(v)
    return edges==len(remain)-components

for k in range(4):
    assert not any(is_forest_after(S) for S in combinations(range(14),k)),k
bases={frozenset(S) for S in combinations(range(14),4) if is_forest_after(S)}
assert len(bases)==70,len(bases)

families=[]
for j in LINES:
    U=frozenset({j} | (set(POINTS)-adj[j]))
    assert len(U)==5
    families.append(U)
for i in POINTS:
    U=frozenset({i} | (set(LINES)-adj[i]))
    assert len(U)==5
    families.append(U)
from_geometry={frozenset(U-set((v,))) for U in families for v in U}
assert bases==from_geometry, (bases-from_geometry,from_geometry-bases)

neighbors={S: set() for S in bases}
for S in bases:
    for u in S:
        for v in set(range(14))-S:
            T=frozenset((S-{u})|{v})
            if T in bases: neighbors[S].add(T)
assert all(len(neighbors[S])==4 for S in bases)

seen=set(); sizes=[]; edge_counts=[]
for S in bases:
    if S in seen: continue
    seen.add(S); component={S}; queue=deque([S])
    while queue:
        for T in neighbors[queue.popleft()]:
            if T not in seen:
                seen.add(T);component.add(T);queue.append(T)
    sizes.append(len(component))
    edge_counts.append(sum(len(neighbors[T] & component) for T in component)//2)
assert sorted(sizes)==[5]*14
assert sorted(edge_counts)==[10]*14
assert sum(edge_counts)==140
print('VECTOR_CHECK_OK')
print('minimum_feedback_vertex_set_size=4')
print('number_minimum_feedback_vertex_sets=',len(bases))
print('geometric_families=',len(families))
print('exchange_components=',len(sizes))
print('component_sizes=',sorted(sizes))
print('total_exchange_edges=',sum(edge_counts))
