#!/usr/bin/env python3
"""Standalone integer verification of the exact dyadic valuations of ternary-tree counts."""
from collections import Counter
from math import comb

# State order: (previous digit, carry) = (0,0),(1,0),(0,1),(1,1).
# Each entry is (destination state, extra carry exponent).
TRANSITIONS = (
    ((0, 0), (1, 0)),
    ((0, 0), (3, 1)),
    ((0, 0), (3, 1)),
    ((2, 1), (3, 1)),
)


def dp_coefficients(max_level):
    # d[state][k] counts length-r bit words ending at state with k carries.
    d = [[0] * (max_level + 2) for _ in range(4)]
    d[0][0] = 1
    for r in range(max_level + 1):
        out = [0] * (max_level + 2)
        for state, row in enumerate(d):
            tail = int(state == 3)
            for k, count in enumerate(row):
                if count:
                    out[k + tail] += count
        yield r, out[:r + 1]
        nd = [[0] * (max_level + 2) for _ in range(4)]
        for state, row in enumerate(d):
            for dest, carry in TRANSITIONS[state]:
                for k, count in enumerate(row):
                    if count and k + carry < len(row):
                        nd[dest][k + carry] += count
        d = nd


def direct_by_digits(r):
    count = [0] * (r + 1)
    for n in range(1 << r):
        j = 2 * n.bit_count() - (3 * n).bit_count()
        if j < 0 or j > r:
            raise AssertionError((n, j, r))
        count[j] += 1
    return count


def v2(n):
    return (n & -n).bit_length() - 1 if n else 10**9


def main():
    levels = 16
    trials = 0
    for r, poly in dp_coefficients(levels):
        assert sum(poly) == 1 << r, (r, poly)
        assert poly == direct_by_digits(r), (r, poly)
        assert r < 2 or poly[1] == 0
        if r >= 2:
            assert all(poly[j] > 0 for j in range(2, r + 1)), (r, poly)
        x, y = 0, 1
        for _ in range(r + 2):
            x, y = y, x + y
        assert poly[0] == x, (r, poly, x)
        trials += 1 << r
    exact_values = 0
    for n in range(0, 384):
        number = comb(3 * n, n) // (2 * n + 1)
        assert number * (2 * n + 1) == comb(3 * n, n)
        assert v2(number) == 2 * n.bit_count() - (3 * n).bit_count(), n
        exact_values += 1
    print('VERIFY_OK levels=0..16 full_dyadic_enumeration=PASS words=' + str(trials) +
          ' exact_large_integer_Fuss_Catalan=' + str(exact_values) +
          ' no_valuation_one=PASS Fibonacci_odd_counts=PASS full_support=PASS')


if __name__ == '__main__':
    main()
