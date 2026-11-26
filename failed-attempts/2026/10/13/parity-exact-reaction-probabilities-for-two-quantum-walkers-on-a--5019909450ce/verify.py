"""Numerical corroboration of finite-cycle two-particle collision absorption.

Run: python verify.py (requires NumPy and SciPy). Finite checks complement
rather than replace the exact spectral proof.
"""
import numpy as np
from scipy.linalg import eigh, expm


def model(n, hop=1.0):
    a = np.zeros((n, n), float)
    for x in range(n):
        a[x, (x - 1) % n] += hop
        a[x, (x + 1) % n] += hop
    h = np.kron(a, np.eye(n)) + np.kron(np.eye(n), a)
    diagonal = np.array([x * n + x for x in range(n)])
    return h, diagonal


def formula(n, d):
    if d % n == 0:
        return 1.0
    if n % 2:
        return 0.5
    if d % n == n // 2:
        return 0.5 - (1.0 / n if n % 4 == 0 else 0.0)
    return 0.5 - 1.0 / (2 * n)


def dimension(n):
    if n % 2:
        return n * (n + 1) // 2
    return n * n // 2 + (1 if n % 4 == 2 else 0)


def spectral_bright(h, diagonal, tol=5e-8):
    lam, v = eigh(h)
    out = np.zeros_like(h)
    j, count = 0, 0
    while j < len(lam):
        z = j + 1
        while z < len(lam) and abs(lam[z] - lam[j]) < tol:
            z += 1
        p = v[:, j:z]
        u, sing, vh = np.linalg.svd(p[diagonal, :], full_matrices=False)
        rank = int(np.count_nonzero(sing > tol))
        for b in range(rank):
            w = p @ vh[b].conj()
            out += np.outer(w, w.conj()).real
        count += rank
        j = z
    return out, count


def check():
    ranks, probabilities, bosonic = 0, 0, 0
    for n in range(3, 11):
        h, diagonal = model(n)
        p, count = spectral_bright(h, diagonal)
        assert count == dimension(n), (n, count, dimension(n))
        assert np.linalg.norm(p @ p - p, ord='fro') < 2e-8
        ranks += 1
        for x in range(n):
            for y in range(n):
                pos = x * n + y
                actual = float(p[pos, pos])
                assert abs(actual - formula(n, (x - y) % n)) < 2e-8, (n, x, y, actual)
                probabilities += 1
                if x != y:
                    z = np.zeros(n * n)
                    z[x * n + y] = 1 / np.sqrt(2)
                    z[y * n + x] = 1 / np.sqrt(2)
                    b = float(z @ p @ z)
                    assert abs(b - 2 * formula(n, (x-y) % n)) < 2e-8
                    bosonic += 1
    dynamic = 0
    for n in (3, 4, 5, 6):
        h, diagonal = model(n)
        p, _ = spectral_bright(h, diagonal)
        rates = 0.7 + 0.37 * np.arange(n)
        gamma = np.zeros(n*n)
        gamma[diagonal] = rates
        k = h - 0.5j * np.diag(gamma)
        for T in (160.0, 250.0):
            e = expm(-1j * k * T)
            for d in (0, 1, n//2):
                state = np.zeros(n*n)
                state[d*n] = 1
                remaining = np.linalg.norm(e @ state)**2
                expected = 1 - formula(n, d)
                if n <= 5:
                    assert abs(remaining - expected) < 3e-4, (n,T,d,remaining,expected)
                elif T == 250:
                    assert abs(remaining - expected) < 2e-2, (n,T,d,remaining,expected)
                dynamic += 1
    print(f'VERIFY_OK spectral_dimensions={ranks} exact_sitewise={probabilities} bosonic_states={bosonic} lossy_evolutions={dynamic}')


if __name__ == '__main__':
    check()
