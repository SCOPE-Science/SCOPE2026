#!/usr/bin/env python3
"""Exact finite-prefix illustrations of a weighted-shift invariant-law theorem.
The infinite and probabilistic statements are proved in RESULT.md, not by this code.
"""
from fractions import Fraction


def products(weights):
    out = [Fraction(1)]
    for w in weights:
        assert w != 0
        out.append(out[-1] * w)
    return out


def check_prefix(weights, symbols):
    ps = products(weights)
    assert len(symbols) == len(ps)
    for k in range(len(weights)):
        assert weights[k] * (symbols[k + 1] / ps[k + 1]) == symbols[k + 1] / ps[k]
        assert weights[k] / ps[k + 1] == 1 / ps[k]
    for n in range(len(weights) + 1):
        x = symbols[n] / ps[n]
        assert ps[n] * x == symbols[n]


def main():
    checks = 0
    for N in range(2, 70):
        weights = [Fraction(k + 2, k + 1) for k in range(N)]
        ps = products(weights)
        assert ps == [Fraction(k + 1) for k in range(N + 1)]
        symbols = [Fraction((k % 7) - 3, 7) for k in range(N + 1)]
        check_prefix(weights, symbols)
        checks += 2 * N + 3

    all_weights = []
    midpoints = []
    endpoints = []
    for k in range(1, 23):
        all_weights.extend([Fraction(2)] * k)
        midpoints.append((len(all_weights), 2 ** k))
        all_weights.extend([Fraction(1, 2)] * k)
        endpoints.append(len(all_weights))
    ps = products(all_weights)
    for n, height in midpoints:
        assert ps[n] == height
        checks += 1
    for n in endpoints:
        assert ps[n] == 1
        checks += 1
    symbols = [Fraction((k % 13) - 6, 13) for k in range(len(ps))]
    check_prefix(all_weights, symbols)
    checks += 2 * len(all_weights) + 1
    print('PASS:', checks, 'exact rational finite-prefix assertions (not infinite proof)')


if __name__ == '__main__':
    main()
