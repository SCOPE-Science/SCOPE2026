#!/usr/bin/env python3
"""Exact finite-state consistency checks for reciprocal-deformation process conjugacy."""
from fractions import Fraction
from itertools import product


def t_integer(a, t):
    return sum((t ** j for j in range(a)), Fraction(0))


def transform(x, K):
    L = len(x)
    return tuple(K - x[-j % L] for j in range(L))


def marked_jumps(x, K, t, q):
    L = len(x)
    TK = t_integer(K, t)
    for i in range(L):
        j = (i + 1) % L
        a, b = x[i], x[j]
        right = t_integer(a, t) * (TK - t_integer(b, t))
        if right:
            y = list(x)
            y[i] -= 1
            y[j] += 1
            yield ('+', i, tuple(y)), right
        left = q * t_integer(b, t) * (TK - t_integer(a, t))
        if left:
            y = list(x)
            y[i] += 1
            y[j] -= 1
            yield ('-', j, tuple(y)), left


def mapped_mark(direction, departure, L):
    if direction == '+':
        return '+', (-departure - 1) % L
    return '-', (1 - departure) % L


def run():
    tested = 0
    configurations = 0
    max_states = 0
    cases = 0
    for L, K in ((3,2), (4,2), (5,2), (3,3), (4,3), (3,4), (4,4)):
        xall = list(product(range(K + 1), repeat=L))
        max_states = max(max_states, len(xall))
        for t in (Fraction(1,2), Fraction(2,3), Fraction(3,2), Fraction(3)):
            for q in (Fraction(0), Fraction(1,3), Fraction(1), Fraction(2)):
                c = t ** (2 - 2*K)
                cases += 1
                for x in xall:
                    y = transform(x, K)
                    assert transform(y, K) == x
                    configurations += 1
                    original = list(marked_jumps(x, K, t, q))
                    dual = dict(marked_jumps(y, K, 1/t, q))
                    assert len(dual) == len(original)
                    for (direction, departure, dest), rate in original:
                        mdirection, mdeparture = mapped_mark(direction, departure, L)
                        key = mdirection, mdeparture, transform(dest, K)
                        assert key in dual, (L, K, x, key)
                        assert dual[key] == c * rate, (L, K, t, q, x, key, rate, dual[key])
                        tested += 1
    print('PASS cases:', cases)
    print('PASS configurations:', configurations)
    print('PASS marked transition comparisons:', tested)
    print('Largest unrestricted state space:', max_states)
    print('All comparisons exact-rational; covers both directions, q=0, q=1 and q>1.')

if __name__ == '__main__':
    run()
