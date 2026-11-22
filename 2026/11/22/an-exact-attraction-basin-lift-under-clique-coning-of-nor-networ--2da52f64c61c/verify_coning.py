#!/usr/bin/env python3
"""Exhaustive independent-of-proof tests of open-neighborhood NOR cone basin lift.

No external modules required. Run: python3 verify_coning.py
"""
import itertools
import random
from collections import Counter


def graph_edges_from_mask(n, mask):
    pairs = [(i, j) for i in range(n) for j in range(i+1, n)]
    return [pair for k, pair in enumerate(pairs) if (mask >> k) & 1]


def neighbors(n, edges):
    result = [0]*n
    for i,j in edges:
        result[i] |= (1 << j)
        result[j] |= (1 << i)
    return result


def cone_edges(n, base_edges, r):
    edges = list(base_edges)
    for h in range(n,n+r):
        for u in range(h):
            edges.append((u,h))
    return edges


def transitions(n, edge_set):
    adj = neighbors(n, edge_set)
    return [sum((1 << i) for i in range(n) if not (adj[i] & state))
            for state in range(1 << n)]


def basin_decomposition(trans):
    # Compute each successor orbit directly (no graph splitting assumptions).
    basins = Counter()
    point_to_orbit = {}
    for state in range(len(trans)):
        walk = []
        index = {}
        cur = state
        while cur not in index and cur not in point_to_orbit:
            index[cur] = len(walk)
            walk.append(cur)
            cur = trans[cur]
        if cur in point_to_orbit:
            cyc = point_to_orbit[cur]
        else:
            cyc = tuple(sorted(walk[index[cur]:]))
        for v in walk:
            point_to_orbit[v] = cyc
        basins[cyc] += 1
    return basins


def total_dom_count(n, base_edges):
    adj = neighbors(n, base_edges)
    return sum(all(s & a for a in adj) for s in range(1 << n))


def test_one(n, base_edges, r):
    base_map = transitions(n, base_edges)
    base_basins = basin_decomposition(base_map)
    main_base = tuple((0, (1 << n) - 1))
    assert main_base in base_basins, ('nonisolated base must have 0-1 oscillator',n)
    td = total_dom_count(n, base_edges)
    assert base_basins[main_base] == td + 1
    graph_map = transitions(n+r, cone_edges(n,base_edges,r))
    basins = basin_decomposition(graph_map)
    main = (0, (1 << (n+r)) - 1)
    assert basins[main] == (1 << (n+r)) - (1 << n) + td + 1-r, (n,r,td,basins[main])
    # Expected exact labels, not just total basin size.
    expected = Counter({cyc: sz for cyc,sz in base_basins.items() if cyc != main_base})
    expected[main] = base_basins[main_base] + ((1 << (n+r)) - (1 << n)) -r
    for j in range(r):
        expected[(1 << (n+j),)] = 1
    assert basins == expected, (n,r,basins,expected)
    assert basins[main] > max(sz for cyc,sz in basins.items() if cyc!=main)
    assert all(graph_map[graph_map[graph_map[s]]] == graph_map[s]
               for s in range(1 << (n+r)))


def main():
    cases = 0
    for n in range(2,6):
        pairs = n*(n-1)//2
        for mask in range(1 << pairs):
            edges = graph_edges_from_mask(n, mask)
            adj = neighbors(n, edges)
            if not all(adj):
                continue
            for r in (1,2):
                test_one(n,edges,r)
                cases += 1
    random.seed(20261119)
    sampled = 0
    n=6
    for _ in range(150):
        mask = random.getrandbits(n*(n-1)//2)
        edges = graph_edges_from_mask(n,mask)
        if not all(neighbors(n,edges)):
            continue
        for r in (1,2):
            test_one(n,edges,r)
            cases += 1
            sampled +=1
    print('PASS exhaustive non-isolate graphs n=2..5 with r=1,2; random n=6:', sampled)
    print('PASS graph/r experiments:', cases)

if __name__ == '__main__':
    main()
