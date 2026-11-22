#!/usr/bin/env python3
"""Exact finite checks for radius-two adjacent-transposition balls.

Only the Python standard library is required. Finite checks corroborate the
all-length combinatorial proof; they do not replace it.
"""
from collections import Counter
from itertools import product
from math import comb
from fractions import Fraction


def features(word):
    n = len(word)
    if n < 2:
        return (0, 0, 0)
    e = [int(word[i] == word[i + 1]) for i in range(n - 1)]
    k = sum(e)
    c = sum(e[i] * e[i + 1] for i in range(len(e) - 1))
    a = sum(word[i] == word[i + 2] and word[i] != word[i + 1]
            for i in range(n - 2))
    return k, c, a


def closed_ball_size(word):
    n = len(word)
    if n < 2:
        return 1
    k, c, a = features(word)
    m = n - 1
    return comb(m - k, 2) + 2 * m - k - c - 2 * a


def exact_bfs_size(word):
    seen = {word}
    frontier = {word}
    for _ in range(2):
        nxt = set()
        for v in frontier:
            for i in range(len(v) - 1):
                if v[i] != v[i + 1]:
                    nxt.add(v[:i] + (v[i + 1], v[i]) + v[i + 2:])
        seen.update(nxt)
        frontier = nxt
    return len(seen)


def enumerator_transfer(q, n):
    """Dictionary (k,c,a) -> count, independently built by two-state transfer."""
    if n == 1:
        return {(0, 0, 0): q}
    states = {(1, 1, 0, 0): q, (0, 0, 0, 0): q * (q - 1)}
    # key = (last_equal, k, c, a)
    for _ in range(n - 2):
        new = Counter()
        for (old, k, c, a), v in states.items():
            if old:
                new[(1, k + 1, c + 1, a)] += v
                new[(0, k, c, a)] += v * (q - 1)
            else:
                new[(1, k + 1, c, a)] += v
                new[(0, k, c, a + 1)] += v
                new[(0, k, c, a)] += v * (q - 2)
        states = new
    result = Counter()
    for (_, k, c, a), v in states.items():
        result[(k, c, a)] += v
    return result


def check():
    nwords = 0
    for q, last in [(2, 10), (3, 8), (4, 7)]:
        for n in range(1, last + 1):
            observed = Counter()
            by_ball = Counter()
            for w in product(range(q), repeat=n):
                nwords += 1
                exact = exact_bfs_size(w)
                formula = closed_ball_size(w)
                assert exact == formula, (q, n, w, exact, formula)
                observed[features(w)] += 1
                by_ball[exact] += 1
            assert observed == enumerator_transfer(q, n), (q, n)
            assert sum(observed.values()) == q ** n
            if n >= 2:
                m = n - 1
                p = Fraction(q - 1, q)
                mean = (1 + Fraction((m - 1) * (m - 2), 2) * p * p
                        + (3 * m - 2) * p
                        - 2 * (m - 1) * Fraction(q - 1, q * q))
                mean_actual = Fraction(sum(v * k for k, v in by_ball.items()), q ** n)
                assert mean_actual == mean, (q, n, mean, mean_actual)
                if q >= 3:
                    maximum = m * (m + 3) // 2
                    number_max = q * (q - 1) * (q - 2) ** (n - 2)
                    assert max(by_ball) == maximum
                    assert by_ball[maximum] == number_max
            if q == 2 and n >= 2:
                maximum = ({2: 2, 3: 3, 4: 6, 5: 8}.get(n)
                           if n <= 5 else (n - 1) * (n - 2) // 2 + 2)
                number_max = {2: 2, 3: 6, 4: 2, 5: 6}.get(n, 2)
                assert max(by_ball) == maximum
                assert by_ball[maximum] == number_max
            print('OK alphabet', q, 'length', n, 'words', q ** n,
                  'ball classes', len(by_ball))
    print('ALL CHECKS PASSED; exhaustive center words:', nwords)


if __name__ == '__main__':
    check()
