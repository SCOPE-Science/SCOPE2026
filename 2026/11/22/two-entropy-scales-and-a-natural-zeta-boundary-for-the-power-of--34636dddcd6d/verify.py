#!/usr/bin/env python3
"""Exact finite cross-checks for power-of-two even-shift interspersion.

This program is evidence for finite coefficients and a rational entropy bracket.
The general all-period and natural-boundary arguments are mathematical proofs,
not conclusions from an exhaustive finite experiment.
"""
from itertools import product
from fractions import Fraction


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def even_factor(word):
    indices = [i for i, x in enumerate(word) if x == 1]
    return all((j - i - 1) % 2 == 0
               for i, j in zip(indices, indices[1:]))


def even_cycle(word):
    indices = [i for i, x in enumerate(word) if x == 1]
    if not indices:
        return True
    extended = indices + [indices[0] + len(word)]
    return all((j - i - 1) % 2 == 0
               for i, j in zip(extended, extended[1:]))


def valid_cycle(word):
    marked = [i for i, x in enumerate(word) if x == 2]
    if not marked:
        return even_cycle(word)
    extended = marked + [marked[0] + len(word)]
    for i, j in zip(extended, extended[1:]):
        gap = tuple(word[t % len(word)] for t in range(i + 1, j))
        if not gap or not (len(gap) & (len(gap) - 1)) == 0:
            return False
        if not even_factor(gap):
            return False
    return True


def predicted_counts(nmax):
    w = [0] * (nmax + 1)
    s = 1
    while s + 1 <= nmax:
        w[s + 1] = fibonacci(s + 3) - 1
        s *= 2
    inv = [0] * (nmax + 1)
    inv[0] = 1
    for n in range(1, nmax + 1):
        inv[n] = sum(w[i] * inv[n - i] for i in range(1, n + 1))
    a, b = 2, 1  # Lucas_0 and Lucas_1
    lucas = [2, 1]
    for n in range(2, nmax + 1):
        lucas.append(lucas[-1] + lucas[-2])
    return [0] + [lucas[n] + (-1)**(n + 1)
                  + sum(i * w[i] * inv[n - i] for i in range(1, n + 1))
                  for n in range(1, nmax + 1)]


def partial_w(x):
    return sum((fibonacci(2**j + 3) - 1) * x**(2**j + 1)
               for j in range(8))


def check():
    for n in range(0, 15):
        direct = sum(even_factor(word) for word in product((0, 1), repeat=n))
        assert direct == fibonacci(n + 3) - 1, (n, direct)
    predicted = predicted_counts(10)
    direct = [0] + [sum(valid_cycle(word)
                        for word in product((0, 1, 2), repeat=n))
                    for n in range(1, 11)]
    assert predicted == direct, (predicted, direct)

    low, high = Fraction(221, 500), Fraction(443, 1000)
    ratio = Fraction(13, 8) * low
    # c_n = F_{n+3}-1 <= 2(13/8)^n by induction.
    tail_bound = 2 * low * ratio**256 / (1 - ratio**256)
    assert partial_w(low) + tail_bound < 1
    assert partial_w(high) > 1
    print('Even-shift language counts: all 15 exact identities passed.')
    print('Direct cyclic period counts n=1,...,10:', direct[1:])
    print('All 10 periodic-zeta identities passed independently.')
    print('Exact rational entropy-root bracket: 221/500 < r < 443/1000.')


if __name__ == '__main__':
    check()
