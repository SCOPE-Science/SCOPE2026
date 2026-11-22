#!/usr/bin/env python3
"""Independent exact finite-field evaluation of Gabor ambiguity zeros."""
from collections import Counter
from itertools import product

N=9
Q=531613
ZETA=45273
assert Q%9==1
assert all(Q%d for d in range(2,int(Q**0.5)+1))  # elementary primality certificate
assert pow(ZETA,9,Q)==1 and pow(ZETA,3,Q)!=1
assert Q>9**6
roots=[[pow(ZETA,k*t,Q) for t in range(N)] for k in range(N)]
rank_counts=Counter(); zero_profiles=Counter()
for tail in product((-1,1),repeat=8):
    signs=(1,)+tail
    zeros=[]
    for x in range(N):
        row=[signs[t]*signs[(t+x)%N] for t in range(N)]
        for k in range(N):
            val=sum(row[t]*roots[k][t] for t in range(N))%Q
            if val==0:zeros.append((x,k))
    rank_counts[N*N-len(zeros)]+=1
    zero_profiles[len(zeros)]+=1
assert dict(rank_counts)=={73:117,69:81,65:54,21:3,9:1},rank_counts
assert sum(rank_counts.values())==2**8
print('FINITE_FIELD_CHECK_PASS',sorted(rank_counts.items()))
print('MODULUS',Q,'ZETA',ZETA,'NORM_BOUND',N**6)
