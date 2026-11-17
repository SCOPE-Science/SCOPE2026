#!/usr/bin/env python3
"""Exact rational checks for four-weight octagonal conic-spline moduli.

No numerical tolerances are used. This checks finite examples, not the
universal analytical theorem, which is proved separately in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import product

OCT = [(1, 0), (1, 1), (0, 1), (-1, 1),
       (-1, 0), (-1, -1), (0, -1), (1, -1)]
HEX = [(1, 0), (0, 1), (-1, 1),
       (-1, 0), (0, -1), (1, -1)]


def cross(x, y):
    return x[0] * y[1] - x[1] * y[0]


def minus(x, y):
    return x[0] - y[0], x[1] - y[1]


def hull(points):
    """Counterclockwise convex hull, exact non-collinearity test."""
    points = sorted(set(points))

    def half(seq):
        chain = []
        for x in seq:
            while len(chain) >= 2 and cross(
                minus(chain[-1], chain[-2]), minus(x, chain[-1])
            ) <= 0:
                chain.pop()
            chain.append(x)
        return chain

    return half(points)[:-1] + half(points[::-1])[:-1]


def ray_radius(polygon, direction):
    """Find outer radial intersection with a convex polygon."""
    values = []
    for p, r in zip(polygon, polygon[1:] + polygon[:1]):
        edge = minus(r, p)
        det = cross(direction, edge)
        if det == 0:
            continue
        radius = cross(p, edge) / det
        fraction = cross(p, direction) / det
        if radius > 0 and 0 <= fraction <= 1:
            values.append(radius)
    assert values
    return max(values)


def exact_geometric_modulus(rays, nodal):
    vertices = [(Q(x) / val, Q(y) / val)
                for (x, y), val in zip(rays, nodal)]
    polygon = hull(vertices)
    return max(val * ray_radius(polygon, ray)
               for val, ray in zip(nodal, rays))


def twelve_branches(a, b, c, d):
    return [Q(2 * a, b + d), Q(a, b + c), Q(a, c + d),
            Q(2 * c, b + d), Q(c, a + b), Q(c, a + d),
            Q(b, a + c), Q(b, 2 * a + d), Q(b, 2 * c + d),
            Q(d, a + c), Q(d, 2 * a + b), Q(d, 2 * c + b)]


def verify():
    oct_tests = 0
    for a, b, c, d in product(range(1, 9), repeat=4):
        nodal = [Q(a), Q(b), Q(c), Q(d)] * 2
        predicted = max([Q(1)] + twelve_branches(a, b, c, d))
        computed = exact_geometric_modulus(OCT, nodal)
        assert computed == predicted, (a, b, c, d, computed, predicted)
        oct_tests += 1

    witnesses = [(2, 1, 1, 1), (3, 1, 1, 4), (3, 4, 1, 1),
                 (1, 1, 2, 1), (1, 1, 3, 4), (1, 4, 3, 1),
                 (1, 3, 1, 1), (1, 5, 3, 1), (3, 5, 1, 1),
                 (1, 1, 1, 3), (1, 1, 3, 5), (3, 1, 1, 5)]
    for i, abcd in enumerate(witnesses):
        branches = twelve_branches(*abcd)
        assert branches[i] > 1
        assert all(branches[i] > other for j, other in enumerate(branches) if i != j)

    hex_tests = 0
    for a, b, c in product(range(1, 13), repeat=3):
        geometric = exact_geometric_modulus(
            HEX, [Q(a), Q(b), Q(c)] * 2)
        predicted = max(Q(1), Q(a, b + c), Q(b, a + c), Q(c, a + b))
        assert geometric == predicted, (a, b, c)
        hex_tests += 1

    print('PASS: octagonal exact-rational hull comparisons:', oct_tests)
    print('PASS: twelve individually essential ratio branches:', len(witnesses))
    print('PASS: independent six-ray control comparisons:', hex_tests)


if __name__ == '__main__':
    verify()
