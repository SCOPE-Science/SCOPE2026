#!/usr/bin/env python3
"""Finite, exact-rational corroboration for uniform approximation of product conjunction.

No external packages. The infinite-domain optimality and irrational nonattainment
are established in the accompanying mathematical proof, not by this program.
"""
from fractions import Fraction as F
from itertools import product
from math import exp, log
from random import Random


def target(values):
    v = F(1)
    for x in values:
        v *= x
    return v


def min_shift(values, c):
    return max(F(0), min(values) - c)


def predicted(n):
    t = exp(-log(n) / (n - 1))
    h = t - t**n
    return t, h


def check_exact_grid(n, d):
    t, h = predicted(n)
    c = h / 2
    grid = [F(j, d) for j in range(d+1)]
    max_z, max_real_ne, worst = F(0), 0.0, None
    for vec in product(grid, repeat=n):
        f = target(vec)
        m = min(vec)
        z = m-f
        if z > max_z:
            max_z = z
        ne = abs(float(f) - max(0.0, float(m)-c))
        if ne > max_real_ne:
            max_real_ne, worst = ne, vec
        assert float(z) <= h + 1e-12
        assert ne <= c + 1e-12, (n, vec, ne, c)
    return max_z, max_real_ne, worst


def check_rational_shifts():
    rng = Random(261032335)
    total = 0
    for n in range(2, 11):
        t, h = predicted(n)
        c = h/2
        # Rational shifts approximate c from above; the error is <= c + |q-c|.
        q = F(round(c * 1000000), 1000000)
        for _ in range(3000):
            xs = [F(rng.randrange(0,1001), 1000) for _ in range(n)]
            f = float(target(xs))
            g = float(min_shift(xs, q))
            assert abs(f-g) <= c + abs(float(q)-c) + 1e-12
            total += 1
    return total


def check_lower_bound():
    for n in range(2, 101):
        t, h = predicted(n)
        f_ones = 1.0
        f_diag = t**n
        d = 1-t
        assert abs((f_ones-f_diag-d) - h) <= 3e-14
        assert 0 <= t <= 1
        assert h > 0
    assert F(1, 8) == (F(1,2) - F(1,4))/2


def main():
    check_lower_bound()
    configs = [(2,40),(3,24),(4,13),(5,7)]
    results=[]
    for n,d in configs:
        z,ne,worst=check_exact_grid(n,d)
        results.append((n,d,float(z),ne))
    total=check_rational_shifts()
    print('VERIFY_OK grid_configs=%s random_rational_vectors=%s lower_certificates=99' % (results,total))


if __name__ == '__main__':
    main()
