#!/usr/bin/env python3
"""Exact finite checks for Walsh multipliers of partial bipartite matchings."""
from itertools import combinations
from math import comb


def matchings(n):
    def extend(row, taken, mask):
        if row == 3:
            yield mask
            return
        yield from extend(row + 1, taken, mask)
        for col in range(n):
            if not ((taken >> col) & 1):
                yield from extend(row + 1, taken | (1 << col), mask | (1 << (row * n + col)))
    yield from extend(0, 0, 0)


def walsh_transform(values):
    jump = 1
    while jump < len(values):
        for off in range(0, len(values), 2 * jump):
            for j in range(off, off + jump):
                a, b = values[j], values[j + jump]
                values[j], values[j + jump] = a + b, a - b
        jump *= 2
    return values


def check(n):
    space = [0] * (1 << (3 * n))
    configurations = list(matchings(n))
    for m in configurations:
        space[m] = 1
    assert len(configurations) == n**3 + 2*n + 1
    w = walsh_transform(space)
    if n % 2 == 0:
        assert all(value % 2 for value in w)
        print(f'n={n}, count={len(configurations)}, zero=0')
        return
    r = (n + 1) // 2
    assert all(value >= 2*n for mask, value in enumerate(w) if mask.bit_count() <= r)
    first = sum(value == 0 and mask.bit_count() == r + 1 for mask, value in enumerate(w))
    assert first > 0
    for heavy in range(3):
        for columns in combinations(range(n), r):
            mask = sum(1 << (heavy * n + col) for col in columns)
            assert w[mask] == 2*n
            for other in range(3):
                if other == heavy:
                    continue
                for col in columns:
                    assert w[mask | (1 << (other*n+col))] == 0
    assert first >= 6*r*comb(n,r)
    print(f'n={n}, count={len(configurations)}, first-zero-degree={r+1}, first-zero-modes={first}, constructed={6*r*comb(n,r)}')

if __name__ == '__main__':
    for n in (3, 4, 5, 6, 7):
        check(n)
    print('VERIFY_WALSH_OK')
