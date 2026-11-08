#!/usr/bin/env python3
"""Exact finite corroboration of a prime-denominator floor-coprimality theorem.

No finite check proves the infinite-domain result or the analytic uniform bound.
"""
from fractions import Fraction
from math import gcd, lcm


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5) + 1))


def phi(n):
    assert n >= 1
    v, m, d = n, n, 2
    while d * d <= m:
        if m % d == 0:
            while m % d == 0:
                m //= d
            v -= v // d
        d += 1
    if m > 1:
        v -= v // m
    return v


def rad(n):
    assert n >= 1
    z, m, d = 1, n, 2
    while d * d <= m:
        if m % d == 0:
            z *= d
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        z *= m
    return z


def theorem_values(p, a, k):
    assert is_prime(p) and k >= 2 and a > 0 and gcd(a, p) == 1
    vals = [(a * pow(r, k, p)) % p for r in range(1, p)]
    assert all(1 <= t < p for t in vals)
    big_lcm = 1
    for t in vals:
        big_lcm = lcm(big_lcm, t)
    period = p * rad(big_lcm)
    density = sum((Fraction(phi(t), t) for t in vals), Fraction(0)) / p
    return period, density, vals


def floor_indicator(n, p, a, k):
    return gcd(n, (a * n**k) // p) == 1


def residue_indicator(n, p, a, k):
    if n % p == 0:
        return False
    t = (a * pow(n % p, k, p)) % p
    return gcd(n, t) == 1


def factor_primes(n):
    return [z for z in range(2, n + 1) if n % z == 0 and is_prime(z)]


def verify_full_period(p, a, k):
    P, dens, vals = theorem_values(p, a, k)
    assert P <= 100000, (p, a, k, P)
    bits = [floor_indicator(n, p, a, k) for n in range(1, P + 1)]
    assert sum(bits) == P * dens, (p, a, k, P, dens)
    assert all(bits[n - 1] == residue_indicator(n, p, a, k)
               for n in range(1, P + 1))
    # A proper period would have a divisor P/ell for a prime ell|P.
    for ell in factor_primes(P):
        h = P // ell
        assert any(bits[i] != bits[(i + h) % P] for i in range(P)), (p, a, k, ell)
    for n in range(1, 4 * P + 1):
        assert floor_indicator(n, p, a, k) == bits[(n - 1) % P]
    return P, dens


def verify_cosets(p, k):
    values = {}
    for a in range(1, p):
        P, delta, t = theorem_values(p, a, k)
        key = frozenset(t)
        result = P, delta
        if key in values:
            assert values[key] == result
        else:
            values[key] = result
    assert len(values) == gcd(k, p - 1)
    avg = sum((theorem_values(p, a, k)[1] for a in range(1, p)), Fraction(0)) / (p - 1)
    expected = sum((Fraction(phi(t), t) for t in range(1, p)), Fraction(0)) / p
    assert avg == expected, (p, k, avg, expected)
    return len(values), avg


def main():
    checked = 0
    for p in [2, 3, 5, 7, 11, 13]:
        for k in [2, 3, 4]:
            for a in [1, 2]:
                if p == a:
                    continue
                P, delta = verify_full_period(p, a, k)
                checked += 1
    print('EXACT_FLOOR_VS_RESIDUE_PERIOD_AND_DENSITY_OK cases=', checked)
    assert theorem_values(5, 1, 2)[:2] == (10, Fraction(3, 5))
    assert theorem_values(5, 2, 2)[:2] == (30, Fraction(7, 15))
    print('EXAMPLE_P5_K2_OK')
    coset_checks = 0
    for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        for k in [2, 3, 4, 5, 6]:
            verify_cosets(p, k)
            coset_checks += 1
    print('COSET_INVARIANCE_AND_EXACT_AVERAGE_OK cases=', coset_checks)
    print('VERIFY_OK finite_only=True independent_audit=False')


if __name__ == '__main__':
    main()
