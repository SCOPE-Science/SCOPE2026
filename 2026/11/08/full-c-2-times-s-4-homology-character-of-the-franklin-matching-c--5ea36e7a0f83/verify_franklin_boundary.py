#!/usr/bin/env python3
"""Independent mod-2 chain check for the ordinary Franklin matching complex."""
from collections import Counter
n=12
E=set(tuple(sorted((i,(i+1)%n))) for i in range(n))
for i in range(n):
    E.add(tuple(sorted((i,(i+(5 if i%2==0 else -5))%n))))
E=sorted(E)
assert len(E)==18
S=[[] for _ in range(6)]
# independently enumerate all subsets of the 18 graph edges
for bits in range(1,1<<18):
    es=[i for i in range(18) if bits>>i&1]
    if len(es)>6:continue
    endpoints=[v for j in es for v in E[j]]
    if len(endpoints)==len(set(endpoints)):
        S[len(es)-1].append(tuple(es))
assert [len(v) for v in S]==[18,117,336,417,186,17]
# D_k: chains on faces of cardinality k+1 to cardinality k, rank over F2.
def rank2(k):
    source=S[k]
    if k==0:return 1  # augmentation
    targets={face:j for j,face in enumerate(S[k-1])}
    basis={}
    for face in source:
        vector=0
        for j in range(len(face)):
            facet=face[:j]+face[j+1:]
            vector^=1<<targets[facet]
        while vector:
            lead=vector.bit_length()-1
            if lead in basis:vector^=basis[lead]
            else:basis[lead]=vector;break
    return len(basis)
ranks=[rank2(k) for k in range(6)]
assert ranks==[1,17,100,236,169,17],ranks
betti=[len(S[k])-ranks[k]- (ranks[k+1] if k<5 else 0) for k in range(6)]
assert betti==[0,0,0,12,0,0],betti
print('F_VECTOR=18,117,336,417,186,17')
print('MOD2_AUGMENTED_BOUNDARY_RANKS='+','.join(map(str,ranks)))
print('MOD2_REDUCED_BETTI='+','.join(map(str,betti)))
print('FRANKLIN_MATCHING_MOD2_BOUNDARY_PASS')
