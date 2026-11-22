#!/usr/bin/env python3
"""Independent bitwise carry-and-zero-run transfer for Baum-Sweet pair counts.
Uses no closed-form pair characterization. Run: python3 checks/carry_automaton.py
"""
from collections import defaultdict


def pair_count(m, r):
    # State: zero-run parity at the low-to-high reading frontier for n and
    # n+2^r; addition carry. A completed zero run of odd length rejects.
    states = {(0, 0, 0): 1}
    for i in range(m):
        new = defaultdict(int)
        for (p, q, carry), count in states.items():
            for x in (0, 1):
                summand = x + int(i == r) + carry
                y, carry2 = summand & 1, summand >> 1
                if (x and p) or (y and q):
                    continue
                new_p = 0 if x else 1 - p
                new_q = 0 if y else 1 - q
                new[(new_p, new_q, carry2)] += count
        states = new
    # Remaining zero runs are leading padding and are disregarded.
    return sum(count for (p, q, carry), count in states.items() if carry == 0)


def verify():
    fibonacci = [0, 1]
    for _ in range(90):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    for m in range(1, 61):
        for r in range(m):
            expected = fibonacci[r + 1] * ((m - r + 1) // 2)
            actual = pair_count(m, r)
            assert actual == expected, (m, r, actual, expected)
    print('CARRY_DP_OK: 1830 independently computed cells, 1<=m<=60')

if __name__ == '__main__':
    verify()
