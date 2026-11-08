#!/usr/bin/env python3
"""Independent enumeration and mod-2 homology for the 4-cube P3-devoid complex."""
from itertools import combinations
from collections import Counter
n=16
# Enumerate forbidden vertex triples directly from Hamming distance, not the degree test.
forbidden=set()
for centre in range(n):
    neigh=[j for j in range(n) if (centre^j).bit_count()==1]
    for u,v in combinations(neigh,2):forbidden.add((1<<centre)|(1<<u)|(1<<v))
assert len(forbidden)==96
by_dim={i:[] for i in range(8)}
for mask in range(1,1<<n):
    if any(mask & triple == triple for triple in forbidden): continue
    by_dim[mask.bit_count()-1].append(mask)
assert [len(by_dim[i]) for i in range(8)] == [16,120,464,964,960,440,80,10]
# Exact column reduction of ordinary simplicial boundary matrices over F_2.
ranks={0:1} # augmentation C0 -> Z for reduced homology
for d in range(1,8):
    row_ids={s:i for i,s in enumerate(by_dim[d-1])}
    pivots={}
    for s in by_dim[d]:
        col=0
        for j in range(n):
            if s>>j &1:col ^= 1<<row_ids[s^(1<<j)]
        while col:
            p=col.bit_length()-1
            if p in pivots:col ^= pivots[p]
            else:pivots[p]=col;break
    ranks[d]=len(pivots)
    print('BOUNDARY_RANK_MOD2',d,ranks[d])
assert ranks=={0:1,1:15,2:105,3:359,4:589,5:370,6:70,7:10}
betti={d:len(by_dim[d])-ranks[d]-ranks.get(d+1,0) for d in range(8)}
print('FACE_VECTOR', [1]+[len(by_dim[i]) for i in range(8)])
print('REDUCED_BETTI_MOD2',betti)
assert betti=={0:0,1:0,2:0,3:16,4:1,5:0,6:0,7:0}
print('INDEPENDENT_MOD2_CHECKS_PASS')
