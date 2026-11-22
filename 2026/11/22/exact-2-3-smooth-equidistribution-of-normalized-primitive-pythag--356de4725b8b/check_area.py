#!/usr/bin/env python3
"""Exact finite tests for the modular primitive Pythagorean-area theorem.

The unrestricted asymptotic and its local lifting proof are mathematical
arguments; these checks test identities at independently enumerable levels.
"""
from collections import Counter
from math import gcd, isqrt


def area_parameter(m, n):
    return m*n*(m*m-n*n)


def two_fibers(exponent):
    modulus = 2**exponent
    result = Counter(
        area_parameter(m, n) % modulus
        for m in range(modulus) for n in range(modulus)
        if (m+n) % 2 == 1
    )
    assert set(result) == set(range(0, modulus, 2))
    assert all(number == modulus for number in result.values())


def three_fibers(exponent):
    modulus = 3**exponent
    result = Counter(
        area_parameter(m, n) % modulus
        for m in range(modulus) for n in range(modulus)
        if m % 3 or n % 3
    )
    assert set(result) == set(range(0, modulus, 3))
    assert all(number == 8*3**(exponent-1) for number in result.values())


def normalized_fibers(a, b):
    q = 2**a*3**b
    modulus = 6*q
    result = Counter(
        area_parameter(m, n) % modulus
        for m in range(modulus) for n in range(modulus)
        if (m+n) % 2 == 1 and (m % 3 or n % 3)
    )
    assert set(result) == set(range(0, modulus, 6))
    assert all(number == 16*q for number in result.values())


def nonuniform_prime(prime):
    result = Counter(
        area_parameter(m, n) % prime
        for m in range(prime) for n in range(prime)
        if m % prime or n % prime
    )
    assert result[0] == 4*(prime-1)
    assert sum(result.values()) == prime**2-1
    assert 4*(prime-1)*prime != prime**2-1


def finite_triangle_counts(q, bound):
    counts = Counter()
    for m in range(2, isqrt(bound)+1):
        for n in range(1, m):
            if m*m+n*n > bound or gcd(m, n) != 1 or (m+n) % 2 != 1:
                continue
            area = area_parameter(m, n)
            assert area % 6 == 0
            counts[(area//6) % q] += 1
    assert set(counts) == set(range(q)), (q, counts)
    assert max(counts.values()) - min(counts.values()) < 8*isqrt(bound)
    return counts


def main():
    tests = 0
    for exponent in range(1, 8):
        two_fibers(exponent)
        tests += 1
    for exponent in range(1, 6):
        three_fibers(exponent)
        tests += 1
    for a in range(0, 4):
        for b in range(0, 4):
            if 6*2**a*3**b <= 500:
                normalized_fibers(a, b)
                tests += 1
    for prime in [5, 7, 11, 13, 17]:
        nonuniform_prime(prime)
        tests += 1
    for q in [1, 2, 3, 4, 6, 9, 12, 18, 24, 36]:
        finite_triangle_counts(q, 250000)
        tests += 1
    print('CHECK_OK', tests, 'test families')


if __name__ == '__main__':
    main()
