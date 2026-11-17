#!/usr/bin/env python3
"""Exact rational checks of metric certificates for cactus-root polytopes.

Uses only Python's standard library. Finite checks corroborate, not prove,
the all-orders theorem.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import log, isclose
from random import Random


def determinant(a):
    a = [[F(x) for x in row] for row in a]
    n = len(a)
    ans = F(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[pivot], a[j] = a[j], a[pivot]
            ans = -ans
        p = a[j][j]
        ans *= p
        for i in range(j + 1, n):
            mult = a[i][j] / p
            for k in range(j + 1, n):
                a[i][k] -= mult * a[j][k]
            a[i][j] = 0
    return ans


def inverse(a):
    n = len(a)
    m = [[F(z) for z in row] + [F(i == j) for j in range(n)]
         for i, row in enumerate(a)]
    for j in range(n):
        i = next((t for t in range(j, n) if m[t][j]), None)
        assert i is not None
        m[j], m[i] = m[i], m[j]
        pivot = m[j][j]
        m[j] = [x / pivot for x in m[j]]
        for k in range(n):
            if k != j:
                q = m[k][j]
                m[k] = [m[k][t] - q * m[j][t] for t in range(2 * n)]
    return [row[n:] for row in m]


def sample_cactus(rng):
    edges = []
    cycles = []
    n = 1
    nc = rng.randrange(4)
    nb = rng.randrange(1, 7)
    for _ in range(nc):
        length = rng.randrange(3, 9)
        hub = rng.randrange(n)
        vertices = [hub] + list(range(n, n + length - 1))
        n += length - 1
        seq = [tuple(sorted((vertices[i], vertices[(i + 1) % length])))
               for i in range(length)]
        edges.extend(seq)
        cycles.append(seq)
    for _ in range(nb):
        hub = rng.randrange(n)
        edges.append((hub, n))
        n += 1
    assert len(edges) == len(set(edges))
    return n, edges, cycles


def check_example(n, edges, cycles):
    d = n - 1
    membership = {e: len(cyc) for cyc in cycles for e in cyc}
    weights = {e: F(membership[e] - 1, membership[e]) if e in membership
               else F(1) for e in edges}
    assert sum(weights.values()) == d
    lap = [[F(0) for _ in range(d)] for _ in range(d)]
    for (u, v), w in weights.items():
        if u < d:
            lap[u][u] += w
        if v < d:
            lap[v][v] += w
        if u < d and v < d:
            lap[u][v] -= w
            lap[v][u] -= w
    expected = F(1)
    for cyc in cycles:
        k = len(cyc)
        expected *= k * F(k - 1, k)**(k - 1)
    assert determinant(lap) == expected, (n, cycles)
    inv = inverse(lap)
    for u, v in edges:
        b = [F(int(j == u) - int(j == v)) for j in range(d)]
        leverage = sum(b[i] * inv[i][j] * b[j]
                       for i in range(d) for j in range(d))
        assert leverage == 1, (n, (u, v), leverage)
    return len(edges)


def f(k):
    return k * ((k - 1) / k) ** (k - 1)


def check_extrema():
    trials = 0
    for n in range(3, 22):
        for c in range(1, min((n - 1) // 2, 5) + 1):
            options = [parts for parts in combinations_with_replacement(
                range(3, n + 1), c) if sum(k - 1 for k in parts) <= n - 1]
            vals = [sum(log(f(k)) for k in parts) for parts in options]
            floor = c * log(F(4, 3))
            q, r = divmod(n - 1, c)
            ceiling = (c - r)*log(f(q + 1)) + r*log(f(q + 2))
            assert isclose(min(vals), floor, rel_tol=0, abs_tol=1e-10)
            assert isclose(max(vals), ceiling, rel_tol=0, abs_tol=1e-10)
            for parts, val in zip(options, vals):
                if isclose(val, floor, rel_tol=0, abs_tol=1e-10):
                    assert set(parts) == {3}
                if isclose(val, ceiling, rel_tol=0, abs_tol=1e-10):
                    assert sum(k - 1 for k in parts) == n - 1
                    assert max(parts) - min(parts) <= 1
            trials += 1
    return trials


def main():
    rng = Random(20261103)
    edges_tested = 0
    for _ in range(110):
        n, edges, cycles = sample_cactus(rng)
        edges_tested += check_example(n, edges, cycles)
    profiles = check_extrema()
    print('CACTUS_ROOT_ELLIPSOID_EXACT_CHECKS_PASSED', 110,
          edges_tested, profiles)


if __name__ == '__main__':
    main()
