#!/usr/bin/env python3
"""Exact transfer-polynomial and constructive minimum checks for C_n squared."""
from collections import defaultdict


def transitions(state):
    a, b, c, d = ((state >> j) & 1 for j in (3, 2, 1, 0))
    return [(((state << 1) & 15) | e, e) for e in (0, 1)
            if 1 <= a + b + d + e <= 2]


def polynomial(n):
    coefficients = [0] * (n + 1)
    trans = [transitions(i) for i in range(16)]
    for origin in range(16):
        current = {(origin, 0): 1}
        for step in range(n):
            next_values = defaultdict(int)
            for (state, k), count in current.items():
                for successor, bit in trans[state]:
                    next_values[(successor, k + bit)] += count
            current = next_values
        for (state, k), count in current.items():
            if state == origin:
                coefficients[k] += count
    return coefficients


def gamma(n):
    q, r = divmod(n, 7)
    return 2 * q + (0 if r == 0 else 1 if r in (1, 2) else 2)


def construction(n):
    q, r = divmod(n, 7)
    if r == 0:
        long = [5] * q
        short = [2] * q
    elif r in (1, 2):
        long = [5] * q
        if r == 1:
            long[0] = 4
        short = [2] * (q + 1)
    else:
        long = [5] * (q + 1)
        if r == 3:
            long[0:2] = [3, 3]
        elif r == 4:
            long[0:2] = [3, 4]
        elif r == 5:
            long[0] = 3
        elif r == 6:
            long[0] = 4
        short = [2] * (q + 1)
    gaps = []
    for i, length in enumerate(long):
        gaps += [short[i], length]
    if len(short) > len(long):
        gaps.append(short[-1])
    assert sum(gaps) == n and len(gaps) == gamma(n), (n, gaps)
    marked = set()
    p = 0
    for d in gaps:
        marked.add(p)
        p = (p + d) % n
    assert p == 0 and len(marked) == gamma(n)
    for v in range(n):
        count = sum(((v + delta) % n) in marked for delta in (-2, -1, 1, 2))
        assert 1 <= count <= 2, (n, marked, v, count)
    return marked


def main():
    table = []
    for n in range(5, 81):
        construction(n)
        counts = polynomial(n)
        optimum = next((k for k, a in enumerate(counts) if a), None)
        expected = gamma(n)
        assert optimum == expected, (n, optimum, expected)
        r = n % 7
        if r == 0:
            assert counts[optimum] == 7, (n, counts[optimum])
        if r == 1:
            assert counts[optimum] == (2 * (n // 7) - 1) * n, (n, counts[optimum])
        if r == 2:
            assert counts[optimum] == n, (n, counts[optimum])
        if r == 6:
            assert counts[optimum] == 2 * n, (n, counts[optimum])
        if n <= 24:
            table.append((n, optimum, counts[optimum], sum(counts)))
    print('n optimum optimum_count total_valid')
    for row in table:
        print(*row)
    print('PASS transfer polynomial n=5..80, constructive supports n=5..80, four exact multiplicity checks')

if __name__ == '__main__':
    main()
