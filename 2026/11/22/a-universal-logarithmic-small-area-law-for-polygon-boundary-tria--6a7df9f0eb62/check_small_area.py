#!/usr/bin/env python3
"""Reproduce exact side-pair integrations and geometric examples for polygon-boundary triangle areas."""
import math
import random


def side_pair_volume(length, adjacent_length, sine, threshold):
    """Exact arclength-coordinate volume for two points on one edge and one on its neighbor."""
    if not (0 < threshold < length * adjacent_length * sine / 2):
        raise ValueError('threshold must lie below the pair support maximum')
    return (4 * length * threshold / sine *
            math.log(length * adjacent_length * sine / (2 * threshold)) +
            4 * threshold * threshold / (adjacent_length * sine * sine))


def side_pair_volume_quadrature(length, adjacent_length, sine, threshold):
    delta = 2 * threshold / (adjacent_length * sine)
    low = 2 * adjacent_length * (length * delta - delta * delta / 2)
    # Independent midpoint quadrature in logarithmic u-coordinates.
    n = 12000
    aa, bb = math.log(delta), math.log(length)
    du = (bb - aa) / n
    rest = 0.0
    for j in range(n):
        u = math.exp(aa + (j + .5) * du)
        rest += 4 * threshold / sine * (length - u) * du
    return low + rest


def characteristics(vertices):
    """Vertices in counterclockwise order; polygon is strictly convex with no collinear edges."""
    n = len(vertices)
    ell = [math.dist(vertices[i], vertices[(i + 1) % n]) for i in range(n)]
    perimeter = sum(ell)
    sin_alpha = []
    for i in range(n):
        v = vertices[i]
        a = vertices[(i - 1) % n]
        b = vertices[(i + 1) % n]
        u = ((a[0] - v[0]), (a[1] - v[1]))
        w = ((b[0] - v[0]), (b[1] - v[1]))
        s = abs(u[0] * w[1] - u[1] * w[0]) / (math.hypot(*u) * math.hypot(*w))
        sin_alpha.append(s)
    zero_atom = sum((x / perimeter) ** 3 for x in ell)
    rate = 12 / perimeter * sum((ell[(i - 1) % n] + ell[i]) / sin_alpha[i]
                                   for i in range(n))
    return zero_atom, rate


def area(p, q, r):
    return abs((q[0]-p[0])*(r[1]-p[1]) - (q[1]-p[1])*(r[0]-p[0])) / 2


def square_sample(rng):
    t = 4 * rng.random()
    if t < 1:
        return (t, 0.0)
    if t < 2:
        return (1.0, t - 1)
    if t < 3:
        return (3 - t, 1.0)
    return (0.0, 4 - t)


def main():
    for l, m, sine, t in [(1.0, 1.0, 1.0, .002), (1.7, .6, .8, .0001),
                          (3.0, 1.0, .5, .00001)]:
        exact = side_pair_volume(l, m, sine, t)
        quad = side_pair_volume_quadrature(l, m, sine, t)
        assert abs(exact-quad) < 1.e-8 * max(1, exact), (exact, quad)
    sq = [(0,0), (1,0), (1,1), (0,1)]
    rect = [(0,0), (3,0), (3,1), (0,1)]
    tri = [(0,0), (1,0), (.5, math.sqrt(3)/2)]
    assert abs(characteristics(sq)[0] - 1/16) < 1e-13
    assert abs(characteristics(sq)[1] - 24) < 1e-13
    assert abs(characteristics(rect)[0] - 7/64) < 1e-13
    assert abs(characteristics(rect)[1] - 24) < 1e-13
    assert abs(characteristics(tri)[1] - 16*math.sqrt(3)) < 1e-12
    for n in [3, 4, 5, 7, 12]:
        poly = [(math.cos(2*math.pi*j/n), math.sin(2*math.pi*j/n)) for j in range(n)]
        assert abs(characteristics(poly)[1] - 24/math.sin(2*math.pi/n)) < 1e-11
    # Deterministic direct geometric cross-check: the 2-on-edge/1-on-adjacent case.
    rng = random.Random(901)
    for _ in range(1000):
        x, y, z = [rng.random() for _ in range(3)]
        assert abs(area((x,0), (y,0), (0,z)) - abs(x-y)*z/2) < 1e-14
    # A finite test of the entire perimeter law, not a proof of the asymptotic.
    n = 1500000
    t = .003
    count = 0
    for _ in range(n):
        x, y, z = (square_sample(rng), square_sample(rng), square_sample(rng))
        if 0 < area(x,y,z) <= t:
            count += 1
    empirical = count/n
    leading = 1.5*t*math.log(1/t)
    assert abs(empirical-leading) < .004, (empirical, leading)
    print('POLYGON_BOUNDARY_SMALL_AREA_CHECKS_OK')
    print('square_exact_atom=1/16, shape_rate=24; equilateral_rate=16sqrt3')
    print('square_positive_tail_empirical', round(empirical, 7), 'leading', round(leading, 7))


if __name__ == '__main__':
    main()
