#!/usr/bin/env python3
"""Arithmetic verification of the exact genus-four degree-four threshold.

The infinite-range argument is given symbolically in the accompanying proof.
This program checks finite boundary cases and derives the Frobenius polynomial.
"""
from fractions import Fraction
from math import comb, isqrt


def mobius(n):
    if n == 1:
        return 1
    p = 2
    k = 0
    while p * p <= n:
        if n % p == 0:
            n //= p
            k += 1
            if n % p == 0:
                return 0
            while n % p == 0:
                return 0
        p += 1
    if n > 1:
        k += 1
    return -1 if k & 1 else 1


def power_sum(r):
    # Frobenius spectrum: 2 repeated four times,
    # 2*zeta and 2*zeta^2 each repeated twice.
    # zeta^r+zeta^(2r)=2 if 3|r, otherwise -1.
    return 2 ** r * (4 + 2 * (2 if r % 3 == 0 else -1))


def number_points(r):
    return 4 ** r + 1 - power_sum(r)


def closed_places(r):
    s = sum(mobius(r // d) * number_points(d)
            for d in range(1, r + 1) if r % d == 0)
    assert s % r == 0
    return s // r


def strict_universal_bound(r):
    # The proof uses a stronger rational upper bound for every proper divisor.
    return 4 ** r + 1 - 8 * 2 ** r > Fraction(49 * r, 32) * 2 ** r


def main():
    assert [number_points(r) for r in (1, 2, 3, 4)] == [1, 9, 1, 225]
    assert [closed_places(r) for r in (1, 2, 3, 4)] == [1, 4, 0, 54]
    for r in range(4, 100):
        assert strict_universal_bound(r), r
        assert closed_places(r) > 0, r
    # Derivation of multiplicities from m0+2m=8 and m0-m=2.
    sols = [(m0, m) for m0 in range(9) for m in range(5)
            if m0 + 2*m == 8 and m0-m == 2]
    assert sols == [(4, 2)]
    # Compute polynomial (1-2T)^4 (1+2T+4T^2)^2.
    poly = [1]
    for factor in [[1, -2]]*4 + [[1, 2, 4]]*2:
        r = [0]*(len(poly)+len(factor)-1)
        for i,a in enumerate(poly):
            for j,b in enumerate(factor): r[i+j] += a*b
        poly = r
    assert len(poly) == 9
    assert poly[0] == 1 and poly[-1] == 4**4
    print('numerator_coefficients', poly)
    print('N1_N2_N3_N4', [number_points(r) for r in range(1,5)])
    print('B1_B2_B3_B4', [closed_places(r) for r in range(1,5)])
    print('WEIL_CLOSED_POINT_VERIFICATION_OK')

if __name__ == '__main__': main()
