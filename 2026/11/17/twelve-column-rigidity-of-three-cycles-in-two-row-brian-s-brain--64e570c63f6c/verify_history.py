#!/usr/bin/env python3
"""Independent full space-time update verification, without phase-count formulas."""
from itertools import product
from collections import defaultdict

# Histories indexed by the complete three-time sequence of actual states.
SITE = [(0,0,0),(1,2,0),(0,1,2),(2,0,1)]
COL = list(product(SITE,repeat=2))

def permitted(left, center, right):
    for row in (0,1):
        for t in range(3):
            state=center[row][t]
            if state==1: wanted=2
            elif state==2: wanted=0
            else:
                neighbors = (
                    left[row][t], left[1-row][t], left[1-row][t],
                    right[row][t],right[1-row][t],right[1-row][t],
                    center[1-row][t],center[1-row][t])
                wanted = 1 if sum(x==1 for x in neighbors)==2 else 0
            if center[row][(t+1)%3]!=wanted: return False
    return True

adj=defaultdict(list)
for a,b,c in product(range(16),repeat=3):
    if permitted(COL[a],COL[b],COL[c]):
        adj[(a,b)].append((b,c))
vertices=set(adj)
for outs in list(adj.values()):vertices.update(outs)

# Iterative Kosaraju, independently of the standard SCC library.
visited=set();finish=[]
for v in vertices:
    if v in visited: continue
    stack=[(v,False)]
    while stack:
        node,processed=stack.pop()
        if processed:finish.append(node);continue
        if node in visited:continue
        visited.add(node)
        stack.append((node,True))
        for out in adj[node]:
            if out not in visited:stack.append((out,False))
reverse=defaultdict(list)
for v, outs in adj.items():
    for w in outs:reverse[w].append(v)
visited.clear(); cyclic=[]
for v in reversed(finish):
    if v in visited:continue
    stack=[v];visited.add(v);comp=[]
    while stack:
        node=stack.pop();comp.append(node)
        for pred in reverse[node]:
            if pred not in visited:visited.add(pred);stack.append(pred)
    if len(comp)>1 or v in adj[v]: cyclic.append(set(comp))
assert (len(vertices),sum(map(len,adj.values()))) == (199,346)
assert sorted(map(len,cyclic))==[1,12,12]
for comp in cyclic:
    count=sum(v in comp and w in comp for v in comp for w in adj[v])
    assert count==len(comp)
    for v in comp:
        assert sum(w in comp for w in adj[v])==1
print('history table:',len(SITE),'site histories,',len(COL),'column histories')
print('independently reconstructed vertices, edges:',len(vertices),sum(map(len,adj.values())))
print('closed components:',sorted(map(len,cyclic)))
print('all internal degrees exactly one; no other closed walks')
print('ALL INDEPENDENT HISTORY CHECKS PASSED')
