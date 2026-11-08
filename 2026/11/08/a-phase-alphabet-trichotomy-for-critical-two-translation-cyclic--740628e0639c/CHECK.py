#!/usr/bin/env python3
"""Finite exact checks for phase-alphabet two-translation Gabor bases.

No external packages.  Run: python3 CHECK.py
The proof for all lengths is analytic; these checks independently enumerate
small configurations and test constructed windows for larger lengths.
"""
from itertools import product
from math import gcd


def gram_orthogonality_exponents(a, k, q):
    """Necessary and sufficient exact Gram test using a roots-of-unity sum.

    Each modulation difference contributes a complete M-point DFT of the
    M numbers c[j]+c[j+M].  Vanishing means each sum is zero.
    In this restricted two-monomial case, the two q-th roots must be opposites.
    """
    n = len(a)
    m = n // 2
    if q % 2:
        return False
    for j in range(m):
        c0 = (a[(j - k) % n] - a[j]) % q
        h = j + m
        c1 = (a[(h - k) % n] - a[h]) % q
        if (c0 - c1) % q != q // 2:
            return False
    return True


def ratio_criterion(a, k, q):
    n = len(a)
    m = n // 2
    for j in range(n):
        h_j = (a[(j + m) % n] - a[j]) % q
        z = (j - k) % n
        h_z = (a[(z + m) % n] - a[z]) % q
        if q % 2 or (h_z - h_j) % q != q // 2:
            return False
    return True


def predicted_count(n, k, q):
    t = n // gcd(n, k)
    if t % 2:
        return 0
    if t % 4 == 0 and q % 2 == 0:
        return (q ** (n // 2)) * (2 ** gcd(n, k))
    if t % 4 == 2 and q % 4 == 0:
        return (q ** (n // 2)) * (2 ** gcd(n, k))
    return 0


def construct(n, k, q):
    """Choose one sign on each k-orbit and choose all bottom phases 0."""
    if not predicted_count(n, k, q):
        return None
    m = n // 2
    t = n // gcd(n, k)
    initial = 0 if t % 4 == 0 else q // 4
    h = [None] * n
    for start in range(n):
        if h[start] is not None:
            continue
        j = start
        sign = 0
        while h[j] is None:
            h[j] = (initial + sign * (q // 2)) % q
            j = (j - k) % n
            sign ^= 1
        assert j == start
    a = [0] * n
    for j in range(m):
        a[j + m] = h[j]
    assert ratio_criterion(a, k, q)
    assert gram_orthogonality_exponents(a, k, q)
    return a


def exhaustive():
    tests = 0
    classes = 0
    configurations = [(2, 2), (2, 4), (2, 6), (4, 2), (4, 4),
                      (4, 6), (4, 8), (6, 2), (6, 4), (8, 2)]
    for n, q in configurations:
        for k in range(1, n):
            observed = 0
            for a in product(range(q), repeat=n):
                one = gram_orthogonality_exponents(a, k, q)
                two = ratio_criterion(a, k, q)
                assert one == two, (n, q, k, a)
                observed += one
                tests += 1
            expected = predicted_count(n, k, q)
            assert observed == expected, (n, k, q, observed, expected)
            classes += 1
    return tests, classes


def constructive():
    count = 0
    for n in range(2, 35, 2):
        for k in range(1, n):
            for q in (2, 4, 6, 8, 10, 12):
                a = construct(n, k, q)
                assert (a is not None) == (predicted_count(n, k, q) > 0)
                count += 1
    return count


def main():
    tests, classes = exhaustive()
    constructed = constructive()
    print('CHECK_OK exact_phase_arrays=%d exhaustive_parameter_cases=%d constructive_parameter_cases=%d' %
          (tests, classes, constructed))


if __name__ == '__main__':
    main()
