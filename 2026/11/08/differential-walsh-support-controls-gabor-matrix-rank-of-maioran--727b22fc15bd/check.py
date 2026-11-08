#!/usr/bin/env python3
"""Exact arithmetic checks for differential-Walsh Gabor ranks of Boolean graphs.

All transforms are integral and use the counting (unnormalized) convention.
"""
import random


def walsh(values):
    a = list(values)
    n = len(a)
    step = 1
    while step < n:
        for k in range(0, n, 2 * step):
            for j in range(k, k + step):
                u, v = a[j], a[j + step]
                a[j], a[j + step] = u + v, u - v
        step *= 2
    return a


def count_nonzero(a):
    return sum(x != 0 for x in a)


def h_value(table, y):
    return (table >> y) & 1


def graph_values(m, table):
    L = 1 << m
    g = [0] * (2 * L * L)
    for x in range(L):
        for y in range(L):
            z = ((x & y).bit_count() & 1) ^ h_value(table, y)
            g[x | (y << m) | (z << (2 * m))] = 1
    return g


def predicted(m, table):
    L = 1 << m
    D = L * L
    derivative_surplus = 0
    for v in range(1, L):
        derivative_sign = [1 - 2 * (h_value(table, y) ^ h_value(table, y ^ v)) for y in range(L)]
        s = count_nonzero(walsh(derivative_sign))
        derivative_surplus += s - 1
    return D * D + 4 * D - 3 + (2 * L) * derivative_surplus


def measured(m, table):
    g = graph_values(m, table)
    N = len(g)
    outputs = 0
    for a in range(N):
        overlap = [g[x] * g[x ^ a] for x in range(N)]
        outputs += count_nonzero(walsh(overlap))
    return outputs


def cubic_table(m):
    return sum(1 << y for y in range(1 << m) if (y & 7) == 7)


def check(m, table):
    actual = measured(m, table)
    expected = predicted(m, table)
    assert actual == expected, (m, table, actual, expected)
    return actual


def main():
    runs = 0
    for m in (1, 2):
        for table in range(1 << (1 << m)):
            check(m, table)
            runs += 1
    # Full census of all 3-variable Boolean perturbations, not extrapolation.
    for table in range(1 << 8):
        check(3, table)
        runs += 1
    assert check(3, 0) == 4349
    assert check(3, cubic_table(3)) == 4685
    assert check(4, cubic_table(4)) == 67901
    assert check(4, 0) == 66557
    runs += 4
    rng = random.Random(7052026)
    for _ in range(12):
        check(4, rng.getrandbits(16))
        runs += 1
    print('DIFFERENTIAL_WALSH_GABOR_CHECKS_OK', 'cases=', runs)


if __name__ == '__main__':
    main()
