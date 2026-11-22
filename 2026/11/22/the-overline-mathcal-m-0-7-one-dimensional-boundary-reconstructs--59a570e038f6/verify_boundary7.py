#!/usr/bin/env python3
"""Exact S7 Frobenius action on stable dual trees of Mbar_0,7.

All calculations use Python's integer arithmetic and the standard library.
A split of the seven labelled leaves is an unordered bipartition with
at least two leaves on each side, encoded by the smaller integer bitmask.
"""
import collections
import itertools
import json
import math

N = 7
FULL = (1 << N) - 1


def partitions(n, hi=None):
    if not n:
        yield ()
        return
    for d in range(min(n, hi or n), 0, -1):
        for tail in partitions(n - d, d):
            yield (d,) + tail


def canonical_split(mask):
    return min(mask, mask ^ FULL)


def is_compatible(a, b):
    ac, bc = a ^ FULL, b ^ FULL
    return not (a & b and a & bc and ac & b and ac & bc)


def all_split_systems(r):
    splits = sorted(set(canonical_split(x) for x in range(1, FULL)
                        if 2 <= x.bit_count() <= N - 2))
    assert len(splits) == 56
    for system in itertools.combinations(splits, r):
        if all(is_compatible(a, b) for a, b in itertools.combinations(system, 2)):
            yield system


def generate_binary_trees():
    # Start with a three-leaf tripod and repeatedly subdivide an edge.
    trees = [{(0, 7), (1, 7), (2, 7)}]
    for leaf in range(3, N):
        next_trees = []
        vertex = N + leaf - 2
        for edges in trees:
            for x, y in edges:
                updated = set(edges)
                updated.remove((x, y))
                updated.add(tuple(sorted((x, vertex))))
                updated.add(tuple(sorted((y, vertex))))
                updated.add(tuple(sorted((leaf, vertex))))
                next_trees.append(updated)
        trees = next_trees
    assert len(trees) == 945
    return trees


def splits_from_edges(edges):
    graph = collections.defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    result = []
    for u, v in edges:
        visited = {u}
        queue = [u]
        for x in queue:
            for y in graph[x]:
                if y not in visited and (x, y) not in ((u, v), (v, u)):
                    visited.add(y)
                    queue.append(y)
        m = sum(1 << k for k in visited if k < N)
        if 2 <= m.bit_count() <= N - 2:
            result.append(canonical_split(m))
    assert len(result) == 4
    return tuple(sorted(result))


def representative(cycle_lengths):
    p = list(range(N))
    offset = 0
    for d in cycle_lengths:
        for j in range(d):
            p[offset + j] = offset + ((j + 1) % d)
        offset += d
    return tuple(p)


def image_split(m, p):
    m2 = 0
    for k in range(N):
        if m & (1 << k):
            m2 |= (1 << p[k])
    return canonical_split(m2)


def transform(system, p):
    return tuple(sorted(image_split(m, p) for m in system))


def orbit_histogram(systems, perm):
    remaining = set(systems)
    hist = collections.Counter()
    while remaining:
        original = min(remaining)
        current = original
        orbit = []
        while current not in orbit:
            assert current in remaining, 'Permutation broke stable-split set'
            orbit.append(current)
            current = transform(current, perm)
        assert current == original
        remaining.difference_update(orbit)
        hist[len(orbit)] += 1
    assert sum(k * v for k, v in hist.items()) == len(systems)
    return dict(sorted(hist.items()))


def fixed(hist, n):
    return sum(d * count for d, count in hist.items() if n % d == 0)


def main():
    # Independent construction of all boundary trees: maximal compatible
    # split systems versus edge-insertion followed by edge contraction.
    binary_edge = generate_binary_trees()
    binary_splits = {splits_from_edges(tree) for tree in binary_edge}
    zero = set(all_split_systems(4))
    one = set(all_split_systems(3))
    contracted = {tuple(x for j, x in enumerate(t) if j != i)
                  for t in binary_splits for i in range(4)}
    assert len(zero) == len(binary_splits) == 945
    assert zero == binary_splits
    assert len(one) == len(contracted) == 1260
    assert one == contracted
    assert len(list(partitions(N))) == 15
    rows = []
    for part in partitions(N):
        p = representative(part)
        h1 = orbit_histogram(one, p)
        h0 = orbit_histogram(zero, p)
        rows.append({
            'cycle_partition': list(part),
            'one_dim_orbit_lengths': {str(k): v for k, v in h1.items()},
            'zero_dim_orbit_lengths': {str(k): v for k, v in h0.items()},
            'one_dim_fixed_degrees_1_to_5': [fixed(h1, k) for k in range(1, 6)],
            'zero_dim_fixed_degrees_1_to_5': [fixed(h0, k) for k in range(1, 6)],
        })
    signatures_one = [tuple(sorted(row['one_dim_orbit_lengths'].items())) for row in rows]
    signatures_zero = [tuple(sorted(row['zero_dim_orbit_lengths'].items())) for row in rows]
    assert len(set(signatures_one)) == 15
    assert len(set(signatures_zero)) == 11
    for k in range(1, 5):
        assert len({tuple(row['one_dim_fixed_degrees_1_to_5'][:k]) for row in rows}) < 15
    assert len({tuple(row['one_dim_fixed_degrees_1_to_5']) for row in rows}) == 15
    by_part = {tuple(r['cycle_partition']): r for r in rows}
    assert (by_part[(7,)]['one_dim_fixed_degrees_1_to_5'][:4]
            == by_part[(5, 2)]['one_dim_fixed_degrees_1_to_5'][:4]
            == by_part[(5, 1, 1)]['one_dim_fixed_degrees_1_to_5'][:4]
            == [0, 0, 0, 0])
    assert [by_part[part]['one_dim_fixed_degrees_1_to_5'][4]
            for part in [(7,), (5, 2), (5, 1, 1)]] == [0, 210, 1260]
    zero_collision_pairs = []
    for i, row in enumerate(rows):
        for other in rows[i+1:]:
            if row['zero_dim_orbit_lengths'] == other['zero_dim_orbit_lengths']:
                zero_collision_pairs.append([row['cycle_partition'], other['cycle_partition']])
    assert len(zero_collision_pairs) == 4
    result = {
        'geometric_one_dimensional_strata': 1260,
        'geometric_zero_dimensional_strata': 945,
        'S7_conjugacy_types': 15,
        'one_dimensional_spectra': 15,
        'zero_dimensional_spectra': 11,
        'minimum_consecutive_extension_cutoff_one_dimensional': 5,
        'zero_dimensional_collision_pairs': zero_collision_pairs,
        'rows': rows,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    print('PASS: exact 15-class finite-stratum Frobenius reconstruction', file=__import__('sys').stderr)

if __name__ == '__main__':
    main()
