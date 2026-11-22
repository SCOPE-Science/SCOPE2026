#!/usr/bin/env python3
"""Independent exhaustive certificate for edge-general-position subsets of Q4.
Build shortest paths by BFS distance layers; construct the feasible family
in increasing binary masks; detect maximal elements by direct supersets.
"""
from itertools import combinations
from collections import Counter

D=4
N=1<<D
edges=[(v,v^(1<<j)) for v in range(N) for j in range(D) if v < (v^(1<<j))]
assert len(edges)==32
edge_id={tuple(sorted(x)):i for i,x in enumerate(edges)}
forbidden=set()
for src in range(N):
    # DFS in BFS layers from src: every prefix is a shortest path.
    stack=[(src,0,())]
    while stack:
        v,depth,path=stack.pop()
        if depth>=3:
            for t in combinations(path,3):
                forbidden.add(tuple(sorted(t)))
        if depth==D: continue
        for j in range(D):
            u=v^(1<<j)
            if (src^u).bit_count()==depth+1:
                stack.append((u,depth+1,path+(edge_id[tuple(sorted((v,u)))],)))
assert len(forbidden)==576, len(forbidden)
pairs=[[] for _ in edges]
for a,b,c in forbidden:
    pairs[c].append((1<<a)|(1<<b))
    pairs[b].append((1<<a)|(1<<c))
    pairs[a].append((1<<b)|(1<<c))
feasible=[0]
for e in range(len(edges)):
    new=[]
    for mask in feasible:
        if all(mask & p != p for p in pairs[e]):
            new.append(mask|(1<<e))
    feasible += new
fs=set(feasible)
assert len(fs)==len(feasible)
face_count=Counter(m.bit_count() for m in fs)
facet_count=Counter()
maxima=[]
for mask in fs:
    if not any(mask|(1<<e) in fs for e in range(len(edges)) if not(mask>>e&1)):
        facet_count[mask.bit_count()]+=1
        if mask.bit_count()==16: maxima.append(mask)
# Check the extremizers against all unions of two coordinate edge classes.
directions=[[e for e,(a,b) in enumerate(edges) if (a^b)==1<<j] for j in range(D)]
expected={(sum(1<<i for i in directions[x]+directions[y])) for x,y in combinations(range(D),2)}
assert set(maxima)==expected
print('forbidden_triples',len(forbidden))
print('all_feasible',len(feasible),'inclusion_maximal',sum(facet_count.values()))
for k in range(17):
    print(k,face_count[k],facet_count[k])
print('six coordinate-pair extremizers confirmed')
