#!/usr/bin/env python3
"""Exact exhaustive periodic-point calculation for finite Kolakoski shifts.

The routine uses integer tuples and no external libraries. It enumerates all
primitive cyclic words of at most 20 letters in the one-derivative shift, then
all oriented inverse-run-length branches of period at most 269.
"""
from itertools import product
from fractions import Fraction

ALPHABET = (1, 2)
CAP = 269
MAX_SEED = 20
DEPTH = 10
EXPECTED_MIN = (2, 3, 8, 12, 18, 27, 80, 120, 180, 269)
EXPECTED_MIN_COUNTS = (1, 2, 1, 2, 4, 8, 4, 8, 16, 16)
EXPECTED_LAYER_COUNTS = (2170, 3474, 5632, 9073, 11218, 5590, 2666, 300, 32, 16)


def rotate_min(word):
    return min(word[i:] + word[:i] for i in range(len(word)))


def complement(word):
    return tuple(3 - c for c in word)


def least_period(word):
    n = len(word)
    for d in range(1, n + 1):
        if n % d == 0 and all(word[i] == word[i % d] for i in range(n)):
            return d
    raise ArithmeticError('non-periodic finite word')


def once_differentiable(word):
    n = len(word)
    return n > 1 and all(not (word[i] == word[(i + 1) % n] ==
                                  word[(i + 2) % n]) for i in range(n))


def inverse_runs(parent):
    # A primitive odd-period run list must be read twice, so that the
    # periodic expansion contains an even number of alternating runs.
    runs = parent if len(parent) % 2 == 0 else parent + parent
    result = []
    symbol = 1
    for run in runs:
        result.extend((symbol,) * run)
        symbol = 3 - symbol
    assert symbol == 1
    return rotate_min(tuple(result))


def cyc_derivative(word):
    n = len(word)
    word = word[:least_period(word)]
    n = len(word)
    boundaries = [i for i in range(n) if word[i] != word[(i - 1) % n]]
    assert boundaries
    start = boundaries[0]
    result = []
    size = 1
    for pos in range(1, n + 1):
        if pos == n or word[(start + pos) % n] != word[(start + pos - 1) % n]:
            result.append(size)
            size = 1
        else:
            size += 1
    assert all(x in ALPHABET for x in result)
    result = tuple(result)
    return rotate_min(result[:least_period(result)])


def enumerate_levels():
    # Each nonconstant cyclic binary word has a rotation beginning with 1.
    # Retain both orientations: quotienting by complement would be INVALID
    # for intermediate run-length words, since 1 and 2 are run lengths.
    seeds = set()
    for n in range(2, MAX_SEED + 1):
        for suffix in product(ALPHABET, repeat=n - 1):
            word = (1,) + suffix
            if once_differentiable(word) and least_period(word) == n:
                seeds.add(rotate_min(word))
                seeds.add(rotate_min(complement(word)))
    levels = [seeds]
    parents = []
    for k in range(1, DEPTH):
        child_parents = {}
        for parent in levels[-1]:
            child = inverse_runs(parent)
            if len(child) <= CAP:
                child_parents[child] = parent
                child_parents[rotate_min(complement(child))] = parent
        parents.append(child_parents)
        levels.append(set(child_parents))
    return levels, parents


def independent_short_periods():
    # Directly check small periods without the inverse-run generator.
    candidates = ((2, 1), (3, 2), (8, 3), (12, 4), (18, 5))
    for max_len, depth in candidates:
        found = []
        for n in range(2, max_len + 1):
            for suffix in product(ALPHABET, repeat=n - 1):
                w = (1,) + suffix
                if least_period(w) != n:
                    continue
                z = w
                valid = True
                for j in range(depth):
                    if not once_differentiable(z):
                        valid = False
                        break
                    z = cyc_derivative(z)
                if valid:
                    found.append(n)
        assert found and min(found) == max_len, (max_len, depth, found[:10])


def main():
    # Every primitive C1 run word has at least one '2' per three positions.
    # Thus each inverse step lengthens its least period by >= 4/3.
    assert Fraction(CAP, 1) * Fraction(3, 4) ** (DEPTH - 1) < MAX_SEED + 1
    assert Fraction(CAP, 1) * Fraction(3, 4) ** (DEPTH - 1) >= MAX_SEED
    levels, parents = enumerate_levels()
    counts = tuple(len(level) for level in levels)
    minima = tuple(min(map(len, level)) for level in levels)
    min_counts = tuple(sum(len(w) == m for w in level)
                       for m, level in zip(minima, levels))
    assert counts == EXPECTED_LAYER_COUNTS, counts
    assert minima == EXPECTED_MIN, minima
    assert min_counts == EXPECTED_MIN_COUNTS, min_counts
    assert all(least_period(word) == len(word) for level in levels
               for word in level)
    final = sorted(w for w in levels[-1] if len(w) == CAP)
    assert len(final) == 16
    assert len({rotate_min(complement(w)) for w in final}) == 16
    # All k-fold primitive periods <=269 have a C1 derivative of length<=20.
    # The final layer therefore gives an exhaustive (not sampled) census.
    for word in final:
        z = word
        for k in range(DEPTH):
            assert once_differentiable(z), (k, z)
            z = cyc_derivative(z)
    # An independent direct-brute method checks the low-depth anchors.
    independent_short_periods()
    print('CERTIFICATE_OK')
    print('seed_bound=20, base_oriented_necklaces=2170')
    print('counts_with_seed_bound=' + ','.join(map(str, counts)))
    print('minimal_periods=' + ','.join(map(str, minima)))
    print('minimizer_shift_orbits=' + ','.join(map(str, min_counts)))
    print('depth_10_short_periods_below_269=0')
    print('depth_10_primitive_period_269_shift_orbits=16')
    print('small_period_direct_bruteforce=passed')
    print('witness=' + ''.join(map(str, final[0])))


if __name__ == '__main__':
    main()
