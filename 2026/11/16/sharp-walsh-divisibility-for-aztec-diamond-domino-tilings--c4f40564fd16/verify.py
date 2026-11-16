#!/usr/bin/env python3
"""Exact finite checks for signed Aztec-diamond domino sums.

Run with Python 3.10+; no third-party modules are required.
The all-order assertion rests on the proof, not these finite checks.
"""
from collections import Counter
from functools import lru_cache
from math import gcd


def coordinates(n):
    rows = [(j, k) for j in range(n) for k in range(n + 1)]
    cols = [(p, q) for p in range(n + 1) for q in range(n)]
    return rows, cols


def adjacent(w, b):
    j, k = w
    p, q = b
    return p in (j, j + 1) and k in (q, q + 1)


def rank_mod_two(rows, width):
    arr = list(rows)
    rank = 0
    for bit in range(width):
        pivot = next((i for i in range(rank, len(arr))
                      if (arr[i] >> bit) & 1), None)
        if pivot is None:
            continue
        arr[rank], arr[pivot] = arr[pivot], arr[rank]
        for i in range(rank + 1, len(arr)):
            if (arr[i] >> bit) & 1:
                arr[i] ^= arr[rank]
        rank += 1
    return rank


def matrix_check(n):
    rows, cols = coordinates(n)
    full = [sum((1 << i) for i, b in enumerate(cols) if adjacent(w, b))
            for w in rows]
    assert rank_mod_two(full, len(cols)) == n * n
    excluded_rows = {(j, j) for j in range(n)}
    excluded_cols = {(j, j) for j in range(n)}
    keep_r = [r for r in rows if r not in excluded_rows]
    keep_c = [c for c in cols if c not in excluded_cols]
    sub = [sum((1 << i) for i, b in enumerate(keep_c)
               if adjacent(w, b)) for w in keep_r]
    assert len(sub) == n*n and rank_mod_two(sub, len(keep_c)) == n*n


def diagonal_signed_sums(n):
    rows, cols = coordinates(n)
    m = len(rows)
    ci = {c: i for i, c in enumerate(cols)}
    options = []
    for j, k in rows:
        allowed = []
        for p in (j, j + 1):
            for q in (k - 1, k):
                if (p, q) in ci:
                    mark = (1 << j) if j == k == p == q else 0
                    allowed.append((ci[(p, q)], mark))
        options.append(allowed)

    @lru_cache(maxsize=None)
    def count(i, used):
        if i == m:
            return ((0, 1),)
        out = Counter()
        for col, mark in options[i]:
            if not ((used >> col) & 1):
                for mask, count_ in count(i + 1, used | (1 << col)):
                    out[mask ^ mark] += count_
        return tuple(sorted(out.items()))

    counts = dict(count(0, 0))
    assert sum(counts.values()) == 1 << (n * (n + 1) // 2)
    vals = [sum(number * (-1 if ((mask & flips).bit_count() & 1) else 1)
                for mask, number in counts.items())
            for flips in range(1 << n)]
    assert all(v % (1 << n) == 0 for v in vals)
    assert gcd(*vals) == (1 << n)
    assert sum((v // (1 << n)) & 1 for v in vals) % 2 == 1
    return vals


def determinant_bareiss(mat):
    a = [list(row) for row in mat]
    size = len(a)
    prev = 1
    sign = 1
    for k in range(size - 1):
        if a[k][k] == 0:
            pivot = next((r for r in range(k + 1, size) if a[r][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        q = a[k][k]
        for i in range(k + 1, size):
            for j in range(k + 1, size):
                num = a[i][j] * q - a[i][k] * a[k][j]
                assert num % prev == 0
                a[i][j] = num // prev
            a[i][k] = 0
        prev = q
    return sign * a[-1][-1]


def determinant_check(n, vals):
    rows, cols = coordinates(n)
    for flips in range(1 << n):
        matrix = []
        for j, k in rows:
            r = []
            for p, q in cols:
                s = int(adjacent((j, k), (p, q)))
                if s and p == j + 1 and q == k:
                    s = -s  # one negative edge direction per bounded face
                if s and j == k == p == q and ((flips >> j) & 1):
                    s = -s
                r.append(s)
            matrix.append(r)
        assert abs(determinant_bareiss(matrix)) == abs(vals[flips])


def main():
    for n in range(1, 13):
        matrix_check(n)
    for n in range(1, 6):
        vals = diagonal_signed_sums(n)
        if n <= 4:
            determinant_check(n, vals)
        print(f'n={n}: {1 << (n*(n+1)//2)} tilings; '
              f'{1 << n} controlled signings; gcd={gcd(*vals)}; '
              f'sharp signings={sum((v//(1<<n))&1 for v in vals)}')
    print('AZTEC_SIGNED_WALSH_GCD_PASS ranks_n=1..12 direct_sums_n=1..5 determinants_n=1..4')


if __name__ == '__main__':
    main()
