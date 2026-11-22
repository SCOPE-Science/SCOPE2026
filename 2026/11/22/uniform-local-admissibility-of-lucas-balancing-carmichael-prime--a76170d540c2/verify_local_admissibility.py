#!/usr/bin/env python3
"""Exact local-residue checks for Lucas-balancing Carmichael prime triples.

Finite checks only: the all-index/all-prime theorem is proved separately.
Uses the standard library, with exact integer arithmetic.
"""
from math import gcd, isqrt


def primes_below(limit):
    out = []
    for n in range(2, limit):
        if all(n % p for p in out if p * p <= n):
            out.append(n)
    return out


def lucas_balancing(count):
    c = [1, 3]
    for _ in range(2, count):
        c.append(6 * c[-1] - c[-2])
    return c


def prime_by_trial_division(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def run():
    c = lucas_balancing(37)
    primes = primes_below(160)
    assert len(primes) == 37
    checked = 0
    for n in range(2, 36, 2):
        A, B, D = c[n:n+3]
        M = A * D
        assert M - B * B == 8
        assert M % 48 == 17 and B % 3 == 0
        assert gcd(A, B) == gcd(B, D) == gcd(A, D) == 1
        k0 = (25 * M + 7) // 48
        assert 48 * k0 == 25 * M + 7
        K = k0 + (k0 % 2) * M
        assert K % 2 == 0
        for ell in primes:
            good = 0
            for u in range(ell):
                k = K + 2 * M * u
                if all((1 + B * k * v) % ell != 0 for v in (A, B, D)):
                    good += 1
            assert good > 0, (n, ell)
            if ell == 2 or B % ell == 0 or M % ell == 0:
                assert good == ell, (n, ell, good)
            else:
                assert ell >= 5 and good >= ell - 3, (n, ell, good)
            checked += 1
    A, B, D = c[2:5]
    k = 7136252
    M = A * D
    k0 = (25 * M + 7) // 48
    K = k0 + (k0 % 2) * M
    assert k == K + 2 * M * 363
    factors = [1 + B * k * v for v in (A, B, D)]
    assert factors == [12010312117, 69942405853, 407644122997]
    assert all(prime_by_trial_division(p) for p in factors)
    prod = 1
    for p in factors:
        prod *= p
    assert all((prod - 1) % (p - 1) == 0 for p in factors)
    print('LOCAL_ADMISSIBILITY_EXACT_OK indices=17 primes=37 prime_example=3')


if __name__ == '__main__':
    run()
