#!/usr/bin/env python3
"""Independent checks for finite labelled extensions of K4-free windmill bases.

This program independently compares local transfer counts with direct K4
enumeration. These finite tests do not establish the unbounded theorem.
"""
from itertools import combinations
from math import comb

def all_cliques4(edges, n):
    return any(all(tuple(sorted(pair)) in edges for pair in combinations(q,2))
               for q in combinations(range(n),4))

def edge_pairs(r, mask):
    pairs = list(combinations(range(r),2))
    return {pairs[i] for i in range(len(pairs)) if (mask>>i)&1}

def transfer(H, r, C):
    # Counts allowed ordered neighborhoods (U,V) into each old petal.
    if any(set(tri) <= C for tri in combinations(range(r),3)
           if all(tuple(sorted(p)) in H for p in combinations(tri,2))):
        return 0
    triangles=[sum(1<<i for i in tri) for tri in combinations(range(r),3)
               if all(tuple(sorted(p)) in H for p in combinations(tri,2))]
    ans = 0
    for u in range(1<<r):
        if any((u&t)==t for t in triangles):
            continue
        for v in range(1<<r):
            if any((v&t)==t for t in triangles):
                continue
            if (u&v)&sum(1<<i for i in C):
                continue
            okay = True
            for i,j in H:
                edge_mask = (1<<i)|(1<<j)
                if (u&v&edge_mask)==edge_mask:
                    okay=False;break
                if i in C and j in C:
                    if (u&edge_mask)==edge_mask or (v&edge_mask)==edge_mask:
                        okay=False;break
            if okay:
                ans+=1
    return ans

def formula(H, r, m):
    return sum(transfer(H,r,{i for i in range(r) if (cm>>i)&1})**m
               for cm in range(1<<r))

def direct(H, r, m):
    # Old vertices: hub r; petals: (r+1+2*j,r+2+2*j).
    old_edges = set()
    for j in range(m):
        a,b=r+1+2*j,r+2+2*j
        old_edges.update(((r,a),(r,b),(a,b)))
    old=r+2*m+1
    ans=0
    clq=list(combinations(range(old),4))
    for bit in range(1<<((2*m+1)*r)):
        edges=old_edges.copy(); edges.update(H)
        for i in range(r):
            for j in range(2*m+1):
                if bit>>(i*(2*m+1)+j)&1:
                    edges.add((i,r+j))
        if not any(all(p in edges for p in combinations(q,2)) for q in clq):
            ans+=1
    return ans

def independent_weight(H,r):
    return sum(3**(r-s.bit_count()) for s in range(1<<r)
               if all(not ((s>>i)&1 and (s>>j)&1) for i,j in H))

def main():
    cases=0
    for r,m in [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(4,1)]:
        for h in range(1<<comb(r,2)):
            H=edge_pairs(r,h)
            if any(all(p in H for p in combinations(t,2))
                   for t in combinations(range(r),4)):
                continue
            x=formula(H,r,m); y=direct(H,r,m)
            assert x==y,(r,m,H,x,y)
            cases+=1
    assert formula(set(),2,1)==49
    assert formula({(0,1)},2,1)==46
    assert formula(set(),2,2)==(4**2+3**2)**2
    assert formula({(0,1)},2,2)==15**2+2*12**2+7**2
    assert independent_weight({(0,1)},2)==15
    kk=0
    for r in range(3,6):
        all_e=list(combinations(range(r),2))
        for k in range(1,r):
            star={(0,j) for j in range(1,k+1)}
            v=independent_weight(star,r)
            assert v==3*4**(r-k-1)*(4**k+3**(k-1))
            for edges in combinations(all_e,k):
                value=independent_weight(set(edges),r)
                assert value<=v,(r,k,edges,value,v)
                if value==v and k>=2:
                    degrees=[sum(i in e for e in edges) for i in range(r)]
                    assert max(degrees)==k,(r,k,edges)
                kk+=1
    print('PASS_DIRECT_EXTENSION_DIAGRAMS',cases)
    print('PASS_SMALL_WEIGHTED_EXTREMAL_CHECKS',kk)
    print('PASS_PAIR_CHANNEL', 'm=1',49,46,'m=2',169,15**2+2*12**2+7**2)
    print('FINITE_TESTS_NOT_AN_INFINITE_PROOF')
if __name__=='__main__': main()
