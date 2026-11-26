#!/usr/bin/env python3
"""Independent subset enumeration for minimal total domination in rook graphs.

Usage: python3 verify.py
Uses standard-library integer bitmasks and no external libraries.
"""
from collections import Counter
from math import comb, factorial


def predicted(n):
    out = Counter()
    out[3] += n
    out[4] += 3 * n * n * (n-1) // 2
    if n >= 6:
        out[6] += factorial(n) // (8 * factorial(n-6))
    out[n] += 3 * (2**n - 2*n - 1)
    if n == 3:
        out[4] += 18
    return {k: v for k, v in out.items() if v}


def brute(n):
    width = 3
    num = width * n
    nbrs = []
    for i in range(width):
        for j in range(n):
            mask = 0
            for h in range(width):
                for k in range(n):
                    if ((i == h) or (j == k)) and (i, j) != (h, k):
                        mask |= 1 << (h*n+k)
            nbrs.append(mask)
    result = Counter()
    for selected in range(1, 1 << num):
        privates = 0
        for neighbors in nbrs:
            dom = neighbors & selected
            if not dom:
                break
            if dom & (dom-1) == 0:
                privates |= dom
        else:
            if privates & selected == selected:
                result[selected.bit_count()] += 1
    return dict(result)


def main():
    checked = 0
    for n in range(3, 8):
        got = brute(n)
        expect = predicted(n)
        assert got == expect, (n, got, expect)
        checked += (1 << (3*n)) - 1
        print(f'n={n}: {got}')
    print(f'VERIFY_OK cases=5 tested_subsets={checked}')

if __name__ == '__main__':
    main()
