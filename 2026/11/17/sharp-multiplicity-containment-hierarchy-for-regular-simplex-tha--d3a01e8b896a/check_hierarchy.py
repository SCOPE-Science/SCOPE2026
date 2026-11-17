#!/usr/bin/env python3
"""Independent numerical diagnostics for regular-simplex Thales-ball multiplicity.

Requires only Python 3 standard library. Floating-point tests are not proofs.
"""
import math
import random
from itertools import combinations


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def unit(a):
    norm = math.sqrt(dot(a, a))
    return tuple(x / norm for x in a)


def vertices(d):
    n = d + 1
    scale = math.sqrt(n / d)
    return [tuple(scale * ((i == j) - 1 / n) for j in range(n)) for i in range(n)]


def point(V, I, k, m):
    d = len(V) - 1
    alpha = math.sqrt((d + 1 - m) / (d * m))
    s = [sum(V[i][j] for i in I) / m for j in range(d + 1)]
    u = unit([s[j] / alpha - V[k][j] for j in range(d + 1)])
    r = dot(u, s)
    return tuple(r * y for y in u), u, r


def gauge(V, x):
    return -(len(V) - 1) * min(dot(x, v) for v in V)


def members(V, x):
    return [i for i, v in enumerate(V)
            if dot(tuple(x[j] - v[j] / 2 for j in range(len(x))),
                   tuple(x[j] - v[j] / 2 for j in range(len(x))))
            <= 1 / 4 + 2e-11]


def main():
    rng = random.Random(190726)
    assertions = 0
    for d in range(2, 12):
        V = vertices(d)
        n = d + 1
        for i in range(n):
            for j in range(n):
                expected = 1 if i == j else -1 / d
                assert abs(dot(V[i], V[j]) - expected) < 2e-12
                assertions += 1
        for m in range(1, d + 1):
            bound = (1 + math.sqrt(d * (d + 1 - m) / m)) / 2
            seen = []
            for k in range(n):
                for I in combinations([i for i in range(n) if i != k], m):
                    x, u, r = point(V, I, k, m)
                    a = [dot(u, v) for v in V]
                    assert r > 0 and abs(r - sorted(a, reverse=True)[m - 1]) < 1e-10
                    assert set(members(V, x)) == set(I)
                    assert min(range(n), key=lambda z: a[z]) == k
                    assert abs(gauge(V, x) - bound) < 2e-10
                    seen.append(x)
                    assertions += 4
            assert len(seen) == n * math.comb(d, m)
            assertions += 1
            # Rank/dimension-independent upper bound tested on random directions.
            for _ in range(1600):
                w = [rng.gauss(0, 1) for _ in range(n)]
                mean = sum(w) / n
                u = unit([v - mean for v in w])
                a = sorted((dot(u, v) for v in V), reverse=True)
                r = max(0, a[m - 1])
                upper = d * r * (-a[-1])
                assert upper < bound + 1e-10
                assertions += 1
            assert bound > 1 if m < d else abs(bound - 1) < 1e-14
            assertions += 1
    print(f"PASS: {assertions} deterministic floating-point assertions, d=2..11")
    print("All-dimensional validity requires the analytic proof in RESULT.md.")


if __name__ == '__main__':
    main()
