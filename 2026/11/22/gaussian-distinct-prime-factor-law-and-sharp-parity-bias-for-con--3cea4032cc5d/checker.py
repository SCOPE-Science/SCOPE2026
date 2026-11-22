#!/usr/bin/env python3
"""Exact finite tests for distinct prime factors of consecutive product/LCM quotients.
No external dependencies are needed. Infinite asymptotics are established in RESULT.md.
"""
from fractions import Fraction
from math import gcd, lcm, prod
from collections import Counter


def primes_through(k):
    return [p for p in range(2, k + 1) if all(p % d for d in range(2, int(p ** .5) + 1))]


def theoretical(k):
    length = k + 1
    primes = primes_through(k)
    forced = sum(2 * p <= length for p in primes)
    boundary = [p for p in primes if 2 * p > length]
    period = prod(boundary)
    distribution = {forced: Fraction(1)}
    for p in boundary:
        a = Fraction(length - p, p)
        out = {}
        for j, mass in distribution.items():
            out[j] = out.get(j, Fraction(0)) + (1 - a) * mass
            out[j + 1] = out.get(j + 1, Fraction(0)) + a * mass
        distribution = out
    bias = sum((-1) ** j * mass for j, mass in distribution.items())
    return period, distribution, bias


def exact_omega_of_quotient(k, n):
    terms = range(n, n + k + 1)
    quotient = prod(terms) // lcm(*terms)
    count = 0
    for p in primes_through(k):
        if quotient % p == 0:
            count += 1
    # All possible prime factors of the quotient are at most k.
    return count


def check():
    checked = 0
    for k in range(1, 15):
        period, dist, bias = theoretical(k)
        seen = Counter(exact_omega_of_quotient(k, n) for n in range(1, period + 1))
        assert {j: Fraction(c, period) for j, c in seen.items()} == {j: a for j, a in dist.items() if a}
        assert bias == Fraction(sum((-1) ** j * c for j, c in seen.items()), period)
        assert sum(dist.values()) == 1
        for smaller in range(1, period):
            if period % smaller == 0:
                assert any(exact_omega_of_quotient(k, n) != exact_omega_of_quotient(k, n + smaller) for n in range(1, period + 1))
        checked += period
    assert theoretical(2)[2] == 0
    assert all(theoretical(k)[2] for k in range(3, 40))
    print(f'PASS: {checked} exact quotient instances across k=1..14; distributions and least periods match.')
    print('PASS: exact sign bias vanishes for k=2 and for no k from 3 through 39.')


if __name__ == '__main__':
    check()
