#!/usr/bin/env python3
"""Standalone finite checks for multi-riffle no-feedback score asymptotics.

Run with Python 3: python CHECKER.py
The finite checks corroborate identities; the limit theorem uses an analytical proof.
"""
import itertools
import math
import random
from fractions import Fraction


def guess(i, n, a):
    if i <= (n + 1) // 2:
        return i // a + 1
    return n - (n + 1 - i) // a


def labels_to_cards(labels, a):
    counts = [labels.count(r) for r in range(a)]
    starts = [sum(counts[:r]) for r in range(a)]
    visited = [0] * a
    cards = []
    for r in labels:
        visited[r] += 1
        cards.append(starts[r] + visited[r])
    return cards


def score_and_extremes(labels, a):
    n = len(labels)
    h = (n + 1) // 2
    total = extremes = foreign = 0
    for i, (r, card) in enumerate(zip(labels, labels_to_cards(labels, a)), 1):
        if card == guess(i, n, a):
            total += 1
            if (i <= h and r == 0) or (i > h and r == a - 1):
                extremes += 1
            else:
                foreign += 1
    return total, extremes, foreign


def local_score(labels, a):
    n = len(labels)
    h = (n + 1) // 2
    total = 0
    for section, wanted in ((labels[:h], 0), (list(reversed(labels[h:])), a - 1)):
        rank = 0
        for t, r in enumerate(section, 1):
            if r == wanted:
                rank += 1
                if -a <= t - a * rank <= -1:
                    total += 1
    return total


def exact_marginal_checks():
    checks = 0
    for a, n in ((2, 5), (4, 5), (4, 6)):
        counts = [[0] * n for _ in range(n)]
        for labs in itertools.product(range(a), repeat=n):
            for i, card in enumerate(labels_to_cards(list(labs), a)):
                counts[i][card - 1] += 1
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                expression = Fraction(0)
                for t in range(a):
                    q0, q1 = Fraction(t, a), Fraction(t + 1, a)
                    for u in range(n - i + 1):
                        v = j - 1 - u
                        if 0 <= v < i:
                            term = (math.comb(n - i, u) * q0 ** u
                                    * (1 - q0) ** (n - i - u)
                                    * math.comb(i - 1, v) * q1 ** v
                                    * (1 - q1) ** (i - 1 - v))
                            expression += term / a
                assert Fraction(counts[i - 1][j - 1], a ** n) == expression
                checks += 1
    return checks


def sampled_occupation_checks():
    rng = random.Random(731031)
    checks = 0
    for a, n, trials in ((2, 800, 500), (4, 2000, 700), (8, 3500, 700)):
        values = []
        foreign = 0
        for _ in range(trials):
            labels = [rng.randrange(a) for _ in range(n)]
            total, extremes, outside = score_and_extremes(labels, a)
            assert extremes == local_score(labels, a)
            assert total == extremes + outside
            checks += 2
            foreign += outside
            values.append(total / math.sqrt(n))
        mean = sum(values) / trials
        var = sum((v - mean) ** 2 for v in values) / trials
        target_mean = 2 / math.sqrt(math.pi * (a - 1))
        target_var = (1 - 2 / math.pi) / (a - 1)
        assert abs(mean - target_mean) < 0.12
        assert abs(var - target_var) < 0.12
        checks += 2
        print('packets', a, 'n', n, 'mean', round(mean, 5),
              'variance', round(var, 5), 'other-packet hits', foreign)
    return checks


if __name__ == '__main__':
    exact = exact_marginal_checks()
    sampled = sampled_occupation_checks()
    print('PASS:', exact, 'exact marginal comparisons;', sampled,
          'independent occupation and moment checks')
