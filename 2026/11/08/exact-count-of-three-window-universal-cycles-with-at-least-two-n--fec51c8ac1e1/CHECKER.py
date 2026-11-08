#!/usr/bin/env python3
"""Exact finite checks of the restricted three-window universal-cycle formula.

Standard-library Python only. Infinite parameter claim has a symbolic proof
in RESULT.md; this code performs finite, independently specified checks.
"""
from functools import lru_cache
from math import factorial


def make_graph(q):
    assert isinstance(q, int) and q >= 2
    vertices = [(a, b) for a in range(q) for b in range(q) if a or b]
    indexes = {v: i for i, v in enumerate(vertices)}
    triples = [(a, b, c) for a in range(q) for b in range(q)
               for c in range(q) if (a != 0) + (b != 0) + (c != 0) >= 2]
    edges = [(indexes[a, b], indexes[b, c]) for a, b, c in triples]
    lap = [[0] * len(vertices) for _ in vertices]
    deg = [0] * len(vertices)
    for u, v in edges:
        deg[u] += 1
        lap[u][v] -= 1
        lap[u][u] += 1
    assert len(vertices) == q * q - 1
    assert len(triples) == (q - 1) ** 2 * (q + 2)
    return vertices, triples, edges, lap, deg


def bareiss_det(matrix):
    """Exact determinant using fraction-free elimination with row pivoting."""
    a = [list(map(int, row)) for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    previous = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            r = next((r for r in range(k + 1, n) if a[r][k]), None)
            if r is None:
                return 0
            a[k], a[r] = a[r], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
        for i in range(k + 1, n):
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def predicted_arborescences(q):
    return q ** (q * (q - 2)) * (q - 1) ** (2 * (q - 2))


def predicted_cycles(q):
    return (predicted_arborescences(q)
            * factorial(q - 2) ** (2 * (q - 1))
            * factorial(q - 1) ** ((q - 1) ** 2))


def count_euler_circuits_directly(q):
    """Enumerate paths beginning with triple (1,1,1), no tree theorem used."""
    vertices, triples, edges, _, _ = make_graph(q)
    assert q <= 3
    start_edge = triples.index((1, 1, 1))
    root = vertices.index((1, 1))
    assert edges[start_edge] == (root, root)
    outgoing = [[] for _ in vertices]
    for i, (u, v) in enumerate(edges):
        outgoing[u].append((i, v))
    complete = (1 << len(edges)) - 1

    @lru_cache(None)
    def visit(at, used):
        if used == complete:
            return int(at == root)
        return sum(visit(nxt, used | (1 << i)) for i, nxt in outgoing[at]
                   if not (used >> i) & 1)

    return visit(root, 1 << start_edge)


def main():
    for q in range(2, 7):
        vertices, triples, edges, lap, deg = make_graph(q)
        indeg = [0] * len(vertices)
        for u, v in edges:
            indeg[v] += 1
        assert deg == indeg
        got = bareiss_det([row[1:] for row in lap[1:]])
        want = predicted_arborescences(q)
        assert got == want, (q, got, want)
        factorial_part = 1
        for d in deg:
            factorial_part *= factorial(d - 1)
        assert got * factorial_part == predicted_cycles(q)
        print(f'q={q}: edges={len(triples)}, arborescences={got}, cycles={predicted_cycles(q)}')
    for q in (2, 3):
        actual = count_euler_circuits_directly(q)
        assert actual == predicted_cycles(q)
        print(f'q={q}: direct Euler enumeration={actual}')
    print('VERIFIED: 5 exact Laplacian determinants, 2 independent Euler-tour enumerations')


if __name__ == '__main__':
    main()
