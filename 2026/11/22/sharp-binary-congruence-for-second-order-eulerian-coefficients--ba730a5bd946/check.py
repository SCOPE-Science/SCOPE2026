#!/usr/bin/env python3
"""Exact finite diagnostics for the dyadic second-order Eulerian theorem.

The infinite statement is proved in RESULT.md; this checker probes mistakes in
boundary conventions, indexing, normalization, and binomial parity.
Python 3 standard library only. Run: python3 check.py
"""
from math import comb

MAX_N = 360
checks = 0
rows = [[1]]
for n in range(1, MAX_N + 1):
    prev = rows[-1]
    row = [0] * n
    for k in range(n):
        row[k] = (k + 1) * (prev[k] if k < len(prev) else 0) + (
            2 * n - k - 1
        ) * (prev[k - 1] if k else 0)
    rows.append(row)
    assert sum(row) == (1 if n == 1 else (2 * n - 1) * sum(prev))
    checks += 1

# Independent small-n enumeration by insertion of adjacent maximum pairs.
words = [()]
for n in range(1, 7):
    words = [w[:i] + (n, n) + w[i:] for w in words for i in range(len(w) + 1)]
    hist = [0] * n
    for w in words:
        # Count ascents with first entry compared to zero.
        asc = sum(1 for i in range(1, len(w)) if w[i - 1] < w[i])
        hist[asc] += 1
    assert hist == rows[n]
    checks += n

first = {}
for n, row in enumerate(rows):
    for k, value in enumerate(row):
        c = (k + 1) // 2
        mod = 1 << c
        assert value % mod == 0, (n, k, value, mod)
        checks += 1
        upper = n - c
        expected = (comb(upper, k) & 1) if upper >= k else 0
        actual = (value // mod) & 1
        assert actual == expected, (n, k, actual, expected)
        checks += 1
        if actual and k not in first:
            first[k] = n
        # A literal Lucas bit test, independently of Python's binomial.
        if k:
            bit = int((upper & k) == k) if upper >= 0 else 0
            assert expected == bit, (n, k, expected, bit)
            checks += 1

for k in range(1, (MAX_N * 2) // 3):
    if ((3*k + 1)//2) <= MAX_N and ((3*k + 1)//2) >= k + 1:
        assert first.get(k) == (3*k + 1)//2, (k, first.get(k))
        checks += 1

for k in range(1, 90):
    r = k.bit_length()
    modulus = 1 << r
    residues = [t for t in range(modulus) if t & k == k]
    assert len(residues) == 1 << (r - k.bit_count())
    checks += 1
    # Every positive period of a length-2^r binary word divides a power of 2.
    assert any(((t + (modulus >> 1)) % modulus) & k != k for t in residues)
    checks += 1

print("PASS", checks, "exact assertions; N=", MAX_N)
