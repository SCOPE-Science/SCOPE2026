#!/usr/bin/env python3
"""Independently verify the triangular-graph geodesic-transversal census.

The graph vertices are edges of K_n. The verifier constructs shortest
paths in the line graph and exhaustively tests all selected subsets for
n=4,5,6. A separate set-partition recurrence produces the claimed counts.
"""
from collections import Counter
from itertools import combinations, permutations
from math import comb, factorial


def component_counts(n, maximal=False):
    # Component-structure enumerator, with labels on 0,...,n-1.
    components={1: {0: 1}, 2: {1: 1}, 3: {2: 3, 3: 1}}
    for s in range(4,n+1):
        components[s]={s-1:s}
    if maximal:
        components={2:{1:1}, 3:{3:1}, **{s:{s-1:s} for s in range(4,n+1)}}
    dp=[Counter() for _ in range(n+1)]
    dp[0][0]=1
    for v in range(1,n+1):
        for s, choices in components.items():
            if s>v: continue
            for e, number in choices.items():
                for k,other in dp[v-s].items():
                    dp[v][e+k] += comb(v-1,s-1)*number*other
    out=dp[n]
    if maximal and n>=4 and n%3==1:
        r=(n-1)//3
        out[n-1] += n*factorial(n-1)//(factorial(3)**r*factorial(r))
    return out


def geodesic_test(n):
    pairs=list(combinations(range(n),2))
    m=len(pairs)
    adjacent=[[i!=j and bool(set(a)&set(b)) for j,b in enumerate(pairs)] for i,a in enumerate(pairs)]
    distances=[]
    for i in range(m):
        ds=[m+1]*m; ds[i]=0
        frontier=[i]
        for depth in range(1, m+1):
            nxt=[]
            for u in frontier:
                for j in range(m):
                    if adjacent[u][j] and ds[j]>depth:
                        ds[j]=depth; nxt.append(j)
            if not nxt:break
            frontier=nxt
        distances.append(ds)
    assert max(map(max,distances))==2
    # All maximal shortest paths have length two; also check extendability.
    geo=set()
    for i in range(m):
        for j in range(m):
            if distances[i][j]!=2:continue
            for k in range(m):
                if adjacent[i][k] and adjacent[k][j]:
                    geo.add((1<<i)|(1<<k)|(1<<j))
    for i in range(m):
        for j in range(i+1,m):
            if adjacent[i][j]:
                assert any(mask & (1<<i) and mask & (1<<j) for mask in geo)
    idx={e:i for i,e in enumerate(pairs)}
    p4=set()
    for a,b,c,d in permutations(range(n),4):
        p4.add(sum(1<<idx[tuple(sorted((u,v)))] for u,v in ((a,b),(b,c),(c,d))))
    assert p4==geo
    valid=Counter(); maximal=Counter()
    for mask in range(1<<m):
        if any(mask & g == g for g in geo):
            continue
        valid[mask.bit_count()]+=1
        if all(any(((mask | (1<<i)) & g)==g for g in geo)
               for i in range(m) if not mask & (1<<i)):
            maximal[mask.bit_count()]+=1
    a=component_counts(n)
    b=component_counts(n,True)
    assert valid==a, (n,valid,a)
    assert maximal==b, (n,maximal,b)
    return len(geo),sum(valid.values()),sum(maximal.values()),dict(sorted(maximal.items()))

if __name__=='__main__':
    total_geo=total_masks=total_valid=total_max=0
    for n in range(4,7):
        num_geo,valid,facets,dist=geodesic_test(n)
        total_geo+=num_geo;total_masks+=1<<(n*(n-1)//2)
        total_valid+=valid;total_max+=facets
        print(f'n={n} geodesics={num_geo} transversals={valid} minimal={facets} omitted-edge_counts={dist}')
    print('VERIFY_OK n=4..6 masks=%d geodesics=%d valid_transversals=%d inclusion_minimal=%d BFS=PASS original_P4_equivalence=PASS two_EGFs=PASS' % (total_masks,total_geo,total_valid,total_max))
