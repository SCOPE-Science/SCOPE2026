#!/usr/bin/env python3
"""Verify exact color-refinement stabilization on starlike trees.
Python 3 standard library only. Run: python verify_spider.py
"""
from itertools import combinations_with_replacement
from collections import defaultdict


def spider(arms):
    assert len(arms) >= 3 and all(x >= 1 for x in arms)
    n = 1 + sum(arms)
    adjacency = [set() for _ in range(n)]
    coordinates = [None]  # the unique branching center
    next_vertex = 1
    for length in arms:
        parent = 0
        for distance in range(1, length + 1):
            v = next_vertex
            next_vertex += 1
            adjacency[v].add(parent)
            adjacency[parent].add(v)
            coordinates.append((distance, length - distance))
            parent = v
    assert next_vertex == n
    return adjacency, coordinates


def same_partition(a, b):
    return all((a[i] == a[j]) == (b[i] == b[j])
               for i in range(len(a)) for j in range(i))


def rounds_and_check(arms):
    adjacency, coords = spider(arms)
    colors = [0] * len(coords)
    distinct = sorted(set(arms))
    expected_rounds = max((distinct[-1] + 1) // 2,
                          (distinct[-2] + 1 if len(distinct) >= 2 else 0))
    stable = None
    for t in range(1, len(coords) + 1):
        keys = [(colors[v], tuple(sorted(colors[w] for w in adjacency[v])))
                for v in range(len(coords))]
        palette = {key: i for i, key in enumerate(sorted(set(keys)))}
        next_colors = [palette[key] for key in keys]
        expected_types = [(-1, -1) if d is None else
                          (min(d[0], t), min(d[1], t)) for d in coords]
        assert same_partition(next_colors, expected_types), (arms, t, 'capped pair')
        if len(set(next_colors)) == len(set(colors)):
            stable = t - 1
            break
        colors = next_colors
    # The stabilization time is the last round with a genuine split.
    assert stable == expected_rounds, (arms, stable, expected_rounds)
    orbit_types = [(-1, -1) if d is None else (d[0], d[1]) for d in coords]
    assert same_partition(colors, orbit_types), (arms, 'orbit')
    return stable


def main():
    totals = {}
    for k in (3, 4, 5, 6):
        count = 0
        maximal_rounds = 0
        for arms in combinations_with_replacement(range(1, 10), k):
            actual = rounds_and_check(arms)
            maximal_rounds = max(maximal_rounds, actual)
            count += 1
        totals[k] = (count, maximal_rounds)
        print(f'arms={k} length_range=1..9 cases={count} max_rounds={maximal_rounds}')
    for k in (3, 5, 8, 12):
        for m in (10, 16, 24, 35):
            for arms in [(m,) * k, (1,) * (k - 1) + (m,),
                         (m - 1,) * (k - 1) + (m,)]:
                rounds_and_check(arms)
    print('large_adversarial_cases=48')
    print('VERIFY_OK cases=' + str(sum(v[0] for v in totals.values()) + 48))


if __name__ == '__main__':
    main()
