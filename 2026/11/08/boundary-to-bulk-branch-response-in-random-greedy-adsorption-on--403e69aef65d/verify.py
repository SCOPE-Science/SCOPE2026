#!/usr/bin/env python3
"""Exact finite checks for pendant-branch random sequential adsorption.

The theorem and its limit are proved analytically in RESULT.md; this checks
finite coefficients against two direct process constructions.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import comb, factorial, exp


def graph_for_spider(a, b):
    edges = []
    current = 1
    for length in (a, b, 1):
        prior = 0
        for _ in range(length):
            edges.append((prior, current))
            prior = current
            current += 1
    return current, edges


def path_edges(n):
    return [(v, v + 1) for v in range(n - 1)]


def first_arrival_expectation(n, edges):
    neighborhoods = [1 << v for v in range(n)]
    for u, v in edges:
        neighborhoods[u] |= 1 << v
        neighborhoods[v] |= 1 << u

    @lru_cache(maxsize=None)
    def expected(mask):
        if not mask:
            return Fraction(0)
        summation = Fraction(1)
        cursor = mask
        while cursor:
            lowest = cursor & -cursor
            cursor -= lowest
            vertex = lowest.bit_length() - 1
            summation += expected(mask & ~neighborhoods[vertex]) / mask.bit_count()
        return summation

    return expected((1 << n) - 1)


def permutation_expectation(n, edges):
    adjacency = [set() for _ in range(n)]
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    total = 0
    for order in permutations(range(n)):
        selected = set()
        for vertex in order:
            if not (adjacency[vertex] & selected):
                selected.add(vertex)
        total += len(selected)
    return Fraction(total, factorial(n))


def numerator_coefficient(p, q):
    # [x^p y^q] N(x,y), from its three explicit elementary integrals.
    if p == 0 and q == 0:
        return Fraction(0)
    degree = p + q
    first = Fraction(1, (degree + 1) * (degree + 2))
    second = sum((Fraction(comb(p, h) * 2 ** (p - h) * (-1) ** h,
                           q + h + 2) for h in range(p + 1)), Fraction(0)) / 2
    third = sum((Fraction(comb(q, h) * 2 ** (q - h) * (-1) ** h,
                          p + h + 2) for h in range(q + 1)), Fraction(0)) / 2
    return Fraction((-1) ** (degree + 1), factorial(p) * factorial(q)) * (first + second + third)


def pendant_increment(a, b):
    return sum((numerator_coefficient(p, q)
                for p in range(a + 1) for q in range(b + 1)), Fraction(0))


def run():
    checks = 0
    # Direct first-arrival recurrence is a logically distinct finite construction.
    for a in range(6):
        for b in range(6):
            n, edges = graph_for_spider(a, b)
            exact_process = first_arrival_expectation(n, edges)
            increment = exact_process - first_arrival_expectation(n - 1, path_edges(n - 1))
            assert increment == pendant_increment(a, b), (a, b, increment)
            checks += 1
    # Exhaustive, rather than simulated, priority permutations on small graphs.
    for a in range(4):
        for b in range(4):
            n, edges = graph_for_spider(a, b)
            if n > 7:
                continue
            assert permutation_expectation(n, edges) == first_arrival_expectation(n, edges)
            checks += 1
    # Exact adjacent-coefficient sign and decrease inequalities at finite orders;
    # the proof in RESULT.md establishes them for every integer order.
    def column_abs(p):
        return sum((abs(numerator_coefficient(p, q)) for q in range(60)), Fraction(0))
    prev = None
    for p in range(1, 11):
        value = column_abs(p)
        if prev is not None:
            assert value < prev
            checks += 1
        prev = value
    # Both limiting constants approach the values proved by generating functions.
    bulk = (1 - exp(-2)) / 4
    boundary_two = (1 - 5 * exp(-2)) / 2
    assert abs(float(pendant_increment(2, 35) - pendant_increment(0, 38)) - boundary_two) < 1e-12
    checks += 1
    assert abs(float(pendant_increment(30, 30) - pendant_increment(0, 61)) - bulk) < 1e-11
    checks += 1
    print('VERIFY_OK', checks, 'exact comparisons and limiting-value tests')


if __name__ == '__main__':
    run()
