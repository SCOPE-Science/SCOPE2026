#!/usr/bin/env python3
"""Finite checks for the two-prime-support quadratic polynomial Jacobsthal law.

This is a reproducibility check, not a substitute for the all-prime proof.
Python 3 standard library only.
"""
from math import gcd


def factors(n):
    f = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            f.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        f.append(n)
    return f


def predicted_counts(n):
    primes = factors(n)
    if len(primes) == 1:
        p = primes[0]
        counts = [1, int(p == 3), 0, 0, 0, 0]
    elif len(primes) == 2:
        p, q = primes
        counts = [p + q - 1, q if p == 3 else 2,
                  int(p <= 5), int(p == 3 or (p, q) == (2, 3)),
                  int(p == 3 or (p, q) == (2, 3)), 0]
    else:
        raise ValueError('Requires one or two distinct prime factors')
    rad = 1
    for p in primes:
        rad *= p
    return [v * (n // rad) for v in counts]


def direct_counts(n):
    out = [0] * 6
    for x in range(n):
        for k in range(1, 7):
            if gcd(x + k*k, n) == 1:
                break
            out[k-1] += 1
    return out


def local_cover_counts(p, q):
    """Independent CRT calculation by admissible quadratic residue fibers."""
    sq_p = [k*k % p for k in range(1, 7)]
    sq_q = [k*k % q for k in range(1, 7)]
    out = [0] * 6
    for a in range(p):
        cover_p = [(a + v) % p == 0 for v in sq_p]
        for b in range(q):
            cover_q = [(b + v) % q == 0 for v in sq_q]
            for i in range(6):
                if not (cover_p[i] or cover_q[i]):
                    break
                out[i] += 1
    return out


def primes_below(limit):
    return [p for p in range(2, limit) if factors(p) == [p]]


def main():
    checked_n = 0
    for n in range(2, 1601):
        if len(factors(n)) <= 2:
            assert direct_counts(n) == predicted_counts(n), (n, direct_counts(n), predicted_counts(n))
            checked_n += 1
    ps = primes_below(79)
    checked_pairs = 0
    for i, p in enumerate(ps):
        for q in ps[i+1:]:
            n = p*q
            actual = direct_counts(n)
            fiber = local_cover_counts(p, q)
            theory = predicted_counts(n)
            assert actual == fiber == theory, (p, q, actual, fiber, theory)
            checked_pairs += 1
    print('PASS: all integers 2..1600 with at most two distinct prime factors:', checked_n)
    print('PASS: distinct prime pairs p<q<79 (direct gcd vs independent CRT):', checked_pairs)
    print('Checks include k=1,2,3,4,5,6; k>6 vanishes by monotonicity.')
    print('This is finite evidence only; uniform bounds require the written proof.')


if __name__ == '__main__':
    main()
