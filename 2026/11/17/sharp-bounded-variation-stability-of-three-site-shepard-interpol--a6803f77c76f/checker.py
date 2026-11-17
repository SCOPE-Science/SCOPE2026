#!/usr/bin/env python3
"""Numerical and symbolic checks for sharp three-site Shepard BV gain.

The identity is established analytically; finite tests are supplementary.
"""
import math
import random


def interpolation(x, a, b, p, y):
    sites = (0.0, a, a + b)
    for j, t in enumerate(sites):
        if x == t:
            return float(y[j])
    logs = [-p * math.log(abs(x - t)) for t in sites]
    shift = max(logs)
    weights = [math.exp(v - shift) for v in logs]
    return sum(weights[j] * y[j] for j in range(3)) / sum(weights)


def exact_norm(a, b, p):
    r = min(a / b, b / a)
    c = (1.0 + 1.0 / r) ** (1.0 / (p + 1.0))
    q = 1.0 + r * (1.0 + c)
    return 1.0 + 2.0 / (1.0 + q ** p * (1.0 + c ** (-p)))


def bounded_extremum(f, left, right, maximize=False):
    """Independent derivative-free golden-section extremum search."""
    phi = (math.sqrt(5) - 1) / 2
    c = right - phi * (right - left)
    d = left + phi * (right - left)
    fc = f(c) * (-1 if maximize else 1)
    fd = f(d) * (-1 if maximize else 1)
    for _ in range(125):
        if fc < fd:
            right, d, fd = d, c, fc
            c = right - phi * (right - left)
            fc = f(c) * (-1 if maximize else 1)
        else:
            left, c, fc = c, d, fd
            d = left + phi * (right - left)
            fd = f(d) * (-1 if maximize else 1)
    return (left + right) / 2


def single_jump_variation(a, b, p, y):
    # Independently locate all extrema by scalar optimization; no use of
    # the theoretical critical-point location in these computations.
    nodal_breaks = (0.0, a, a + b)
    total = 0.0
    for left, right in zip(nodal_breaks[:-1], nodal_breaks[1:]):
        f = lambda x: interpolation(x, a, b, p, y)
        xmax = bounded_extremum(f, left, right, maximize=True)
        xmin = bounded_extremum(f, left, right)
        positions = sorted([left, right, xmax, xmin])
        values = [interpolation(x, a, b, p, y) for x in positions]
        total += sum(abs(values[j+1] - values[j]) for j in range(3))
    return total


if __name__ == '__main__':
    assert abs(exact_norm(1, 1, 1) - (2 - 1 / math.sqrt(2))) < 1e-13
    print('EXACT_UNIFORM_INVERSE_DISTANCE_IDENTITY_PASS')
    rg = random.Random(102394)
    count = 0
    for _ in range(220):
        a = math.exp(rg.uniform(-2.4, 2.4))
        b = math.exp(rg.uniform(-2.4, 2.4))
        p = rg.uniform(.3, 7.0)
        expected = exact_norm(a, b, p)
        observed = max(single_jump_variation(a, b, p, (0, 1, 1)),
                       single_jump_variation(a, b, p, (0, 0, 1)))
        assert abs(observed - expected) < 5e-8, (a, b, p, observed, expected)
        count += 1
    print('INDEPENDENT_NUMERICAL_STEP_RESPONSE_MAXIMA_PASS', count)

    for p in (0.25, 0.5, 1.0, 2.0, 3.0, 8.0):
        ks = [exact_norm(r, 1, p) for r in (1.0, 0.7, 0.2, 0.05, 0.001)]
        assert all(ks[i] < ks[i+1] for i in range(4)), (p, ks)
        assert 1.0 < ks[0] < 2.0
    print('MESH_CONTRAST_MONOTONICITY_STRESS_PASS')
    assert exact_norm(.01, 1, 2.0) > exact_norm(.01, 1, 1.0)
    assert exact_norm(1, 1, 2.0) < exact_norm(1, 1, 1.0)
    print('SHAPE_PARAMETER_STABILITY_REVERSAL_PASS')
    for t in (0.1, 0.5, 1.0, 2.0):
        p = 100000.0
        r = t / p
        target = 1.0 + 2.0 / (1.0 + math.exp(2 * t))
        assert abs(exact_norm(r, 1.0, p) - target) < 1e-4
    print('HIGH_POWER_MESH_CLUSTERING_SCALING_PASS')
    print('ALL_THREE_SITE_SHEPARD_BV_CHECKS_PASS')
