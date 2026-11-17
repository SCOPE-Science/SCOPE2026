"""Reproducibility checks of the random closed-polygon area identities.

Run: python check_area_variance.py
Requires Python 3 and NumPy for the optional Stiefel simulation.
The exact permutation checks use only the Python standard library.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def area_from_order(edges):
    pos = (0, 0)
    twice = 0
    for edge in edges:
        q = (pos[0] + edge[0], pos[1] + edge[1])
        twice += cross(pos, q)
        pos = q
    assert pos == (0, 0)
    return Fraction(twice, 2)


def exact_test(edges):
    assert all(sum(e[k] for e in edges) == 0 for k in (0, 1))
    n = len(edges)
    values = [area_from_order([edges[i] for i in p]) for p in permutations(range(n))]
    mean = sum(values, Fraction(0)) / factorial(n)
    variance = sum((v - mean) ** 2 for v in values) / factorial(n)
    predicted = sum(Fraction(cross(edges[i], edges[j]) ** 2, 12)
                    for i in range(n) for j in range(i + 1, n))
    assert mean == 0 and variance == predicted, (n, mean, variance, predicted)
    s_xx = sum(e[0] ** 2 for e in edges)
    s_yy = sum(e[1] ** 2 for e in edges)
    s_xy = sum(e[0] * e[1] for e in edges)
    assert 12 * variance == s_xx * s_yy - s_xy ** 2
    return n


def test_exact():
    total = 0
    for n in range(3, 8):
        for seed in range(4 if n < 7 else 2):
            edges = [((3 * j * j + seed * j + 1) % 7 - 3,
                      (j * j + seed * 3 + 2 * j) % 9 - 4)
                     for j in range(n - 1)]
            edges.append((-sum(p[0] for p in edges), -sum(p[1] for p in edges)))
            exact_test(edges)
            total += 1
    print('EXACT_PERMUTATION_SETS_OK', total)


def test_stiefel():
    import numpy as np
    rng = np.random.default_rng(784521)
    for n in [3, 4, 5, 10, 25]:
        count = 180000
        batches = 9
        vals = []
        for _ in range(batches):
            raw = rng.normal(size=(count // batches, n, 2))
            frame, _ = np.linalg.qr(raw)
            u, v = frame[:, :, 0], frame[:, :, 1]
            e = (u * u - v * v) + 2j * u * v
            # Consecutive shoelace contributions from ordered edge lists.
            start = np.cumsum(e, axis=1) - e
            a = np.imag(np.conjugate(start) * e).sum(axis=1) / 2
            vals.append(a)
        sample = np.concatenate(vals)
        observed = float(np.var(sample))
        expected = 4 * (n - 2) / (3 * (n + 1) * (n + 2) * (n + 4))
        # Broad, documented stochastic tolerance, not a proof.
        assert abs(observed / expected - 1) < 0.04, (n, observed, expected)
        print('STIEFEL', n, 'observed', f'{observed:.9f}',
              'expected', f'{expected:.9f}')
    print('STIEFEL_AREA_VARIANCE_SAMPLING_OK')


if __name__ == '__main__':
    test_exact()
    test_stiefel()
    print('EXCHANGEABLE_SIGNED_AREA_VARIANCE_OK')
