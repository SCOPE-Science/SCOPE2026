#!/usr/bin/env python3
"""Exact finite-permutation checks for rare common triplets and signed adjacency counts.

Only the accompanying mathematical argument proves the asymptotic theorem.
Run with: python3 verify.py
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import factorial


def evaluate(p):
    n = len(p)
    pos = {v: j for j, v in enumerate(p)}
    inc = sum(pos[j + 1] == pos[j] + 1 for j in range(1, n))
    dec = sum(pos[j + 1] == pos[j] - 1 for j in range(1, n))
    trip = tuple(i for i in range(1, n - 1)
                 if max(pos[i], pos[i + 1], pos[i + 2])
                    - min(pos[i], pos[i + 1], pos[i + 2]) == 2)
    return inc, dec, trip, pos


def verify():
    assertions = 0
    total = 0
    for n in range(3, 9):
        count = 0
        sum_inc = sum_dec = sum_trip = 0
        triplet_forces_adjacency = True
        trip_event = Counter()
        pair_event = Counter()
        marks = Counter()
        signed_sums = Counter()
        for p in permutations(range(1, n + 1)):
            count += 1
            inc, dec, triples, pos = evaluate(p)
            total += 1
            sum_inc += inc
            sum_dec += dec
            sum_trip += len(triples)
            if triples and inc + dec < 1:
                triplet_forces_adjacency = False
            for i in triples:
                trip_event[i] += 1
                signed_sums[i] += inc
                induced = tuple(v for v in p if i <= v <= i + 2)
                marks[(i, induced)] += 1
            for j, i in enumerate(triples):
                for k in triples[j + 1:]:
                    pair_event[(i, k)] += 1
        assert count == factorial(n)
        assertions += 1
        assert Fraction(sum_inc, count) == Fraction(n - 1, n)
        assert Fraction(sum_dec, count) == Fraction(n - 1, n)
        assert Fraction(sum_trip, count) == Fraction(6 * (n - 2), n * (n - 1))
        assertions += 3
        for i in range(1, n - 1):
            assert Fraction(trip_event[i], count) == Fraction(6, n * (n - 1))
            assertions += 1
            for ordering in permutations((i, i + 1, i + 2)):
                assert marks[i, ordering] == factorial(n - 2)
                assertions += 1
            boundary = int(i > 1) + int(i + 2 < n)
            expected_inc = Fraction(2, 3) + Fraction(n - 3 - boundary, n - 2) + Fraction(boundary, 3 * (n - 2))
            assert Fraction(signed_sums[i], trip_event[i]) == expected_inc
            assertions += 1
        if n >= 6:
            for i in range(1, n - 1):
                for j in range(i + 1, n - 1):
                    delta = j - i
                    if delta == 1:
                        expect = Fraction(4, n * (n - 1) * (n - 2))
                    elif delta == 2:
                        expect = Fraction(8, n * (n - 1) * (n - 2) * (n - 3))
                    else:
                        expect = Fraction(36, n * (n - 1) * (n - 2) * (n - 3))
                    assert Fraction(pair_event[i, j], count) == expect
                    assertions += 1
        # A shared triplet forces at least one shared pair, irrespective of orientation.
        assert triplet_forces_adjacency
        assertions += 1
        print(f"n={n}: {count} permutations; {sum_trip} triplet events; {sum_inc} positive adjacencies")
    assert sum(1 for p in permutations((1, 2, 3))
               if sum(p[k + 1] - p[k] == 1 for k in (0, 1)) == 2) == 1
    assertions += 1
    print(f"PASS: {total} exhaustively enumerated permutations; {assertions} exact assertions")


if __name__ == '__main__':
    verify()
