#!/usr/bin/env python3
"""Finite checks of a symbolic maximal-palindrome classification.

This checks windows in finite prefixes only; the accompanying proof gives
unbounded quantifiers and natural densities.
"""

def valuation_parity(t, base):
    count = 0
    while t % base == 0:
        t //= base
        count ^= 1
    return count

def word(base, length):
    return ''.join(str(valuation_parity(t, base)) for t in range(1, length + 1))

def inflate_palindrome(p, base):
    padding = '0' * (base - 1)
    return padding + padding.join('1' if x == '0' else '0' for x in p) + padding

def occurrences(haystack, needle):
    pos = 0
    out = []
    while True:
        pos = haystack.find(needle, pos)
        if pos < 0:
            return out
        out.append(pos)
        pos += 1

def predicted_starts(base, k, n, length):
    out = []
    v = 1
    while base**k * (base * base * v - base) + n <= length:
        if valuation_parity(v, base) == 0:
            for extra in (0, 1):
                start = base**k * (base * base * v - base + extra)
                if start + n <= length:
                    out.append(start)
        v += 1
    return sorted(out)

def verify():
    tested_windows = 0
    total_length_cases = 0
    occurrence_checks = 0
    for base in range(2, 9):
        length = max(17000, 2 * base**5)
        s = word(base, length)
        max_n = 150
        pal = {}
        for n in range(1, max_n + 3):
            current = set()
            for i in range(length - n + 1):
                t = s[i:i+n]
                if t == t[::-1]:
                    current.add(t)
            pal[n] = current
            tested_windows += length - n + 1
        expected = {}
        p = '0' * (2 * base - 2)
        k = 0
        while len(p) <= max_n:
            expected[len(p)] = (k, p)
            assert p == p[::-1]
            assert len(p) == (2*base-1)*base**k-1
            actual_starts = occurrences(s, p)
            formula_starts = predicted_starts(base, k, len(p), length)
            assert actual_starts == formula_starts, (base,k,len(p),actual_starts[:8],formula_starts[:8])
            occurrence_checks += len(actual_starts)
            p = inflate_palindrome(p, base)
            k += 1
        for n in range(1, max_n + 1):
            maximal = pal[n] - {v[1:-1] for v in pal[n+2]}
            expect = {expected[n][1]} if n in expected else set()
            assert maximal == expect, (base,n,maximal,expect)
            total_length_cases += 1
    print(f'VERIFY_OK bases=2..8 lengths_per_base=1..150 length_cases={total_length_cases} '
          f'palindrome_window_tests={tested_windows} occurrence_checks={occurrence_checks}')

if __name__ == '__main__':
    verify()
