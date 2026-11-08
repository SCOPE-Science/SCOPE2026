#!/usr/bin/env python3
"""Reproduce the middle-graph semitotal-domination census (Python 3 stdlib)."""
from collections import Counter
from itertools import combinations
from math import comb
from random import Random


def connected(n, edges):
    reach = {0}
    while True:
        nxt = reach | {v for u, v in edges if u in reach} | {u for u, v in edges if v in reach}
        if nxt == reach:
            return len(reach) == n
        reach = nxt


def middle(n, edges):
    adj = [0] * (n + len(edges))
    def link(a, b):
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    for j, (u, v) in enumerate(edges):
        link(n + j, u)
        link(n + j, v)
    for i, (a, b) in enumerate(edges):
        for j, (c, d) in enumerate(edges[:i]):
            if a == c or a == d or b == c or b == d:
                link(n + i, n + j)
    dist2 = []
    for i, nbr in enumerate(adj):
        near = nbr
        x = nbr
        while x:
            bit = x & -x
            x -= bit
            near |= adj[bit.bit_length() - 1]
        dist2.append(near & ~(1 << i))
    return adj, dist2


def is_dom(mask, adj):
    return all((mask >> i & 1) or (mask & nbr) for i, nbr in enumerate(adj))


def is_semi(mask, dist2):
    x = mask
    while x:
        bit = x & -x
        x -= bit
        if not mask & dist2[bit.bit_length() - 1]:
            return False
    return True


def predicted_coeff(n, edges):
    ans = Counter()
    m = len(edges)
    for fmask in range(1 << m):
        covered = 0
        for i, (a, b) in enumerate(edges):
            if fmask >> i & 1:
                covered |= (1 << a) | (1 << b)
        c = covered.bit_count()
        baseline = fmask.bit_count() + n - c
        for j in range(c + 1):
            ans[baseline + j] += comb(c, j)
    return ans


def all_dom_census(n, edges):
    adj, dist2 = middle(n, edges)
    counts = Counter()
    for mask in range(1 << len(adj)):
        if is_dom(mask, adj):
            assert is_semi(mask, dist2), (n, edges, mask)
            counts[mask.bit_count()] += 1
    assert counts == predicted_coeff(n, edges), (n, edges, counts, predicted_coeff(n, edges))
    return sum(counts.values())


def check_general():
    tally = Counter()
    for n in (3, 4, 5):
        possible = list(combinations(range(n), 2))
        for msk in range(1 << len(possible)):
            edges = [edge for i, edge in enumerate(possible) if msk >> i & 1]
            if connected(n, edges):
                all_dom_census(n, edges)
                tally[n] += 1
    rng = Random(1609)
    for n in (6, 7):
        possible = list(combinations(range(n), 2))
        seen = set()
        for trial in range(120):
            # Begin with a random spanning tree, then add up to four other edges.
            edges = set()
            for v in range(1, n):
                edges.add(tuple(sorted((v, rng.randrange(v)))))
            extra = rng.randrange(5)
            for _ in range(extra):
                edges.add(possible[rng.randrange(len(possible))])
            t = tuple(sorted(edges))
            if t in seen:
                continue
            seen.add(t)
            all_dom_census(n, list(t))
            tally[n] += 1
    print('GENERAL_CONNECTED_ROOTS_OK', dict(tally), sum(tally.values()), flush=True)


def is_minimum_set(n, edges, S):
    adj, dist2 = middle(n, edges)
    mask = sum(1 << i for i in S)
    return is_dom(mask, adj) and is_semi(mask, dist2)


def classified_minima(n, cycle):
    es = [(i, i + 1) for i in range(n - 1)] + ([(n - 1, 0)] if cycle else [])
    if n % 2 == 0:
        # Only perfect matchings, two if cyclic and one otherwise.
        configs = [frozenset(n + j for j in range(shift, len(es), 2)) for shift in range(2 if cycle else 1)]
    else:
        configs = []
        for old in range(n):
            # Unique matching of the remaining even path, if it exists.
            if not cycle and old % 2 == 1:
                continue
            available = [v for v in range(n) if v != old]
            if cycle:
                available = [(old + 1 + j) % n for j in range(n - 1)]
            paired = []
            for j in range(0, n - 1, 2):
                target = frozenset((available[j], available[j + 1]))
                ix = next(i for i, (u, v) in enumerate(es) if frozenset((u, v)) == target)
                paired.append(n + ix)
            configs.append(frozenset([old] + paired))
        # Covers by edges, with a unique double-covered old vertex.
        for repeated in range(n):
            if not cycle and repeated % 2 == 0:
                continue
            cover = []
            if cycle:
                # Edges adjacent to the repeated vertex, then unique remaining matching.
                for j, (u, v) in enumerate(es):
                    if repeated in (u, v):
                        cover.append(n + j)
                remaining = [(repeated + 2 + k) % n for k in range(n - 3)]
            else:
                # Repeated old vertex is even in 1-based indexing, odd in 0-based.
                for j, (u, v) in enumerate(es):
                    if repeated in (u, v):
                        cover.append(n + j)
                remaining = list(range(0, repeated - 1)) + list(range(repeated + 2, n))
            for j in range(0, len(remaining), 2):
                pair = frozenset((remaining[j], remaining[j + 1]))
                ix = next(i for i, (u, v) in enumerate(es) if frozenset((u, v)) == pair)
                cover.append(n + ix)
            configs.append(frozenset(cover))
    return es, set(configs)


def check_paths_cycles():
    for cycle in (False, True):
        for n in range(3, 13):
            es, expected = classified_minima(n, cycle)
            target = (2 if cycle else 1) if n % 2 == 0 else (2 * n if cycle else n)
            assert len(expected) == target, ('COUNT', cycle, n, expected)
            optsize = (n + 1) // 2
            assert all(len(S) == optsize and is_minimum_set(n, es, S) for S in expected), ('CLASS', cycle, n)
            actual = set()
            adj, dist2 = middle(n, es)
            for tup in combinations(range(len(adj)), optsize):
                mask = sum(1 << x for x in tup)
                if is_dom(mask, adj) and is_semi(mask, dist2):
                    actual.add(frozenset(tup))
            assert actual == expected, ('EXHAUSTIVE', cycle, n, actual ^ expected)
            print('MINIMUM_CLASSIFICATION_OK', 'cycle' if cycle else 'path', n, optsize, len(actual))


if __name__ == '__main__':
    check_general()
    check_paths_cycles()
    # Excluded K2 boundary: singleton middle edge dominates but lacks support.
    adj, dist2 = middle(2, [(0, 1)])
    assert is_dom(1 << 2, adj) and not is_semi(1 << 2, dist2)
    print('SHARP_TWO_VERTEX_BOUNDARY_OK')
    print('VERIFY_OK')
