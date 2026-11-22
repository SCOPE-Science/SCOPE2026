#!/usr/bin/env python3
"""Independent exact checks for universal cycles with a required letter.

Uses only the Python standard library. Finite checks corroborate an all-order
matrix identity proved separately; they do not establish that identity.
"""
from itertools import product
from math import factorial


def determinant(a):
    """Integer determinant by fraction-free elimination."""
    a = [list(row) for row in a]
    n = len(a)
    if n == 0:
        return 1
    d = 1
    sign = 1
    for k in range(n - 1):
        if not a[k][k]:
            h = next((h for h in range(k + 1, n) if a[h][k]), None)
            if h is None:
                return 0
            a[k], a[h] = a[h], a[k]
            sign = -sign
        p = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                t = a[i][j] * p - a[i][k] * a[k][j]
                assert t % d == 0
                a[i][j] = t // d
            a[i][k] = 0
        d = p
    return sign * a[-1][-1]


def graph(q, n):
    assert q >= 2 and n >= 2
    vs = list(product(range(q), repeat=n - 1))
    pos = {v: i for i, v in enumerate(vs)}
    edges = []
    for v in vs:
        for c in range(q):
            if 0 in v or c == 0:
                edges.append((pos[v], pos[v[1:] + (c,)], v + (c,)))
    return vs, edges


def laplacian(vs, edges):
    l = [[0] * len(vs) for _ in vs]
    for i, j, _ in edges:
        l[i][i] += 1
        l[i][j] -= 1
    return l


def count_tours(vs, edges, q, n):
    """Independently count Euler circuits starting with the 0^n edge."""
    start = next(i for i, e in enumerate(edges) if e[2] == (0,) * n)
    outgoing = [[] for _ in vs]
    for i, (u, _v, _w) in enumerate(edges):
        outgoing[u].append(i)
    u0 = edges[start][0]
    current = edges[start][1]
    used0 = 1 << start
    allused = (1 << len(edges)) - 1
    memo = {}

    def walk(v, used):
        if used == allused:
            return int(v == u0)
        key = (v, used)
        if key in memo:
            return memo[key]
        val = sum(walk(edges[e][1], used | (1 << e))
                  for e in outgoing[v] if not (used >> e) & 1)
        memo[key] = val
        return val

    return walk(current, used0)


def check(q, n, tours=False):
    vs, edges = graph(q, n)
    l = laplacian(vs, edges)
    size = q ** (n - 1)
    empty = (q - 1) ** (n - 1)
    active = size - empty
    assert len(vs) == size and len(edges) == q**n - (q - 1)**n
    assert [sum(row) for row in l] == [0] * size
    assert [sum(l[i][j] for i in range(size)) for j in range(size)] == [0] * size
    t = determinant([row[1:] for row in l[1:]])
    assert t == q ** (active - n + 1), (q, n, t)
    for x in (1, 2, 5):
        matrix = [[(x if i == j else 0) + l[i][j]
                   for j in range(size)] for i in range(size)]
        expected = x * (x + 1) ** (empty - 1) * (x + q) ** active
        assert determinant(matrix) == expected, (q, n, x)
    prediction = t * factorial(q - 1) ** active
    if tours:
        actual = count_tours(vs, edges, q, n)
        assert prediction == actual, (q, n, actual, prediction)
    print('CHECK', q, n, 'vertices', size, 'edges', len(edges),
          'arborescences', t, 'cyclic_words', prediction,
          'tours_checked', tours)


def main():
    for q in range(2, 5):
        for n in range(2, 5):
            if q**(n - 1) <= 64:
                check(q, n, tours=(q, n) in ((2, 2), (2, 3), (2, 4),
                                             (3, 2), (3, 3), (4, 2)))
    check(2, 7)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
