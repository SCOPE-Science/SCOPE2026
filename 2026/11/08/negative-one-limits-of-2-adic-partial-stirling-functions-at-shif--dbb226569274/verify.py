#!/usr/bin/env python3
"""Finite checks for the negative-one dyadic partial-Stirling limit formula.

Requires Python 3.8+. Every assertion is finite; convergence is proved separately.
"""
from fractions import Fraction
from math import comb


def pminusone_exact(n):
    if n == 0:
        return Fraction(0, 1)
    s = sum((Fraction(comb(n, j), j) for j in range(1, n + 1, 2)), Fraction(0, 1))
    factorial = 1
    for k in range(1, n + 1):
        factorial *= k
    return s / factorial


def unit_factorial(n, modulus):
    product = 1
    for k in range(1, n + 1):
        product = product * (k // (k & -k)) % modulus
    return product


def pminusone_mod(n, bits):
    modulus = 1 << bits
    factorial_valuation = n - n.bit_count()
    high_modulus = 1 << (factorial_valuation + bits)
    num = 0
    for j in range(1, n + 1, 2):
        num = (num + comb(n, j) * pow(j, -1, high_modulus)) % high_modulus
    assert num % (1 << factorial_valuation) == 0
    return ((num >> factorial_valuation) * pow(unit_factorial(n, modulus), -1, modulus)) % modulus


def fraction_mod_two_power(q, bits):
    m = 1 << bits
    num = q.numerator
    den = q.denominator
    while den % 2 == 0:
        den //= 2
        assert num % 2 == 0
        num //= 2
    return (num * pow(den, -1, m)) % m


def valuation_difference(a, b, bits):
    d = (a - b) % (1 << bits)
    return bits if d == 0 else ((d & -d).bit_length() - 1)


def main():
    # Exact rational verification of the binomial-harmonic identity.
    for n in range(1, 31):
        left = sum((Fraction(comb(n, j), j) for j in range(1, n + 1, 2)), Fraction(0, 1))
        right = sum((Fraction(2 ** (j - 1), j) for j in range(1, n + 1)), Fraction(0, 1))
        assert left == right, n

    bits = 13
    mod = 1 << bits
    # Compare independent modular summation with exact-rational definitions.
    for n in range(0, 27):
        assert pminusone_mod(n, bits) == fraction_mod_two_power(pminusone_exact(n), bits), n

    # General-a factorial units at a fixed known-stable precision.
    for a in (1, 2, 3, 5):
        z1 = unit_factorial(a * (1 << 13), mod)
        z2 = unit_factorial(a * (1 << 14), mod)
        assert z1 == z2, (a, z1, z2)

    # Different parameters a and Delta: the error's 2-adic order grows.
    cases = 0
    lowest = 100
    records = []
    for a in (1, 2, 3, 5):
        z = unit_factorial(a * (1 << 14), mod)
        for delta in range(0, 6):
            target = ((1 << a.bit_count()) * pminusone_mod(delta, bits) * pow(z, -1, mod)) % mod
            orders = []
            for e in range(4, 8):
                observed = pminusone_mod(a * (1 << e) + delta, bits)
                v = valuation_difference(observed, target, bits)
                # Only a modest finite-range check, not a claimed uniform convergence rate.
                assert v >= e - 4, (a, delta, e, v)
                lowest = min(lowest, v)
                orders.append(v)
                cases += 1
            records.append((a, delta, orders))
    print('VERIFY_OK rational_identity_n=30 exact_modular_n=27 factorial_unit_a=4')
    print(f'LIMIT_SAMPLES a_delta_pairs={len(records)} finite_approximants={cases} bits={bits} minimum_error_order={lowest}')
    for a, delta, vals in records:
        if delta in (0, 1, 3):
            print(f'a={a} Delta={delta} error_valuations_e4_to_e7={vals}')


if __name__ == '__main__':
    main()
