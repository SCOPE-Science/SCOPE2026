"""Independent exact-formula and numeric spectral checks for minority split attractors.

Usage: python3 artifacts/check_spectrum.py
Requires numpy; it is not part of the mathematical proof.
"""
from itertools import combinations
from math import comb
import numpy as np


def spectrum_formula(d, k):
    q = d - k
    eigenvalues = []
    for j in range(q):
        mult = comb(d, j) - (comb(d, j - 1) if j >= 1 else 0)
        eigenvalues += [j] * mult + [d + 1 - j] * mult
    mult = comb(d, q) - comb(d, q - 1)
    eigenvalues += [q] * mult
    return sorted(eigenvalues)


def check(d, k, n):
    bottom = list(combinations(range(d), k))
    top = list(combinations(range(d), k + 1))
    idx = {s: i for i, s in enumerate(bottom + top)}
    mat = np.zeros((len(idx), len(idx)), dtype=float)
    for small in bottom:
        i = idx[small]
        seen = set(small)
        for v in range(d):
            if v not in seen:
                j = idx[tuple(sorted(small + (v,)))]
                mat[i, i] += 1
                mat[j, j] += 1
                mat[i, j] -= 1
                mat[j, i] -= 1
    got = sorted(float(x) for x in np.linalg.eigvalsh(mat))
    expected = spectrum_formula(d, k)
    assert len(got) == len(expected)
    assert max(abs(x - y) for x, y in zip(got, expected)) < 1e-8, (d, k)
    assert abs(got[1] - 1) < 1e-8, (d, k, got[1])
    assert abs((1 - got[1] / n) - (1 - 1 / n)) < 1e-10
    return len(idx)


def main():
    tests = 0
    matrix_dimensions = 0
    for a in range(2, 9):
        for b in range(1, 9):
            n = a + b
            if n > 12 or n % 2 == 0 or b >= a:
                continue
            if b == 1:
                d, k = a + 1, a // 2
            else:
                d, k = a, (n - 1) // 2
            matrix_dimensions += check(d, k, n)
            tests += 1
    print('SPECTRUM_CHECK_OK')
    print('nonabsorbing_cases', tests)
    print('summed_matrix_dimensions', matrix_dimensions)
    print('every exact Laplacian eigenvalue and discrete-time gap confirmed')

if __name__ == '__main__':
    main()
