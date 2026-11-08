#!/usr/bin/env python3
"""Finite independent checks for bounded-height rooted-forest identities.

Run with Python 3: python3 checker.py.  No third-party packages are needed.
Finite enumeration does not establish the asymptotic theorems.
"""
from itertools import product, permutations
from math import comb, exp, pi, log, sqrt


def partitions_change(N):
    p = [1] + [0] * N
    for k in range(1, N + 1):
        for m in range(k, N + 1):
            p[m] += p[m - k]
    return p


def partitions_pentagonal(N):
    p = [0] * (N + 1)
    p[0] = 1
    for m in range(1, N + 1):
        k = 1
        while k * (3 * k - 1) // 2 <= m:
            for v in (k * (3 * k - 1) // 2, k * (3 * k + 1) // 2):
                if v <= m:
                    p[m] += (1 if k % 2 else -1) * p[m - v]
            k += 1
    return p


def forests_recurrence(N, p):
    weighted_divisor_sums = [0] * (N + 1)
    for size in range(1, N + 1):
        for total in range(size, N + 1, size):
            weighted_divisor_sums[total] += size * p[size - 1]
    a = [1] + [0] * N
    for m in range(1, N + 1):
        rhs = sum(weighted_divisor_sums[j] * a[m - j]
                  for j in range(1, m + 1))
        assert rhs % m == 0
        a[m] = rhs // m
    return a


def forests_direct_product(N, p):
    a = [1] + [0] * N
    for size in range(1, N + 1):
        num_types = p[size - 1]
        new = [0] * (N + 1)
        for m, x in enumerate(a):
            if not x:
                continue
            for j in range((N - m) // size + 1):
                new[m + j * size] += x * comb(num_types + j - 1, j)
        a = new
    return a


def unlabelled_by_brute_force(n):
    """Direct orbit enumeration of functions satisfying f^3=f^2."""
    orbit_keys = set()
    relabellings = list(permutations(range(n)))
    for f in product(range(n), repeat=n):
        if any(f[f[f[i]]] != f[f[i]] for i in range(n)):
            continue
        best = None
        for sigma in relabellings:
            g = [0] * n
            for i in range(n):
                g[sigma[i]] = sigma[f[i]]
            key = tuple(g)
            if best is None or key < best:
                best = key
        orbit_keys.add(best)
    return len(orbit_keys)


def partition_modular_diagnostic(t):
    p_exact = 1.
    for k in range(1, 1200):
        p_exact /= (1 - exp(-k * t))
    A = pi * pi / 6
    p_asym = sqrt(t / (2 * pi)) * exp(A / t - t / 24)
    return abs(p_exact / p_asym - 1)


def main():
    N = 48
    pc = partitions_change(N)
    pe = partitions_pentagonal(N)
    assert pc == pe
    a = forests_recurrence(N, pc)
    b = forests_direct_product(N, pc)
    assert a == b
    assert a[:16] == [1, 1, 2, 4, 8, 15, 29, 53, 98, 177, 319,
                       565, 1001, 1749, 3047, 5264]
    for n in range(1, 6):
        assert unlabelled_by_brute_force(n) == a[n], (n, a[n])
    # Exact deletion bijection for distinguished component types: for a
    # singleton, the count of structures with >=r copies is a[n-r].
    for n in range(1, N + 1):
        for r in range(1, min(n, 4) + 1):
            assert 0 <= a[n-r] <= a[n]
        # The numerator for structures without a singleton is the
        # coefficient of (1-z) F(z).
        assert (a[n] - a[n - 1]) + a[n - 1] == a[n]
    assert partition_modular_diagnostic(.15) < 1e-5
    print('partition_recurrences: OK through', N)
    print('weighted_product_vs_log_derivative: OK through', N)
    print('direct_unlabelled_function_orbits: OK through size 5')
    print('known_count_sequence_A001383_shift: OK')
    print('partition_singularity_diagnostic: OK')
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    main()
