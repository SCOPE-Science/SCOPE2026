#!/usr/bin/env python3
"""Independent exact graph construction and three-step adjacency trace, n=3..8."""
import collections
import itertools

EXPECTED = {3:(80,26),4:(122,40),5:(170,56),6:(170,56),7:(230,76),8:(296,98)}

def standardize(values):
    ranks = {a:i for i,a in enumerate(sorted(values))}
    return tuple(ranks[a] for a in values)

def count(n):
    vertices = list(itertools.permutations(range(n)))
    rank = {v:i for i,v in enumerate(vertices)}
    edges = [collections.Counter() for _ in vertices]
    for i,v in enumerate(vertices):
        for t in range(n+1):
            extended=tuple(x+(x>=t) for x in v)+(t,)
            edges[i][rank[standardize(extended[1:])]] += 1
    walks=0
    for a,ends in enumerate(edges):
        for b,ab in ends.items():
            for c,bc in edges[b].items():
                walks += ab*bc*edges[c][a]
    return walks, (walks-2)//3

if __name__ == '__main__':
    for n,(walks,cycles) in EXPECTED.items():
        actual=count(n)
        assert actual==(walks,cycles), (n,actual)
        print(f'n={n} closed3={actual[0]} directed3cycles={actual[1]}')
    print('DIRECT_GRAPH_CHECK_OK')
