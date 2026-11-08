#!/usr/bin/env python3
"""Finite independent checks of the Dyck up-step shattering theorem.

All computations use the standard Python library; tests are finite corroboration,
not a substitute for the general combinatorial proof.
"""
from itertools import combinations
from math import comb


def bases(n):
    for c in combinations(range(2 * n), n):
        b = sum(1 << x for x in c)
        height = 0
        for p in range(2 * n):
            height += 1 if (b >> p) & 1 else -1
            if height < 0:
                break
        else:
            yield b


def corridor_condition(n, subset):
    N = n - 1
    k = subset.bit_count()
    if subset & (1 | (1 << (2 * n - 1))):
        return False
    d = N - k
    if d < 0:
        return False
    h = 0
    for i in range(1, N + 1):
        # Positions (2i, 2i+1) in one-based notation.
        selected = (subset >> (2 * i - 1)) & 3
        h += 1 - selected.bit_count()
        if h < 0 or h > d:
            return False
    return h == d


def mat_count(n, k):
    N = n - 1
    d = N - k
    if d < 0:
        return 0
    row = [0] * (d + 1)
    row[0] = 1
    for _ in range(N):
        nxt = [0] * (d + 1)
        for h, value in enumerate(row):
            nxt[h] += 2 * value
            if h > 0:
                nxt[h - 1] += value
            if h < d:
                nxt[h + 1] += value
        row = nxt
    return row[d]


def direct_shattered(bases_list, support):
    positions = [i for i in range(support.bit_length()) if (support >> i) & 1]
    traces = set()
    for b in bases_list:
        t = 0
        for j, p in enumerate(positions):
            if (b >> p) & 1:
                t |= 1 << j
        traces.add(t)
        if len(traces) == 1 << len(positions):
            return True
    return False


def run():
    for n in range(1, 8):
        bl = list(bases(n))
        assert len(bl) == comb(2 * n, n) // (n + 1), (n, len(bl))
        numbers = [0] * (n + 1)
        for mask in range(1 << (2 * n - 2)):
            support = mask << 1
            cond = corridor_condition(n, support)
            actual = direct_shattered(bl, support)
            assert cond == actual, (n, support, cond, actual)
            if actual:
                numbers[mask.bit_count()] += 1
        computed = [mat_count(n, k) for k in range(n)]
        assert numbers[:n] == computed and numbers[n] == 0, (n, numbers, computed)
        assert computed[-1] == 2 ** (n - 1)
        if n >= 2:
            assert computed[-2] == (3 ** (n - 1) - 1) // 2
        print('n=', n, 'Dyck_bases=', len(bl), 'shattered_coefficients=', computed)
    for n in range(8, 25):
        assert mat_count(n, n-1) == 2 ** (n-1)
        assert mat_count(n, n-2) == (3 ** (n-1) - 1)//2
        assert mat_count(n, 0) == 1
    print('CATALAN_SHATTERING_CORRIDOR_PASS')

if __name__ == '__main__':
    run()
