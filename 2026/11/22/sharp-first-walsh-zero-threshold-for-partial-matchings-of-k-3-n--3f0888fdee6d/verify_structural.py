#!/usr/bin/env python3
"""Independent direct signed-rook computation, without a Walsh transform."""
from itertools import combinations
from math import comb


def total(n):
    return sum(comb(3, j)*comb(n, j)*__import__('math').factorial(j) for j in range(4) if j <= n)


def matching_sum(n, negative_edges):
    """Assign a distinct column to each occupied row; exact signed sum."""
    acc = 0
    for chosen_rows_size in range(4):
        for rows in combinations(range(3), chosen_rows_size):
            def rec(t, used, parity):
                if t == len(rows):
                    return -1 if parity else 1
                row = rows[t]
                ans = 0
                for col in range(n):
                    if col not in used:
                        ans += rec(t+1, used | {col}, parity ^ ((row,col) in negative_edges))
                return ans
            acc += rec(0, set(), False)
    return acc


def check():
    for n in range(3, 24):
        assert total(n) == n**3+2*n+1
        q = 1 + 2*(n-1) + (n-1)*(n-2)
        assert q == n*n-n+1
        if n % 2 == 0:
            assert total(n) % 2 == 1
            continue
        r = (n + 1)//2
        assert total(n)-2*r*q == 2*n
        for heavy in range(3):
            selected = tuple(range(r))
            star = {(heavy,c) for c in selected}
            assert matching_sum(n,star) == 2*n
            other = (heavy+1) % 3
            assert matching_sum(n,star | {(other,selected[-1])}) == 0
    print('VERIFY_STRUCTURAL_OK')

if __name__ == '__main__':
    check()
