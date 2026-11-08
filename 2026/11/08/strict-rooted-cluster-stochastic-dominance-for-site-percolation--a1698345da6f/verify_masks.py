#!/usr/bin/env python3
"""Exact rooted site-percolation histogram: exhaustive 16-bit site masks.
Run with Python 3, standard library only.
"""
from math import comb

N=16
ROOT=0

def make_rook():
    return [sum(1 << (4*r+c) for r in range(4) for c in range(4)
                if (r == u//4 or c == u%4) and 4*r+c != u)
            for u in range(N)]

def make_shrikhande():
    steps={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
    return [sum(1 << (4*r+c) for r in range(4) for c in range(4)
                if ((r-u//4)%4,(c-u%4)%4) in steps)
            for u in range(N)]

def assert_parameters(adjacency):
    for u in range(N):
        assert adjacency[u].bit_count() == 6
        assert (adjacency[u] & (1<<u)) == 0
        for v in range(N):
            assert bool(adjacency[u] & (1<<v)) == bool(adjacency[v] & (1<<u))
            if u != v:
                assert (adjacency[u] & adjacency[v]).bit_count() == 2

def root_cluster_size(adjacency,occupied):
    if occupied&1 == 0:
        return 0
    reached=1
    frontier=1
    while frontier:
        vertex_bit=frontier & -frontier
        frontier^=vertex_bit
        vertex=vertex_bit.bit_length()-1
        fresh=adjacency[vertex] & occupied & ~reached
        reached|=fresh
        frontier|=fresh
    return reached.bit_count()

def histogram(adjacency):
    out=[[0]*17 for _ in range(17)]
    for occupied in range(1<<N):
        out[occupied.bit_count()][root_cluster_size(adjacency,occupied)]+=1
    for k,row in enumerate(out):
        assert sum(row)==comb(N,k), (k,sum(row))
    return out

def evaluate():
    assert_parameters(make_rook());assert_parameters(make_shrikhande())
    R=histogram(make_rook());S=histogram(make_shrikhande())
    delta=[[S[k][s]-R[k][s] for s in range(17)] for k in range(17)]
    expected={4:{3:-12,4:12},5:{3:-36,4:-24,5:60},
              6:{3:-36,4:-48,5:-30,6:114},
              7:{3:-12,4:-24,6:-6,7:42},
              8:{4:-6,8:6}}
    for k in range(17):
        for s in range(17):
            assert delta[k][s] == expected.get(k,{}).get(s,0),(k,s,delta[k][s])
    tails=[[sum(delta[k][s] for s in range(t,17)) for k in range(17)]
           for t in range(1,17)]
    expected_tails={4:[12,36,36,12,0],5:[0,60,84,36,6],
                    6:[0,0,114,36,6],7:[0,0,0,42,6],8:[0,0,0,0,6]}
    for t in range(1,17):
        assert tails[t-1][4:9]==expected_tails.get(t,[0]*5)
        assert all(tails[t-1][k]==0 for k in list(range(4))+list(range(9,17)))
    weighted=[sum(s*delta[k][s] for s in range(17)) for k in range(17)]
    assert weighted==[0]*4+[12,96,234,126,24]+[0]*8
    assert sum(weighted)==492
    return delta

if __name__=='__main__':
    evaluate()
    print('PASS: all 65,536 site masks per graph, 17x17 histograms, all tails and moments')
