"""Independent exhaustive exact-cover and Fourier-zero certificate.

Run: python check_recursive.py
Pure Python; no external dependencies. Uses integer masks and recursion.
"""
from itertools import combinations, product
from collections import Counter
from math import lcm
import json

TYPES = [(16,), (8,2), (4,4), (4,2,2), (2,2,2,2)]

def solve(dims):
    points = list(product(*(range(v) for v in dims)))
    idx = {v:i for i,v in enumerate(points)}
    n=len(points); e=lcm(*dims)
    add = [[idx[tuple((a+b)%m for a,b,m in zip(p,q,dims))]
            for q in points] for p in points]
    sub = [[idx[tuple((a-b)%m for a,b,m in zip(p,q,dims))]
            for q in points] for p in points]
    exps = [[sum((a*b*(e//m) for a,b,m in zip(p,q,dims))) % e
             for p in points] for q in points]
    full=(1<<n)-1

    def fourier_zeros(B):
        mask=0
        for q in range(1,n):
            c=[0]*e
            for x in B: c[exps[q][x]]+=1
            if all(c[j]==c[j+e//2] for j in range(e//2)):
                mask |= 1<<q
        return mask

    zcache={}
    def complement_sets(A):
        shifted=[sum(1<<add[t][x] for x in A) for t in range(n)]
        def rec(covered,T):
            if covered==full:
                yield T; return
            missing=(~covered)&full
            first=(missing&-missing).bit_length()-1
            for x in A:
                t=sub[first][x]
                if shifted[t]&covered: continue
                yield from rec(covered|shifted[t], T+(t,))
        yield from rec(shifted[0],(0,))

    def clique_zeros(allowed, degree):
        if degree==1: return (0,)
        candidates=[t for t in range(1,n) if (allowed>>t)&1]
        def rec(chosen, pool):
            if len(chosen)==degree: return tuple(chosen)
            if len(chosen)+len(pool)<degree:return None
            while pool:
                x,pool=pool[0],pool[1:]
                v=rec(chosen+[x],[y for y in pool if (allowed>>sub[x][y])&1])
                if v is not None:return v
            return None
        return rec([0],candidates)

    subgroups={}
    for m in (1,2,4,8,16):
        subgroups[m]=[]
        for tail in combinations(range(1,n),m-1):
            H=(0,)+tail
            if all(add[x][y] in H for x in H for y in H):
                subgroups[m].append(H)

    totals=Counter(); obstruct=Counter(); examples={}; normalized=Counter()
    for k in (1,2,4,8,16):
        for rest in combinations(range(1,n),k-1):
            A=(0,)+rest
            found=0; common=full^1
            for B in complement_sets(A):
                found+=1
                b=tuple(sorted(B))
                if b not in zcache:zcache[b]=fourier_zeros(b)
                common &= zcache[b]
            if not found:continue
            normalized[k]+=1
            W=clique_zeros(common,n//k)
            assert W is not None,(dims,A,found,common)
            has_subgroup=any(all((common>>sub[x][y])&1
                                   for x,y in combinations(H,2))
                             for H in subgroups[n//k])
            totals[k]+=n//k
            if not has_subgroup:
                obstruct[k]+=n//k
                if k not in examples:examples[k]={'tile':A,'common_spectrum':W,
                                         'normalized_complement_count':found}
    assert sum(totals.values())==sum(normalized[k]*n//k for k in normalized)
    return {'group':list(dims),'tile_count':sum(totals.values()),
            'tile_count_by_size':{str(k):totals[k] for k in (1,2,4,8,16)},
            'non_subgroup_universal_spectrum_count':sum(obstruct.values()),
            'non_subgroup_count_by_size':{str(k):obstruct[k] for k in (1,2,4,8,16)},
            'all_tiles_have_universal_spectrum':True,
            'examples':{str(k):v for k,v in sorted(examples.items())}}

if __name__=='__main__':
    print(json.dumps([solve(ds) for ds in TYPES],sort_keys=True,indent=2))
