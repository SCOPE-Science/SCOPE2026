#!/usr/bin/env python3
"""Finite consistency checks for the Prouhet annulus localization formula.

Uses only Python's standard library. Tests are not a replacement for the
infinite-dimensional estimates proved in RESULT.md.
"""
import math


def sign(j):
    return -1 if j.bit_count() % 2 else 1


def gamma_shell_mass(n, j):
    # For integer n>=0 this is integral_j^(j+1) exp(-t)*t^n/n! dt.
    s0 = math.fsum((j**r) / math.factorial(r) for r in range(n + 1))
    s1 = math.fsum(((j + 1)**r) / math.factorial(r) for r in range(n + 1))
    return math.exp(-j) * s0 - math.exp(-j - 1) * s1


def q(n, max_shell=110):
    return math.fsum(sign(j) * gamma_shell_mass(n, j) for j in range(max_shell))


def b(n, k):
    assert n >= k + 1 and k >= 1
    r1 = math.exp(0.5 * (math.lgamma(k + 1) + math.lgamma(n - k + 1) - math.lgamma(n + 1)))
    r2 = math.exp(0.5 * (math.lgamma(k + 2) + math.lgamma(n - k) - math.lgamma(n + 1)))
    return (2.0 ** (k * (k - 1) / 2)) * ((2.0 ** (-k)) * r1 + r2)


def product_of_thue_factors(x):
    ans = 1.0
    p = 1
    while x**p > 1e-17:
        ans *= 1 - x**p
        p *= 2
    return ans


def main():
    assertions = 0
    for k in range(1, 11):
        for degree in range(k):
            lhs = sum(sign(j) * j**degree for j in range(2**k))
            assert lhs == 0, (k, degree, lhs)
            assertions += 1
    for n in range(0, 13):
        value = q(n)
        assert abs(value) <= 1 + 1e-11, (n, value)
        assertions += 1
        if n >= 2:
            for k in range(1, min(5, n-1) + 1):
                assert abs(value) < b(n, k) + 1e-9, (n,k,value,b(n,k))
                assertions += 1
    q0_product = (1-math.exp(-1)) * product_of_thue_factors(math.exp(-1))
    assert abs(q(0)-q0_product) < 2e-13
    assertions += 1
    assert q(0) > .33 and q(1) < -.18 and q(4) > 0 and q(12) < 0
    assertions += 4
    for z in (.10, .35):
        # Radius <1 gives a rapidly convergent Taylor series, independently
        # confirming the Laplace-transform generating-function identity.
        lhs = sum(q(n)*z**n for n in range(0,13))
        w = 1-z
        rhs = -math.expm1(-w)/w * product_of_thue_factors(math.exp(-w))
        assert abs(lhs-rhs) < 2e-7, (z,lhs,rhs)
        assertions += 1
    print(f'THUE_MORSE_FOCK_CHECKS_PASS {assertions}')


if __name__ == '__main__':
    main()
