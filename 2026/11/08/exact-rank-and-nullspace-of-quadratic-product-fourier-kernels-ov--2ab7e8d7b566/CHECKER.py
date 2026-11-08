"""Independent finite checks for quadratic-product Fourier rank over prime-square rings.

Run: python3 CHECKER.py. Requires numpy for direct complex-matrix SVD.
The discriminant tests are exact integer arithmetic, the SVD tests are finite corroboration.
"""
import math
import numpy as np


def primes_through(n):
    return [p for p in range(3, n + 1, 2)
            if all(p % d for d in range(3, math.isqrt(p) + 1, 2))]


def predicted_rank(p):
    return p * p - (p - 1) ** 2 // 2


def root_census(p, a, b):
    """Classify the p wild-frequency stationarity conditions exactly."""
    assert a % p and b % p and p % 2
    freqs = []
    for r in range(p):
        roots = [x for x in range(1, p) if (r + a*x + 2*b*x*x) % p == 0]
        freqs.append(roots)
        discr = (a*a - 8*b*r) % p
        assert (not roots) == (discr != 0 and pow(discr, (p-1)//2, p) == p-1)
        if len(roots) == 2:
            x, y = roots
            assert (a*(x-y)*pow(2, -1, p)) % p != 0
    assert sum(not r for r in freqs) == (p - 1)//2
    return freqs


def svd_rank(p, a, b):
    q = p*p
    t = np.arange(q, dtype=np.int64)
    st = (t[:, None]*t[None, :]) % q
    exponent = (a*st+b*st*st) % q
    matrix = np.exp(2j * np.pi * exponent/q)
    singular = np.linalg.svd(matrix, compute_uv=False)
    observed = int(np.sum(singular > 1e-7))
    assert observed == predicted_rank(p), (p, a, b, observed)
    assert singular[observed-1] > 1e-4
    assert singular[observed] < 1e-7
    return singular[observed-1]


def main():
    tests_exact = 0
    for p in primes_through(151):
        for a, b in [(1,1), (2,1), (1,2), (p+1, p+2)]:
            root_census(p, a, b)
            tests_exact += 1
    tests_svd = 0
    smallest_positive = float('inf')
    for p in [3,5,7,11,13]:
        for a,b in [(1,1), (2,1), (1,2), (p+1,p+2)]:
            smallest_positive = min(smallest_positive, svd_rank(p,a,b))
            tests_svd += 1
    print('QUADRATIC_PRODUCT_RANK_CHECK_PASS')
    print('exact stationary-census tests:', tests_exact)
    print('direct complex SVD tests:', tests_svd)
    print('minimum nonzero singular value among tests:', round(smallest_positive, 8))

if __name__ == '__main__':
    main()
