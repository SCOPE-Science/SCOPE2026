#!/usr/bin/env python3
import collections
import itertools
import math


def integer_partitions(n, lo=1):
    if n == 0:
        yield []
        return
    for first in range(lo, n + 1):
        for rest in integer_partitions(n - first, first):
            yield [first] + rest


def graph(parts):
    part_of = []
    for i, size in enumerate(parts):
        part_of.extend([i] * size)
    n = len(part_of)
    adj = [set() for _ in range(n)]
    for u in range(n):
        for v in range(u + 1, n):
            if part_of[u] != part_of[v]:
                adj[u].add(v)
                adj[v].add(u)
    return adj


def is_zero_forcing(parts, blue):
    adj = graph(parts)
    blue = set(blue)
    while True:
        force = None
        for u in sorted(blue):
            white_neighbors = [v for v in adj[u] if v not in blue]
            if len(white_neighbors) == 1:
                force = white_neighbors[0]
                break
        if force is None:
            break
        blue.add(force)
    return len(blue) == len(adj)


def brute_coefficients(parts):
    n = sum(parts)
    counts = collections.Counter()
    for mask in range(1 << n):
        blue = [v for v in range(n) if (mask >> v) & 1]
        if is_zero_forcing(parts, blue):
            counts[len(blue)] += 1
    return dict(counts)


def formula_coefficients(parts):
    n = sum(parts)
    s = sum(size == 1 for size in parts)
    q = len(parts) - s
    counts = {n: 1, n - 1: n}
    if q:
        cross_pairs = sum(parts[i] * parts[j]
                          for i in range(len(parts))
                          for j in range(i + 1, len(parts)))
        counts[n - 2] = cross_pairs - math.comb(s, 2)
    return {k: v for k, v in counts.items() if v}


def main():
    tested = 0
    for n in range(2, 9):
        for parts in integer_partitions(n):
            if len(parts) < 2:
                continue
            got = brute_coefficients(parts)
            want = formula_coefficients(parts)
            assert got == want, (parts, got, want)
            tested += 1
    assert tested == 58
    print('VERIFY_OK')
    print('multipartite_types_checked=58')
    print('orders_checked=2..8')


if __name__ == '__main__':
    main()
