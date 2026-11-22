"""Supplementary finite-dimensional checks for two integer block averages.
Run: python check.py ; requires NumPy. The infinite-dimensional proof is in RESULT.md.
"""
import math
import numpy as np


def compressed(m, n):
    """m<n coprime; Gram and residue-path matrix on one length-mn cell."""
    assert 2 <= m < n and math.gcd(m, n) == 1
    overlap = np.zeros((n, m))
    for k in range(n):
        for j in range(m):
            overlap[k, j] = max(0, min((k + 1) * m, (j + 1) * n)
                                 - max(k * m, j * n)) / math.sqrt(m * n)
    weights = np.array([(j * n % m) * (m - (j * n % m)) / m
                        for j in range(1, m)])
    lap = np.zeros((m, m))
    for j, w in enumerate(weights):
        lap[j, j] += w
        lap[j + 1, j + 1] += w
        lap[j, j + 1] -= w
        lap[j + 1, j] -= w
    return overlap, lap


def block_projection(q, N):
    assert N % q == 0
    return np.kron(np.eye(N // q), np.ones((q, q)) / q)


def positive_amplitudes(m, n):
    # gcd reduction is exact, including the divisible case.
    g = math.gcd(m, n)
    m, n = sorted((m // g, n // g))
    if m == 1:
        return np.array([])
    _, lap = compressed(m, n)
    lam = np.linalg.eigvalsh(lap)[1:] / n
    assert np.min(lam) > 0 and np.max(lam) < 1
    return np.sqrt(lam * (1 - lam))


def run():
    checks = 0
    # Exact matrix identity and positivity for all small coprime scale pairs.
    for m in range(2, 18):
        for n in range(m + 1, 3 * m + 4):
            if math.gcd(m, n) != 1:
                continue
            B, lap = compressed(m, n)
            np.testing.assert_allclose(np.eye(m) - B.T @ B, lap / n, atol=8e-14)
            eig = np.linalg.eigvalsh(lap)
            assert abs(eig[0]) < 1e-11 and eig[1] > 0 and eig[-1] < n
            checks += 1
            if n % m in (1, m - 1):
                predicted = np.array([k * (k + 1) / m for k in range(m)])
                np.testing.assert_allclose(eig, predicted, atol=1e-10)
                checks += 1
                if n >= 2 * (m - 1):
                    actual = np.max(positive_amplitudes(m, n))
                    expected = math.sqrt((m - 1) * (n - m + 1)) / n
                    assert abs(actual - expected) < 1e-11
                    checks += 1
    # Independent full commutator diagonalization on finite length-mn cells.
    for m, n in [(2, 3), (3, 4), (3, 5), (4, 5), (4, 7), (5, 6), (5, 7),
                 (5, 8), (5, 9), (6, 7), (3, 10), (4, 9), (5, 12), (6, 13)]:
        N = m * n
        P, Q = block_projection(m, N), block_projection(n, N)
        C = P @ Q - Q @ P
        observed = np.linalg.eigvalsh(1j * C)
        amps = positive_amplitudes(m, n)
        predicted = np.sort(np.r_[-amps, amps, np.zeros(N - 2 * (m - 1))])
        np.testing.assert_allclose(observed, predicted, atol=3e-13)
        checks += 1
    # GCD collapse, including exactly nested partitions.
    for m, n in [(2, 4), (3, 9), (4, 6), (6, 10), (6, 14),
                 (6, 15), (8, 12), (9, 15), (10, 14)]:
        g = math.gcd(m, n)
        np.testing.assert_allclose(positive_amplitudes(m, n),
                                   positive_amplitudes(m // g, n // g), atol=1e-13)
        checks += 1
    print(f"PASS: {checks} finite spectral / exact-formula assertions")


if __name__ == '__main__':
    run()
