#!/usr/bin/env python3
"""Standalone graph and exact-arithmetic verification of a rook-graph census.

Requires Python 3.9+ standard library only. Finite checks supplement, not
replace, the structural proof of the infinite family.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import comb


def bounded_matrices(rows, column_sums, target_rows):
    """Count 0/1 incidence matrices with the specified *labeled* degrees."""
    column_sums = tuple(column_sums)
    target_rows = tuple(target_rows)

    @lru_cache(None)
    def solve(column, degrees):
        if column == len(column_sums):
            return int(degrees == target_rows)
        result = 0
        for chosen in combinations(range(rows), column_sums[column]):
            nxt = list(degrees)
            for i in chosen:
                nxt[i] += 1
            if all(nxt[i] <= target_rows[i] for i in chosen):
                result += solve(column + 1, tuple(nxt))
        return result

    return solve(0, (0,) * rows)


def regular(n):
    return 0 if n < 3 else bounded_matrices(n, (3,) * n, (3,) * n)


def two_deficits(n):
    return 0 if n < 3 else bounded_matrices(
        n, (2,) + (3,) * (n - 1), (2,) + (3,) * (n - 1)
    )


def saturated_rows(m, n):
    """Labeled m-by-n 0/1 matrices with row sums three, col sums at most three."""
    @lru_cache(None)
    def solve(j, degrees):
        if j == n:
            return int(degrees == (3,) * m)
        result = 0
        for k in range(4):
            for chosen in combinations(range(m), k):
                nxt = list(degrees)
                for i in chosen:
                    nxt[i] += 1
                if max(nxt) <= 3:
                    result += solve(j + 1, tuple(nxt))
        return result

    return solve(0, (0,) * m)


def predicted(m, n):
    assert 3 <= m <= n
    if m < n:
        result = Counter({3 * m: saturated_rows(m, n)})
        if n == m + 1 and m >= 4:
            result[3 * m - 1] += m * comb(n, 2) * regular(m - 1)
        return +result
    return +Counter({
        3 * n - 2: n * n * regular(n - 1) + comb(n, 2)**2 * regular(n - 2),
        3 * n - 1: n * n * (n - 1)**2 * two_deficits(n - 1),
        3 * n: regular(n),
    })


def direct(m, n):
    """Independently enumerate every subset, test each possible extension."""
    output = Counter()
    count = 0
    for mask in range(1 << (m * n)):
        row = [0] * m
        col = [0] * n
        for i in range(m):
            bits = (mask >> (n * i)) & ((1 << n) - 1)
            row[i] = bits.bit_count()
            for j in range(n):
                col[j] += (bits >> j) & 1
        if max(row) > 3 or max(col) > 3:
            continue
        if any(row[i] < 3 and col[j] < 3 and not (mask >> (i*n+j)) & 1
               for i in range(m) for j in range(n)):
            continue
        output[mask.bit_count()] += 1
        count += 1
    return +output, count


def has_three_coloring(m, n, mask):
    """Proper vertex-coloring of the induced rook graph, without degree shortcut."""
    chosen = [a for a in range(m * n) if (mask >> a) & 1]
    size = len(chosen)
    neighbours = [set() for _ in range(size)]
    for i in range(size):
        for j in range(i+1, size):
            a, b = chosen[i], chosen[j]
            if a//n == b//n or a%n == b%n:
                neighbours[i].add(j)
                neighbours[j].add(i)
    colors = [-1] * size

    def dfs(remaining):
        if remaining == 0:
            return True
        uncolored = [i for i in range(size) if colors[i] < 0]
        v = max(uncolored, key=lambda x: (
            len({colors[u] for u in neighbours[x] if colors[u] >= 0}),
            len(neighbours[x])
        ))
        forbidden = {colors[u] for u in neighbours[v] if colors[u] >= 0}
        for color in range(3):
            if color not in forbidden:
                colors[v] = color
                if dfs(remaining - 1):
                    return True
                colors[v] = -1
        return False

    return dfs(size)


def direct_graph_check(m, n):
    graph_max = Counter()
    matrix_max = Counter()
    for mask in range(1 << (m * n)):
        row = [0] * m
        col = [0] * n
        for i in range(m):
            for j in range(n):
                if (mask >> (i*n+j)) & 1:
                    row[i] += 1
                    col[j] += 1
        degree_ok = max(row) <= 3 and max(col) <= 3
        colored = has_three_coloring(m, n, mask)
        assert degree_ok == colored, (m, n, mask, degree_ok, colored)
        if not colored:
            continue
        eligible = [a for a in range(m*n) if not (mask >> a)&1]
        gmax = not any(has_three_coloring(m, n, mask | (1 << a)) for a in eligible)
        mmax = not any(row[a//n] < 3 and col[a%n] < 3 for a in eligible)
        assert gmax == mmax, (m,n,mask)
        if gmax: graph_max[mask.bit_count()] += 1
        if mmax: matrix_max[mask.bit_count()] += 1
    assert graph_max == matrix_max == predicted(m,n)
    return graph_max


def main():
    cases = [(3,3),(3,4),(3,5),(3,6),(4,4),(4,5)]
    candidates = 0
    for m,n in cases:
        a, count = direct(m,n)
        b = predicted(m,n)
        assert a == b, (m,n,a,b)
        candidates += 1 << (m*n)
    for m,n in [(3,3),(3,4)]:
        direct_graph_check(m,n)
    assert [regular(n) for n in range(3,8)] == [1,24,2040,297200,68938800]
    assert [two_deficits(n) for n in range(3,7)] == [1,27,1656,190000]
    assert predicted(4,4) == {10:16,11:144,12:24}
    assert predicted(4,5) == {11:40,12:4320}
    assert predicted(5,5) == {13:700,14:10800,15:2040}
    print('VERIFY_OK graph_colorings=3x3,3x4 exhaustive_degree_enumeration_cases=6'
          f' total_candidate_subsets={candidates} exact_margin_counts=PASS')


if __name__ == '__main__':
    main()
