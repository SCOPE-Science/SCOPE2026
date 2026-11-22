#!/usr/bin/env python3
"""Exact, standalone verification for sharp spanning-forest biclique thresholds.
Run: python3 verify_forests.py. No third-party dependencies.
"""
from itertools import product
from collections import defaultdict
from math import comb

def make_coefficients(a):
    # Directly count ordered connector tuples by union-find on the left shore.
    options=[tuple(i for i in range(a) if (mask>>i)&1)
             for mask in range(1<<a) if mask.bit_count()>=2]
    counts=[1]
    for length in range(1,a):
        total=0
        for sequence in product(options,repeat=length):
            parent=list(range(a))
            def root(v):
                while parent[v]!=v:
                    v=parent[v]
                return v
            good=True
            for subset in sequence:
                roots=[root(v) for v in subset]
                if len(set(roots))!=len(roots):
                    good=False;break
                for rt in roots[1:]:parent[rt]=roots[0]
            if good:total+=1
        counts.append(total)
    return tuple(counts)

def f_formula(a,b,c):
    # Each nonspecial right vertex is isolated or has one of a possible edges.
    return sum(comb(b,j)*c[j]*(a+1)**(b-j)
               for j in range(min(a-1,b)+1))

def count_forests_by_edges(a,b):
    # Separate exhaustive enumeration of *all* edge subsets, checking cycles.
    n=a+b
    edges=[(i,a+j) for i in range(a) for j in range(b)]
    result=0
    for mask in range(1<<len(edges)):
        parent=list(range(n));rank=[0]*n;ok=True
        def root(v):
            while v!=parent[v]:v=parent[v]
            return v
        for i,(u,v) in enumerate(edges):
            if not ((mask>>i)&1):continue
            x,y=root(u),root(v)
            if x==y:ok=False;break
            if rank[x]<rank[y]:x,y=y,x
            parent[y]=x
            if rank[x]==rank[y]:rank[x]+=1
        result+=ok
    return result

def run():
    expected={3:(1,4,6),4:(1,11,54,96),5:(1,26,300,1560,3000)}
    for a,c in expected.items():
        got=make_coefficients(a)
        assert got==c,(a,got,c)
    print('DIRECT_ORDERED_CONNECTOR_CERTIFICATES_PASS',expected)
    # Independent full-edge brute force checks the transfer formula.
    for a,b in [(3,3),(3,4),(3,5),(4,3),(4,4)]:
        got=count_forests_by_edges(a,b)
        assert got==f_formula(a,b,expected[a]),(a,b,got)
    print('INDEPENDENT_ALL_EDGE_SUBSETS_FORESTS_PASS 5')
    thresholds={3:(14,10),4:(22,18),5:(31,27)}
    for a,(b_star,b_mono) in thresholds.items():
        c=expected[a]
        # Negative to just before boundary, positive at boundary.
        for b in range(a,b_star):
            assert f_formula(a,b,c)<a**b*b**a,(a,b,'below')
        assert f_formula(a,b_star,c)>a**b_star*b_star**a
        # Coefficient polynomial is nondecreasing after a-1, and this
        # exact inequality implies R(b+1)>R(b) for every b>=b_mono.
        assert (a+1)*b_mono**a>a*(b_mono+1)**a,(a,b_mono)
        for b in range(b_mono,b_mono+5):
            assert (a+1)*b**a>a*(b+1)**a
        print('EXACT_SHARP_WIDTH_THRESHOLD_PASS',a,b_star)
    # For K_{a,b} on at most 17 vertices, a>=6 implies b<=11<=2a;
    # those cases are covered by the cited published minimum-degree theorem.
    # The only remaining possible parameter pairs have a<=5 and are exact.
    for a in [3,4,5]:
        for b in range(a,18-a):
            d=f_formula(a,b,expected[a])-a**b*b**a
            assert (d>0)==(a==3 and b==14),(a,b,d)
    assert f_formula(3,14,expected[3])==13186891776
    assert 3**14*14**3==13124466936
    print('UNIQUE_FIRST_SEVENTEEN_VERTEX_BICLIQUE_WITNESS_PASS')
    print('VERIFY_OK')
if __name__=='__main__':run()
