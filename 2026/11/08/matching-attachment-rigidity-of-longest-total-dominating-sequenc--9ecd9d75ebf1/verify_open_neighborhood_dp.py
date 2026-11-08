#!/usr/bin/env python3
"""Exact dynamic programming using open-neighborhood masks in triangular graphs."""
from functools import lru_cache
from itertools import combinations
from math import factorial


def solve(n):
    edges = list(combinations(range(n), 2))
    neighborhoods = [sum(1 << j for j, f in enumerate(edges)
                         if f != e and (set(e) & set(f)))
                     for e in edges]
    full = (1 << len(edges)) - 1

    @lru_cache(None)
    def dp(covered):
        if covered == full:
            return (0, 1)
        best = -1
        number = 0
        for mask in neighborhoods:
            if mask & ~covered:
                length, ways = dp(covered | mask)
                length += 1
                if length > best:
                    best, number = length, ways
                elif length == best:
                    number += ways
        assert best >= 0
        return best, number

    return dp(0), dp.cache_info().currsize


def main():
    for n in range(3, 12):
        (length, count), states = solve(n)
        expected_length = n - 1 if n % 2 else n - 2
        assert length == expected_length, (n, length, expected_length)
        if n % 2:
            expected_count = factorial(n) * factorial(n - 1) // (2 ** ((n - 1) // 2))
            assert count == expected_count, (n, count, expected_count)
        print(f'n={n}; max_length={length}; maximum_ordered_sequences={count}; DP_states={states}')
    print('PASS: exact open-neighborhood recursion')


if __name__ == '__main__':
    main()
