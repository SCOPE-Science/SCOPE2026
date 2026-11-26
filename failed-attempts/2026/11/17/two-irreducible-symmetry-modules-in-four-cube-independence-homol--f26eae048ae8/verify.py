#!/usr/bin/env python3
"""Exact finite verification of the rational symmetry action on Ind(Q4).
Uses only the Python standard library. All enumerations are complete.
"""
import itertools
from collections import Counter

N=16
V=tuple(range(N))
NEI=tuple(sum(1 << (v ^ (1 << j)) for j in range(4)) for v in V)

def independent(mask):
    x=mask
    while x:
        bit=x & -x
        v=bit.bit_length()-1
        if NEI[v] & mask: return False
        x^=bit
    return True

F={s:[] for s in range(9)}
for mask in range(1<<N):
    if independent(mask): F[mask.bit_count()].append(mask)
assert [len(F[i]) for i in range(9)]==[1,16,88,208,228,128,56,16,2]
assert sum(map(len,F.values()))==743

def binary_rank(cols):
    pivots={}
    for x in cols:
        while x:
            h=x.bit_length()-1
            if h in pivots: x^=pivots[h]
            else:
                pivots[h]=x
                break
    return len(pivots)

R=[]
for size in range(1,9):
    target={f:i for i,f in enumerate(F[size-1])}
    columns=[]
    for f in F[size]:
        x=f;col=0
        while x:
            bit=x&-x;x^=bit
            col^=1<<target[f^bit]
        columns.append(col)
    R.append(binary_rank(columns))
assert R==[1,15,73,135,86,42,14,2],R  # augmented boundaries: C_0 -> C_-1 included
betti={}
# R[dim] is rank of the augmented boundary out of dimension dim.
for dim in range(8):
    lower=R[dim]
    higher=R[dim+1] if dim+1<len(R) else 0
    betti[dim]=len(F[dim+1])-lower-higher
assert betti=={0:0,1:0,2:0,3:7,4:0,5:0,6:0,7:0},betti
assert sum((-1)**(s-1)*len(F[s]) for s in range(9))==-7 # (-1)^{-1} treated -1 via Python

perms=tuple(itertools.permutations(range(4)))

def perm_parity(p):
    return -1 if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2 else 1

def signed_perm_image(x,p):
    return sum(((x>>i)&1)<<p[i] for i in range(4))

def face_lefschetz(g):
    # Reduced Lefschetz: -1 for empty face, plus signed trace of each nonempty simplex.
    L=-1
    for size in range(1,9):
        for mask in F[size]:
            vs=[i for i in V if mask>>i&1]
            ims=[g[i] for i in vs]
            if sum(1<<w for w in ims)!=mask: continue
            inversions=sum(ims[i]>ims[j] for i in range(len(ims)) for j in range(i+1,len(ims)))
            L+=(-1)**(size-1+inversions)
    return -L # reduced homology is H3, and L=-chi

def orbit_independence_eval(g):
    seen=set();orbits=[]
    for x in V:
        if x in seen: continue
        cyc=[];y=x
        while y not in seen:
            seen.add(y);cyc.append(y);y=g[y]
        orbits.append(tuple(cyc))
    good=[o for o in orbits if not any((NEI[x]>>y)&1 for x in o for y in o)]
    blocks=[sum(1<<x for x in o) for o in good]
    conflict=[0]*len(good)
    for i,a in enumerate(blocks):
        for j,b in enumerate(blocks):
            if j==i:continue
            if any(NEI[x]&b for x in V if a>>x&1): conflict[i]|=1<<j
    # Evaluate independence polynomial at -1 by deletion-contraction of an orbit vertex.
    from functools import lru_cache
    @lru_cache(None)
    def eval_rec(keep):
        if not keep:return 1
        bit=keep&-keep
        i=bit.bit_length()-1
        return eval_rec(keep^bit)-eval_rec((keep^bit)&~conflict[i])
    return eval_rec((1<<len(blocks))-1)

assert len(perms)*16==384
trace={};counts=Counter()
for p in perms:
    s=perm_parity(p)
    fixed=sum(p[i]==i for i in range(4))
    for b in range(16):
        g=tuple(signed_perm_image(x,p)^b for x in V)
        q=face_lefschetz(g)
        q2=orbit_independence_eval(g)
        conjectured=s*(fixed-1+sum((-1)**((b & (15^(1<<i))).bit_count()) for i in range(4) if p[i]==i))
        assert q==q2==conjectured,(p,b,q,q2,conjectured)
        trace[(p,b)]=q
        counts[q]+=1
assert counts==Counter({1:188,-1:161,-3:24,3:6,5:4,7:1}),counts
identity=tuple(range(4))
assert trace[identity,0]==7
assert [trace[identity,b] for b in range(16)]==[7,1,1,3,1,3,3,5,1,3,3,5,3,5,5,-1]
assert sum(t*t for t in trace.values())==2*384

# Translation Fourier coefficients (each integer in characteristic zero).
mult={mask:sum(trace[identity,b] * (-1 if (mask&b).bit_count()%2 else 1) for b in range(16))//16 for mask in range(16)}
assert mult[0]==3
assert {m for m in mult if mult[m]==1}=={7,11,13,14}
assert all(v==0 for m,v in mult.items() if m not in {0,7,11,13,14})

# On translation-invariants, character = sign(p)*(number of fixed points-1).
for p in perms:
    t=sum(trace[p,b] for b in range(16))//16
    assert t==perm_parity(p)*(sum(p[i]==i for i in range(4))-1)

invariants={
 'translations':sum(trace[identity,b] for b in range(16))//16,
 'even_translations':sum(trace[identity,b] for b in range(16) if b.bit_count()%2==0)//8,
 'central_inversion':(trace[identity,0]+trace[identity,15])//2,
 'coordinate_permutations':sum(trace[p,0] for p in perms)//24,
 'even_coordinate_permutations':sum(trace[p,0] for p in perms if perm_parity(p)==1)//12,
 'all_384':sum(trace.values())//384,
}
assert invariants=={'translations':3,'even_translations':3,'central_inversion':3,'coordinate_permutations':0,'even_coordinate_permutations':1,'all_384':0},invariants
print('faces_by_cardinality:',[len(F[i]) for i in range(9)])
print('augmented_boundary_ranks_dim0_to7:',R)
print('reduced_F2_betti_dim0_to7:',[betti[i] for i in range(8)])
print('group_order:',len(trace))
print('character_distribution:',dict(sorted(counts.items())))
print('Fourier_multiplicities:',dict(sorted((k,v) for k,v in mult.items() if v)))
print('character_square_inner_product:',sum(t*t for t in trace.values())//384)
print('quotient_top_cohomology_ranks:',invariants)
print('Q4_INDEPENDENCE_B4_CHARACTER_PASS')
