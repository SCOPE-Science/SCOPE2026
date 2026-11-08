#!/usr/bin/env python3
"""Exact closed-neighborhood parity enumeration by binary row reduction."""
from collections import Counter


def expected(n):
    if n % 5:
        return {n: (2 if n % 2 else 4)}
    if n % 2:
        return {3*n//5: 10, n: 12, 7*n//5: 10}
    return {3*n//5: 10, n: 44, 7*n//5: 10}


def direct_solutions(n):
    m = 2*n
    rows = []
    for i in range(n):
        row = 0
        for v in [i, (i-1) % n, (i+1) % n, n+i]:
            row ^= 1 << v
        rows.append(row | (1 << m))
    for i in range(n):
        row = 0
        for v in [n+i, n+(i-2) % n, n+(i+2) % n, i]:
            row ^= 1 << v
        rows.append(row | (1 << m))
    pivots = []
    rank = 0
    for col in range(m):
        found = next((j for j in range(rank, m) if (rows[j] >> col) & 1), None)
        if found is None:
            continue
        rows[rank], rows[found] = rows[found], rows[rank]
        for j in range(m):
            if j != rank and ((rows[j] >> col) & 1):
                rows[j] ^= rows[rank]
        pivots.append(col)
        rank += 1
    for r in rows[rank:]:
        assert r == 0, 'system inconsistent'
    free = [i for i in range(m) if i not in set(pivots)]
    out = Counter()
    for mask in range(1 << len(free)):
        state = sum(((mask >> j) & 1) << col for j, col in enumerate(free))
        for j, col in enumerate(pivots):
            rhs = (rows[j] >> m) & 1
            parity = (rows[j] & state).bit_count() % 2
            if rhs ^ parity:
                state |= 1 << col
        for row in rows:
            assert ((row & state).bit_count() ^ ((row >> m) & 1)) % 2 == 0
        out[state.bit_count()] += 1
    return dict(out), len(free)


if __name__ == '__main__':
    for n in range(5, 61):
        actual, nullity = direct_solutions(n)
        assert actual == expected(n), (n, actual, expected(n))
        target_nullity = 1 if n % 2 else 2
        if n % 5 == 0:
            target_nullity = 5 if n % 2 else 6
        assert nullity == target_nullity, (n, nullity)
        if n in (5, 6, 7, 10, 15, 20, 25, 30, 60):
            print('matrix', n, 'kernel_dimension', nullity, 'weight_counts', sorted(actual.items()))
    print('DIRECT_GF2_MATRIX_PASS_n5_to60')
