#!/usr/bin/env python3
"""Supplementary finite checks for the rank-penalized KL proximal formulas.

The analytic arguments in RESULT.md establish the infinite statements;
these computations are supplementary finite tests, not certificates of novelty.
"""
import itertools
import math
import random


def pava_desc(x):
    blocks = []
    for z in x:
        blocks.append([float(z), 1])
        while len(blocks) > 1 and blocks[-2][0] / blocks[-2][1] < blocks[-1][0] / blocks[-1][1]:
            a = blocks.pop()
            blocks[-1][0] += a[0]
            blocks[-1][1] += a[1]
    return [s / m for s, m in blocks for _ in range(m)]


def independent_isotonic(x):
    """Enumerate all contiguous block partitions; valid through dimension 7."""
    n = len(x)
    best = None
    best_loss = float('inf')
    for mask in range(1 << (n - 1)):
        ends = [k + 1 for k in range(n - 1) if mask & (1 << k)] + [n]
        starts = [0] + ends[:-1]
        vals = [sum(x[a:b]) / (b - a) for a, b in zip(starts, ends)]
        if any(vals[k] < vals[k + 1] - 1e-12 for k in range(len(vals) - 1)):
            continue
        v = [m for (a, b), m in zip(zip(starts, ends), vals) for _ in range(a, b)]
        loss = sum((a - b) ** 2 for a, b in zip(x, v))
        if loss < best_loss:
            best_loss, best = loss, v
    return best


def tmap(y, a, t):
    n = len(y)
    sigma = sorted(range(n), key=lambda i: (-y[i], i))
    z = [math.log(y[i]) - t * a[j] for j, i in enumerate(sigma)]
    v = pava_desc(z)
    m = max(v)
    exps = [math.exp(w - m) for w in v]
    out = [0.0] * n
    scale = sum(exps)
    for j, i in enumerate(sigma):
        out[i] = exps[j] / scale
    return out


def hitting_time(y, a):
    sigma = sorted(range(len(y)), key=lambda i: -y[i])
    z = [math.log(y[i]) for i in sigma]
    n = len(y)
    zm, am = sum(z) / n, sum(a) / n
    return max(
        (sum(z[:k]) - k * zm) / (sum(a[:k]) - k * am)
        for k in range(1, n)
    )


def kkt_entropy(y, a, t, p):
    """Check all first-order inequalities via independent active-block KKT."""
    n = len(y)
    sigma = sorted(range(n), key=lambda i: (-y[i], i))
    zs = [math.log(y[i]) - t * a[j] for j, i in enumerate(sigma)]
    ps = [p[i] for i in sigma]
    v = [math.log(s) for s in ps]
    tol = 2e-8
    if any(ps[j] < ps[j + 1] - tol for j in range(n - 1)):
        return False
    base = sum(v[j] - zs[j] for j in range(n)) / n
    g = [v[j] - zs[j] - base for j in range(n)]
    cumulative = 0.0
    for j in range(n - 1):
        cumulative += g[j]
        if cumulative < -tol:
            return False
        if ps[j] > ps[j + 1] + tol and abs(cumulative) > tol:
            return False
    return abs(sum(g)) < tol


def main():
    rng = random.Random(271828)
    n_checks = 0
    for n in range(2, 8):
        for _ in range(180):
            x = [rng.uniform(-6, 6) for _ in range(n)]
            v = pava_desc(x)
            alt = independent_isotonic(x)
            assert max(abs(a - b) for a, b in zip(v, alt)) < 1e-9
            n_checks += 1
    for n in range(2, 12):
        for _ in range(750):
            raw = [rng.uniform(-5, 5) for _ in range(n)]
            exps = [math.exp(z - max(raw)) for z in raw]
            y = [z / sum(exps) for z in exps]
            a = sorted((rng.uniform(-3, 4) for _ in range(n)), reverse=True)
            if abs(max(a) - min(a)) < 1e-12:
                continue
            s, t = rng.uniform(0, 4), rng.uniform(0, 4)
            p = tmap(y, a, t)
            q = tmap(p, a, s)
            r = tmap(y, a, t + s)
            assert max(abs(qi - ri) for qi, ri in zip(q, r)) < 3e-11
            assert kkt_entropy(y, a, t, p)
            T = hitting_time(y, a)
            assert T >= -1e-10
            uniform = tmap(y, a, T + 1e-7)
            assert max(abs(ui - 1 / n) for ui in uniform) < 1e-7
            if T > 1e-4:
                pre = tmap(y, a, T * .99)
                assert max(abs(pi - 1 / n) for pi in pre) > 1e-10
            n_checks += 4
    y = [.6, .3, .1]
    a = [2., 1., 0.]
    T = hitting_time(y, a)
    assert abs(T - math.log(18.) / 3.) < 1e-12 or abs(T - math.log(18.) / 3.) < 1e-10
    # Here T = (1/2)*log(18) / (3/2) = log(18)/3.
    print(f'PASS: {n_checks} finite assertions; example uniformization time={T:.12f}')


if __name__ == '__main__':
    main()
