#!/usr/bin/env python3
"""Independent finite checks for the fixed-weight Rule 150 image-spectrum theorem.

Run with: python CHECK.py
Uses only the Python 3 standard library.
"""
from collections import Counter
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def predicted(n, w):
    if n < 1 or not 0 <= w <= n:
        raise ValueError('Require n >= 1 and 0 <= w <= n')
    if n % 3:
        return {1: choose(n, w)}
    m = n // 3
    M1 = choose(n, w)
    M2 = 3 * choose(2 * m, m) * choose(m, w - m) // 2
    M3 = choose(m, 2 * m - w) * choose(m, w - m) ** 2
    M4 = (choose(m, m // 2) ** 3 // 4
          if m % 2 == 0 and 2 * w == 3 * m else 0)
    B4 = M4
    B3 = M3 - 4 * M4
    B2 = M2 - 3 * M3 + 6 * M4
    B1 = M1 - 2 * M2 + 3 * M3 - 4 * M4
    assert all(v >= 0 for v in (B1, B2, B3, B4))
    assert sum(j * v for j, v in enumerate((0, B1, B2, B3, B4))
               if j) == choose(n, w)
    return {j: v for j, v in enumerate((0, B1, B2, B3, B4)) if j and v}


def update(x, n):
    y = 0
    for i in range(n):
        b = ((x >> ((i - 1) % n)) ^ (x >> i) ^
             (x >> ((i + 1) % n))) & 1
        y |= b << i
    return y


def exhaustive(n, w):
    buckets = Counter()
    for x in range(1 << n):
        if x.bit_count() == w:
            buckets[update(x, n)] += 1
    return dict(Counter(buckets.values()))


def main():
    cases = 0
    sources = 0
    for n in range(1, 19):
        for w in range(n + 1):
            expected = predicted(n, w)
            actual = exhaustive(n, w)
            assert expected == actual, (n, w, expected, actual)
            cases += 1
            sources += choose(n, w)
    assert cases == 189
    assert sources == sum(1 << n for n in range(1, 19))
    assert predicted(9, 3) == {1: 27, 2: 27, 3: 1}
    assert predicted(6, 3) == {2: 6, 4: 2}
    for m in range(1, 81):
        n = 3 * m
        for w in range(n + 1):
            d = predicted(n, w)
            assert sum(j * v for j, v in d.items()) == choose(n, w)
            assert (sum(v for j, v in d.items()) == choose(n, w)) == (
                w < m or w > 2 * m)
            if m % 2 == 0 and w * 2 == 3 * m:
                assert d.get(4, 0) > 0 and d.get(3, 0) == 0
            elif m <= w <= 2 * m:
                assert d.get(3, 0) > 0
    print(f'PASS: {cases} exhaustive (n,w) slices for 1 <= n <= 18')
    print(f'PASS: {sources} source evaluations across all slices')
    print('PASS: 80 arithmetic parameter sweeps with all weights')
    print('PASS: injectivity threshold and triple/quadruple boundary checks')


if __name__ == '__main__':
    main()
