#!/usr/bin/env python3
"""Exhaustive small-n check of geometric subgroup-fixed Rips complexes.

Standard-library only. Builds translation orbits directly and tests all Hamming
cross distances, then constructs explicit graph isomorphisms to cube graphs.
"""
from collections import Counter, deque
from itertools import combinations
from math import comb


def subspaces(n):
    seen = set()
    for a, b in combinations(range(1, 1 << n), 2):
        w = tuple(sorted((0, a, b, a ^ b)))
        if w not in seen:
            seen.add(w)
            yield w


def fixed_graph(n, w, scale):
    seen, orbits = set(), []
    for x in range(1 << n):
        if x in seen:
            continue
        o = sorted(x ^ y for y in w)
        seen.update(o)
        if max((a ^ b).bit_count() for a, b in combinations(o, 2)) <= scale:
            orbits.append(o)
    adj = [set() for _ in orbits]
    for i, j in combinations(range(len(orbits)), 2):
        if max((a ^ b).bit_count() for a in orbits[i] for b in orbits[j]) <= scale:
            adj[i].add(j)
            adj[j].add(i)
    return adj


def components(adj):
    unseen = set(range(len(adj)))
    result = []
    while unseen:
        root = min(unseen)
        seen = {root}
        todo = [root]
        unseen.remove(root)
        while todo:
            v = todo.pop()
            for w in adj[v]:
                if w in unseen:
                    unseen.remove(w)
                    seen.add(w)
                    todo.append(w)
        result.append(seen)
    return result


def verify_cube(adj, k):
    if k == 0:
        assert len(adj) == 1 and len(adj[0]) == 0
        return
    assert len(adj) == 1 << k
    assert all(len(neighbors) == k for neighbors in adj)
    dist = [-1] * len(adj)
    dist[0] = 0
    levels = [[0]]
    todo = deque([0])
    while todo:
        v = todo.popleft()
        for u in adj[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                if len(levels) <= dist[u]:
                    levels.append([])
                levels[dist[u]].append(u)
                todo.append(u)
    assert len(levels) == k + 1 and all(len(levels[d]) == comb(k,d) for d in range(k+1))
    labels = {0: 0}
    for bit, v in enumerate(sorted(levels[1])):
        labels[v] = 1 << bit
    for d in range(2, k + 1):
        for v in levels[d]:
            lower = [u for u in adj[v] if dist[u] == d-1]
            assert len(lower) == d
            bitset = 0
            for u in lower: bitset |= labels[u]
            assert bitset.bit_count() == d
            labels[v] = bitset
    assert len(set(labels.values())) == len(adj)
    for v in range(len(adj)):
        assert {u for u in range(len(adj)) if (labels[v] ^ labels[u]).bit_count() == 1} == adj[v]


def verify_circles(adj, n):
    comps = components(adj)
    assert len(comps) == 1 << (n-4)
    for comp in comps:
        assert len(comp) == 4
        assert all(len(adj[v]) == 2 and adj[v] <= comp for v in comp)


def main():
    totals = Counter()
    for n in range(2, 9):
        counts = Counter()
        for w in subspaces(n):
            weights = sorted(v.bit_count() for v in w if v)
            support = (w[1] | w[2] | w[3]).bit_count()
            adj = fixed_graph(n,w,3)
            early = fixed_graph(n,w,2)
            assert not fixed_graph(n,w,1)
            if max(weights) <= 2:
                assert len(early) == 1 << (n - 2)
                assert all(not v for v in early)
                counts['scale2_points'] += 1
            else:
                assert not early
            if weights[-1] > 3:
                assert not adj
                typ = 'empty'
            elif support <= 3:
                verify_cube(adj, n - 2)
                typ = 'cube'
            else:
                assert support == 4 and weights == [2,3,3]
                verify_circles(adj,n)
                typ = 'circles'
            counts[typ] += 1
        expected = dict(cube=comb(n,2)+4*comb(n,3),
                        circles=6*comb(n,4))
        expected['empty'] = ((2**n-1)*(2**n-2)//6)-sum(expected.values())
        assert all(counts[t] == expected[t] for t in expected)
        assert counts['scale2_points'] == comb(n,2)+comb(n,3)
        totals.update({key: counts[key] for key in ('cube','circles','empty')})
        print('n=%d subgroups=%d scale2_points=%d cube=%d circle-unions=%d empty=%d' %
              (n, counts['cube']+counts['circles']+counts['empty'],counts['scale2_points'],counts['cube'],counts['circles'],counts['empty']))
    print('all_subgroups=%d distribution=%s' % (sum(totals.values()),dict(sorted(totals.items()))))
    print('RANK_TWO_FIXED_GRAPH_CLASSIFICATION_OK')

if __name__ == '__main__':
    main()
