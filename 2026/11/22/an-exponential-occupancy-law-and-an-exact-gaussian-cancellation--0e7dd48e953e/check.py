#!/usr/bin/env python3
"""Independent finite checks of the simplex Thales occupancy identity.

These tests are not proofs of the limiting statements.
"""
from fractions import Fraction
from math import exp, factorial
from random import Random


def exact_variance():
    # E[E^k] = k! for an independent Exp(1) sample.
    h2 = factorial(4) - 4 * factorial(3) + 4 * factorial(2)
    assert h2 == 8
    # Integral_{2}^{infinity} (x*x-2*x)*exp(-x) dx = 4*exp(-2).
    p = exp(-2)
    var = p * (1 - p) + p * p * h2 - 2 * p * (4*p)
    assert abs(var - p*(1-p)) < 1e-14
    return p


def geom_check():
    r = Random(1783)
    count = 0
    for m in (2, 3, 4, 7, 13):
        for _ in range(700):
            exps = [r.expovariate(1.0) for _ in range(m)]
            total = sum(exps)
            lam = [x/total for x in exps]
            xnorm2 = sum((x-1/m)**2 for x in lam)
            q = sum(x*x for x in lam)
            from_geo = 0
            from_bary = 0
            for i in range(m):
                # The Euclidean diameter sphere: ||x-v_i/2||^2 <= ||v_i||^2/4.
                vi = [float(int(j==i))-1/m for j in range(m)]
                x = [t-1/m for t in lam]
                geo = sum((x[j]-vi[j]/2)**2 for j in range(m)) <= sum(y*y for y in vi)/4+1e-12
                bary = lam[i] >= q-1e-12
                assert geo == bary
                from_geo += geo
                from_bary += bary
                count += 1
            assert from_geo == from_bary
            assert 1 <= from_geo <= m
            assert abs(xnorm2-(q-1/m)) < 1e-12
    return count


def simulation(p):
    r = Random(17711)
    output = []
    for m, reps in ((64,4000), (256,3000), (1024,1700)):
        samples = []
        for _ in range(reps):
            e = [r.expovariate(1.0) for _ in range(m)]
            t = sum(x*x for x in e)/sum(e)
            samples.append(sum(x>=t for x in e))
        avg = sum(samples)/reps/m
        norm_var = sum((z - sum(samples)/reps)**2 for z in samples)/(reps-1)/m
        output.append((m, avg, norm_var))
    assert abs(output[-1][1]-p) < 0.025
    assert abs(output[-1][2]-p*(1-p)) < 0.045
    return output


if __name__ == '__main__':
    prob = exact_variance()
    tested = geom_check()
    mc = simulation(prob)
    print('Geometric equalities tested:', tested)
    print('Predicted limiting mean fraction, variance of normalized count:', prob, prob*(1-prob))
    for m, av, var in mc:
        print('vertices', m, 'mean coverage fraction', round(av, 6), 'variance / vertices', round(var, 6))
    print('PASS (finite checks only)')
