"""Finite consistency checks for a totient limiting-law theorem.
This script is not an infinite-domain proof.
"""
from fractions import Fraction
from math import gcd, isqrt


def sieve(limit):
    mark = bytearray(b'\x01') * (limit + 1)
    mark[:2] = b'\x00\x00'
    for p in range(2, isqrt(limit) + 1):
        if mark[p]:
            for q in range(p * p, limit + 1, p):
                mark[q] = 0
    return [i for i in range(2, limit + 1) if mark[i]]


def direct_totient(n):
    if n == 1:
        return 0
    return sum(gcd(x, n) == 1 and gcd((x - 1) // 2, n) == 1
               for x in range(1, n + 1, 2))


def odd_factor_product(n, primes):
    m = n
    while m % 2 == 0:
        m //= 2
    value = Fraction(1)
    for p in primes:
        if p * p > m:
            break
        if m % p == 0:
            value *= Fraction(p - 2, p)
            while m % p == 0:
                m //= p
    if m > 1:
        value *= Fraction(m - 2, m)
    return value


def check():
    primes = sieve(1200)
    assert direct_totient(1) == 0 and direct_totient(2) == 0
    for n in range(3, 1201):
        m = n
        e = 0
        while m % 2 == 0:
            e += 1
            m //= 2
        R = odd_factor_product(n, primes)
        predicted = (Fraction(1, 2) if e == 0 else Fraction(1, 4)) * R
        t = direct_totient(n)
        omega = sum(m % p == 0 for p in primes)
        assert abs(Fraction(t, n) - predicted) * n <= 3 ** omega * 3, (n, t, R)
        if e >= 2:
            assert t == (2 ** (e - 2)) * m * R, (n, t, R)
    print('DIRECT_TOTIENT_AND_CRT_ESTIMATE_OK n=1..1200')
    print('EXACT_HIGH_TWO_ADIC_BRANCH_OK n<=1200')

    ps = [p for p in sieve(31) if p != 2]
    values = {Fraction(1)}
    for p in ps:
        mult = Fraction(p - 2, p)
        other = {v * mult for v in values}
        assert not (values & other), p
        values |= other
    assert len(values) == 2 ** len(ps)
    print('FINITE_PREFIX_PRODUCT_INJECTIVITY_OK primes=3..31 patterns=%d' % len(values))

    cap = 100000
    approx = [1.0] * (cap + 1)
    for p in sieve(cap):
        if p == 2:
            continue
        mult = (p - 2) / p
        for n in range(p, cap + 1, p):
            approx[n] *= mult
    mean = sum((0.5 if n & 1 else 0.25) * approx[n]
               for n in range(1, cap + 1)) / cap
    euler = 0.375
    for p in sieve(cap):
        if p != 2:
            euler *= 1 - 2 / (p * p)
    assert abs(mean - euler) < 0.0002, (mean, euler)
    print('FIRST_MOMENT_SIEVE_OK X=%d empirical=%.9f truncated_euler=%.9f' %
          (cap, mean, euler))
    print('FINITE_CHECKS_ONLY; SYMBOLIC_INFINITE_PROOF_REQUIRED; INDEPENDENT_AUDIT_NOT_PERFORMED')

if __name__ == '__main__':
    check()
