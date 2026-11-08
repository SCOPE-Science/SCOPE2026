#!/usr/bin/env python3
"""Exact verification of a restricted length-three universal-cycle count.

Only Python's standard library is used.  The determinant is evaluated by
fraction-free Bareiss elimination, independent of symbolic algebra packages.
"""
from itertools import product
from math import factorial


def minor_determinant(a):
    a = [list(row) for row in a]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if a[i][k]), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % prev == 0, (k, i, j)
                a[i][j] = numerator // prev
            a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]


def edge_set(q):
    return [(a, b, c) for a, b, c in product(range(q), repeat=3)
            if a == b or b == c or a == c]


def arborescence_count(q):
    vertices = list(product(range(q), repeat=2))
    index = {v: i for i, v in enumerate(vertices)}
    lap = [[0] * (q*q) for _ in range(q*q)]
    for a, b, c in edge_set(q):
        i = index[(a, b)]
        j = index[(b, c)]
        lap[i][i] += 1
        lap[i][j] -= 1
    return minor_determinant([row[1:] for row in lap[1:]])


def independent_euler_tours(q):
    # Fix the unique edge (0,0,0), so each cycle is visited once.
    edges = edge_set(q)
    out = {(a, b): [] for a in range(q) for b in range(q)}
    for i, (a, b, c) in enumerate(edges):
        out[(a, b)].append((i, (b, c)))
    root_edge = edges.index((0, 0, 0))
    all_edges = (1 << len(edges)) - 1

    def rec(vertex, used):
        if used == all_edges:
            return int(vertex == (0, 0))
        total = 0
        for i, target in out[vertex]:
            if not (used >> i) & 1:
                total += rec(target, used | (1 << i))
        return total

    return rec((0, 0), 1 << root_edge)


def formula(q):
    return 2 ** (q - 1) * 3 ** ((q - 1) * (q - 2) // 2) * q ** (q - 2) * factorial(q - 1) ** q


def main():
    for q in range(2, 7):
        edge_total = len(edge_set(q))
        assert edge_total == 3 * q * q - 2 * q
        t = arborescence_count(q)
        expected_t = 2 ** (q - 1) * 3 ** ((q - 1) * (q - 2) // 2) * q ** (q - 2)
        assert t == expected_t, (q, t, expected_t)
        total = t * factorial(q - 1) ** q
        assert total == formula(q)
        if q <= 3:
            dfs_count = independent_euler_tours(q)
            assert dfs_count == total, (q, dfs_count, total)
        print(f'q={q} edges={edge_total} arborescences={t} universal_cycles={total}')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
