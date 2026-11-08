#!/usr/bin/env python3
"""Exact checks of binary erasure image probabilities and a finite-input cross-check.

The mathematical proof is in RESULT.md; finite tests are supplementary.
"""
from fractions import Fraction
from itertools import product
from math import comb, log


def p_image(word):
    assert word
    prob = Fraction(2 if word[0] == 0 else 1, 3)
    for a, b in zip(word, word[1:]):
        prob *= Fraction(2 if a != b else 1, 3)
    return prob


def p_minimum_preimage(word):
    n = len(word)
    last_one_location = n + int(word[0] == 1) + sum(a == b for a, b in zip(word, word[1:]))
    return Fraction(2 ** (2 * n - last_one_location), 3 ** n)


def prefix_from_raw(bits, num_output):
    kept = [int(index % 2 == 0) for index, value in enumerate(bits, 1) if value == 1]
    if len(kept) < num_output:
        return None
    return tuple(kept[:num_output])


def test():
    total = 0
    for n in range(1, 11):
        all_words = list(product((0, 1), repeat=n))
        for w in all_words:
            assert p_image(w) == p_minimum_preimage(w)
            total += 1
        assert sum((p_image(w) for w in all_words), Fraction()) == 1
        total += 1
    # Independently enumerate all uniform M-bit input strings for n<=4.  Events
    # with fewer than n ones are unresolved, with an exactly known total mass.
    M = 15
    for n in range(1, 5):
        counts = {w: 0 for w in product((0, 1), repeat=n)}
        unresolved = 0
        for raw in product((0, 1), repeat=M):
            out = prefix_from_raw(raw, n)
            if out is None:
                unresolved += 1
            else:
                counts[out] += 1
        tail = Fraction(sum(comb(M, j) for j in range(n)), 2 ** M)
        assert Fraction(unresolved, 2 ** M) == tail
        for word, count in counts.items():
            lo = Fraction(count, 2 ** M)
            target = p_image(word)
            assert 0 <= target - lo <= tail
            total += 1
        total += 1
    dimension = log(3) / log(2) - Fraction(2, 3)
    assert 0 < dimension < 1
    assert log(3) - log(2) / 2 > log(2)
    print('PASS', total, 'exact arithmetic and finite-input checks')
    print('dimension =', float(dimension))


if __name__ == '__main__':
    test()
