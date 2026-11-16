#!/usr/bin/env python3
"""Exact finite tests for semicircle-cut statistics of uniform pairings.

Execute: python3 verify.py. Requires only the Python standard library.
"""
from fractions import Fraction as Q
import math


def pairings(v):
    if not v:
        yield ()
    else:
        x = v[0]
        for j in range(1, len(v)):
            y = v[j]
            for rest in pairings(v[1:j] + v[j + 1:]):
                yield ((x, y),) + rest


def exact_enumeration(m):
    n = 2 * m
    count = 0
    sums = [0] * m
    products = [[0] * m for _ in range(m)]
    arcs = [{(i + t) % n for t in range(m)} for i in range(m)]
    for matching in pairings(tuple(range(n))):
        counts = [sum((u in arcs[i]) != (v in arcs[i]) for u, v in matching)
                  for i in range(m)]
        count += 1
        for i in range(m):
            sums[i] += counts[i]
            for j in range(m):
                products[i][j] += counts[i] * counts[j]
    assert count == math.prod(range(1, n, 2))
    gamma = Q(n - 2, (n - 1) * (n - 3))
    for i in range(m):
        assert Q(sums[i], count) == Q(m * m, n - 1)
        for j in range(m):
            d = abs(i - j)
            observed = Q(products[i][j], count) - Q(sums[i] * sums[j], count**2)
            expected = gamma * (d**2 + (m-d)**2 - Q(m**3, n - 1))
            assert observed == expected, (m, i, j, observed, expected)
    return count * m * m


def exact_precision(m):
    gamma = Q(2*m - 2, (2*m - 1)*(2*m - 3))
    h = Q((m-1)*(m*m-m+1), 3*(2*m-1))
    K = [[gamma*(abs(i-j)**2 + (m-abs(i-j))**2 - Q(m**3, 2*m-1))
          for j in range(m)] for i in range(m)]
    # m=2 is a cycle with two parallel directed cycle edges.
    L = [[2*(i==j) - int((i-j) % m == 1) - int((j-i) % m == 1)
          for j in range(m)] for i in range(m)]
    if m == 2:
        L = [[2, -2], [-2, 2]]
    inv = [[Q(L[i][j], 1)/(4*gamma*m) + Q(1, m)/(gamma*m*h)
            for j in range(m)] for i in range(m)]
    for i in range(m):
        for j in range(m):
            value = sum(K[i][k] * inv[k][j] for k in range(m))
            assert value == int(i == j), (m, i, j, value)
    return m*m


def finite_modes(m):
    h = (m-1)*(m*m-m+1)/(3*(2*m-1))
    modes = [h] + [1/math.sin(math.pi*j/m)**2 for j in range(1, m)]
    maximum = max(range(m), key=lambda j: modes[j])
    minimum = min(range(m), key=lambda j: modes[j])
    assert (maximum == 0) == (m >= 5), (m, maximum)
    assert (minimum == 0) == (m <= 3), (m, minimum)
    if m >= 4:
        assert minimum in (m//2, (m+1)//2)
    ratio = max(modes)/min(modes)
    formula = (3 if m == 2 else 10/7 if m == 3 else 2 if m == 4 else
               h * math.sin(math.pi*(m//2)/m)**2)
    assert abs(ratio - formula) < 1e-10*(1+ratio), (m, ratio, formula)


def main():
    tests = sum(exact_enumeration(m) for m in range(2, 8))
    precision = sum(exact_precision(m) for m in range(2, 18))
    for m in range(2, 500):
        finite_modes(m)
    print('OK: exact pairing comparisons =', tests)
    print('OK: exact precision entry comparisons =', precision)
    print('OK: finite Fourier extremum tests = 498')
    print('All checks passed. These finite tests do not prove all-size assertions.')


if __name__ == '__main__':
    main()
