#!/usr/bin/env python3
"""Reproducibility checks for the sharp finite-abelian cross Fourier synthesis theorem.

Only Python's standard library is used. These are supplementary finite checks;
the universal result requires the analytic argument in RESULT.md.
"""
import cmath
import math
import random


def optimum(m, n, p):
    assert m >= 2 and n >= 2 and p > 1
    a = (m - 1) ** (1 / (p - 1))
    b = (n - 1) ** (1 / (p - 1))
    d = 1 + a + b
    weights = (
        1 - (m - 1) * (1 + a) / (m * d) - (n - 1) * (1 + b) / (n * d),
        (1 + a) / (m * d),
        (1 + b) / (n * d),
    )
    c = (1 + (m - 1) * (n - 1) * math.exp(-(p - 1) * math.log(d))) ** (-1 / p)
    return (a, b, d, weights, c)


def synthesis_grid(m, n, weights):
    center, arm_a, arm_b = weights
    return [
        center + arm_a * sum(cmath.exp(2j * math.pi * k * x / m)
                             for x in range(1, m))
        + arm_b * sum(cmath.exp(2j * math.pi * l * y / n)
                      for y in range(1, n))
        for k in range(m) for l in range(n)
    ]


def normp(vals, p):
    return sum(abs(z) ** p for z in vals) ** (1 / p)


def main():
    checks = 0
    for m in range(2, 10):
        for n in range(2, 9):
            for p in (1.5, 2.0, 2.5, 3.0, 4.0, 6.0, 9.0):
                a, b, d, w, c = optimum(m, n, p)
                f = synthesis_grid(m, n, w)
                expected = ([1.] + [a / d] * (n - 1)
                            + sum(([b / d] + [-1 / d] * (n - 1)
                                   for _ in range(m - 1)), []))
                assert max(abs(x-y) for x, y in zip(f, expected)) < 5e-13
                assert abs(1 / normp(f, p) - c) < 1e-12
                assert abs(sum(w[k] * [1,m-1,n-1][k] for k in range(3))-1) < 2e-14
                checks += 3
    # Exact p=2 special-case formula, which follows from Parseval.
    for m in range(2, 30):
        for n in range(2, 23):
            c = optimum(m, n, 2)[4]
            assert abs(c - math.sqrt((m+n-1)/(m*n))) < 2e-14
            checks += 1
    # Strict convexity consequence: random complex coefficient perturbations cannot improve optimum.
    random.seed(20261120)
    for m, n, p in ((3,5,1.5), (4,7,3), (3,4,4), (8,2,6), (5,9,9)):
        a,b,d,w,c = optimum(m,n,p)
        for _ in range(300):
            coords = [w[1]]*(m-1) + [w[2]]*(n-1)
            jitter = [(random.random()-.5 + 1j*(random.random()-.5))
                      * random.uniform(.001, 1.) for _ in coords]
            vals = [q+r for q, r in zip(coords, jitter)]
            center = 1 - sum(vals)
            arr = [center] + vals[:m-1] + [0]*(n-1)
            # reconstruct transform directly from independent arm coefficients
            F = [center + sum(vals[x-1] * cmath.exp(2j*math.pi*k*x/m)
                              for x in range(1,m))
                       + sum(vals[m-1+y-1] * cmath.exp(2j*math.pi*l*y/n)
                             for y in range(1,n))
                 for k in range(m) for l in range(n)]
            assert abs(F[0]-1) < 5e-14
            assert normp(F,p) >= 1/c - 1e-12
            checks += 2
    # Critical-exponent sign transition for symmetric q=5 (exists), q=4 (does not).
    cp = 1 + math.log(4) / math.log(1.5)
    assert optimum(5,5,cp-.01)[3][0] > 0
    assert abs(optimum(5,5,cp)[3][0]) < 1e-14
    assert optimum(5,5,cp+.01)[3][0] < 0
    assert all(optimum(4,4,p)[3][0] > 0 for p in (2,4,10,100,1000))
    checks += 4
    print(f'PASS: {checks} supplementary evaluations; all-p, all-group proof is analytic.')

if __name__ == '__main__':
    main()
