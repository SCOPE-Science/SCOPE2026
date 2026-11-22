"""Finite checks for the Gaussian angular spectrum of orthogonal two-lineup products.

Run with Python 3, NumPy and SciPy: python VERIFY.py.
These computations corroborate; they do not certify asymptotic limits.
"""
import itertools
import math

import numpy as np
from scipy.integrate import quad
from scipy.stats import norm


def exposed_lineup(x, y):
    vals = sorted(((x[i] + y[j], i, j) for i in range(len(x)) for j in range(len(y))), reverse=True)
    return (vals[0][1:], vals[1][1:])


def count_vertices(p, q):
    seen = set()
    for i, k, j in itertools.product(range(p), range(p), range(q)):
        if i == k:
            continue
        x = [-100.0 - z for z in range(p)]
        y = [-100.0 - z for z in range(q)]
        x[i], x[k], y[j] = 10.0, 8.0, 10.0
        for l in range(q):
            if l != j:
                y[l] -= 50.0
        assert exposed_lineup(x, y) == ((i, j), (k, j))
        v = tuple(round(.7 * (h == i) + .3 * (h == k), 6) for h in range(p)) + tuple(float(l == j) for l in range(q))
        seen.add(v)
    row_count = len(seen)
    assert row_count == p * (p - 1) * q
    for i, j, l in itertools.product(range(p), range(q), range(q)):
        if j == l:
            continue
        x = [-100.0 - z for z in range(p)]
        y = [-100.0 - z for z in range(q)]
        x[i], y[j], y[l] = 10.0, 10.0, 8.0
        for k in range(p):
            if k != i:
                x[k] -= 50.0
        assert exposed_lineup(x, y) == ((i, j), (i, l))
        v = tuple(float(h == i) for h in range(p)) + tuple(round(.7 * (k == j) + .3 * (k == l), 6) for k in range(q))
        seen.add(v)
    assert len(seen) == p * q * (p + q - 2)
    return len(seen)


def full_top_r(x, y, r):
    x = sorted(x, reverse=True)
    y = sorted(y, reverse=True)
    outer = sorted(((a + b, i, j) for i, a in enumerate(x) for j, b in enumerate(y)), reverse=True)
    cropped = sorted(((x[i] + y[j], i, j) for i in range(r) for j in range(r)), reverse=True)
    assert outer[:r] == cropped[:r]


def survival(m, t):
    return m * quad(lambda x: norm.pdf(x) * norm.cdf(x - t) ** (m - 1), -11, 11, epsabs=2e-10)[0]


def gap_density(m, t):
    return m * (m - 1) * quad(lambda x: norm.pdf(x) * norm.pdf(x - t) * norm.cdf(x - t) ** (m - 2), -11, 11, epsabs=2e-10)[0]


def alpha(p, q):
    return quad(lambda t: gap_density(p, t) * survival(q, t), 0, 12, epsabs=5e-9)[0]


def main():
    count = sum(count_vertices(p, q) for p in range(2, 6) for q in range(2, 6))
    rng = np.random.default_rng(420611)
    rank_cases = 0
    for p in range(2, 9):
        for q in range(2, 9):
            for _ in range(70):
                x = rng.normal(size=p).tolist()
                y = rng.normal(size=q).tolist()
                for r in range(1, min(p, q) + 1):
                    full_top_r(x, y, r)
                    rank_cases += 1
    a22, a23, a32, a33 = alpha(2, 2), alpha(2, 3), alpha(3, 2), alpha(3, 3)
    assert abs(a22 - 0.5) < 1e-8
    assert abs(a33 - 0.5) < 1e-8
    assert abs(a23 + a32 - 1) < 1e-8
    assert abs(a23 - 0.404919815756) < 2e-8
    assert abs((a33 * a33 / 18 + (1 - a33) ** 2 / 18) - 1 / 36) < 1e-9
    n = 180000
    x = rng.normal(size=(n, 2))
    y = rng.normal(size=(n, 3))
    monte = np.mean((np.max(x, axis=1) - np.min(x, axis=1)) < (np.max(y, axis=1) - np.partition(y, -2, axis=1)[:, -2]))
    assert abs(monte - a23) < 0.012
    # Independent Gaussian objective pairs directly check the collision formula.
    pair_n = 180000
    def random_vertex_codes():
        xx = rng.normal(size=(pair_n, 2))
        yy = rng.normal(size=(pair_n, 3))
        ri = np.argsort(xx, axis=1)[:, -2:][:, ::-1]
        cj = np.argsort(yy, axis=1)[:, -2:][:, ::-1]
        rd = xx[np.arange(pair_n), ri[:, 0]] - xx[np.arange(pair_n), ri[:, 1]]
        cd = yy[np.arange(pair_n), cj[:, 0]] - yy[np.arange(pair_n), cj[:, 1]]
        typ = (rd < cd).astype(int)
        second = np.where(typ == 1, ri[:, 1], cj[:, 1])
        return np.stack([typ, ri[:, 0], cj[:, 0], second], axis=1)
    c1, c2 = random_vertex_codes(), random_vertex_codes()
    collision_monte = np.mean(np.all(c1 == c2, axis=1))
    c23 = a23*a23/6 + (1-a23)**2/12
    assert abs(collision_monte - c23) < 0.0035
    print(f'LINEUP_ANGULAR_FINITE_PASS vertices={count} top_rank_cases={rank_cases} alpha_2_3={a23:.12f} monte={monte:.6f} collision_monte={collision_monte:.6f}')


if __name__ == '__main__':
    main()
