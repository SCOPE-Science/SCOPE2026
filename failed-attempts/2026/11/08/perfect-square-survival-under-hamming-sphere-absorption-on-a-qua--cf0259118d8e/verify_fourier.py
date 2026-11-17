"""Independent finite-dimensional check of Hamming-shell survival formula.

Run: python verify_fourier.py
Requires numpy, scipy. The theorem's infinite-dimensional quantifiers are
proved analytically in RESULT.md; these are finite regression checks only.
"""
import math
import numpy as np
from scipy.linalg import null_space


def K(n, r, k):
    return sum((-1)**j * math.comb(k, j) * math.comb(n-k, r-j)
               for j in range(max(0, r-(n-k)), min(r, k)+1))


def full_spectral_dark_probability(n, r):
    size = 1 << n
    sites = [i for i in range(size) if i.bit_count() == r]
    p = 0.0
    for k in range(n+1):
        band = [i for i in range(size) if i.bit_count() == k]
        # Restriction of all Fourier eigenvectors in this energy band to the
        # absorbing shell. Numerically compute its full kernel; no Krawtchouk
        # polynomial is used in this route.
        restriction = np.array([
            [(-1)**((s & z).bit_count()) for z in band]
            for s in sites], dtype=float)
        kernel = null_space(restriction, rcond=1e-10)
        corner_coefficients = np.ones(len(band)) / math.sqrt(size)
        p += float(np.linalg.norm(kernel.T @ corner_coefficients)**2)
    return p


def main():
    checks = 0
    for n in range(2, 9):
        for r in range(1, n+1):
            predicted = sum(math.comb(n, k) / (2**n)
                            for k in range(n+1) if K(n, r, k) == 0)
            direct = full_spectral_dark_probability(n, r)
            assert abs(direct-predicted) < 2e-9, (n, r, direct, predicted)
            if r == 2:
                s = math.isqrt(n)
                expected = (2 * math.comb(n, (n-s)//2) / (2**n)
                            if s*s == n else 0.0)
                assert abs(direct-expected) < 2e-9, (n, direct, expected)
            checks += 1
    for n in range(2, 500):
        sq = math.isqrt(n)
        zeros = [k for k in range(n+1) if K(n, 2, k) == 0]
        asserted = [(n-sq)//2, (n+sq)//2] if sq*sq == n else []
        assert zeros == asserted, (n, zeros, asserted)
    print(f'PASS: {checks} independent Fourier-kernel shell comparisons, '
          'plus 498 integer square-root classifications')


if __name__ == '__main__':
    main()
