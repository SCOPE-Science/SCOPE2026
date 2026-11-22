#!/usr/bin/env python3
"""Reproducible rational checks of a sharp convex-prediction sensitivity formula.

These finite checks supplement, but do not replace, the analytic proof in RESULT.md.
Uses only the Python standard library.
"""
from fractions import Fraction as Q
from itertools import product
from random import Random


def predicted(n, tau, kappa):
    m = n // 2
    ell = n - m
    return 1 / (tau + kappa * Q(n, 4 * m * ell))


def extremal_probability(n):
    m = n // 2
    ell = n - m
    return [Q(1, 2 * m)] * m + [Q(1, 2 * ell)] * ell


def jacobian(p, tau, kappa):
    d = [1 / (kappa + tau / t) for t in p]
    total = sum(d)
    return [[(d[i] if i == j else Q(0)) - d[i] * d[j] / total
             for j in range(len(p))] for i in range(len(p))]


def infinity_to_one(j):
    n = len(j)
    # Positive-semidefinite symmetry reduces the cross-norm to signed energy.
    # Brute-force all signs as an independent finite check of that reduction.
    best = Q(0)
    for signs in product((-1, 1), repeat=n):
        q = sum(signs[i] * j[i][k] * signs[k]
                for i in range(n) for k in range(n))
        if q > best:
            best = q
    return best


def run():
    rng = Random(1729)
    checks = 0
    parameters = ((Q(1), Q(1)), (Q(1, 7), Q(3, 2)),
                  (Q(5), Q(1, 11)), (Q(2, 5), Q(12)))
    for n in range(2, 9):
        for tau, kappa in parameters:
            lip = predicted(n, tau, kappa)
            p = extremal_probability(n)
            assert sum(p) == 1 and all(t > 0 for t in p)
            assert infinity_to_one(jacobian(p, tau, kappa)) == lip
            checks += 1
            if n % 2:
                u = [Q(1, n)] * n
                assert infinity_to_one(jacobian(u, tau, kappa)) < lip
                checks += 1
            for k in range(1, n):
                p_k = [Q(1, 2 * k)] * k + [Q(1, 2 * (n-k))] * (n-k)
                expected = 1 / (tau + kappa * Q(n, 4 * k * (n-k)))
                j_k = jacobian(p_k, tau, kappa)
                s_k = [1]*k + [-1]*(n-k)
                cut = sum(s_k[i] * j_k[i][v] * s_k[v]
                          for i in range(n) for v in range(n))
                assert cut == expected
                assert expected <= infinity_to_one(j_k) <= lip
                checks += 2
            for _ in range(14):
                weights = [rng.randrange(1, 40) for _ in range(n)]
                p_random = [Q(w, sum(weights)) for w in weights]
                assert infinity_to_one(jacobian(p_random, tau, kappa)) <= lip
                checks += 1
    print('PASS:', checks, 'exact rational assertions')

if __name__ == '__main__':
    run()
