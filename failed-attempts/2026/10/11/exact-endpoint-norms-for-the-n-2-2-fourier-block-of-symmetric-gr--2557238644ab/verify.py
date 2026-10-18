#!/usr/bin/env python3
"""Exact finite checks for the (n-2,2) character-projection formula.

The proof for all n is mathematical; finite checks below are diagnostics only.
This file uses only Python's standard library and exact rational arithmetic.
"""
from fractions import Fraction
from math import factorial, comb
from itertools import permutations


def partition_types(n, largest=None):
    if largest is None:
        largest = n
    if n == 0:
        yield ()
    else:
        for k in range(min(n, largest), 0, -1):
            for rest in partition_types(n-k, k):
                yield (k,) + rest


def class_cardinality(parts):
    from collections import Counter
    counts = Counter(parts)
    z = 1
    for cycle_length, multiplicity in counts.items():
        z *= cycle_length**multiplicity * factorial(multiplicity)
    return factorial(sum(parts)) // z


def char_22(fixed, two_cycles):
    # The character of the partition (n-2,2), n >= 4.
    return fixed * (fixed - 3) // 2 + two_cycles


def no_one_or_two_cycles(max_n):
    a = [0]*(max_n + 1)
    a[0] = 1
    for n in range(1, max_n+1):
        a[n] = sum(comb(n-1, j-1)*factorial(j-1)*a[n-j]
                   for j in range(3, n+1))
    return a


def class_check(max_n=30):
    a = no_one_or_two_cycles(max_n)
    total_classes = 0
    for n in range(4, max_n + 1):
        sum_char = 0
        sum_square = 0
        sum_abs = 0
        negative_count = 0
        sum_weight = 0
        for parts in partition_types(n):
            total_classes += 1
            weight = class_cardinality(parts)
            f, t = parts.count(1), parts.count(2)
            c = char_22(f, t)
            assert (c < 0) == (f in (1, 2) and t == 0), (n, parts)
            if c < 0:
                assert c == -1
                negative_count += weight
            sum_char += weight*c
            sum_square += weight*c*c
            sum_abs += weight*abs(c)
            sum_weight += weight
        assert sum_weight == factorial(n)
        assert sum_char == 0
        assert sum_square == factorial(n)
        expected_neg = n*a[n-1] + comb(n, 2)*a[n-2]
        assert negative_count == expected_neg
        assert sum_abs == 2*negative_count
        dim = n*(n-3)//2
        norm_from_classes = Fraction(dim * sum_abs, factorial(n))
        norm_closed = n*(n-3)*(Fraction(a[n-1], factorial(n-1))
                                + Fraction(a[n-2], 2*factorial(n-2)))
        assert norm_from_classes == norm_closed
    return total_classes


def cycle_count(p):
    n = len(p)
    seen = [False]*n
    fixed = twos = 0
    for start in range(n):
        if seen[start]:
            continue
        length = 0
        x = start
        while not seen[x]:
            seen[x] = True
            x = p[x]
            length += 1
        fixed += length == 1
        twos += length == 2
    return fixed, twos


def brute_check(max_n=8):
    a = no_one_or_two_cycles(max_n)
    checked = 0
    for n in range(4, max_n+1):
        char_abs_sum = 0
        count_negative = 0
        for p in permutations(range(n)):
            checked += 1
            fixed, twos = cycle_count(p)
            c = char_22(fixed, twos)
            char_abs_sum += abs(c)
            count_negative += c < 0
        assert count_negative == n*a[n-1] + comb(n,2)*a[n-2]
        assert char_abs_sum == 2*count_negative
    return checked


if __name__ == '__main__':
    a = class_check()
    b = brute_check()
    print('VERIFY_OK exact_character_classes=%d permutation_objects=%d n=4..30' % (a,b))
