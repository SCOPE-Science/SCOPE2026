#!/usr/bin/env python3
"""Exact rational check of forbidden-edge Hamiltonian tour Walsh covariance.

This is a finite reproducibility check, not an infinite-dimensional proof.
Requires only Python 3 standard library.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, combinations


def run(n):
    assert n >= 6
    r = n - 2
    edges = [(i, j) for i in range(n) for j in range(i + 1, n) if (i, j) != (0, 1)]
    index = {e: k for k, e in enumerate(edges)}
    m = len(edges)
    first = [0] * m
    second = [[0] * m for _ in range(m)]
    count = 0
    for perm in permutations(range(1, n)):
        if perm[0] > perm[-1]:
            continue  # one representative for each undirected cycle
        path = (0,) + perm
        tour = {tuple(sorted((path[i], path[(i + 1) % n]))) for i in range(n)}
        if (0, 1) in tour:
            continue
        count += 1
        inds = sorted(index[e] for e in tour)
        for i in inds:
            first[i] += 1
        for i in inds:
            for j in inds:
                second[i][j] += 1
    # Number equals ((n-1)!/2)*(1-2/(n-1)) = (n-2)!*(n-3)/2.
    assert count == __import__('math').factorial(n - 2) * (n - 3) // 2
    P = [Fraction(x, count) for x in first]
    C = [[Fraction(second[i][j], count) - P[i] * P[j] for j in range(m)] for i in range(m)]
    low = Fraction(2 * (r - 2), r * (r - 1))
    high = Fraction(2 * (r - 2), (r - 1)**2)

    def expect(v, lam, name):
        cv = [sum(C[i][j] * v[j] for j in range(m)) for i in range(m)]
        assert all(cv[i] == lam * v[i] for i in range(m)), (n, name, cv, lam)

    for vertex in range(n):
        expect([int(vertex in e) for e in edges], Fraction(0), f'degree {vertex}')
    for i in range(2, n - 1):
        u = {i: 1, i + 1: -1}
        minus = [u.get(e[1], 0) if e[0] == 0 else
                 -u.get(e[1], 0) if e[0] == 1 else 0 for e in edges]
        plus = [Fraction(u.get(e[1], 0)) if e[0] in (0, 1) else
                Fraction(-2 * (u.get(e[0], 0) + u.get(e[1], 0)), r - 2)
                for e in edges]
        expect(minus, high, f'standard antisymmetric {i}')
        expect(plus, high, f'standard symmetric {i}')
    for a, b, c, d in combinations(range(2, n), 4):
        w = {(a, b): 1, (c, d): 1, (a, c): -1, (b, d): -1}
        expect([w.get(e, 0) for e in edges], low, f'internal 4-cycle {a,b,c,d}')
    null_dim = n
    high_dim = 2 * (r - 1)
    low_dim = r * (r - 3) // 2
    assert null_dim + high_dim + low_dim == m
    assert sum(C[i][i] for i in range(m)) == high_dim * high + low_dim * low
    print(f'EXACT_PASS n={n} tours={count} dim={m} zero={null_dim} high={high} multiplicity={high_dim} low={low} multiplicity={low_dim}')


if __name__ == '__main__':
    for order in (6, 7, 8, 9):
        run(order)
    print('FORBIDDEN_HAMILTONIAN_TOUR_FOURIER_FRAME_EXACT_PASS')
