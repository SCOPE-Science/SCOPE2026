#!/usr/bin/env python3
"""Exact finite checks of ternary fibers for the fifth binomial polynomial."""
from collections import Counter
from math import comb


def critical_index(branch, levels):
    # The numerator of the derivative of binom(branch+3t,5)/3,
    # multiplied by the 3-adic unit 40.
    assert branch in (0, 1)
    def derivative(t):
        if branch == 0:
            return 135*t**4 - 360*t**3 + 315*t**2 - 100*t + 8
        return 135*t**4 - 180*t**3 + 45*t**2 + 10*t - 2
    t, modulus = 2, 3
    assert derivative(t) % 3 == 0
    for _ in range(1, levels):
        roots = [t + j*modulus for j in range(3)
                 if derivative(t + j*modulus) % (3*modulus) == 0]
        assert len(roots) == 1
        t = roots[0]
        modulus *= 3
    return t


def branch_value(branch, t, modulus):
    if branch == 0:
        numerator = 3*t*(t-1)*(3*t-4)*(3*t-2)*(3*t-1)
    elif branch == 1:
        numerator = 3*t*(t-1)*(3*t-2)*(3*t-1)*(3*t+1)
    else:
        numerator = t*(3*t-2)*(3*t-1)*(3*t+1)*(3*t+2)
    return numerator * pow(40, -1, modulus) % modulus


def square_roots_count(z, m):
    if m == 0:
        return 1
    z %= 3**m
    if z == 0:
        return 3**(m//2)
    v = 0
    while z % 3 == 0:
        v += 1
        z //= 3
    return 0 if v % 2 or z % 3 == 2 else 2*3**(v//2)


def squares_count(m):
    return 1 + sum(3**(m-2*j-1) for j in range((m+1)//2))


def predicted(k, y, beta0, beta1):
    if y % 3:
        return 1
    return 1 + 3*(square_roots_count((y-beta0)//3, k-1)
                  + square_roots_count((beta1-y)//3, k-1))


def check(max_k=10):
    for m in range(0, 7):
        mod = 3**m
        counts = Counter((t*t) % mod for t in range(mod))
        assert len(counts) == squares_count(m)
        assert all(square_roots_count(z, m) == counts.get(z, 0)
                   for z in range(mod))
    checked = 0
    for k in range(1, max_k+1):
        mod = 3**k
        beta0 = branch_value(0, critical_index(0,k), mod)
        beta1 = branch_value(1, critical_index(1,k), mod)
        assert beta0 % 3 == beta1 % 3 == 0
        if k >= 2:
            assert (beta0 % 9, beta1 % 9) == (6, 3)
        counts = [0]*mod
        for n in range(3*mod):
            counts[comb(n, 5) % mod if n >= 5 else 0] += 1
        for y in range(mod):
            actual = counts[y]
            formula = predicted(k, y, beta0, beta1)
            assert actual == formula, (k,y,actual,formula)
        assert sum(counts) == 3*mod
        if k >= 3:
            unique = 3**k - 3**(k-2) - 2*squares_count(k-3)
            assert counts.count(1) == unique
        maximum = 7 if k == 1 else 13 if k in (2,3) else (
            1 + 2*3**(k//2) if k % 2 == 0 else 1 + 3**((k+1)//2))
        assert max(counts) == maximum
        if k >= 4:
            assert counts.count(maximum) == 2
        print(f'k={k}, targets={mod}, max={maximum}, '
              f'fiber_histogram={sorted(Counter(counts).items())}')
        checked += mod
    print('PASS:', checked, 'target congruences checked exhaustively;',
          sum(3**(k+1) for k in range(1,max_k+1)),
          'integer indices in their full periods')


if __name__ == '__main__':
    check()
