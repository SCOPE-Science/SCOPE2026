#!/usr/bin/env python3
"""Exact integer checks for graphwise coprimality in quadratic Beatty vectors."""
from itertools import combinations
from math import gcd, isqrt


def primes_below(limit):
    marks = bytearray(b'\x01') * limit
    if limit > 0:
        marks[0] = 0
    if limit > 1:
        marks[1] = 0
    for k in range(2, isqrt(limit - 1) + 1):
        if marks[k]:
            marks[k * k:limit:k] = b'\x00' * ((limit - 1 - k * k) // k + 1)
    return [k for k in range(2, limit) if marks[k]]


def local_factor(vertices, edges, p):
    # Rational factor, evaluated as an integer numerator over p^vertices.
    count = 0
    for mask in range(1 << vertices):
        if any(mask & (1 << a) and mask & (1 << b) for a, b in edges):
            continue
        t = mask.bit_count()
        count += (p - 1) ** (vertices - t)
    return count, p ** vertices


def check_case(radicals, edges, cutoff=100000, bound=10000):
    vertices = 1 + len(radicals)
    count = 0
    for n in range(1, cutoff + 1):
        row = [n] + [isqrt(r * n * n) for r in radicals]
        if all(gcd(row[a], row[b]) == 1 for a, b in edges):
            count += 1
    product = 1.0
    for p in primes_below(bound):
        num, den = local_factor(vertices, edges, p)
        product *= num / den
    return count, count / cutoff, product


def main():
    trials = [
        ([2, 3], [(0, 1), (1, 2)]),
        ([2, 3], list(combinations(range(3), 2))),
        ([2, 3, 5], list(combinations(range(4), 2))),
    ]
    for radicals, edges in trials:
        count, observed, product = check_case(radicals, edges)
        print('radicals=', radicals, 'edges=', edges,
              'N=100000', 'exact_count=', count,
              'empirical_density=', format(observed, '.8f'),
              'prime_truncation_p<10000=', format(product, '.12f'))
        assert abs(observed - product) < 0.003
    print('VERIFY_OK exact_counts=True truncation_is_not_infinite_product=True')


if __name__ == '__main__':
    main()
