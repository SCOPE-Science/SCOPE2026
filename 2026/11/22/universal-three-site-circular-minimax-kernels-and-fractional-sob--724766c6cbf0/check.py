"""Finite numerical spot checks of an analytically proved circle-kernel theorem.

Run with Python 3.10 or newer: python check.py
All Fourier truncations and random trials are corroborative, not proofs.
"""

import math
import random


def kernel(s, t, terms=4096):
    t = t % 1.0
    a = 2.0 / ((2.0 * math.pi) ** (2.0 * s))
    return a * sum(math.cos(2.0 * math.pi * n * t) / (n ** (2.0 * s))
                   for n in range(1, terms + 1))


def root(s, terms=4096):
    lo, hi = 0.0, 1.0 / 6.0
    assert kernel(s, lo, terms) + kernel(s, 2.0 * lo, terms) > 0
    assert kernel(s, hi, terms) + kernel(s, 2.0 * hi, terms) < 0
    for _ in range(48):
        mid = (lo + hi) / 2.0
        f = kernel(s, mid, terms) + kernel(s, 2.0 * mid, terms)
        if f > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def eigmax_symmetric3(a):
    a = [list(row) for row in a]
    for _ in range(40):
        i, j = max(((0, 1), (0, 2), (1, 2)),
                   key=lambda ij: abs(a[ij[0]][ij[1]]))
        if abs(a[i][j]) < 1e-14 * max(abs(a[k][k]) for k in range(3)):
            break
        tau = (a[j][j] - a[i][i]) / (2.0 * a[i][j])
        t = (1.0 if tau >= 0 else -1.0) / (abs(tau) + math.sqrt(1.0 + tau * tau))
        c = 1.0 / math.sqrt(1.0 + t * t)
        ss = t * c
        v = a[i][j]
        a[i][i] -= t * v
        a[j][j] += t * v
        a[i][j] = a[j][i] = 0.0
        for k in range(3):
            if k not in (i, j):
                z, w = a[k][i], a[k][j]
                a[k][i] = a[i][k] = c * z - ss * w
                a[k][j] = a[j][k] = ss * z + c * w
    return max(a[i][i] for i in range(3))


def gram(s, pts, terms=4096):
    return [[kernel(s, x - y, terms) for y in pts] for x in pts]


def main():
    checks = 0
    # Exact elementary check for the previously known order-one instance.
    d1 = (9.0 - math.sqrt(21.0)) / 30.0
    b = lambda t: (t * t - t + 1.0 / 6.0) / 2.0
    assert abs(b(d1) + b(2.0 * d1)) < 1e-14
    assert abs(1.0 / 12.0 + b(d1) - (11.0 + math.sqrt(21.0)) / 150.0) < 1e-13
    checks += 2

    rng = random.Random(2026)
    for s, terms in ((1.5, 4096), (2.0, 3000), (3.0, 1200), (5.0, 300)):
        d = root(s, terms)
        k = kernel(s, 0, terms)
        p = kernel(s, d, terms)
        best = k + p
        assert 0 < d < 1.0 / 6.0
        assert p > 0
        assert abs(p + kernel(s, 2 * d, terms)) < 1e-12 * k
        assert abs(eigmax_symmetric3(gram(s, [0, d, 2 * d], terms)) - best) < 1e-11 * k
        checks += 4
        for _ in range(180):
            pts = sorted((rng.random(), rng.random(), rng.random()))
            gaps = [pts[1] - pts[0], pts[2] - pts[1],
                    1.0 - (pts[2] - pts[0])]
            pair_lower = k + max(abs(kernel(s, g, terms)) for g in gaps)
            val = eigmax_symmetric3(gram(s, pts, terms))
            assert pair_lower + 1e-10 * k >= best
            assert val + 1e-10 * k >= pair_lower
            checks += 2
        # Equally spaced sites are worse than the double-small-gap design.
        equal = eigmax_symmetric3(gram(s, [0, 1 / 3, 2 / 3], terms))
        assert equal > best
        checks += 1

    target_offset = 1.0 / (3.0 * math.pi * math.sqrt(3.0))
    for s, tol in ((5.0, .002), (7.0, .0003)):
        terms = 300
        d = root(s, terms)
        k = kernel(s, 0, terms)
        best = k + kernel(s, d, terms)
        equi = k - kernel(s, 1 / 3, terms)
        offset = (4.0 ** s) * (1 / 6 - d)
        gain = (4.0 ** s) * (equi - best) / k
        assert abs(offset - target_offset) < tol
        assert abs(gain - 2 / 3) < 0.002
        checks += 2
    print(f"PASS: {checks} numerical checks (finite corroboration only)")


if __name__ == '__main__':
    main()
