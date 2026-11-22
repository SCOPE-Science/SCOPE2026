#!/usr/bin/env python3
"""Finite checks of permutation-diagram external-neighbourhood classification.

All computations use exact integer bitmasks. These tests supplement the proof;
no finite search is used as a proof of the result for arbitrary lengths.
"""
from itertools import permutations


def traces(p):
    n = len(p)
    top = [(1 << i) - 1 for i in range(n + 1)]
    bottom = [0]
    inverse = [0] * n
    for index, rank in enumerate(p):
        inverse[rank] = index
    for index in inverse:
        bottom.append(bottom[-1] | (1 << index))
    return {a ^ b for a in top for b in bottom}


def simple(p):
    n = len(p)
    return all(
        max(p[i:j]) - min(p[i:j]) + 1 != j - i
        for i in range(n)
        for j in range(i + 2, n + 1)
        if j - i < n
    )


def extremal_examples(n):
    if n == 4:
        return (1, 3, 0, 2)
    if n % 2 == 0:
        k = n // 2
        return tuple(list(range(1, n, 2)) + list(range(0, n, 2)))
    k = n // 2
    return tuple(list(range(1, n - 1, 2)) + list(range(0, n - 4, 2)) + [n - 1, n - 3])


def direct_crossing(p, a, b):
    return sum(
        1 << index
        for index, rank in enumerate(p)
        if (index < a) != (rank < b)
    )


def run():
    max_sizes = [2, 4, 8, 15, 24, 35, 48, 63]
    max_counts = [1, 2, 4, 2, 6, 46, 338, 2926]
    for n in range(1, 9):
        best = 0
        best_count = 0
        best_nonsimple = 0
        for p in permutations(range(n)):
            vals = traces(p)
            z = len(vals)
            if n <= 4:
                all_direct = {
                    direct_crossing(p, a, b)
                    for a in range(n + 1)
                    for b in range(n + 1)
                }
                assert all_direct == vals, (n, p)
            if z > best:
                best = z
                best_count = 0
            if z == best:
                best_count += 1
            if n >= 4:
                assert (z == n * n - 1) == simple(p), (n, p, z)
                if not simple(p):
                    best_nonsimple = max(best_nonsimple, z)
        assert best == max_sizes[n-1], (n, best)
        assert best_count == max_counts[n-1], (n, best_count)
        if n >= 4:
            assert best_nonsimple == n*n-2, (n, best_nonsimple)
        print('n=%d max=%d maximizers=%d nonsimple_max=%s' %
              (n, best, best_count, best_nonsimple if n >= 4 else '-'))
    for n in range(4, 31):
        p = extremal_examples(n)
        assert tuple(sorted(p)) == tuple(range(n)), (n, p)
        assert simple(p), (n, p)
        assert len(traces(p)) == n*n-1, (n, p)
    for n in range(5, 31):
        p = (0,) + tuple(x+1 for x in extremal_examples(n-1))
        assert not simple(p)
        assert len(traces(p)) == n*n-2, (n,p)
    assert len(traces((0,2,3,1))) == 14
    print('VERIFY_OK: exhaustive lengths 1..8, constructive families 4..30')


if __name__ == '__main__':
    run()
