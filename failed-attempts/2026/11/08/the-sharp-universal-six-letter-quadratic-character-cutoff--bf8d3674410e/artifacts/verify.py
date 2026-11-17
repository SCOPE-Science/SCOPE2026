#!/usr/bin/env python3
"""Exact finite certificate for the universal six-bit Legendre-word cutoff.

This code uses only integer arithmetic and the Python standard library.
The infinite range is covered separately by the Weil character-sum bound.
"""
from math import isqrt

K = 6
LIMIT = 14000
FULL = (1 << (1 << K)) - 1


def primes_through(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for d in range(2, isqrt(n) + 1):
        if sieve[d]:
            sieve[d*d:n+1:d] = b'\x00' * ((n - d*d)//d + 1)
    return [p for p in range(2, n+1) if sieve[p]]


def coverage_from_squares(p):
    nonzero_square = bytearray(p)
    for x in range(1, (p + 1)//2):
        nonzero_square[x*x%p] = 1
    # pattern 1..6, lowest-order bit represents the first entry.
    mask = sum(nonzero_square[i+1] << i for i in range(K))
    covered = 1 << mask
    witnesses = {mask: 1}
    for n in range(2, p-K+1):
        mask = (mask >> 1) | (nonzero_square[n+K-1] << (K-1))
        covered |= (1 << mask)
        witnesses.setdefault(mask, n)
    return covered, witnesses


def coverage_from_euler(p):
    # Independent calculation, direct Legendre signs by Euler's criterion.
    signs = [int(pow(j, (p-1)//2, p) == 1) for j in range(1,p)]
    covered = 0
    for n in range(1,p-K+1):
        mask = 0
        for j in range(K):
            mask |= signs[n+j-1] << j
        covered |= 1 << mask
    return covered


def main():
    primes = primes_through(LIMIT)
    assert 457 in primes and 461 in primes
    p457, _ = coverage_from_squares(457)
    p461, w461 = coverage_from_squares(461)
    assert p457.bit_count() == 63
    assert FULL ^ p457 == (1 << 63)
    assert p461 == FULL
    assert w461[63] == 19
    checked = [p for p in primes if 461 <= p < LIMIT]
    assert checked[0] == 461
    for p in checked:
        m, _ = coverage_from_squares(p)
        assert m == FULL, ('missing 6-bit words', p, FULL ^ m)
    # Independent Euler/Legendre implementation, boundary and spread check.
    spot = sorted(set([457, 461, 463, 487, 997, 1009, 1999, 5003, 10007] +
                      checked[::29] + [checked[-1]]))
    for p in spot:
        m, _ = coverage_from_squares(p)
        assert coverage_from_euler(p) == m, ('cross check', p)
    # Explicit positivity bound p - 114 sqrt(p) - 207 > 0 for p >= 14000:
    # at 14000 use exact squared rational inequalities instead of floating point.
    assert 14000 > 207
    assert (14000-207)**2 > 114**2 * 14000
    assert 14000 > (114//2)**2 # positivity increasing for p >= 14000.
    print('VERIFY_OK')
    print('k=6 prime=457 63/64 words, missing bit-mask=63 (all six residues)')
    print('k=6 prime=461 64/64 words, first all-residue start=19')
    print('primes p in [461,14000) checked:', len(checked))
    print('first checked prime:', checked[0], 'last checked prime:', checked[-1])
    print('independent Euler criterion checks:', len(spot))
    print('finite certificate: all 64 masks verified for each checked prime')
    print('Weil positivity: (14000 - 207)^2 > 114^2 * 14000; derivative positive beyond 14000')
    print('witnesses at 461, masks 0..63:', [w461[i] for i in range(64)])

if __name__ == '__main__':
    main()
