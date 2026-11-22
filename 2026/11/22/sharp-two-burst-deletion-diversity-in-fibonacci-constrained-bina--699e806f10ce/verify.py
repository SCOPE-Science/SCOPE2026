#!/usr/bin/env python3
"""Reproducible exhaustive and algebraic checks of a binary constrained burst channel.
Uses only the Python 3 standard library. Scientific tests, not a formal proof.
"""
from collections import Counter
from itertools import product


def allowed_words(n):
    for b in product((0, 1), repeat=n):
        if all(not (b[i] == b[i + 1] == 1) for i in range(n - 1)):
            yield b


def descendants(word):
    n = len(word)
    return {word[:i] + word[i + 2:] for i in range(n - 1)}


def score(word):
    return sum(word[i] != word[i + 2] for i in range(len(word) - 2))


def transfer_next(state):
    # polynomial dictionaries: degree -> multiplicity, grouped by last two bits
    out = {(0, 0): Counter(), (0, 1): Counter(), (1, 0): Counter()}
    for (a, b), poly in state.items():
        for c in (0, 1):
            if b == c == 1:
                continue
            target = out[(b, c)]
            for degree, count in poly.items():
                target[degree + int(a != c)] += count
    return out


def spectral_polynomials(limit):
    state = {(0, 0): Counter({0: 1}), (0, 1): Counter({0: 1}), (1, 0): Counter({0: 1})}
    for n in range(2, limit + 1):
        poly = Counter()
        for p in state.values():
            poly.update(p)
        yield n, dict(poly)
        state = transfer_next(state)


def max_degree(n):
    return (2 * (n - 1)) // 3


def max_count(n):
    if n % 3 == 0:
        return 2
    if n % 3 == 1:
        return 1
    return n // 3 + 3


def main():
    ps = dict(spectral_polynomials(250))
    total_checked = 0
    for n in range(2, 19):
        histogram = Counter()
        for word in allowed_words(n):
            d = len(descendants(word))
            assert d == 1 + score(word), (n, word, d)
            histogram[d - 1] += 1
            total_checked += 1
        assert dict(histogram) == ps[n], (n, histogram, ps[n])
    for n, poly in ps.items():
        top = max(poly)
        assert top == max_degree(n), n
        assert poly[top] == max_count(n), (n, poly[top], max_count(n))
        assert sum(poly.values()) == (1 if n == 0 else 0) + fib(n + 2), n
        assert poly[0] == 3, n
        if n >= 5:
            # F_n = F_(n-1) + F_(n-2) + (y^2 -1) F_(n-3)
            expected = Counter(ps[n-1]); expected.update(ps[n-2]); expected.update({j+2:c for j,c in ps[n-3].items()})
            expected.subtract(ps[n-3])
            assert all(v >= 0 for v in expected.values()), n
            assert {j:v for j,v in expected.items() if v} == poly, n
    print('VERIFY_OK')
    print('exhaustive_words=', total_checked, 'length_range=2..18')
    print('transfer_and_recurrence_lengths=2..250')
    print('maxima_2..14=', [(n, max(ps[n]), ps[n][max(ps[n])]) for n in range(2,15)])


def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

if __name__ == '__main__':
    main()
