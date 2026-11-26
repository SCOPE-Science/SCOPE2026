#!/usr/bin/env python3
"""Exhaustive finite geometry/adjacency verification using 6-subset line tests."""
import hashlib
from collections import Counter, deque
from itertools import combinations, product
import json

def times(a, b):
    w = 0
    for i in range(2):
        for j in range(2):
            if (a >> i) & 1 and (b >> j) & 1:
                w ^= 1 << (i + j)
    return w ^ (7 if w & 4 else 0)

F = range(4)
P = set()
for v in product(F, repeat=3):
    if v == (0, 0, 0):
        continue
    s = next(x for x in v if x)
    inv = next(x for x in (1, 2, 3) if times(x, s) == 1)
    P.add(tuple(times(inv, x) for x in v))
P = sorted(P)
assert len(P) == 21
L = set()
for coeff in P:
    L.add(sum(1 << j for j, pt in enumerate(P)
              if times(coeff[0], pt[0]) ^ times(coeff[1], pt[1]) ^ times(coeff[2], pt[2]) == 0))
assert len(L) == 21 and all(x.bit_count() == 5 for x in L)

H = []
for c in combinations(range(21), 6):
    s = sum(1 << v for v in c)
    if all((s & line).bit_count() <= 2 for line in L):
        H.append(s)
assert len(H) == 168 and len(set(H)) == 168

hist = [Counter() for _ in H]
adj = []
for i, a in enumerate(H):
    row = set()
    for j, b in enumerate(H):
        t = (a & b).bit_count()
        hist[i][t] += 1
        if i != j and t == 3:
            row.add(j)
    adj.append(row)
assert all(hist[i] == Counter({0:10, 1:72, 2:45, 3:40, 6:1}) for i in range(168))
assert all(len(x) == 40 for x in adj)
assert all((i in adj[j]) == (j in adj[i]) for i in range(168) for j in range(168))

common = {k:Counter() for k in range(4)}
for i, a in enumerate(H):
    for j in range(i+1,168):
        t = (a & H[j]).bit_count()
        common[t][len(adj[i] & adj[j])] += 1
expected = {0:{4:840},1:{5:6048},2:{16:3780},3:{11:3360}}
assert {t:dict(c) for t,c in common.items()} == expected
# Every nonneighbor has a common neighbor, so diameter 2.
assert all(common[t][c] > 0 for t,c in [(0,4),(1,5),(2,16)])
# Even intersection defines equivalence classes; calculate, not assume.
classes = []
remaining=set(range(168))
while remaining:
    i = min(remaining)
    block={j for j in remaining if ((H[i] & H[j]).bit_count() & 1) == 0}
    assert len(block) == 56
    assert all(((H[x] & H[y]).bit_count() & 1)==0 for x in block for y in block)
    assert all(((H[x] & H[z]).bit_count() & 1)==1 for x in block for z in remaining-block)
    classes.append(block); remaining-=block
assert len(classes)==3
assert all(len(adj[i] & classes[k]) in (0,20) for i in range(168) for k in range(3))
assert all(len(adj[i] & classes[k]) == (0 if i in classes[k] else 20) for i in range(168) for k in range(3))
# Exact integer check of annihilating polynomial, with trace moments.
import numpy as np
A=np.zeros((168,168),dtype=np.int64)
for i,row in enumerate(adj):
    for j in row:A[i,j]=1
roots=[0,-6,12,-20,40]
coeff=[1]
for lam in roots:
    new=[0]*(len(coeff)+1)
    for k,c in enumerate(coeff):new[k]+=c;new[k+1]-=lam*c
    coeff=new
I=np.identity(168,dtype=np.int64)
T=I.copy()
for c in coeff[1:]:T=T@A+c*I
assert not T.any()
multiplicities={0:105,-6:40,12:20,-20:2,40:1}
mat=I.copy()
traces=[]
for p in range(5):
    traces.append(int(np.trace(mat)))
    assert traces[-1] == sum(m*lam**p for lam,m in multiplicities.items())
    mat=mat@A
# Canonical finite certificate, ordering determined by sorted P and sorted H.
certificate = '\n'.join(format(x,'021b') for x in sorted(H))+'\n'
print(json.dumps({'points':len(P),'lines':len(L),'hyperovals':len(H),
 'intersection_per_base':dict(sorted(hist[0].items())),
 'unordered_pair_counts':{str(t):sum(cnt.values()) for t,cnt in common.items()},
 'common_neighbor_counts':{str(t):dict(sorted(cnt.items())) for t,cnt in common.items()},
 'class_sizes':sorted(map(len,classes)),'cross_class_degree':20,
 'swap_edges':sum(len(x) for x in adj)//2,'diameter':2,
 'spectrum':{str(k):multiplicities[k] for k in roots},'traces_0_to_4':traces,
 'annihilator_coeff_descending':coeff,
 'canonical_hyperoval_sha256':hashlib.sha256(certificate.encode()).hexdigest(),
 'verified':True},sort_keys=True,indent=2))
