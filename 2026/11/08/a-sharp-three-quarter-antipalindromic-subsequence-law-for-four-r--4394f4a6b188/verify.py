#!/usr/bin/env python3
"""Finite tests by a separate method for circular antipalindromic subsequences.

The dynamic program does not use the closed-form theorem.  These finite tests
are auxiliary; the proof of the unbounded assertion is in RESULT.md.
"""
from functools import lru_cache
from itertools import product


def dynamic_linear(word):
    @lru_cache(None)
    def dp(i, j):
        if i >= j:
            return 0
        best = max(dp(i + 1, j), dp(i, j - 1))
        if word[i] != word[j]:
            best = max(best, dp(i + 1, j - 1) + 2)
        return best
    return dp(0, len(word) - 1)


def direct_circular(a, b, c, d):
    word = '0' * a + '1' * b + '0' * c + '1' * d
    return max(dynamic_linear(word[i:] + word[:i]) for i in range(len(word)))


def formula(a, b, c, d):
    return 2 * max(min(a, b + d), min(c, b + d),
                   min(b, a + c), min(d, a + c),
                   min(a, d) + min(b, c),
                   min(a, b) + min(c, d))


def run():
    comparisons = 0
    for a, b, c, d in product(range(1, 6), repeat=4):
        actual = direct_circular(a, b, c, d)
        predicted = formula(a, b, c, d)
        assert actual == predicted, (a, b, c, d, actual, predicted)
        comparisons += 1

    balance = 0
    for N in range(2, 101):
        values = []
        for a, b in product(range(1, N), repeat=2):
            c, d = N - a, N - b
            direct_closed = formula(a, b, c, d)
            u, v = abs(a - b), abs(a + b - N)
            simplified = 2 * max((N + u + v) // 2, N - u, N - v)
            assert direct_closed == simplified
            values.append(direct_closed)
            balance += 1
        assert min(values) == 2 * (N - N // 4)
        if N >= 4:
            assert formula(N // 4, N // 2, N - N // 4,
                           N - N // 2) == min(values)

    for h in range(1, 80):
        N = 4 * h
        extremals = []
        for a, b in product(range(1, N), repeat=2):
            u, v = abs(a - b), abs(a + b - N)
            F = max((N + u + v) // 2, N - u, N - v)
            if F == 3 * h:
                extremals.append((a, b))
        expected = {(h, 2*h), (2*h, h), (2*h, 3*h), (3*h, 2*h)}
        assert set(extremals) == expected, (N, extremals)

    print('PASS: separate-method dynamic-programming comparisons:', comparisons)
    print('PASS: balanced formula/equality comparisons:', balance)
    print('PASS: sharpness and all extremizers at 79 lengths divisible by four')


if __name__ == '__main__':
    run()
