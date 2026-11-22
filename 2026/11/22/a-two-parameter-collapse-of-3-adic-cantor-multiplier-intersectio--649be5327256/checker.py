#!/usr/bin/env python3
"""Exact finite checks for the ternary Cantor multiplier-collapse theorem.

This is a finite check, not a substitute for the all-parameter proof.
Run: python checker.py
"""
from itertools import product


def L(m):
    return (3 ** m - 1) // 2


def ternary_01(z, digits):
    for _ in range(digits):
        if z % 3 == 2:
            return False
        z //= 3
    return True


def allowed_by_gaps(mask, n, k):
    last = -k
    for j in range(n):
        if mask >> j & 1:
            if j - last < k:
                return False
            last = j
    return True


def test_pair(r, k, n):
    assert 2 <= r <= k - 2
    a, b = L(r), 3 ** (k - 1) + L(k - r)
    # A product of a length-n input with a k-digit multiplier has no
    # digits past n+k-1. Testing n+k digits is therefore exhaustive.
    good = 0
    for mask in range(1 << n):
        x = sum(3 ** i for i in range(n) if mask >> i & 1)
        actual = ternary_01(a*x, n+k) and ternary_01(b*x, n+k)
        predicted = allowed_by_gaps(mask, n, k)
        assert actual == predicted, (r, k, n, mask, actual, predicted)
        good += int(actual)
    return good


def count_recurrence(k, n):
    a = [j+1 for j in range(k)]
    for j in range(k, n+1):
        a.append(a[j-1] + a[j-k])
    return a[n]


def main():
    pairs = 0
    words = 0
    for r in range(2, 6):
        for k in range(r+2, min(13, r+6)):
            for n in (k, k+2, k+4):
                actual = test_pair(r, k, n)
                assert actual == count_recurrence(k, n), (r, k, n, actual)
                words += 1 << n
                pairs += 1
    print(f"PASS: {pairs} pair/depth tests and {words} complete input-word checks")

if __name__ == '__main__':
    main()
