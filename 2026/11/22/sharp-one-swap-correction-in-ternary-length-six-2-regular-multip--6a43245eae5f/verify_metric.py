#!/usr/bin/env python3
"""Second, independent distance implementation, using canonical rank permutations."""
from itertools import combinations, permutations
from collections import deque
W = sorted(set(permutations((0,0,1,1,2,2))))

def mapped(w):
    p = [0,0,0]
    out=[]
    for x in w:
        out.append(2*x + p[x]); p[x]+=1
    return out

def rank_distance(a,b):
    pa, pb = mapped(a), mapped(b)
    where = {v:i for i,v in enumerate(pb)}
    order = [where[v] for v in pa]
    return sum(order[i]>order[j] for i in range(6) for j in range(i+1,6))

def swaps(w):
    for j in range(5):
        if w[j]!=w[j+1]:
            v=list(w);v[j],v[j+1]=v[j+1],v[j]
            yield tuple(v)

for source in W:
    d={source:0}; queue=deque([source])
    while queue:
        v=queue.popleft()
        for t in swaps(v):
            if t not in d: d[t]=d[v]+1;queue.append(t)
    assert len(d)==90
    for target in W:
        assert d[target] == rank_distance(source,target), (source,target,d[target],rank_distance(source,target))

reps=['001122','010221','011220','020211','021102','021201']
C={tuple((int(v)+s)%3 for v in rep) for s in range(3) for rep in reps}
assert len(C)==18
assert min(rank_distance(a,b) for a,b in combinations(C,2))>=3
print('All 8100 shortest-path distances agree with inversion-count metric; eighteen-word witness has minimum distance',min(rank_distance(a,b) for a,b in combinations(C,2)))
