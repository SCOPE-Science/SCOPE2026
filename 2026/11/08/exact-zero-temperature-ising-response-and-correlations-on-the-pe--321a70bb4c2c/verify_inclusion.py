#!/usr/bin/env python3
"""Exact inclusion-exclusion for line-Petersen Ising ground states.
Independent of the spin-mask enumerator; Python 3 standard library only.
"""
from functools import lru_cache
from math import comb

N = 10
EDGES = tuple([(i, (i+1)%5) for i in range(5)] +
              [(i, i+5) for i in range(5)] +
              [(i+5, 5+(i+2)%5) for i in range(5)])
assert len(EDGES) == 15 and len(set(tuple(sorted(e)) for e in EDGES)) == 15

def mul_one_plus_x_power(p, d):
    ret = p[:]
    for j, a in enumerate(p):
        if j+d < 16:
            ret[j+d] += a
    return ret

def components_of_selected(mask):
    remaining = {v for v in range(N) if (mask>>v)&1}
    out = []
    while remaining:
        seed = min(remaining)
        remaining.remove(seed)
        C = {seed}
        stack = [seed]
        while stack:
            u = stack.pop()
            for a, b in EDGES:
                w = b if a == u else a if b == u else -1
                if w in remaining:
                    remaining.remove(w)
                    C.add(w)
                    stack.append(w)
        out.append(C)
    return out

def not_all_equal_polynomial():
    F = [0]*16
    for S in range(1<<N):
        comps = components_of_selected(S)
        forced = set()
        block_sizes = []
        for C in comps:
            own = {i for i,(u,v) in enumerate(EDGES) if u in C or v in C}
            assert not (own & forced)
            forced |= own
            block_sizes.append(len(own))
        poly = [0]*16
        for k in range(16-len(forced)):
            poly[k] = comb(15-len(forced), k)
        for d in block_sizes:
            poly = mul_one_plus_x_power(poly, d)
        sgn = -1 if S.bit_count()&1 else 1
        for k in range(16):
            F[k] += sgn * poly[k]
    return F

@lru_cache(None)
def match_poly(remaining):
    if remaining == 0:
        return (1,)
    v = (remaining & -remaining).bit_length()-1
    skip = remaining & ~(1<<v)
    p0 = match_poly(skip)
    result = [0]*7
    for k, a in enumerate(p0):result[k] += a
    for a,b in EDGES:
        w = b if a==v else a if b==v else -1
        if w >= 0 and ((remaining>>w)&1):
            for k,x in enumerate(match_poly(skip & ~(1<<w))):
                if k+1 < len(result):result[k+1] += x
    return tuple(result)

F = not_all_equal_polynomial()
M = match_poly((1<<N)-1)
assert F == [0,0,0,0,0,6,195,690,690,195,6,0,0,0,0,0], F
assert M == (1,15,75,145,90,6,0), M
assert sum(F)==1782 and sum(M)==332
print('IE_MATCHING_OK zero_field=1782 critical_field=332 perfect_matchings=6')
print('zero_field_count_by_negative_edge_count',F)
print('matching_polynomial',M)

# Exact two-point functions by the same independent inclusion-exclusion identity.
# When a selected component forces both edge spins, their product is +1;
# all other blocks have independent symmetric signs and contribute zero.
def pair_numerators_by_ie():
    nums = [[0]*15 for _ in range(15)]
    for S in range(1<<N):
        comps=components_of_selected(S)
        block=[-1]*15
        for ci,C in enumerate(comps):
            for i,(u,v) in enumerate(EDGES):
                if u in C or v in C:
                    assert block[i] in (-1,ci)
                    block[i]=ci
        f=block.count(-1)
        weight=(-1 if (S.bit_count()&1) else 1)*(1<<(len(comps)+f))
        for e in range(15):
            if block[e]==-1: continue
            for t in range(e+1,15):
                if block[e]==block[t]: nums[e][t]+=weight
    return nums

# Compute distance in the line graph from the outer/spoke/star representation.
adj=[[] for _ in range(15)]
for e,(a,b) in enumerate(EDGES):
    for f,(c,d) in enumerate(EDGES):
        if f>e and (a==c or a==d or b==c or b==d):
            adj[e].append(f);adj[f].append(e)
assert sum(map(len,adj))==60
numerators=pair_numerators_by_ie()
pair_counts=[0]*4
for e in range(15):
    dist=[99]*15;dist[e]=0
    queue=[e]
    for v in queue:
        for t in adj[v]:
            if dist[t]==99:dist[t]=dist[v]+1;queue.append(t)
    for t in range(e+1,15):
        r=dist[t]
        assert 1<=r<=3
        pair_counts[r]+=1
        assert numerators[e][t]=={1:-594,2:190,3:-290}[r],(e,t,r,numerators[e][t])
assert pair_counts==[0,30,60,15]
print('IE_CORRELATION_OK adjacent=-594/1782 dist2=190/1782 dist3=-290/1782')
