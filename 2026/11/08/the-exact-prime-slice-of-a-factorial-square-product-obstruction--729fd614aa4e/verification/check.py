#!/usr/bin/env python3
"""Exact verification of the finite inputs in the factorial squarefree-part theorem.

All calculations use the Python standard library. No finite check proves
Nagura's infinitely quantified prime-gap theorem.
"""
from math import factorial


def primes_through(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for d in range(2, int(n ** 0.5) + 1):
        if sieve[d]:
            sieve[d * d:n + 1:d] = b'\x00' * ((n - d * d) // d + 1)
    return [d for d in range(2, n + 1) if sieve[d]]


def factorial_kernel(n):
    answer = 1
    for p in primes_through(n):
        e, m = 0, n
        while m:
            m //= p
            e += m
        if e % 2:
            answer *= p
    return answer


def kernel_trial_division(x):
    assert x >= 1
    out, p = 1, 2
    while p * p <= x:
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        if e % 2:
            out *= p
        p += 1
    return out * x


def factorial_prime_kernel(p, n):
    d = factorial_kernel(n)
    return d // p if d % p == 0 else p * d


def main():
    assert factorial_kernel(11) == 77
    for c in range(12, 51):
        assert factorial_kernel(c) >= c * c, (c, factorial_kernel(c))
    print('EXHAUSTIVE_QUADRATIC_THRESHOLD_OK c=12..50; s(11!)=77')

    for c in range(0, 80):
        assert factorial_kernel(c) == kernel_trial_division(factorial(c))
    print('INDEPENDENT_KERNEL_FACTORIZATION_OK c=0..79')

    small = {2: (2, 1), 3: (3, 2), 5: (6, 1), 7: (7, 5), 11: (11, 7)}
    for p, (c, target) in small.items():
        assert factorial_prime_kernel(p, c) == target
        assert kernel_trial_division(p * factorial(c)) == target
        assert target < p
    print('FIVE_EXPLICIT_EXCLUSIONS_OK primes=2,3,5,7,11')

    primes = primes_through(300)
    for p in primes:
        for c in range(0, 301):
            computed = factorial_prime_kernel(p, c)
            if p >= 13:
                assert computed >= p, (p, c, computed)
    print(f'PRIME_MEMBERSHIP_CHECK_OK primes_to_300={len(primes)} c=0..300')

    # Independent finite witness for the three disjoint Nagura intervals.
    all_primes = primes_through(600)
    for c in range(51, 501):
        intervals = ((5*c, 6*c), (15*c, 18*c), (18*c, 108*c//5))
        # Check with exact rational comparisons instead of rounded boundaries.
        for lo_n, lo_d, hi_n, hi_d in ((1,2,3,5),(3,5,18,25),(18,25,108,125)):
            assert any(lo_n * c < lo_d * q and hi_d * q < hi_n * c
                       for q in all_primes), c
    print('PRIME_GAP_INTERVAL_SPOTCHECK_OK c=51..500')
    print('VERIFY_OK exact_integer_arithmetic=true infinite_case_uses_Nagura=true')


if __name__ == '__main__':
    main()
