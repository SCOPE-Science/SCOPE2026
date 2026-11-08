#!/usr/bin/env python3
"""Exact checks for random-order greedy independence on a chorded path.

Run with Python 3.9 or later; requires only the standard library.
All expected values are rational; no Monte Carlo is used.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import factorial

CHECKS = 0

def equal(a, b):
    global CHECKS
    assert a == b, (a, b)
    CHECKS += 1

def graph(n, chord=False):
    edges = [(i, i + 1) for i in range(n - 1)]
    if chord:
        edges.append((0, 3))
    adj = [0] * n
    for i, j in edges:
        adj[i] |= 1 << j
        adj[j] |= 1 << i
    return tuple(adj)

@lru_cache(None)
def exact_expectation(adj, mask):
    n = mask.bit_count()
    if n == 0:
        return Fraction(0)
    return 1 + sum(exact_expectation(adj, mask & ~(1 << v) & ~adj[v])
                   for v in range(len(adj)) if mask & (1 << v)) / n

def exact_graph(n, chord):
    return exact_expectation(graph(n, chord), (1 << n) - 1)

def brute_permutations(n, chord):
    adj = graph(n, chord)
    total = 0
    for order in permutations(range(n)):
        taken = 0
        count = 0
        for v in order:
            if not (taken & adj[v]):
                taken |= (1 << v)
                count += 1
        total += count
    return Fraction(total, factorial(n))

def coef_e_minus_two(n):
    return Fraction((-2) ** n, factorial(n)) if n >= 0 else 0

def predicted_increment(n):
    return Fraction(-(-2) ** (n - 2) * (n - 3) * (n - 4), 2 * factorial(n))

def expected_path(n):
    return sum((Fraction((-2) ** j, factorial(j+1)) * (n - j)
               for j in range(n)), Fraction(0))

def predicted_delta(n):
    # Coefficients of ((3 - 3z + z^2) - (3 + 3z + z^2)e^-2z)/(2(1-z)).
    if n < 0:
        return 0
    out = Fraction(0)
    for k in range(n + 1):
        polynomial = ({0:3, 1:-3, 2:1}.get(k, 0))
        conv = 3 * coef_e_minus_two(k) + 3 * coef_e_minus_two(k-1) + coef_e_minus_two(k-2)
        out += (polynomial - conv) / 2
    return out

def main():
    f = {k: expected_path(k) for k in range(0, 150)}
    g = {4: Fraction(2)}
    for n in range(1, 50):
        equal(f[n], 1 + Fraction(2, n) * sum((f.get(k,0) for k in range(n-1)), Fraction(0)))
    for n in range(5, 150):
        F = lambda t: f[t] if t >= 0 else Fraction(0)
        tail = (Fraction(14, 3) + F(n-3) + 2*F(n-4) + F(n-5) + F(n-6)
                + sum((F(j) for j in range(0, n-6)), Fraction(0)))
        rec = 1 + (tail + sum((g[k] for k in range(4, n-1)), Fraction(0))) / n
        g[n] = rec
        equal(g[n] - f[n], predicted_delta(n))
        equal(predicted_delta(n) - predicted_delta(n-1), predicted_increment(n))
    for n in range(4, 14):
        equal(exact_graph(n, False), f[n])
        equal(exact_graph(n, True), g[n])
    for n in range(4, 9):
        equal(brute_permutations(n, False), f[n])
        equal(brute_permutations(n, True), g[n])
    equal(predicted_delta(4), 0)
    equal(predicted_delta(5), Fraction(1,15))
    equal(predicted_delta(6), 0)
    equal(predicted_delta(7), Fraction(4,105))
    for n in range(7, 150):
        assert predicted_delta(n) > 0
        CHECK = 1
        global CHECKS
        CHECKS += CHECK
    print('VERIFY_OK', CHECKS, 'exact assertions')

if __name__ == '__main__':
    main()
