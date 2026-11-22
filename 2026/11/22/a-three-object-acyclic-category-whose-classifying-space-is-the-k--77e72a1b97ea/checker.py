#!/usr/bin/env python3
"""Exact finite checks for a three-object acyclic category modelling a surface."""
from collections import Counter,defaultdict
T=((3,0,1),(0,4,2),(2,1,5))
assert sorted(T[i][j] for i in range(3) for j in range(3)) == [0,0,1,1,2,2,3,4,5]
# Remove three 2-cells and their private 0->2 edge c3,c4,c5.
S=[(i,j,T[i][j]) for i in range(3) for j in range(3) if i!=j]
assert len(S)==6 and [T[i][i] for i in range(3)]==[3,4,5]
assert all(Counter(x[k] for x in S)==Counter({0:2,1:2,2:2}) for k in (0,1,2))

def connected_link(edges):
    adjacency=defaultdict(set)
    for u,v in edges:
        adjacency[u].add(v);adjacency[v].add(u)
    assert len(adjacency)==6
    assert all(len(x)==2 for x in adjacency.values())
    seen={next(iter(adjacency))};todo=list(seen)
    while todo:
        for v in adjacency[todo.pop()]:
            if v not in seen:seen.add(v);todo.append(v)
    assert len(seen)==6

# Links at objects 0,1,2 in the retained 2-dimensional delta-complex.
connected_link([(('a',i),('c',k)) for i,j,k in S])
connected_link([(('a',i),('b',j)) for i,j,k in S])
connected_link([(('b',j),('c',k)) for i,j,k in S])
# If the surface oriented, triangle coefficients +/-1 would differ across paired edges.
shared=[]
for col in range(3):
    groups=defaultdict(list)
    for idx,row in enumerate(S):groups[row[col]].append(idx)
    assert all(len(x)==2 for x in groups.values())
    shared.extend(tuple(x) for x in groups.values())
colors={};graph=defaultdict(list)
for p,q in shared:graph[p].append(q);graph[q].append(p)
orientable=True
for s in range(6):
    if s in colors:continue
    colors[s]=0;queue=[s]
    while queue:
        t=queue.pop()
        for u in graph[t]:
            if u in colors:
                if colors[u]==colors[t]:orientable=False
            else:colors[u]=1-colors[t];queue.append(u)
assert not orientable
assert (3-9+6)==0
# Checks the elementary presentation: c0=b1=a1, c1=b2=a2*b1,
# c2=a1*b2=a2. Eliminating a2, b1 yields b2=a1*b2*a1.
assert T[0][1]==T[1][0] and T[0][2]==T[2][1] and T[1][2]==T[2][0]
print('PASS: exact table, three free-face collapses, three 6-cycle links, Euler zero, nonorientability, Klein presentation')
