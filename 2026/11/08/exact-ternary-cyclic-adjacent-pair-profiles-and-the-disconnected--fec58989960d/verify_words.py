#!/usr/bin/env python3
"""Enumerate cyclic ternary words and independently evaluate a coefficient GF."""
from itertools import product
from math import comb


def observed(n):
    profiles = set()
    for w in product(range(3), repeat=n):
        counts = [0] * 9
        for i in range(n):
            counts[3 * w[i] + w[(i + 1) % n]] += 1
        profiles.add(tuple(counts))
    return len(profiles)


def coefficient(n):
    # Disjoint support-graph types; coefficient extraction from geometric factors.
    count = 3  # One active vertex with positive loops.
    for b in range(1, n // 2 + 1):
        count += 3 * (n - 2 * b + 1)
    for b in range(1, n // 2 + 1):
        for c in range(1, (n - 2 * b) // 2 + 1):
            count += 3 * comb(n - 2 * b - 2 * c + 2, 2)
            for e in range(1, (n - 2 * b - 2 * c) // 2 + 1):
                count += comb(n - 2 * b - 2 * c - 2 * e + 2, 2)
    for d in range(1, n // 3 + 1):
        rem = n - 3 * d
        for b in range(rem // 2 + 1):
            for c in range((rem - 2 * b) // 2 + 1):
                for e in range((rem - 2 * b - 2 * c) // 2 + 1):
                    count += 2 * comb(rem - 2 * b - 2 * c - 2 * e + 2, 2)
    return count


def main():
    expected = [3, 6, 11, 24, 48, 95, 174, 306, 510, 819]
    for n, want in enumerate(expected, 1):
        a, b = observed(n), coefficient(n)
        assert (a, b) == (want, want), (n, a, b, want)
    print('WORDS_VERIFY_OK n=1..10')


if __name__ == '__main__':
    main()
