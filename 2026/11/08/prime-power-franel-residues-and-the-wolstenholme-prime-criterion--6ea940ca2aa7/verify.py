#!/usr/bin/env python3
"""Exact modular checks of the Franel prime-power leading coefficient theorem.

Requires Python 3 standard library only. Finite checks are not an infinite proof.
"""
from fractions import Fraction
from math import comb


def primes_upto(n):
    return [k for k in range(2, n + 1) if all(k % j for j in range(2, int(k ** .5) + 1))]


def franel_mod(n, m):
    c = 1
    s = 0
    for k in range(n + 1):
        s = (s + pow(c % m, 3, m)) % m
        if k < n:
            c = c * (n - k) // (k + 1)
    return s


def alternating_cubic(p):
    return sum((1 if j & 1 else -1) * pow(j, -3, p) for j in range(1, p)) % p


def bernoulli(n):
    b = [Fraction(1)]
    for m in range(1, n + 1):
        b.append(-sum(Fraction(comb(m + 1, j)) * b[j] for j in range(m)) / (m + 1))
    return b[n]


def modfrac(x, p):
    assert x.denominator % p
    return (x.numerator * pow(x.denominator, -1, p)) % p


def middle_binom_unit(p, a, j):
    n = p ** a
    k = j * (p ** (a - 1))
    c = comb(n, k)
    assert c % p == 0
    return (c // p) % p


def main():
    checks = 0
    for p in primes_upto(43):
        if p == 2:
            continue
        s = alternating_cubic(p)
        if p >= 5:
            assert s == modfrac(bernoulli(p - 3) / 2, p), ('Bernoulli', p)
            checks += 1
        else:
            assert s == 2
        for a in range(1, 5):
            n = p ** a
            if n > 1800:
                break
            modulus = p ** 4
            assert franel_mod(n, modulus) == (2 + p ** 3 * s) % modulus, ('Franel', p, a)
            checks += 1
            for j in range(1, p):
                assert middle_binom_unit(p, a, j) == ((-1 if j % 2 == 0 else 1) * pow(j, -1, p)) % p
                checks += 1
    for a in range(1, 12):
        n = 2 ** a
        assert (franel_mod(n, 16) - 2) % 16 == 8
        checks += 1
    for a in range(1, 8):
        n = 3 ** a
        assert (franel_mod(n, 81) - 2) % 81 == 54
        checks += 1
    # Known Wolstenholme prime: independently test its two congruence criteria
    p = 16843
    s = alternating_cubic(p)
    assert s == 0
    c = 1
    mod = p ** 4
    for j in range(1, p):
        c = (c * (1 + p * pow(j, -1, mod))) % mod
    assert c == 1
    checks += 2
    print('VERIFY_OK prime_power_Franel_mod_p4=PASS Bernoulli_reduction=PASS primitive_binomial_units=PASS p2_p3_exact_valuations=PASS Wolstenholme_16843=PASS checks=', checks)

if __name__ == '__main__':
    main()
