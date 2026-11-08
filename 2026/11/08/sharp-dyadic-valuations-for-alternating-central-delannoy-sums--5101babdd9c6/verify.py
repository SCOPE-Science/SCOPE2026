#!/usr/bin/env python3
"""Independent finite checks of identities for central Delannoy sums.

The mathematical proof, not these finite checks, establishes the infinite claim.
"""
from math import comb


def v2(v):
    assert isinstance(v, int) and v != 0
    v = abs(v)
    return (v & -v).bit_length() - 1


def central_delannoy(limit):
    seq = [1, 3]
    for n in range(2, limit + 1):
        num = (6 * n - 3) * seq[-1] - (n - 1) * seq[-2]
        assert num % n == 0
        seq.append(num // n)
    return seq[:limit + 1]


def main():
    bound = 1024
    D = central_delannoy(bound)
    cumulative = 0
    for n in range(1, bound + 1):
        k = n - 1
        cumulative += (-1 if k % 2 else 1) * (2 * k + 1) * D[k]
        assert (D[n] + D[n - 1]) % 4 == 0
        a = (D[n] + D[n - 1]) // 4
        assert a > 0
        expected = 0 if n % 2 else 3 * v2(n) - 1
        assert v2(a) == expected, (n, a, expected)
        assert cumulative == (-1 if n % 2 == 0 else 1) * n * a
        assert v2(cumulative) == (0 if n % 2 else 4 * v2(n) - 1)
        if n <= 128:
            from_binomial = sum(comb(n - 1, j) * comb(n + j, j) for j in range(n))
            assert a == from_binomial
        if n <= 64:
            # Formal coefficient of ((1+z)/(1-z))**n, divided by 2.
            coeff = sum(comb(n, j) * comb(2 * n - j - 1, n - j)
                        for j in range(n + 1))
            assert coeff == 2 * a
    harmonic_cases = 0
    for s in range(0, 8):
        for odd_u in range(1, 16, 2):
            m = (1 << s) * odd_u
            precision = 2 * s + 5
            mod = 1 << precision
            val = sum(pow(2 * j - 1, -1, mod) for j in range(1, m + 1)) % mod
            assert v2(val) == 2 * s, (s, odd_u, val)
            harmonic_cases += 1
    print(f"VERIFY_OK delannoy_n={bound} binomial_n=128 coefficient_n=64 harmonic_cases={harmonic_cases} max_harmonic_m={(1<<7)*15}")


if __name__ == '__main__':
    main()
