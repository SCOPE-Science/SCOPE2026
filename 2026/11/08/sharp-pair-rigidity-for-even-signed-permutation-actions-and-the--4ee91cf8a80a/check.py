#!/usr/bin/env python3
"""Finite diagnostic for even-sign permutation orbit norm; not an infinite proof."""
import itertools
import math


def inner(x, y):
    return sum(a * b for a, b in zip(x, y))


def max_orbit(u, v):
    d = len(u)
    best = -1e100
    for perm in itertools.permutations(range(d)):
        for signs in itertools.product((-1., 1.), repeat=d):
            if math.prod(signs) != 1:
                continue
            z = [signs[j] * u[perm[j]] for j in range(d)]
            best = max(best, inner(z, v))
    return best


def norm_rank_one(u, v):
    d = len(u)
    A = [[(1. if i == j else 0.) + u[i] * v[j] for j in range(d)] for i in range(d)]
    if d != 2:
        raise ValueError('Use dimension two for direct Frobenius/determinant formula')
    trace = sum(A[i][j] ** 2 for i in range(2) for j in range(2))
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    return math.sqrt((trace + math.sqrt(trace**2 - 4 * det**2)) / 2)


def test():
    for d in (3, 4, 5):
        h = 1 / math.sqrt(d)
        axis = [1.] + [0.] * (d - 1)
        flat = [h] * d
        opposite = flat[:]
        opposite[0] *= -1
        target = 1 / 3 if d == 3 else h
        assert abs(max_orbit(flat, opposite) - (1 / 3 if d == 3 else (d-2)/d)) < 1e-12
        assert abs(max_orbit(axis, flat) - h) < 1e-12
        if d == 4:
            assert abs(max_orbit(flat, opposite) - target) < 1e-12
        if d == 5:
            assert max_orbit(flat, opposite) > target
    for c in (-1, -.75, 0, .25, 1):
        a = [1., 0.]
        v = [c, math.sqrt(max(0, 1 - c*c))]
        actual = norm_rank_one(a, v)
        expected = (1 + math.sqrt(5 + 4*c)) / 2
        assert abs(actual - expected) < 1e-12
    print('PASS: finite signed-permutation and rank-one checks')


if __name__ == '__main__':
    test()
