#!/usr/bin/env python3
"""Independent finite checks of a threefold parabola convolution identity.

Uses standard-library exact integer counts and a limited floating-point
Fourier orthogonality regression; finite checks do not certify the theorem.
"""
from collections import Counter
from cmath import exp
from math import pi


def norm_count(n, c):
    c %= n
    if c == 0:
        return n
    while c % 3 == 0:
        c //= 3
    return 2 * n if c % 3 == 1 else 0


def predicted(n, s, t):
    s %= n
    if s % 3:
        return n
    h = s // 3
    return norm_count(n, 2 * t - 6 * h * h)


def run_one(k):
    n = 3 ** k
    r = Counter()
    for u in range(n):
        for v in range(n):
            w0 = u + v
            t0 = u * u + v * v
            for w in range(n):
                r[((w0 + w) % n, (t0 + w * w) % n)] += 1
    counts = Counter()
    for s in range(n):
        for t in range(n):
            got = r[(s, t)]
            assert got == predicted(n, s, t), (n, s, t, got, predicted(n, s, t))
            counts[got] += 1
    expected = {0: n * (n - 1) // 6,
                n: n * (2 * n + 1) // 3,
                2 * n: n * (n - 1) // 6}
    assert dict(counts) == expected, (n, counts, expected)
    assert sum(counts.values()) == n * n
    assert len(r) == n * (5 * n + 1) // 6
    energy = sum(value * value for value in r.values())
    assert energy == n ** 3 * (4 * n - 1) // 3
    if n <= 9:
        zeta = exp(2j * pi / n)
        moment = 0.0
        for a in range(n):
            for b in range(n):
                g = sum(zeta ** ((a * u + b * u * u) % n) for u in range(n))
                moment += abs(g) ** 6
        moment /= n * n
        assert abs(moment - energy) < 1e-7 * max(1, energy), (moment, energy)
    print('k', k, 'N', n, 'multiplicities', dict(counts),
          'sumset', len(r), 'sixth_moment', energy, 'PASS')


if __name__ == '__main__':
    for k in range(1, 5):
        run_one(k)
    print('TERNARY_PARABOLA_TRIPLE_CONVOLUTION_CHECK_PASS')
