#!/usr/bin/env python3
"""Separate phase-based confirmation, using pairwise comparisons instead of frequency tables."""
from itertools import product


def is_primitive(v):
    n = len(v)
    return all(v != v[:d] * (n // d) for d in range(1, n) if n % d == 0)


def phase_class_distinct(v):
    return len({v[i:] + v[:i] for i in range(len(v))}) == len(v)


def duplicate(T, i, length):
    w = T[i:i + length]
    return any(T[j:j + length] == w for j in range(len(T) - length + 1) if j != i)


def net_without_frequency_dict(T):
    n = len(T)
    out = []
    for length in range(1, n):
        for i in range(n - length + 1):
            if not duplicate(T, i, length):
                continue
            if i > 0 and duplicate(T, i - 1, length + 1):
                continue
            if i + length < n and duplicate(T, i, length + 1):
                continue
            out.append((i, i + length))
    return sorted(out)


def main():
    cases = 0
    for q, max_len in [(2, 7), (3, 5)]:
        for p in range(1, max_len + 1):
            for chars in product(range(q), repeat=p):
                v = ''.join(str(c) for c in chars)
                if not is_primitive(v):
                    continue
                assert phase_class_distinct(v)
                for exponent in (3, 4):
                    T = v * exponent
                    N = len(T)
                    expected = [(0, N - p), (p, N)]
                    got = net_without_frequency_dict(T)
                    assert got == expected, (v, exponent, got, expected)
                    cases += 1
    print(f'PASS phase/independent-dupe checks: {cases} cases; all primitive rotations distinct')

if __name__ == '__main__':
    main()
