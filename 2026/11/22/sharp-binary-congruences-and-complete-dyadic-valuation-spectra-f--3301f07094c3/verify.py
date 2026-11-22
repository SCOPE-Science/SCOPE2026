#!/usr/bin/env python3
"""Finite diagnostics for the sharp binary congruence of type-B Eulerian rows.

Run with Python 3 (standard library only). The mathematical theorem is
proved independently of these finite checks.
"""
from math import comb
from collections import Counter


def v2(x):
    assert x != 0
    return (abs(x) & -abs(x)).bit_length() - 1


def row_step(prev, n):
    return [
        (2 * k + 1) * (prev[k] if k < len(prev) else 0)
        + (2 * n - 2 * k + 1) * (prev[k - 1] if k else 0)
        for k in range(n + 1)
    ]


def explicit(n, k):
    return sum((-1)**(k-j)*comb(n+1, k-j)*(2*j+1)**n
               for j in range(k+1))


def main():
    tests = 0
    row = [1]
    for n in range(1, 513):
        row = row_step(row, n)
        assert row[0] == row[-1] == 1; tests += 1
        if n <= 32:
            for k in range(n+1):
                assert row[k] == explicit(n, k); tests += 1
        if n >= 2:
            q = 1 << (1 + v2(n*(n-1)))
            for k, val in enumerate(row):
                assert (val - comb(n, k)) % q == 0
                tests += 1
            assert v2(row[1]-n) == 1+v2(n*(n-1)); tests += 1
        if n & (n-1) == 0 and n >= 2:
            r = n.bit_length()-1
            observed = Counter()
            for k in range(1,n):
                val = v2(row[k]); assert val == r-v2(k)
                observed[val] += 1; tests += 1
            for j in range(1,r+1):
                assert observed[j] == 1 << (j-1); tests += 1
    print(f"PASS {tests} exact assertions; rows 1..512, independent finite formulas through 32")


if __name__ == '__main__':
    main()
