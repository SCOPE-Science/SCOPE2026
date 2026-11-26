"""Exact rational identities and finite independent diagnostics for the spherical-cap simplex theorem.

Run using Python 3 without additional packages: python verify.py.
Finite diagnostics illustrate, but do not establish, the all-dimensional result.
"""
from fractions import Fraction as Q
from math import factorial, sqrt
import random


def verify_exact(n, t):
    t = Q(t)
    assert n >= 2 and Q(-1) < t <= Q(1, n)
    a2 = Q(n * n) * (1 - t * t) / (n * n - 1)
    b = Q(n) * (1 + t) / (n + 1)
    c = (1 - n * t) / (n + 1)
    assert (1 - c) / b == 1
    assert (-t - c) / b == -Q(1, n)
    assert (1 - t * t) / a2 == Q(n * n - 1, n * n)
    assert -(Q(n * n - 1, n * n) / (n - 1)) + Q(1, n * n) == -Q(1, n)
    for j in range(49):
        z = -t + (1 + t) * Q(j, 48)
        surplus = a2 * (1 - ((z - c) / b) ** 2) - (1 - z * z)
        factored = Q(2) * (1 - n * t) * (1 - z) * (z + t) / ((n - 1) * (1 + t))
        assert surplus == factored >= 0
    vball_sq = Q((n + 1) ** (n + 1), factorial(n) ** 2 * n ** n)
    cap_sq = ((1 + t) / n) ** 2 * Q(n ** n, factorial(n - 1) ** 2 * (n - 1) ** (n - 1)) * (1 - t * t) ** (n - 1)
    assert cap_sq == vball_sq * a2 ** (n - 1) * b * b
    if t == Q(1, n):
        assert cap_sq == vball_sq
    return 49


def det_float(mat):
    a = [list(row) for row in mat]
    m = len(a)
    val = 1.0
    for i in range(m):
        j = max(range(i, m), key=lambda k: abs(a[k][i]))
        if abs(a[j][i]) < 1e-14:
            return 0.0
        if j != i:
            a[i], a[j] = a[j], a[i]
            val = -val
        pivot = a[i][i]
        val *= pivot
        for j in range(i + 1, m):
            scale = a[j][i] / pivot
            for k in range(i + 1, m):
                a[j][k] -= scale * a[i][k]
    return val


def sample_point(n, t, rng):
    z = -t + (1 + t) * rng.random()
    transverse = [rng.gauss(0, 1) for _ in range(n - 1)]
    norm = sqrt(sum(x * x for x in transverse))
    radius = sqrt(max(0, 1 - z * z)) * rng.random() ** (1 / (n - 1))
    return [radius * x / norm for x in transverse] + [z]


def predicted_volume(n, t):
    full = (n + 1) ** ((n + 1) / 2) / (factorial(n) * n ** (n / 2))
    if t >= 1 / n:
        return full
    r = sqrt(1 - t * t)
    return (1 + t) / n * (n ** (n / 2)) / (factorial(n - 1) * (n - 1) ** ((n - 1) / 2)) * r ** (n - 1)


def main():
    exact = 0
    for n in range(2, 17):
        for t in (Q(-3, 4), Q(-1, 2), Q(0), Q(1, 2 * n), Q(1, n)):
            exact += verify_exact(n, t)
    rng = random.Random(20261011)
    tested = 0
    for n in range(2, 6):
        for t in (-0.8, -0.3, 0.0, 1 / n, 0.8):
            limit = predicted_volume(n, t)
            for _ in range(400):
                vertices = [sample_point(n, t, rng) for _ in range(n + 1)]
                columns = [[vertices[j][k] - vertices[0][k] for j in range(1, n + 1)] for k in range(n)]
                vol = abs(det_float(columns)) / factorial(n)
                assert vol <= limit * (1 + 1e-10)
                tested += 1
    print(f'VERIFY_OK exact_rational_surplus_checks={exact} stochastic_simplex_tests={tested} dimensions=2..16')


if __name__ == '__main__':
    main()
