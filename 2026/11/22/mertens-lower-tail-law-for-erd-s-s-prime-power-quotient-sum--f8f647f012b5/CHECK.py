#!/usr/bin/env python3
"""Exact finite checks for the prime-power reciprocal-sum endpoint law.

Finite examples test definitions and independent local coefficients; they are
not used as a proof of the limiting or infinite-prime statements.
"""
from fractions import Fraction


def primes_upto(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            for j in range(p * p, n + 1, p):
                sieve[j] = False
    return [i for i in range(n + 1) if sieve[i]]


def factor_prime_power_reciprocal(n):
    """Exact rational value of W(n)/n, W(1)/1=0."""
    assert n >= 1
    val = Fraction(0)
    rem = n
    for p in range(2, int(rem ** 0.5) + 2):
        if p > rem // p:
            break
        if rem % p:
            continue
        pp = 1
        while rem % p == 0:
            pp *= p
            rem //= p
        val += Fraction(1, pp)
    if rem > 1:
        val += Fraction(1, rem)
    return val


def w_integer(n):
    if n == 1:
        return 0
    return n * factor_prime_power_reciprocal(n)


def local_probability(p, a):
    """Probability of p-adic valuation a, a nonnegative integer."""
    if a == 0:
        return Fraction(p - 1, p)
    return Fraction(p - 1, p ** (a + 1))


def finite_prime_upper(y):
    """Exact Mertens cylinder and necessary-condition upper product."""
    assert y >= 2
    m, upper = Fraction(1), Fraction(1)
    for p in primes_upto(y):
        m *= Fraction(p - 1, p)
        power = p
        while power < y:
            power *= p
        upper *= Fraction(p - 1, p) + Fraction(1, power)
    return m, upper


def test():
    # Completely independent definition from n/p^a, in integer arithmetic.
    for n in range(1, 4501):
        f = factor_prime_power_reciprocal(n)
        assert w_integer(n) == n * f
        pp = 1
        m = n
        summands = 0
        for p in primes_upto(n):
            if p > m:
                break
            if m % p == 0:
                pp = 1
                while m % p == 0:
                    m //= p
                    pp *= p
                summands += n // pp
        assert summands == w_integer(n), (n, summands, w_integer(n))

    # Exactly count geometric valuation cylinders on a full finite period.
    local_checks = 0
    for p in (2, 3, 5, 7):
        for depth in range(1, 6):
            modulus = p ** depth
            tally = [0] * (depth + 1)
            for n in range(1, modulus + 1):
                k, m = 0, n
                while k < depth and m % p == 0:
                    m //= p
                    k += 1
                tally[k] += 1
            for k in range(depth):
                assert Fraction(tally[k], modulus) == local_probability(p, k)
                local_checks += 1
            assert tally[depth] == 1
            local_checks += 1

    # The necessary local condition has probability
    # 1-1/p+1/p^{ceil(log_p(y))}. It contains the no-small-prime event.
    for y in (3, 5, 10, 20, 50, 100, 300, 1000):
        m, u = finite_prime_upper(y)
        assert m <= u <= 1, (y, m, u)
    m1000, u1000 = finite_prime_upper(1000)
    assert u1000 / m1000 < Fraction(103, 100)
    print('PRIME_POWER_RECIPROCAL_ENDPOINT_OK',
          'definition_n=4500', 'local_checks=', local_checks,
          'upper_ratio_y1000=', float(u1000 / m1000))


if __name__ == '__main__':
    test()
