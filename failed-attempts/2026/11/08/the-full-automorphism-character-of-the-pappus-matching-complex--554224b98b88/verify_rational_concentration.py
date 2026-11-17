#!/usr/bin/env python3
"""Independent mod-two boundary-rank and Euler check for the Pappus matching complex; pure Python."""
from collections import Counter
N=18
lcf=[5,7,-7,7,-7,-5]*3
edges=tuple(sorted({tuple(sorted((i,(i+1)%N))) for i in range(N)}|{tuple(sorted((i,(i+lcf[i])%N))) for i in range(N)}))
assert len(edges)==27
# Distinct combinatorial construction via compatible edge masks.
B=[(1<<u)|(1<<v) for u,v in edges]
by_size=[[] for _ in range(10)]
by_size[0]=[0]
for k in range(27):
    v=B[k]
    for n in range(8,-1,-1):
        for mask in list(by_size[n]):
            chosen=mask
            bad=False
            while chosen:
                bit=chosen&-chosen
                j=bit.bit_length()-1
                if B[j]&v:bad=True;break
                chosen^=bit
            if not bad:by_size[n+1].append(mask | (1<<k))
assert [len(x) for x in by_size]==[1,27,297,1719,5643,10557,10737,5319,1026,42]

def rank_binary(vectors):
    pivots={}
    for v in vectors:
        while v:
            h=v.bit_length()-1
            if h not in pivots:
                pivots[h]=v;break
            v^=pivots[h]
    return len(pivots)

# Augmented boundary maps d_k: C_k -> C_{k-1}; C_{-1}=F2.
ranks=[1]
for k in range(2,10):
    rows={mask:j for j,mask in enumerate(by_size[k-1])}
    cols=[]
    for mask in by_size[k]:
        v=0;x=mask
        while x:
            bit=x&-x;x^=bit
            v^=1<<rows[mask^bit]
        cols.append(v)
    ranks.append(rank_binary(cols))
assert ranks==[1,26,271,1448,4195,6362,4335,984,42], ranks
# b_k = dim C_k -rank d_k-rank d_{k+1}; (ranks[k] = rank d_{k-1})
betti=[len(by_size[k])-ranks[k-1]-(ranks[k] if k<len(ranks) else 0) for k in range(1,10)]
assert betti==[0,0,0,0,0,40,0,0,0],betti
# In any characteristic zero field the integer boundary rank is at least its mod-2 rank,
# whence rational Betti numbers are bounded by these mod-two Betti numbers.
# Euler characteristic ensures the only allowed positive b_5 has rank exactly 40.
euler=sum((-1 if k%2==0 else 1)*len(by_size[k]) for k in range(10))
assert euler==-40 # reduced Euler is minus rank of degree-five homology
print('AUGMENTED_GF2_BOUNDARY_RANKS',ranks)
print('REDUCED_GF2_BETTI_BY_DIMENSION',betti)
print('AUGMENTED_MATCHING_EULER',euler)
print('RATIONAL_BETTI_CONCENTRATED_DEGREE_5_RANK_40')
print('PAPPUS_RATIONAL_HOMOLOGY_CONCENTRATION_PASS')
