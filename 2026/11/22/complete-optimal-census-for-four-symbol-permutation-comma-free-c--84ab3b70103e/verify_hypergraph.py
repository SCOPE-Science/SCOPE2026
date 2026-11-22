#!/usr/bin/env python3
"""Independent hypergraph/Burnside certificate; Python standard library only.
The checker constructs 3-uniform forbidden hyperedges from crossed windows,
not by applying a comma-free function to each selected codebook.
"""
import itertools
from collections import Counter, defaultdict
S = tuple(itertools.permutations(range(4)))
index = {x:i for i,x in enumerate(S)}
# Rotation classes form the six possible composition-preserving necklace classes.
classes=[]; visited=set()
for a in S:
    if a in visited: continue
    O = [(a[k:]+a[:k]) for k in range(4)]
    classes.append(tuple(index[x] for x in O));visited.update(O)
assert len(classes)==6 and len(visited)==24
# Every offending overlap is a 3-element hyperedge, possibly repeated indices.
forbidden=set()
for i,x in enumerate(S):
    for j,y in enumerate(S):
        for k in range(1,4):
            z=x[k:]+y[:k]
            if z in index:
                forbidden.add(frozenset((i,j,index[z])))
# Include all sizes two or three, and a direct self-loop check.
assert all(len(e)>1 for e in forbidden)
# Search via six-level constraint propagation.
solutions=[]
def dfs(depth, chosen):
    if depth==6:
        solutions.append(frozenset(chosen));return
    for v in classes[depth]:
        attempt=set(chosen);attempt.add(v)
        if not any(e.issubset(attempt) for e in forbidden):
            dfs(depth+1,chosen+[v])
dfs(0,[])
assert len(solutions)==2872
solset=set(solutions)
# Burnside avoids orbit collection and provides a logically separate symmetry check.
def cycle_type(p):
    d=dict(enumerate(p));done=set();parts=[]
    for x in range(4):
        if x in done: continue
        y=x;length=0
        while y not in done:
            done.add(y);length+=1;y=d[y]
        parts.append(length)
    return tuple(sorted(parts,reverse=True))
expected={((1,1,1,1),0):(1,2872),((1,1,1,1),1):(1,64),
          ((2,1,1),0):(6,60),((2,1,1),1):(6,0),
          ((2,2),0):(3,0),((2,2),1):(3,16),
          ((3,1),0):(8,16),((3,1),1):(8,4),
          ((4,),0):(6,0),((4,),1):(6,0)}
grouped=defaultdict(list)
for p in itertools.permutations(range(4)):
    for reflect in (0,1):
        image=tuple(index[tuple(p[x] for x in (w[::-1] if reflect else w))] for w in S)
        fixed=sum(1 for C in solset if frozenset(image[x] for x in C)==C)
        grouped[(cycle_type(p),reflect)].append(fixed)
assert {k:(len(v),v[0]) for k,v in grouped.items()} == expected
assert all(len(set(v))==1 for v in grouped.values())
assert sum(sum(v) for v in grouped.values())==3504
print('HYPERGRAPH_BURNSIDE_OK choices=4096 labeled_optima=2872 fixed_sum=3504 orbit_classes=73')
print('conjugacy_type reverse multiplicity fixed_per_group_element')
for k,v in sorted(grouped.items()):print(k[0],k[1],len(v),v[0])
