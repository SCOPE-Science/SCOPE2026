"""Reproduce the exact three-erasure concentration calculations.

Requires Python 3, NumPy; exhaustive checks are finite corroboration only.
"""
import itertools
import math
import numpy as np


def g(n, k):
    return 1 + 2 * math.cos(2 * math.pi * k / n)


def lambda_formula(n):
    d, e = g(n, 1), g(n, 2)
    return 3 + e/2 + math.sqrt(e*e/4 + 2*d*d)


def spectral_radius_of_erasure(n, erasures):
    t = np.array(erasures, dtype=float)
    z = np.exp(2j * np.pi * t/n)
    v = z[:, None] ** np.arange(3)[None, :]
    return float(np.linalg.eigvalsh(v @ v.conj().T)[-1])


def is_consecutive(n, erasures):
    a = set(erasures)
    return any({k % n, (k+1) % n, (k+2) % n} == a for k in a)


def main():
    for n in range(6, 41):
        d, e = g(n, 1), g(n, 2)
        L = lambda_formula(n)
        # Analytic spectral factorization of the actual contiguous Gram matrix.
        K = np.array([[3., d, e], [d, 3., d], [e, d, 3.]])
        expected = sorted([3-e, 3+e/2 - math.sqrt(e*e/4 + 2*d*d), L])
        assert np.allclose(np.linalg.eigvalsh(K), expected, rtol=0, atol=2e-12)
        assert 0 < L < n
        for E in itertools.combinations(range(n), 3):
            current = spectral_radius_of_erasure(n, E)
            if is_consecutive(n, E):
                assert abs(current-L) < 1e-9, (n,E,L,current)
            else:
                assert current < L-1e-9, (n,E,L,current)
    # Explicit minimally redundant endpoint (three kept, three erased).
    l6 = lambda_formula(6)
    assert abs(l6 - (3 + 2*math.sqrt(2))) < 1e-13
    assert abs(1-l6/6 - (3-2*math.sqrt(2))/6) < 1e-13
    # Rigorous proof uses the monotone cosine kernel and Perron comparison.
    for n in range(8, 201):
        d, e = g(n,1), g(n,2)
        assert d > e >= 1 - 2e-14
        assert all(abs(g(n,k)) <= e+2e-13 for k in range(2,n//2+1))
    # Large-grid expansion: 9 - lambda = 16*pi^2/n^2 + O(n^-4).
    for n in [200, 400, 800]:
        scaled = (9-lambda_formula(n))*n*n
        assert abs(scaled-16*math.pi**2) < 0.05
    print('THREE_ERASURE_GRAM_EIGENVALUES_OK n=6..40')
    print('EXHAUSTIVE_MASK_EQUALITY_CLASS_OK n=6..40')
    print('COSINE_DOMINATION_AND_LARGE_GRID_ASYMPTOTIC_OK')
    print('SHARP_ENDPOINT_N6_OK', (3-2*math.sqrt(2))/6)
    print('ALL_THREE_ERASURE_CHECKS_OK')


if __name__ == '__main__':
    main()
