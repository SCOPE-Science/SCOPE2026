"""Exact finite checks for switched Markov-hole survival counts.

Run with Python 3.9 or newer: python checker.py
These tests corroborate the identities but are not proofs for all bases or horizons.
"""
from itertools import product
from math import sqrt, log

assertions = 0


def test(condition, description):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(description)


def symbolic_survivors(base, schedule):
    counts = [1] * base
    for choice in schedule:
        old_total = sum(counts)
        excluded = (base - 1) * choice
        counts = [old_total - counts[letter] if letter == excluded
                  else old_total for letter in range(base)]
    return sum(counts)


def direct_survivors(base, schedule):
    total = 0
    for digits in product(range(base), repeat=len(schedule) + 1):
        if all(not (digits[j] == digits[j + 1] == (base - 1) * choice)
               for j, choice in enumerate(schedule)):
            total += 1
    return total


def optimal_recurrence(base, n):
    older, current = base, base * base - 1
    if n == 0:
        return older
    for _ in range(n - 1):
        older, current = current, base * current - older
    return current


# Independently enumerate base-b digit strings and compare with the count vector.
for base in range(2, 5):
    for n in range(0, 6):
        for schedule in product((0, 1), repeat=n):
            test(symbolic_survivors(base, schedule) == direct_survivors(base, schedule),
                 ('direct count', base, n, schedule))

# Exhaustive optimization over all choices for each finite horizon.
for base in range(2, 9):
    for n in range(0, 12):
        counts = [(symbolic_survivors(base, s), s)
                  for s in product((0, 1), repeat=n)]
        exact_min = min(count for count, _ in counts)
        rec_min = optimal_recurrence(base, n)
        test(exact_min == rec_min, ('recurrence minimum', base, n))
        winners = [s for count, s in counts if count == exact_min]
        if n >= 2:
            predicted = [tuple((j + initial) % 2 for j in range(n)) for initial in (0, 1)]
            test(set(winners) == set(predicted), ('unique alternating winners', base, n))
        elif n == 1:
            test(set(winners) == {(0,), (1,)}, ('single-choice symmetry', base))
        else:
            test(winners == [()], ('empty schedule', base))

# Check recurrence and static-hole comparison at larger horizons.
for base in range(2, 12):
    static_old, static_cur = base, base * base - 1
    for n in range(2, 150):
        static_old, static_cur = static_cur, (base - 1) * (static_cur + static_old)
        test(static_cur > optimal_recurrence(base, n), ('strict fixed-hole gap', base, n))
    root = (base + sqrt(base * base - 4)) / 2
    fixed_root = (base - 1 + sqrt((base - 1) * (base + 3))) / 2
    test(fixed_root > root, ('strict growth gap', base))
    if base == 2:
        for n in range(300):
            test(optimal_recurrence(base, n) == n + 2, ('binary linear law', n))
    else:
        for n in (40, 70, 100):
            approx_rate = log(optimal_recurrence(base, n)) / n
            test(abs(approx_rate - log(root)) < .11, ('Perron root convergence', base, n))

print(f'PASS: {assertions} finite exact/computational assertions; no infinite claims inferred.')
