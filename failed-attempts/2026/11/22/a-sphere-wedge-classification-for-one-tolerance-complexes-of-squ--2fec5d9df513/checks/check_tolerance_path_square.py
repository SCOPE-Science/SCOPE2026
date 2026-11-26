#!/usr/bin/env python3
"""Independent finite checks for tolerance complexes of path-square clique complexes.
Public source-free combinatorial verification; proof remains in RESULT.md.
"""
from itertools import combinations
from collections import Counter
from math import comb

def choose(n,k):
    return comb(n,k) if n >= k >= 0 else 0

def rank2(columns):
    pivots = {}
    for x in columns:
        while x:
            bit = x.bit_length()-1
            if bit in pivots:
                x ^= pivots[bit]
            else:
                pivots[bit] = x
                break
    return len(pivots)

def run(n, algebra=True):
    assert n >= 4
    verts = range(n)
    edges = set((a,b) for a,b in combinations(verts,2) if b-a <= 2)
    original_triangles = set(tuple(range(i,i+3)) for i in range(n-2))
    triangles = [x for x in combinations(verts,3) if any(pair in edges for pair in combinations(x,2))]
    tet = set(x for x in combinations(verts,4) if any(y in original_triangles for y in combinations(x,3)))
    assert len(triangles) == choose(n,3)-choose(n-4,3)
    assert len(tet) == (n-3)**2
    initial = len(tet)
    used = set()
    # Type L: the first three positions are consecutive. Process by increasing a.
    L = sorted((x for x in tet if x[1]==x[0]+1 and x[2]==x[0]+2),key=lambda x:(x[0],x[3]))
    for a,b,c,d in L:
        sigma = (a,b,c,d); tau=(a,b,d)
        containing = sum(tau[0] in z and tau[1] in z and tau[2] in z for z in tet)
        assert containing == 1, ('L not free',n,sigma,tau,containing)
        assert tau in triangles and tau not in used
        used.add(tau);tet.remove(sigma)
    # Type R: last three positions consecutive, but first three not consecutive.
    R = sorted(tet,key=lambda x:(-x[1],x[0]))
    for a,b,c,d in R:
        assert c==b+1 and d==b+2
        tau=(a,c,d);sigma=(a,b,c,d)
        containing=sum(tau[0] in z and tau[1] in z and tau[2] in z for z in tet)
        assert containing == 1, ('R not free',n,sigma,tau,containing)
        assert tau in triangles and tau not in used
        used.add(tau);tet.remove(sigma)
    assert not tet and len(used)==initial
    beta=choose(n-4,2)
    assert len(triangles)-len(used)-choose(n-1,2)==beta
    if algebra:
        edges_complete=list(combinations(verts,2)); edge_index={x:i for i,x in enumerate(edges_complete)}
        triangles_index={x:i for i,x in enumerate(triangles)}
        d2 = [sum(1<<edge_index[e] for e in combinations(tri,2)) for tri in triangles]
        tetra = [x for x in combinations(verts,4) if any(y in original_triangles for y in combinations(x,3))]
        d3 = [sum(1<<triangles_index[tri] for tri in combinations(x,3)) for x in tetra]
        r2,r3=rank2(d2),rank2(d3)
        assert len(edges_complete)-(n-1)-r2 == 0
        assert len(triangles)-r2-r3 == beta
        assert len(tetra)-r3 == 0
    return initial,beta,len(triangles)

if __name__ == '__main__':
    count=0; collapse_pairs=0
    for n in range(4,51):
        t,b,faces=run(n,algebra=n<=12)
        count+=1;collapse_pairs+=t
    print('PASS: n=4..50,',count,'complete free-face collapse certificates,',collapse_pairs,'elementary pairs')
    print('PASS: n=4..12, exact F2 boundary ranks, H1=H3=0, H2=binomial(n-4,2)')
    print('PASS: combinatorial f-vectors and Euler identity for every checked n')
