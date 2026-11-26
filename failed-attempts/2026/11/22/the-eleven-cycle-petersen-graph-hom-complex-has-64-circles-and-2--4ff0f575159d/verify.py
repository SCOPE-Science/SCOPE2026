#!/usr/bin/env python3
"""Standalone exact graph-Hom component and CW-cell enumeration for C_11 -> Petersen.
Only the Python standard library is used. The point-or-circle theorem is cited
separately; this verifier establishes the finite enumeration premises.
"""
from itertools import combinations
from collections import Counter, defaultdict

M=11
V=list(combinations(range(5),2))
N=tuple(tuple(j for j,b in enumerate(V) if set(a).isdisjoint(b)) for a in V)
assert len(V)==10 and all(len(a)==3 for a in N)
assert all(len(set(N[a])&set(N[b]))<=1 for a in range(10) for b in range(a+1,10))
W=[]
def walk(path):
    if len(path)==M:
        if path[0] in N[path[-1]]: W.append(tuple(path))
        return
    for v in N[path[-1]]:
        path.append(v)
        walk(path)
        path.pop()
for u in range(10):walk([u])
assert len(W)==3**M+5+4*(-2)**M==168960
loc={w:i for i,w in enumerate(W)}
parent=list(range(len(W)))
size=[1]*len(W)
def find(a):
    while parent[a]!=a:
        parent[a]=parent[parent[a]]
        a=parent[a]
    return a
def union(a,b):
    a,b=find(a),find(b)
    if a!=b:
        if size[a]<size[b]:a,b=b,a
        parent[b]=a
        size[a]+=size[b]
for i,w in enumerate(W):
    for j in range(M):
        a,b=w[(j-1)%M],w[(j+1)%M]
        for v in set(N[a])&set(N[b]):
            if v!=w[j]:
                union(i,loc[w[:j]+(v,)+w[j+1:]])
counts=Counter(find(i) for i in range(len(W)))
by_size=Counter(counts.values())
assert by_size==Counter({1:2640,198:40,6600:24}),by_size

# Independently count every product-of-simplices cell by a finite-state
# transfer over the 50 nonempty subsets of Petersen vertex neighborhoods.
MASKS=sorted({sum(1<<v for v in c) for row in N for k in (1,2,3)
              for c in combinations(row,k)})
assert len(MASKS)==50
NM=tuple(sum(1<<j for j in a) for a in N)
def compatible(a,b):
    return all((NM[i]&b)==b for i in range(10) if a&(1<<i))
NEXT={a:tuple(b for b in MASKS if compatible(a,b)) for a in MASKS}
assert sum(map(len,NEXT.values()))==110
v=Counter()
for root in MASKS:
    current={(root,root.bit_count()-1):1}
    for _ in range(M-1):
        upcoming=defaultdict(int)
        for (state,deg),multiplicity in current.items():
            for other in NEXT[state]:
                upcoming[(other,deg+other.bit_count()-1)]+=multiplicity
        current=upcoming
    for (state,deg),multiplicity in current.items():
        if root in NEXT[state]:v[deg]+=multiplicity
expected={0:168960,1:582120,2:859320,3:693000,
          4:323400,5:83160,6:9240}
assert dict(v)==expected,(dict(v),expected)
assert sum((-1)**k*a for k,a in v.items())==2640
print('HOM_C11_OK maps=168960 components=2704 singleton=2640 size198=40 size6600=24')
print('CELL_VECTOR_OK '+repr(tuple(v[i] for i in range(7))))
print('EULER_OK characteristic=2640')
print('THEOREM_INPUTS_OK nontrivial_components=64')
