#!/usr/bin/env python3
"""Exact rational checks for ternary-prime-power affine Wang--Sun sums.

Finite checks complement but do not prove the general cyclotomic argument.
"""
from fractions import Fraction
from math import comb


def power_sum(coefficients, exponent):
    """Newton sums for a monic polynomial with leading coefficient one."""
    degree = len(coefficients) - 1
    sums = [Fraction(0)] * (exponent + 1)
    for k in range(1, exponent + 1):
        total = sum(coefficients[j] * sums[k - j]
                    for j in range(1, min(k - 1, degree) + 1))
        if k <= degree:
            total += k * coefficients[k]
        sums[k] = -total
    return sums[exponent]


def cotangent_block(m):
    """Compute C_(2m) from root power sums for odd positive m."""
    assert m >= 1 and m % 2 == 1
    # Even-root polynomial: ((x+1)^m-(x-1)^m)/(2m).
    even = [Fraction(0)] * m
    even[0] = Fraction(1)
    for j in range(2, m, 2):
        even[j] = Fraction(comb(m, j + 1), m)
    # Odd-root polynomial: ((x+1)^m+(x-1)^m)/2.
    odd = [Fraction(comb(m, j)) if j % 2 == 0 else Fraction(0)
           for j in range(m + 1)]
    return power_sum(even, 2 * m) - power_sum(odd, 2 * m)


def affine_sum(a):
    """Specialized published divisor reduction for modulus 2*3**a."""
    assert a >= 1
    m = 3 ** a
    result = cotangent_block(m)
    for j in range(1, a):
        multiplier = 2 * 3 ** (2 * (a - j) - 1)
        result += multiplier * cotangent_block(3 ** j)
    return result


def valuation_three(q):
    assert q
    num, den = abs(q.numerator), q.denominator
    ans = 0
    while num % 3 == 0:
        num //= 3
        ans += 1
    while den % 3 == 0:
        den //= 3
        ans -= 1
    return ans


def main():
    assert cotangent_block(1) == 0
    checks = {1: Fraction(1456, 27),
              2: Fraction(1450048309488389824, 19683)}
    for a in (1, 2, 3):
        m = 3 ** a
        block = cotangent_block(m)
        affine = affine_sum(a)
        assert valuation_three(block) == -m
        assert valuation_three(affine) == -m
        assert block.denominator == 3 ** m
        assert affine.denominator == 3 ** m
        assert affine.numerator % 3 == 1
        if a in checks:
            assert affine == checks[a]
        print('BLOCK_AND_AFFINE_OK', 'a='+str(a), 'n='+str(2*m),
              'denominator='+str(affine.denominator),
              'numerator_mod_3='+str(affine.numerator % 3))
    print('VERIFY_OK exact_rational_arithmetic=true finite_only=true independent_audit=false')


if __name__ == '__main__':
    main()
