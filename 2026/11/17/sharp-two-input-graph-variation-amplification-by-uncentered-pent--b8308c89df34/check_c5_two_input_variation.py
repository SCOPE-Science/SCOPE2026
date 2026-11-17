#!/usr/bin/env python3
"""Exact rational verification of the five-cycle uncentered ball-maximal variation bound."""
from fractions import Fraction as F
from itertools import product

N = 5
VERTICES = range(N)


def balls_at(i):
    result = set()
    for c in VERTICES:
        for radius in (0, 1, 2):
            ball = tuple(j for j in VERTICES
                         if min((j-c) % N, (c-j) % N) <= radius)
            if i in ball:
                result.add(ball)
    assert len(result) == 5
    return tuple(sorted(result))


BALLS = tuple(balls_at(i) for i in VERTICES)
ROWS = tuple(tuple(tuple(F(int(j in ball), len(ball)) for j in VERTICES)
                   for ball in BALLS[i]) for i in VERTICES)


def tv(x):
    return sum(abs(x[i] - x[(i+1) % N]) for i in VERTICES)


def apply_matrix(matrix, x):
    return tuple(sum(a*b for a, b in zip(row, x)) for row in matrix)


def maximal(x):
    return tuple(max(sum(x[j] for j in ball) / len(ball) for ball in BALLS[i])
                 for i in VERTICES)


def orbit_certificate():
    patterns = (
        ((1, 0, 0, 0, 0), F(8, 3), F(4, 3)),
        ((1, 1, 0, 0, 0), F(14, 5), F(7, 5)),
        ((1, 0, 1, 0, 0), F(4, 1), F(1, 1)),
    )
    for binary, max_tv, max_ratio in patterns:
        endpoints = []
        for i in VERTICES:
            values = [sum(F(binary[j], len(b)) for j in b) for b in BALLS[i]]
            endpoints.append((min(values), max(values)))
        values = [tv(z) for z in product(*endpoints)]
        assert len(values) == 32
        assert max(values) == max_tv
        assert max(values) / tv(binary) == max_ratio
    print('CUT_ORBIT_BOX_VERTICES_EXACT', len(patterns)*32)


def independent_complete_row_check():
    all_cuts = [tuple(int((mask >> j) & 1) for j in VERTICES)
                for mask in range(1, (1 << N)-1)]
    best = F(0)
    count = 0
    for indices in product(range(5), repeat=N):
        a = tuple(ROWS[i][indices[i]] for i in VERTICES)
        for cut in all_cuts:
            ratio = tv(apply_matrix(a, cut)) / tv(cut)
            assert ratio <= F(7, 5), (indices, cut, ratio)
            if ratio > best:
                best = ratio
            count += 1
    assert best == F(7, 5)
    assert count == 3125 * 30
    print('ALL_ROW_SELECTION_CUT_CERTIFICATES_EXACT', count)


def sharp_nonlinear_pair():
    f = (F(0), F(3), F(4), F(1), F(4))
    v = (F(0), F(0), F(1), F(1), F(0))
    e = F(1, 100)
    g = tuple(f[i] + e*v[i] for i in VERTICES)
    assert min(f) >= 0 and min(g) >= 0
    a = maximal(f)
    b = maximal(g)
    assert a == (F(12, 5), F(3), F(4), F(3), F(4))
    assert b == (F(601, 250), F(3), F(401, 100), F(451, 150), F(4))
    assert tv(tuple(g[i]-f[i] for i in VERTICES)) == F(1, 50)
    assert tv(tuple(b[i]-a[i] for i in VERTICES)) == F(7, 250)
    for x in (f, g):
        for i in VERTICES:
            values = [sum(x[j] for j in ball)/len(ball) for ball in BALLS[i]]
            assert values.count(max(values)) == 1
    print('EXACT_POSITIVE_PERTURBATION_SHARPNESS_PASSED')


if __name__ == '__main__':
    orbit_certificate()
    independent_complete_row_check()
    sharp_nonlinear_pair()
    print('ALL_C5_UNCENTERED_BV_STABILITY_CHECKS_PASSED')
