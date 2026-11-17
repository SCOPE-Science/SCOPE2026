#!/usr/bin/env python3
"""Independent Burnside fixed-flag census for a binary projective three-space."""
from itertools import combinations
P=0b10011

def gf_mul(a,b):
    out=0
    while b:
        if b&1: out ^=a
        a <<= 1
        if a&16:a ^=P
        b >>=1
    return out

def gf_pow(a,n):
    x=1
    for _ in range(n):x=gf_mul(x,a)
    return x

def subspace(vs):
    v={0}
    for t in vs:
        v |= {u^t for u in tuple(v)}
    return frozenset(v)

spaces={k:set() for k in (1,2,3)}
for k in (1,2,3):
    for seed in combinations(range(1,16),k):
        S=subspace(seed)
        if len(S)==(1<<k):spaces[k].add(S)
vertices=[(k,S) for k in (1,2,3) for S in spaces[k]]
flags=[(v,) for v in vertices]
flags += [(u,v) for u in vertices for v in vertices if u[0]<v[0] and u[1]<v[1]]
flags += [(u,v,w) for u in vertices for v in vertices for w in vertices if u[0]==1 and v[0]==2 and w[0]==3 and u[1]<v[1]<w[1]]
assert len(flags)==65+315+315
by_dim=[[],[],[]]
for t in flags:by_dim[len(t)-1].append(t)

def apply(v,i,k):
    d,S=v
    return (d, frozenset(gf_mul(gf_pow(2,i),gf_pow(x,1<<k)) for x in S))

fixed_by_k=[]
for k in range(4):
    total=[0,0,0]
    for i in range(15):
        for d in range(3):total[d]+=sum(all(apply(v,i,k)==v for v in f) for f in by_dim[d])
    fixed_by_k.append(total)
assert all(z%60==0 for z in [sum(row[d] for row in fixed_by_k) for d in range(3)])
print('raw flag counts',*[len(v) for v in by_dim])
print('Burnside fixed-flag totals per Frobenius power k',fixed_by_k)
print('orbit flag counts',tuple(sum(row[d] for row in fixed_by_k)//60 for d in range(3)))
print('Euler',sum((-1)**d * sum(row[d] for row in fixed_by_k)//60 for d in range(3)))
