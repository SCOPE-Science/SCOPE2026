#!/usr/bin/env python3
"""Independent adjacency-based graph automorphism and exhaustive-subset verification.
Requires networkx >= 2.8. Does not use affine or row/column automorphism formulas.
"""
from itertools import product
from collections import Counter
from math import comb
import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher
P=list(product(range(4),repeat=2))
Sstep={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
def make(kind):
    G=nx.Graph(); G.add_nodes_from(P)
    for i,(a,b) in enumerate(P):
        for c,d in P[i+1:]:
            if kind=='S': edge=((c-a)%4,(d-b)%4) in Sstep
            else: edge=(a==c or b==d)
            if edge: G.add_edge((a,b),(c,d))
    assert G.number_of_edges()==48
    return G

def check(kind):
    G=make(kind)
    maps=list(GraphMatcher(G,G).isomorphisms_iter())
    assert len(maps)==(192 if kind=='S' else 1152)
    # For each nontrivial full-graph automorphism, compute fixed vertices.
    fixed=[]
    for p in maps:
        if all(p[v]==v for v in P):continue
        fixed.append(sum(1<<i for i,v in enumerate(P) if p[v]==v))
    freq=[0]*17
    # Exhaustively check the actual pointwise stabilizer for all subsets.
    for m in range(1<<16):
        is_good=all(m&x!=m for x in fixed)
        freq[m.bit_count()]+=is_good
    expectedS=[0,0,0,448,1792,4368,8008,11440,12870,11440,8008,4368,1820,560,120,16,1]
    expectedR=[0,0,0,0,1008,3696,7672,11344,12858,11440,8008,4368,1820,560,120,16,1]
    assert freq==(expectedS if kind=='S' else expectedR),freq
    print('PASS graph-isomorphism',kind,'automorphisms',len(maps),'determining-subset coefficients',freq)
check('S');check('R')
