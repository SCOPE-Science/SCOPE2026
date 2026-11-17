#!/usr/bin/env python3
"""Exact modular tests for the period classification of odd self-powers."""
from collections import Counter


def valuation(n):
    if n == 0:
        raise ValueError("valuation of zero is infinite")
    return (n & -n).bit_length() - 1


def predicted_period(x, k):
    if k == 1:
        return 1
    modulus = 1 << k
    x %= modulus
    assert x % 2
    if x % 4 == 1:
        r = k if x == 1 else valuation(x - 1)
        return 1 << max(0, k - 2 * r)
    r = k if x == modulus - 1 else valuation(x + 1)
    if k <= r + 1:
        return 1
    return 1 << max(1, k - 3 * r + 1)


def predicted_cycle_counts(k):
    if k == 1:
        return Counter({1: 1})
    points = Counter({1: 2})  # The classes +1 and -1.
    for r in range(2, k):
        size = 1 << (k - r - 1)
        plus_period = 1 << max(0, k - 2 * r)
        minus_period = 1 if k <= r + 1 else 1 << max(1, k - 3 * r + 1)
        points[plus_period] += size
        points[minus_period] += size
    assert sum(points.values()) == 1 << (k - 1)
    assert all(n % period == 0 for period, n in points.items())
    return Counter({period: n // period for period, n in points.items()})


def directly_enumerated_cycles(k):
    modulus = 1 << k
    seen = set()
    counts = Counter()
    for start in range(1, modulus, 2):
        if start in seen:
            continue
        x = start
        length = 0
        while x not in seen:
            seen.add(x)
            length += 1
            x = pow(x, x, modulus)
        assert x == start, (k, start, x)
        counts[length] += 1
        assert length == predicted_period(start, k), (k, start, length)
    return counts


def valuation_mod(x, modulus):
    x %= modulus
    return None if x == 0 else valuation(x)


def test_valuations():
    modulus = 1 << 40
    tested = 0
    for x in range(3, 256, 2):
        r = valuation(x - 1) if x % 4 == 1 else valuation(x + 1)
        if x % 4 == 1:
            assert valuation_mod(pow(x, x, modulus) - x, modulus) == 2 * r
        else:
            y = pow(x, x, modulus)
            assert valuation_mod(y - x, modulus) == r + 1
            assert valuation_mod(pow(y, y, modulus) - x, modulus) == 3 * r
        y = x
        for j in range(8):
            for _ in range(1 << (j - 1) if j else 1):
                y = pow(y, y, modulus)
            expected = (2 * r + j) if x % 4 == 1 else (r + 1 if j == 0 else 3 * r + j - 1)
            assert valuation_mod(y - x, modulus) == expected, (x, j, expected)
            tested += 1
    return tested


def main():
    cycles = 0
    for k in range(1, 17):
        actual = directly_enumerated_cycles(k)
        expected = predicted_cycle_counts(k)
        assert actual == expected, (k, actual, expected)
        cycles += sum(actual.values())
        if k >= 6:
            assert actual[1 << (k - 4)] == 2
        if k >= 3:
            assert actual[1] == (1 << (k // 2)) + 2
        if k >= 5:
            rooted_two_walks = sum(length * count for length, count in actual.items() if length <= 2)
            published = (1 << ((k + 1) // 2)) + (1 << (k // 3 + (k + 1) // 3))
            assert rooted_two_walks == published
    tests = test_valuations()
    print(f"VERIFY_OK k=1..16 complete_odd_cycles=PASS total_cycles={cycles} "
          f"valuation_tests={tests} max_cycles=PASS prior_two_walk_counts=PASS")


if __name__ == '__main__':
    main()
