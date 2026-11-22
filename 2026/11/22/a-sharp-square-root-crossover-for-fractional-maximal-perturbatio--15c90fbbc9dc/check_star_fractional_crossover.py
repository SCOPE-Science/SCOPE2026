#!/usr/bin/env python3
"""Reproduce finite-star fractional-maximal perturbation diagnostics (stdlib only)."""
import cmath
import math
import random


def maximal(x, alpha):
    m = len(x) - 1
    assert m >= 2 and 0.0 < alpha < 1.0
    z = [abs(v) for v in x]
    h = (m + 1) ** (alpha - 1)
    b = 2 ** (alpha - 1)
    total = sum(z)
    return [max(z[0], h * total)] + [
        max(z[i], b * (z[0] + z[i]), h * total) for i in range(1, m + 1)
    ]


def norm(x):
    return math.sqrt(sum(abs(v) ** 2 for v in x))


def edge_norm(x):
    return norm([v - x[0] for v in x[1:]])


def bounds(m, alpha):
    h = (m + 1) ** (alpha - 1)
    lo = math.sqrt(m * ((1 - h) ** 2 + m * h ** 2))
    hi = 1 + math.sqrt(m + m * m * h * h)
    return lo, hi


def witness(m, alpha):
    h = (m + 1) ** (alpha - 1)
    b = 2 ** (alpha - 1)
    U = (1 / h - 1) / m
    assert 0 < U < min(1, 1 / b - 1) + 2e-13
    for k in range(1, 50):
        u = U * (1 - 2 ** (-k))
        glob = h * (1 + m * u)
        if 1 > glob > max(u, b * (1 + u)):
            break
    else:
        raise AssertionError('no feasible strict branch found')
    x = [1.0] + [u] * m
    w = [h - 1] + [h] * m
    wnorm = norm(w)
    for k in range(6, 48):
        eps = 2 ** (-k)
        y = [v + eps * t / wnorm for v, t in zip(x, w)]
        if min(y) <= 0:
            continue
        hy = h * sum(y)
        if not (y[0] > hy and all(hy > max(y[i], b * (y[0] + y[i])) for i in range(1, m + 1))):
            continue
        mx, my = maximal(x, alpha), maximal(y, alpha)
        direct = edge_norm([a - c for a, c in zip(my, mx)]) / norm([a - c for a, c in zip(y, x)])
        expected = math.sqrt(m) * wnorm
        if math.isclose(direct, expected, rel_tol=2e-7, abs_tol=1e-7):
            return expected, direct
    raise AssertionError('failed finite local witness')


def run():
    rng = random.Random(73549)
    count = 0
    for m in (2, 3, 4, 5, 8, 15, 32, 80):
        for alpha in (0.1, 0.35, 0.5, 0.72, 0.9):
            lo, hi = bounds(m, alpha)
            exact, direct = witness(m, alpha)
            assert math.isclose(lo, exact, rel_tol=2e-13)
            assert math.isclose(lo, direct, rel_tol=2e-7)
            assert lo <= hi
            for _ in range(70):
                f = [rng.uniform(-3, 5) for _ in range(m + 1)]
                g = [rng.uniform(-3, 5) for _ in range(m + 1)]
                mf, mg = maximal(f, alpha), maximal(g, alpha)
                delta = [u - v for u, v in zip(mf, mg)]
                ratio = edge_norm(delta) / norm([u - v for u, v in zip(f, g)])
                assert ratio <= hi + 1e-10
                count += 1
            for _ in range(30):
                f = [complex(rng.uniform(-2, 2), rng.uniform(-2, 2)) for _ in range(m + 1)]
                g = [complex(rng.uniform(-2, 2), rng.uniform(-2, 2)) for _ in range(m + 1)]
                mf, mg = maximal(f, alpha), maximal(g, alpha)
                delta = [u - v for u, v in zip(mf, mg)]
                ratio = edge_norm(delta) / norm([u - v for u, v in zip(f, g)])
                assert ratio <= hi + 1e-10
                count += 1
    for s in (-1.0, 0.0, 1.0):
        target = math.sqrt(1 + math.exp(2 * s))
        m = 10 ** 7
        a = 0.5 + s / math.log(m)
        lo, hi = bounds(m, a)
        assert lo / math.sqrt(m) <= target + 0.01
        assert hi / math.sqrt(m) >= target - 0.01
        assert abs(lo / math.sqrt(m) - target) < 0.005
        assert abs(hi / math.sqrt(m) - target) < 0.005
    print('PASS: 40 strict positive local extremizing pairs; 4000 real/complex two-input estimates; three critical-window checks')


if __name__ == '__main__':
    run()
