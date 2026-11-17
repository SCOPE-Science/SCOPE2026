#!/usr/bin/env python3
"""Deterministic checks for sharp weighted tetrahedral projection quadrature.

Run with Python 3.9+ (standard library only):
    python tetra_quadrature_verifier.py
These finite checks supplement, but do not replace, the analytic proof.
"""
import itertools
import math
import random

V = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))
C = math.sqrt(2.0 / 3.0)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def norm(a):
    return math.sqrt(dot(a, a))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def point_value(n, w):
    assert len(w) == 4
    return (2.0 / math.sqrt(3.0)) * sum(wi * abs(dot(v, n)) for v, wi in zip(V, w)) / norm(n)


def bounds(w):
    assert len(w) == 4 and all(x > 0 for x in w)
    assert abs(sum(w) - 1.0) < 1e-12
    m = 2.0 * C * sum(sorted(w)[:2])
    imbalance = min(abs(sum(s * x for s, x in zip(sign, w)))
                    for sign in itertools.product((-1, 1), repeat=4))
    M = 4.0 / math.sqrt(3.0) * math.sqrt(sum(x * x for x in w) - imbalance * imbalance / 4.0)
    return m, M


def close(a, b, rtol=1e-11):
    assert abs(a - b) <= rtol * max(1.0, abs(a), abs(b)), (a, b)


def run():
    checks = 0
    for i, vi in enumerate(V):
        for j, vj in enumerate(V):
            assert dot(vi, vj) == (3 if i == j else -1)
            checks += 1
    for i, j in itertools.combinations(range(4), 2):
        n = cross(V[i], V[j])
        close(dot(n, V[i]), 0)
        close(dot(n, V[j]), 0)
        for k in set(range(4)) - {i, j}:
            close(abs(dot(n, V[k])) / (norm(n) * math.sqrt(3)), C)
            checks += 1
    rng = random.Random(20260905)
    tuples = [(1, 1, 1, 1), (1, 2, 3, 4), (1, 1, 1, 13),
              (2, 3, 5, 7), (1, 1, 2, 2), (3, 4, 4, 5)]
    tuples.extend(tuple(rng.randrange(1, 31) for _ in range(4)) for __ in range(40))
    for raw in tuples:
        w = tuple(float(x) / sum(raw) for x in raw)
        m, M = bounds(w)
        assert 0 < m <= M <= 2 + 1e-12
        # Every facet-normal candidate is represented; its least value is the true m.
        facet_vals = [point_value(cross(V[i], V[j]), w)
                      for i, j in itertools.combinations(range(4), 2)]
        close(min(facet_vals), m)
        checks += 1
        # Every signed vertex candidate is represented; its largest norm is the true M.
        signs = list(itertools.product((-1, 1), repeat=4))
        zvecs = [tuple(sum(s * wi * v[k] for s, wi, v in zip(sign, w, V))
                       for k in range(3)) for sign in signs]
        direct_max = 2 * max(norm(z) for z in zvecs) / math.sqrt(3)
        close(M, direct_max)
        checks += 1
        j = max(range(len(zvecs)), key=lambda k: norm(zvecs[k]))
        close(point_value(zvecs[j], w), M)
        checks += 1
        # No sample may violate the exact proved two-sided bound.
        for _ in range(250):
            n = tuple(rng.gauss(0, 1) for k in range(3))
            val = point_value(n, w)
            assert m - 1e-10 <= val <= M + 1e-10
            checks += 1
        E = max(1 - m, M - 1)
        assert E + 1e-12 >= 1 - C
        if len(set(raw)) == 1:
            close(E, 1 - C)
        else:
            assert E > 1 - C
        checks += 1
    uniform = (0.25,) * 4
    mu, Mu = bounds(uniform)
    close(mu, math.sqrt(2 / 3))
    close(Mu, 2 / math.sqrt(3))
    for i in range(3):
        n = tuple(1 if k == i else 0 for k in range(3))
        close(point_value(n, uniform), Mu)
        checks += 1
    for i in range(3):
        for j in range(i + 1, 3):
            for a in (-1, 1):
                for b in (-1, 1):
                    n = tuple(a if k == i else b if k == j else 0 for k in range(3))
                    close(point_value(n, uniform), mu)
                    checks += 1
    # Average over slab facet normals approaches the extremizing directional value.
    for raw in [(1, 1, 1, 1), (1, 2, 3, 4)]:
        w = tuple(float(x) / sum(raw) for x in raw)
        n = cross(V[0], V[1])
        u = tuple(x / norm(n) for x in n)
        t1 = tuple(x / norm(V[0]) for x in V[0])
        t2 = cross(u, t1)
        for thickness in (1e-2, 1e-4, 1e-6):
            slab_ratio = (point_value(u, w) + thickness * (point_value(t1, w) + point_value(t2, w))) / (1 + 2 * thickness)
            assert abs(slab_ratio - point_value(u, w)) < 4 * thickness
            checks += 1
    print(f"PASS: {checks} independent deterministic numerical/structural checks; no external dependencies")


if __name__ == '__main__':
    run()
