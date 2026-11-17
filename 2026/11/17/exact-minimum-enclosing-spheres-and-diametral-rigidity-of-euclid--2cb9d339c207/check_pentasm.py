#!/usr/bin/env python3
"""Exact finite checks for Euclidean circumradius and diameter of pentasms.

Run: python check_pentasm.py
All calculations use Python standard-library fractions; the general theorem
requires the accompanying symbolic proof, not finite enumeration.
"""
from fractions import Fraction as F
from itertools import combinations


def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def squared_distance(u, v):
    return sum((x - y) ** 2 for x, y in zip(u, v))


def coordinates(d, t):
    zero = tuple(F(0) for _ in range(d))
    e = [tuple(F(int(k == j)) for k in range(d)) for j in range(d)]
    shift = tuple(t * (int(j < 2)) for j in range(d))
    pts = {"zero": zero, "shift": shift}
    for j in range(d):
        pts[f"base_{j + 1}"] = e[j]
        pts[f"top_{j + 1}"] = tuple(e[j][k] + shift[k] for k in range(d))
    return pts


def predicted(d, t):
    m = d - 2
    denom = m * (2*t+1)**2 + 2
    a = (2*t+1) * (m*t*(t+1)+1) / denom
    b = (2*t*t+2*t+1) / denom
    radius_squared = (2*m*t**4+4*m*t**3+6*m*t*t+4*m*t+m+1) / denom
    slack0 = (m + 4*(m-1)*t*(t+1)) / denom
    slack1 = 2*t*(2*m*t*t+3*m*t+m-2*t) / denom
    slack4 = 2*t*(2*m*t*t+m*t+2*t+2) / denom
    center = (a, a) + (b,) * m
    weights = {f"base_{j}": b for j in range(3, d + 1)}
    weights.update({"top_1": a/(2*t+1), "top_2": a/(2*t+1)})
    return center, radius_squared, (slack0, slack1, slack4), weights


def verify_case(d, t):
    pts = coordinates(d, t)
    center, r2, slacks, weights = predicted(d, t)
    contacts = set(weights)
    assert len(pts) == 2*d + 2
    assert len(set(pts.values())) == 2*d + 2
    assert r2 > 0 and all(s > 0 for s in slacks)
    assert all(w > 0 for w in weights.values())
    assert sum(weights.values()) == 1
    for j in range(d):
        assert sum(weights[key] * pts[key][j] for key in weights) == center[j]

    for name, point in pts.items():
        actual = r2 - squared_distance(point, center)
        if name in contacts:
            assert actual == 0, (d, t, name, actual)
        elif name == 'zero':
            assert actual == slacks[0], (d, t, name)
        elif name in ('base_1', 'base_2'):
            assert actual == slacks[1], (d, t, name)
        elif name.startswith('top_') and int(name.split('_')[1]) >= 3:
            assert actual == slacks[2], (d, t, name)
        else:
            assert name == 'shift'
            assert actual == (d-2)*(2*t+1)*(2*t*t+2*t+1)/((d-2)*(2*t+1)**2+2)
            assert actual > 0
    # Even the nonvertex Minkowski endpoint called 'shift' is strictly interior.
    assert r2 - squared_distance(pts['shift'], center) > 0
    assert sum(weights[k]*squared_distance(pts[k], center) for k in weights) == r2

    # The true vertices are all the above endpoints except the 'shift' point.
    actual_vertices = {k: v for k, v in pts.items() if k != 'shift'}
    diam2 = 2*t*t + 2*t + 2
    expected_pairs = {
        frozenset((f'base_{j}', f'top_{i}'))
        for j in range(3, d + 1) for i in (1, 2)
    }
    got_pairs = {
        frozenset((k, l))
        for (k, u), (l, v) in combinations(actual_vertices.items(), 2)
        if squared_distance(u, v) == diam2
    }
    assert expected_pairs == got_pairs, (d, t, len(got_pairs))
    for (k, u), (l, v) in combinations(actual_vertices.items(), 2):
        assert squared_distance(u, v) <= diam2, (d, t, k, l)
    return len(pts) + len(weights) + len(actual_vertices)*(len(actual_vertices)-1)//2


def main():
    samples = [F(1, 29), F(1, 7), F(1, 3), F(1, 2), F(1), F(5, 3), F(2), F(13, 5), F(10), F(57)]
    total = 0
    for d in range(3, 25):
        for t in samples:
            total += verify_case(d, t)
    print(f'PASS: {22*len(samples)} rational instances, {total} exact endpoint and distance comparisons')
    print('Domain tested: 3 <= d <= 24; t positive in {1/29, 1/7, 1/3, 1/2, 1, 5/3, 2, 13/5, 10, 57}.')


if __name__ == '__main__':
    main()
