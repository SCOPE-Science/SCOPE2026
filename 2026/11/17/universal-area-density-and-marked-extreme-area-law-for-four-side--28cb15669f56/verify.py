#!/usr/bin/env python3
"""Numerical checks for a four-edge-stratified area law; not a proof."""
import math
import random


def survival(t):
    assert 0 <= t <= 1
    if t == 0:
        return 1.0
    if t == 1:
        return 0.0
    if t == .5:
        return .5
    z = abs(2*t - 1)
    upper = .5 + (2*z + z*z)*math.log(z) + 2*z - 2.5*z*z
    return upper if t > .5 else 1 - upper


def density(t):
    assert 0 < t < 1 and t != .5
    z = abs(2*t - 1)
    return -4*(1+z)*math.log(z) - 8*(1-z)


def quadrilateral_area(u, v, w, z):
    points = [(u, 0.0), (1.0, v), (w, 1.0), (0.0, z)]
    twice = sum(points[i][0]*points[(i+1) % 4][1]
                - points[i][1]*points[(i+1) % 4][0] for i in range(4))
    return twice/2


def run():
    rng = random.Random(20261109)
    size = 420_000
    thresholds = [.05, .1, .25, .4, .5, .6, .75, .9, .95]
    counts = [0]*len(thresholds)
    second = 0
    for _ in range(size):
        u, v, w, z = (rng.random() for _ in range(4))
        t = quadrilateral_area(u, v, w, z)
        assert abs(t - (1+(u-w)*(v-z))/2) < 1e-15
        second += (t-.5)**2
        for j, threshold in enumerate(thresholds):
            counts[j] += (t > threshold)
    for n, threshold in zip(counts, thresholds):
        exact = survival(threshold)
        observed = n/size
        sigma = math.sqrt(exact*(1-exact)/size)
        assert abs(observed-exact) <= 6.5*sigma + .0005, (threshold, observed, exact)
    assert abs(second/size - 1/144) < .00012
    assert abs(survival(.25)+survival(.75)-1) < 1e-14
    # Independent numerical integral over the product's positive x range.
    for zz in (.13, .37, .73):
        n = 200000
        h = (1-zz)/n
        integr = sum((1-x)*(1-zz/x)/x for x in (zz+(j+.5)*h for j in range(n)))*h
        product_density = 2*integr
        expected = density((1+zz)/2)/2
        assert abs(product_density - expected) < 2e-10
    # Exact fourth-order rare-event coefficient; moderate eps test.
    for eps in (.15, .1, .05, .025):
        ratio = survival(1-eps)/eps**4
        assert 4/3 < ratio < 1.75
    # Check the limiting simplex law by direct independent uniform endpoint deficits.
    eps = .008
    trials = 850000
    accepted = 0
    mean_coords = [0.0]*5
    for _ in range(trials):
        d = [2*eps*rng.random() for _ in range(4)]
        a, b = d[0]+d[1], d[2]+d[3]
        z = (a+b-a*b)/(2*eps)
        if z >= 1:
            continue
        accepted += 1
        marks = [v/(2*eps) for v in d] + [1-z]
        for i, value in enumerate(marks):
            mean_coords[i] += value
    assert accepted > trials*.04
    for i, value in enumerate(mean_coords):
        approx = value/accepted
        assert abs(approx-.2) < .014, (i,approx)
    print('FOUR_SIDE_QUADRILATERAL_AREA_LAW_OK',size,'exact-law simulations;',accepted,'near-max samples')


if __name__ == '__main__':
    run()
