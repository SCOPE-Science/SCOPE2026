"""Independent finite checks for an extreme priority-envy cluster law.

Uses the allocation i -> i. Ranks 0-based; an excessive advantage is a
positive difference of priority rank greater than n-h.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
import math
import random


def explicit_count(preferences, priorities, h):
    n = len(preferences)
    pr = [{v: rank for rank, v in enumerate(order)} for order in priorities]
    pref = [{v: rank for rank, v in enumerate(order)} for order in preferences]
    return sum(
        pref[i][j] < pref[i][i]
        and pr[j][j] - pr[j][i] > n - h
        for i in range(n) for j in range(n) if i != j
    )


def critical_count(preferences, priorities, h):
    n = len(preferences)
    pref = [{v: rank for rank, v in enumerate(order)} for order in preferences]
    result = 0
    for j, order in enumerate(priorities):
        incumbent_rank = order.index(j)  # zero-based, larger is worse
        t = incumbent_rank - (n - h)  # candidates strictly advantaged by > n-h
        if t > 0:
            result += sum(pref[i][j] < pref[i][i] for i in order[:t])
    return result


def exhaustive():
    cases = 0
    for n in (2, 3):
        orders = tuple(permutations(range(n)))
        hist = {h: Counter() for h in range(2, n + 1)}
        for prefs in product(orders, repeat=n):
            for priorities in product(orders, repeat=n):
                for h in hist:
                    a = explicit_count(prefs, priorities, h)
                    b = critical_count(prefs, priorities, h)
                    assert a == b, (n, h, prefs, priorities, a, b)
                    hist[h][a] += 1
                    cases += 1
        for h, counts in hist.items():
            total = sum(counts.values())
            mean = Fraction(sum(k*v for k,v in counts.items()), total)
            expected_mean = Fraction(h*(h-1), 4)
            assert mean == expected_mean, (n,h,mean,expected_mean)
            print(f'exhaustive n={n}, h={h}, profiles={total}, E[X]={mean}, P[X=0]={Fraction(counts[0],total)}')
    print(f'PASS exhaustive profile/threshold comparisons: {cases}')


def randomized():
    rng = random.Random(6112643)
    cases = 0
    for n in (4, 9, 28):
        h_values = range(2, min(5,n+1))
        repeats = 3000 if n < 20 else 6000
        sums = {h: 0 for h in h_values}
        zeros = {h: 0 for h in h_values}
        for _ in range(repeats):
            prefs = []
            priorities = []
            for i in range(n):
                a = list(range(n)); rng.shuffle(a); prefs.append(a)
                b = list(range(n)); rng.shuffle(b); priorities.append(b)
            for h in h_values:
                a = explicit_count(prefs,priorities,h)
                b = critical_count(prefs,priorities,h)
                assert a == b
                sums[h] += a
                zeros[h] += (a == 0)
                cases += 1
        for h in h_values:
            mu = h*(h-1)/4
            empirical = sums[h]/repeats
            assert abs(empirical-mu) <= max(0.25, .2*mu), (n,h,empirical,mu)
            print(f'finite random n={n}, h={h}, E[X]~{empirical:.4f} vs exact {mu:.4f}, P0~{zeros[h]/repeats:.4f} vs limit {math.exp(-(h-2+2**(1-h))):.4f}')
    print(f'PASS random profile/threshold comparisons: {cases}')

if __name__ == '__main__':
    exhaustive()
    randomized()
