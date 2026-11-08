#!/usr/bin/env python3
"""Finite consistency checks for an all-period Thue--Morse Abelian-square law.

The infinite result is proved mathematically in RESULT.md.  These bounded
checks do not establish existence of natural densities or infinite extrema.
Requires only Python 3.10+.
"""
from functools import lru_cache
from fractions import Fraction


@lru_cache(maxsize=None)
def correlation(offset):
    assert isinstance(offset, int) and offset >= 0
    if offset == 0:
        return Fraction(1)
    if offset == 1:
        return Fraction(-1, 3)
    if offset % 2 == 0:
        return correlation(offset // 2)
    half = offset // 2
    return -(correlation(half) + correlation(half + 1)) / 2


def predicted_density(period):
    assert period >= 1
    if period % 2:
        return (1 - correlation(period)) / 4
    return (5 + 3 * correlation(period // 2)) / 8


def local_occurrence(period, start, bits):
    if period % 2:
        if start % 2 == 0:
            return False
        q = (start - 1) // 2
        return bits[q] != bits[q + period]
    if start % 2 == 0:
        return True
    q = (start - 1) // 2
    half = period // 2
    return bits[q] == bits[q + half] == bits[q + 2 * half]


def main():
    cap = 1 << 16
    largest_period = 128
    bits = bytearray((v.bit_count() & 1) for v in range(cap + 2 * largest_period + 1))
    count_prefix = [0]
    for value in bits:
        count_prefix.append(count_prefix[-1] + value)

    tests = 0
    for period in range(1, largest_period + 1):
        count = 0
        for start in range(cap):
            a = count_prefix[start + period] - count_prefix[start]
            b = count_prefix[start + 2 * period] - count_prefix[start + period]
            is_square = (a == b)
            if start < 2048:
                assert is_square == local_occurrence(period, start, bits), (period, start)
                tests += 1
            count += is_square
        observed = Fraction(count, cap)
        delta = predicted_density(period)
        assert abs(observed - delta) < Fraction(1, 1000), (period, observed, delta)
        tests += 1

    assert predicted_density(1) == Fraction(1, 3)
    assert predicted_density(3) == Fraction(1, 6)
    assert predicted_density(9) == Fraction(5, 24)
    assert predicted_density(11) == Fraction(7, 24)
    assert predicted_density(13) == Fraction(7, 24)
    assert predicted_density(15) == Fraction(5, 24)
    tests += 6

    for half in range(1, 8193):
        val = correlation(half)
        assert Fraction(-1, 3) <= val <= Fraction(1, 3)
        if val == Fraction(-1, 3):
            assert half & (half - 1) == 0
        if val == Fraction(1, 3):
            assert half % 3 == 0 and (half // 3) & ((half // 3) - 1) == 0
        period = 2 * half
        observed = predicted_density(period)
        assert Fraction(1, 2) <= observed <= Fraction(3, 4)
        tests += 4

    print("VERIFY_OK local_and_density_tests=" + str(tests))
    print("first_16_densities=" + ",".join(str(predicted_density(n)) for n in range(1, 17)))


if __name__ == "__main__":
    main()
