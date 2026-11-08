#!/usr/bin/env python3
"""Reproduce the exact cyclic binary trigram histogram count.

Independent exhaustive string-to-spectrum enumeration is compared with a
separate parameterization of balanced connected de Bruijn flows.  Standard
library only; no external data or dependencies.
"""
from collections import defaultdict
from fractions import Fraction


def spectrum(word):
    """Counts circular 3-grams in bit string word, with wraparound."""
    n = len(word)
    counts = [0] * 8
    for i in range(n):
        counts[(word[i] << 2) | (word[(i + 1) % n] << 1) | word[(i + 2) % n]] += 1
    return tuple(counts)


def observed(n):
    """Enumerate every binary word; rotations do not affect the spectrum."""
    ans = set()
    for v in range(1 << n):
        word = tuple((v >> i) & 1 for i in range(n))
        ans.add(spectrum(word))
    return ans


def constructed(n):
    """All balanced, connected edge multiplicity vectors of total n."""
    vectors = {(n, 0, 0, 0, 0, 0, 0, 0),
               (0, 0, 0, 0, 0, 0, 0, n)}
    if n % 2 == 0:
        t = n // 2
        vectors.add((0, 0, t, 0, 0, t, 0, 0))
    for t in range(1, n // 2 + 1):
        for x in range(t + 1):
            for y in range(t + 1):
                if x == y == 0:
                    continue
                rem = n - (2 * t + x + y)
                if rem < 0:
                    continue
                if x == 0:
                    possible_a = (0,)
                elif y == 0:
                    possible_a = (rem,)
                else:
                    possible_a = range(rem + 1)
                for a in possible_a:
                    h = rem - a
                    if y == 0 and h != 0:
                        continue
                    if x == 0 and a != 0:
                        continue
                    vectors.add((a, x, t - y, y, x, t - x, y, h))
    return vectors


def analytic_count(n):
    """Coefficient of the claimed rational generating function, independently."""
    value = 2 + (n % 2 == 0)
    for t in range(1, n // 2 + 1):
        for x in range(1, t + 1):
            if 2 * t + x <= n:
                value += 2
            for y in range(1, t + 1):
                value += max(0, n - 2 * t - x - y + 1)
    return value


def check():
    total_words = 0
    total_spectra = 0
    for n in range(1, 18):
        found = observed(n)
        expected = constructed(n)
        assert found == expected, ('flow mismatch', n,
                                  list(expected - found)[:2], list(found - expected)[:2])
        assert len(found) == analytic_count(n), ('coefficient mismatch', n)
        total_words += 1 << n
        total_spectra += len(found)
    for n in range(18, 81):
        expected = constructed(n)
        assert len(expected) == analytic_count(n), ('long coefficient mismatch', n)
    prefix = [analytic_count(n) for n in range(1, 14)]
    assert prefix == [2, 3, 4, 6, 8, 13, 18, 27, 38, 53, 72, 98, 128]
    assert spectrum(tuple(map(int, '001011'))) == spectrum(tuple(map(int, '001101')))
    print('PASS', 'exhaustive_lengths=1..17', 'words=', total_words,
          'distinct_spectra=', total_spectra,
          'parameter_and_coefficient_lengths=1..80', 'prefix=', prefix)


if __name__ == '__main__':
    check()
