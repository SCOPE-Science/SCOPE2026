"""Reproduce finite consistency tests for concentric Gaussian Fock Gram matrices.

The asymptotic and recurrence statements require the accompanying analytic proof.
Run: python CHECK.py  (requires numpy and mpmath).
"""
import math
import numpy as np
import mpmath as mp

mp.mp.dps = 65
checks = 0


def residue_moments(n, ell, t):
    # Truncation is exclusively for numerical cross-checks; not an infinite proof.
    Q = max(45, int((t + 20 * mp.sqrt(t)) / n) + 20)
    w = [mp.exp(-t) * t ** (ell + n * q) / mp.factorial(ell + n * q)
         for q in range(Q)]
    z = sum(w)
    mean = sum((ell + n * q) * v for q, v in enumerate(w)) / z
    variance = sum(((ell + n * q) - mean) ** 2 * v
                   for q, v in enumerate(w)) / z
    return n * z, variance


def c_moment(n, ell, r):
    lam, variance = residue_moments(n, ell, r * r)
    return lam * variance / (2 * r * r)


def c_roots(n, ell, t):
    omega = mp.exp(2j * mp.pi / n)
    terms = [omega ** (-ell * j) * mp.exp(t * (omega ** j - 1))
             for j in range(n)]
    v = [sum(terms[j] * (omega ** j - 1) ** k for j in range(n))
         for k in range(3)]
    return mp.re((v[0] + v[1] + t * v[2] - t * v[1] ** 2 / v[0]) / 2)


for n in (2, 3, 4, 5, 6, 9):
    for r_string in ('0.4', '1.1', '2.7'):
        r = mp.mpf(r_string)
        for ell in range(n):
            left = c_moment(n, ell, r)
            right = c_roots(n, ell, r * r)
            assert mp.almosteq(left, right, rel_eps=mp.mpf('1e-28'))
            checks += 1

for n in (2, 3, 4, 5):
    r = mp.mpf('0.03')
    vals = [c_moment(n, ell, r) for ell in range(n)]
    assert min(range(n), key=lambda j: vals[j]) == n - 1
    predicted = mp.mpf(n) ** 3 * r ** (4 * n - 4) / (2 * mp.factorial(2 * n - 1))
    assert abs(vals[n - 1] / predicted - 1) < mp.mpf('0.05')
    checks += 2

for n in (3, 4, 5, 6):
    theta = 2 * mp.pi / n
    omega = mp.exp(1j * theta)
    beta = mp.sin(theta)
    phi = mp.arg((omega - 1) ** 2)
    for ell in range(n):
        t = (mp.pi + ell * theta - phi + 12 * mp.pi) / beta
        vals = [c_roots(n, j, t) for j in range(n)]
        assert min(range(n), key=lambda j: vals[j]) == ell
        checks += 1

for n in (2, 3, 4, 6):
    for r, s in ((0.6, 1.1), (1.5, 1.9), (2.5, 2.8)):
        omega = np.exp(2j * np.pi / n)
        points = np.array([radius * omega ** j
                           for radius in (r, s) for j in range(n)])
        G = np.exp(points[:, None] * points[None, :].conjugate()
                   - (np.abs(points[:, None]) ** 2
                      + np.abs(points[None, :]) ** 2) / 2)
        direct = np.linalg.eigvalsh(G)
        blocks = []
        for ell in range(n):
            def F(x):
                term = x ** ell / math.factorial(ell)
                total = term
                for q in range(1, 45):
                    term *= x ** n / math.prod(range(ell + n * (q-1) + 1, ell + n*q + 1))
                    total += term
                return total
            B = n * np.array([[np.exp(-r*r)*F(r*r),
                               np.exp(-(r*r+s*s)/2)*F(r*s)],
                              [np.exp(-(r*r+s*s)/2)*F(r*s),
                               np.exp(-s*s)*F(s*s)]])
            blocks.extend(np.linalg.eigvalsh(B))
        assert np.allclose(direct, sorted(blocks), atol=2e-13, rtol=2e-11)
        checks += 1

print(f'PASS: {checks} independent finite consistency assertions; analytic proof is separate.')
