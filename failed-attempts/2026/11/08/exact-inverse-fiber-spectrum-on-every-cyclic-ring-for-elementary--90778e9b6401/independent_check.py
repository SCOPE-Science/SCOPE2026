#!/usr/bin/env python3
"""Independent direct-rule enumeration and 4-by-4 matrix trace validation."""
from collections import Counter


def next_ring(x, n):
    ans = 0
    for i in range(n):
        left = (x >> ((i - 1) % n)) & 1
        mid = (x >> i) & 1
        right = (x >> ((i + 1) % n)) & 1
        idx = 4 * left + 2 * mid + right
        ans |= ((106 >> idx) & 1) << i
    return ans


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def inverse_count(y, n):
    matrix = [[int(i == j) for j in range(4)] for i in range(4)]
    for i in range(n):
        val = (y >> i) & 1
        step = [[0] * 4 for _ in range(4)]
        for j in range(4):
            left, mid = j >> 1, j & 1
            for right in range(2):
                if ((106 >> (4 * left + 2 * mid + right)) & 1) == val:
                    step[j][(mid << 1) | right] = 1
        matrix = mul(matrix, step)
    return sum(matrix[i][i] for i in range(4))


def main():
    expected = [None,
       (1, 0, 1, 0), (1, 2, 1, 0), (3, 3, 1, 1),
       (5, 6, 5, 0), (6, 20, 6, 0), (12, 41, 10, 1),
       (22, 84, 22, 0), (33, 190, 33, 0),
       (57, 399, 55, 1), (101, 822, 101, 0),
       (166, 1716, 166, 0), (280, 3537, 278, 1)]
    for n in range(1, 13):
        observed = Counter(next_ring(x, n) for x in range(1 << n))
        hist = Counter(observed.values())
        spectrum = (1 << n) - len(observed), hist[1], hist[2], hist[3]
        assert spectrum == expected[n], (n, spectrum)
        # Matrix trace is derived separately from the published Wolfram truth table.
        for y in range(1 << n):
            assert inverse_count(y, n) == observed[y], (n, y)
        assert sum(spectrum[:3]) + spectrum[3] == 1 << n
    print('INDEPENDENT_OK: all indexed rings through length 12')

if __name__ == '__main__':
    main()
