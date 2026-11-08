#!/usr/bin/env python3
"""Independent GF(2) homology check of cube nonmatching subcomplexes.
Uses a separate vertex-based maximum-matching dynamic program.
"""
from functools import lru_cache
from collections import defaultdict

E=[(a,b) for a in range(8) for b in range(a+1,8) if (a^b).bit_count()==1]
assert len(E)==12

@lru_cache(None)
def nu(edge_mask):
    # max matching by choosing the first active graph vertex
    if not edge_mask: return 0
    active={u for i,(u,v) in enumerate(E) if edge_mask&(1<<i)} | {v for i,(u,v) in enumerate(E) if edge_mask&(1<<i)}
    u=min(active)
    rest=edge_mask
    for i,(a,b) in enumerate(E):
        if u in(a,b):rest&=~(1<<i)
    ans=nu(rest)
    for i,(a,b) in enumerate(E):
        if edge_mask&(1<<i) and u in(a,b):
            v=b if a==u else a
            child=rest
            for j,(c,d) in enumerate(E):
                if v in(c,d):child&=~(1<<j)
            ans=max(ans,1+nu(child))
    return ans


def rank_gf2(columns):
    piv={}
    for val in columns:
        while val:
            high=val.bit_length()-1
            if high not in piv:
                piv[high]=val
                break
            val^=piv[high]
    return len(piv)

EXPECTED={2:{1:5},3:{3:9},4:{5:1}}
for k in (2,3,4):
    chain=defaultdict(list)
    for bits in range(1<<len(E)):
        if nu(bits)<k:
            if bits:chain[bits.bit_count()-1].append(bits)
    dmax=max(chain)
    dims={i:len(chain[i]) for i in range(dmax+1)}
    ranks={}
    for d in range(1,dmax+1):
        rowids={face:i for i,face in enumerate(chain[d-1])}
        columns=[]
        for s in chain[d]:
            v=0
            t=s
            while t:
                low=t&-t;t-=low
                v ^= 1<<rowids[s^low]
            columns.append(v)
        ranks[d]=rank_gf2(columns)
    bettis={d:dims[d]-ranks.get(d,0)-ranks.get(d+1,0) for d in range(dmax+1)}
    bettis[0]-=1
    positive={d:b for d,b in bettis.items() if b}
    assert positive==EXPECTED[k],(k,positive)
    assert all(b>=0 for b in bettis.values())
    print('k=',k,'chain_dimensions=',dims,'boundary_ranks=',ranks,'reduced_mod2_betti=',positive)
print('INDEPENDENT_MOD2_CHECKS_PASS')
