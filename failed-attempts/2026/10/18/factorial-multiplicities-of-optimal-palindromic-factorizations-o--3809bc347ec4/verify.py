#!/usr/bin/env python3
"""Independent palindrome expansion and exact optimal-factorization counting.

Usage: python verify.py
No third-party dependencies.
"""
from collections import Counter
from math import comb, factorial
from random import Random


def binary_runs(n):
    return (n ^ (n >> 1)).bit_count() if n else 0


def expected_count(r):
    return factorial((r + 1) // 2) * factorial(r // 2)


def check_prefixes(max_bits=16):
    limit = (1 << max_bits) - 1
    letters = [(j & -j).bit_length() - 1 for j in range(1, limit + 1)]
    pal_starts = [[] for _ in range(limit + 1)]
    examined = 0
    # Independently find all palindrome occurrences by expanding around every
    # possible odd and even center. No suffix/bit-transition formula is used.
    for c in range(limit):
        left = right = c
        while left >= 0 and right < limit and letters[left] == letters[right]:
            pal_starts[right + 1].append(left)
            examined += 1
            left -= 1
            right += 1
    for c in range(limit - 1):
        left, right = c, c + 1
        while left >= 0 and right < limit and letters[left] == letters[right]:
            pal_starts[right + 1].append(left)
            examined += 1
            left -= 1
            right += 1

    length = [0] * (limit + 1)
    ways = [0] * (limit + 1)
    ways[0] = 1
    levels = Counter()
    for n in range(1, limit + 1):
        best = min(length[i] for i in pal_starts[n])
        length[n] = best + 1
        ways[n] = sum(ways[i] for i in pal_starts[n] if length[i] == best)
        r = binary_runs(n)
        assert length[n] == r, ('length', n, length[n], r)
        assert ways[n] == expected_count(r), ('multiplicity', n, ways[n], expected_count(r))
        levels[r] += 1
    for r in range(1, max_bits + 1):
        assert levels[r] == comb(max_bits, r), (r, levels[r])
    return limit, examined, len(pal_starts), levels


def check_large_bit_transitions(cases=4000):
    rng = Random(2348172)
    total = 0
    for _ in range(cases):
        n = rng.getrandbits(rng.randint(1, 256)) + 1
        r = binary_runs(n)
        for i in range(n.bit_length()):
            if ((n >> i) & 1) == 0:
                continue
            lower = n & ((1 << i) - 1)
            m = n - 2 * lower - 1
            delta = 1 if ((n >> (i + 1)) & 1) else -1
            assert binary_runs(m) == r + delta, (n, i, m, r, delta)
            total += 1
    return total


if __name__ == '__main__':
    n, pal_count, endpoints, hist = check_prefixes()
    bit_checks = check_large_bit_transitions()
    print('VERIFY_OK ruler_Zimin_optimal_palindrome_factorizations',
          'exhaustive_prefixes=' + str(n),
          'palindrome_occurrences=' + str(pal_count),
          'dyadic_histogram_levels=' + str(len(hist)),
          'large_integer_bit_transition_checks=' + str(bit_checks))
