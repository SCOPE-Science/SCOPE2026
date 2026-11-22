#!/usr/bin/env python3
"""Petersen vertex-to-edge landmark census via direct two-subset intersection geometry.
No external packages; exact exhaustiveness over 2^10 labelled landmark masks.
"""
from itertools import combinations, permutations
from collections import Counter

edges5 = list(combinations(range(5), 2))
p_edges = [(i, j) for i in range(10) for j in range(i+1, 10)
           if set(edges5[i]).isdisjoint(edges5[j])]
assert len(p_edges) == 15

# In the Petersen graph, distinct intersecting 2-subsets have distance 2.
def distance(i, j):
    return 0 if i == j else (1 if set(edges5[i]).isdisjoint(edges5[j]) else 2)

D = [[min(distance(i, a), distance(i, b)) for a,b in p_edges]
     for i in range(10)]
R = Counter(); C = Counter(); J = Counter()
resolving_by_k = {k: set() for k in range(11)}
for mask in range(1 << 10):
    landmarks = [i for i in range(10) if (mask >> i) & 1]
    signatures = {tuple(D[i][e] for i in landmarks) for e in range(15)}
    resolving = len(signatures) == 15
    covering = all(any(D[i][e] <= 1 for i in landmarks) for e in range(15))
    k = len(landmarks)
    if resolving: R[k] += 1; resolving_by_k[k].add(mask)
    if covering: C[k] += 1
    if resolving and covering: J[k] += 1

assert dict(R) == {4:15, 5:162, 6:195, 7:120, 8:45, 9:10, 10:1}
assert dict(C) == {3:60, 4:195, 5:252, 6:210, 7:120, 8:45, 9:10, 10:1}
assert dict(J) == {5:162, 6:195, 7:120, 8:45, 9:10, 10:1}

# The 15 non-covering 4-sets are exactly the four cross-pairs associated with
# each Petersen edge. Every one of them resolves all 15 edges.
noncover = set()
for a,b in p_edges:
    cross = [i for i,p in enumerate(edges5)
             if bool(set(p) & set(edges5[a])) and bool(set(p) & set(edges5[b]))]
    assert len(cross) == 4
    noncover.add(sum(1 << i for i in cross))
assert len(noncover) == 15
assert noncover == resolving_by_k[4]

# Full S5 action on five ground labels. Classify the 252 five-edge graph supports.
perms = list(permutations(range(5)))
edge_id = {e:i for i,e in enumerate(edges5)}
actions = [tuple(edge_id[tuple(sorted((p[a],p[b])))] for a,b in edges5)
           for p in perms]

def orbits(k):
    unvisited = {mask for mask in range(1<<10) if mask.bit_count() == k}
    rows = []
    while unvisited:
        mask = min(unvisited)
        orb = {sum(1 << act[i] for i in range(10) if (mask >> i) & 1)
               for act in actions}
        assert orb <= unvisited
        unvisited -= orb
        yes = mask in resolving_by_k[k]
        assert all((z in resolving_by_k[k]) == yes for z in orb)
        deg = [0]*5
        tri = 0
        for i,(a,b) in enumerate(edges5):
            if mask >> i & 1: deg[a]+=1; deg[b]+=1
        for a,b,c in combinations(range(5),3):
            if all((mask >> edge_id[e]) & 1 for e in ((a,b),(a,c),(b,c))):tri+=1
        rows.append((len(orb),tuple(sorted(deg)),tri,yes,mask))
    return sorted(rows, reverse=True)

for k, expected in [(4,[(60,False),(60,False),(60,False),(15,True),(10,False),(5,False)]),
                    (5,[(60,True),(60,True),(60,False),(30,True),(30,False),(12,True)])]:
    rows = orbits(k)
    assert sorted((a,d) for a,_,_,d,_ in rows) == sorted(expected)
    print('S5_ORBITS',k,';'.join('%s:%s:%s:%s:%s'%(sz,','.join(map(str,deg)),t,int(valid),
          ','.join(''.join(map(str,edges5[i])) for i in range(10) if mask>>i&1))
          for sz,deg,t,valid,mask in rows))

print('EDGE_RESOLVING',sorted(R.items()))
print('VERTEX_EDGE_COVERING',sorted(C.items()))
print('JOINT',sorted(J.items()))
print('PET_X5_SYMBOLIC_OK')
