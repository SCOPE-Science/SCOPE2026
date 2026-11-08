#!/usr/bin/env python3
"""Exact mass identities and independent geometric Monte Carlo checks.

Requires Python 3 standard library only. It does not certify literature priority.
"""
from fractions import Fraction as F
from math import sqrt
from random import Random


def exact_mass_checks(sides):
    sides = tuple(F(x) for x in sides)
    perim = sum(sides)
    p = [x / perim for x in sides]
    assert all(x > 0 and x < F(1, 2) for x in p)
    z = [p[1] * p[2], p[0] * p[2], p[0] * p[1]]
    e2 = sum(z)
    singular = sum(x*x for x in p)
    assert singular + 2*e2 == 1
    assert F(1, 4) < e2 <= F(1, 3)
    assert all(4*x < 1 for x in z)
    assert 4*e2 > 1
    # Corner triangle mass, central medial mass, boundary mass.
    assert singular + e2 + sum(z) == 1
    # Independently integrate the density signs over four equal-area cells.
    tv_integral = (singular + (4*e2-1)/4 + sum((1-4*x)/4 for x in z))/2
    tv_hahn = singular + e2 - F(1, 4)
    assert tv_integral == tv_hahn == F(3, 4)-e2
    assert F(5,12) <= tv_hahn < F(1,2)
    # Each edge's triangular linear density integrates to its squared probability.
    for a, pi in zip(sides, p):
        integ = 4/perim**2 * (a*a/8 + a*a/8)
        assert integ == pi*pi
    return p, e2, z, singular, tv_hahn


def sample_one(rng, p):
    v = rng.random()
    a = 0
    while a < 2 and v >= p[a]:
        v -= p[a]
        a += 1
    t = v / p[a]
    # barycentric endpoints of the three sides, opposite each corresponding vertex
    coords = [[0.0, 1-t, t], [t, 0.0, 1-t], [1-t, t, 0.0]]
    return a, coords[a]


def geometric_check(sides, trials, seed):
    p, e2, z, singular, tv = exact_mass_checks(sides)
    pf = [float(x) for x in p]
    rng = Random(seed)
    counts = [0, 0, 0, 0, 0] # three corners, central, boundary
    for _ in range(trials):
        i, x = sample_one(rng,pf)
        j, y = sample_one(rng,pf)
        if i == j:
            counts[4] += 1
        else:
            m = [(x[k] + y[k])/2 for k in range(3)]
            dominant = [k for k in range(3) if m[k] > .5]
            if dominant:
                assert len(dominant) == 1
                counts[dominant[0]] += 1
            else:
                counts[3] += 1
    predicted = [float(x) for x in z] + [float(e2),float(singular)]
    for observed, goal in zip(counts,predicted):
        # A six-sigma-like broad deterministic tolerance, fixed seed.
        assert abs(observed/trials-goal) < 0.012, (sides,counts,predicted)
    return counts


def main():
    cases = [(1,1,1),(3,4,5),(20,20,3),(7,8,9), (49,49,2)]
    for sides in cases:
        geometric_check(sides, 35000, 17000 + sum(sides))
    assert exact_mass_checks((1,1,1))[-1] == F(5,12)
    # Exact isosceles family tends to the sharp, nonattained upper bound.
    assert exact_mass_checks((100,100,1))[-1] > F(49,100)
    print('VERIFY_OK exact_cases=6 exact_mass_relations=7 per_case monte_carlo_trials=35000 total_trials=175000')


if __name__ == '__main__':
    main()
