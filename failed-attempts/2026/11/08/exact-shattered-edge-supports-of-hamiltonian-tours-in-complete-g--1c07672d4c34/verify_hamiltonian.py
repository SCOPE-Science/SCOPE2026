#!/usr/bin/env python3
"""Independent finite trace checks for Hamilton-cycle edge shattering.

Standard-library-only. Run with Python 3.9+.
"""
from collections import Counter
from itertools import combinations, permutations
from math import factorial


def undirected_cycles(n):
    edges = list(combinations(range(n), 2))
    index = {e: i for i, e in enumerate(edges)}
    masks = []
    for p in permutations(range(1, n)):
        if p[0] > p[-1]:
            continue
        q = (0,) + p
        masks.append(sum(1 << index[tuple(sorted((q[i], q[(i + 1) % n])))]
                         for i in range(n)))
    assert len(masks) == factorial(n-1) // 2
    return edges, masks


def is_shattered(indices, masks):
    mask = sum(1 << i for i in indices)
    traces = {c & mask for c in masks}
    return len(traces) == (1 << len(indices))


def classify(n, indices, edges):
    m = len(indices)
    if m == 0:
        return True
    if m >= n-1:
        return False
    degree = [0] * n
    parent = list(range(n))

    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v

    for i in indices:
        a, b = edges[i]
        degree[a] += 1
        degree[b] += 1
        if degree[a] > 2 or degree[b] > 2:
            return False
        a, b = root(a), root(b)
        if a == b:
            return False
        parent[a] = b
    if m <= n-3:
        return True
    # m=n-2: exactly two path components, including isolated points.
    comp = Counter(root(v) for v in range(n))
    lens = sorted(v - 1 for v in comp.values())
    assert len(lens) == 2 and sum(lens) == m
    return (lens[0] == 0 and lens[1] >= 3) or (lens[0] >= 3)


def partitions(total, low=1):
    if total == 0:
        yield ()
        return
    for v in range(low, total + 1):
        for tail in partitions(total - v, v):
            yield (v,) + tail


def forest_count(n):
    out = Counter()
    for comp_sizes in partitions(n):
        a = Counter(comp_sizes)
        denom = 1
        for size, multiplicity in a.items():
            denom *= factorial(multiplicity)
            if size >= 2:
                denom *= 2 ** multiplicity
        m = n - len(comp_sizes)
        assert factorial(n) % denom == 0
        out[m] += factorial(n) // denom
    return out


def expected_counts(n):
    f = forest_count(n)
    out = Counter({0: 1})
    for m in range(1, n - 2):
        out[m] = f[m]
    if n >= 5:
        unequal = max(0, (n-1)//2 - 3)
        out[n-2] = (factorial(n)//2 + factorial(n)//4 * unequal
                    + (factorial(n)//8 if n % 2 == 0 and n >= 8 else 0))
    return out


def representative(n, lengths, edges):
    edge_index = {e: i for i, e in enumerate(edges)}
    used = 0
    inds = []
    for length in lengths:
        for j in range(length):
            inds.append(edge_index[(used+j, used+j+1)])
        used += length+1
    assert used <= n
    return tuple(inds)


def verify():
    fully_checked = 0
    representatives = 0
    for n in range(3, 8):
        edges, cycles = undirected_cycles(n)
        tally = Counter({0: 1})
        for m in range(1, n+1):
            for indices in combinations(range(len(edges)), m):
                actual = is_shattered(indices, cycles)
                predicted = classify(n, indices, edges)
                assert actual == predicted, (n, indices, actual, predicted)
                fully_checked += 1
                tally[m] += actual
        expected = expected_counts(n)
        assert {k:v for k,v in tally.items() if v} == {k:v for k,v in expected.items() if v}, (n, tally, expected)
        print('EXHAUSTIVE', n, 'shattered counts', sorted(tally.items()))
    for n in (8, 9):
        edges, cycles = undirected_cycles(n)
        for m in range(1, n):
            for lengths in partitions(m):
                if m + len(lengths) > n:
                    continue
                inds = representative(n, lengths, edges)
                assert is_shattered(inds, cycles) == classify(n, inds, edges), (n, lengths)
                representatives += 1
        print('REPRESENTATIVE_TYPES', n, 'passed')
    assert expected_counts(8)[6] == 25200
    assert expected_counts(9)[7] == 272160
    print('HAMILTONIAN_EDGE_SHATTERING_CHECKS_PASS',
          'exhaustive_supports=', fully_checked,
          'representative_types=', representatives)


if __name__ == '__main__':
    verify()
