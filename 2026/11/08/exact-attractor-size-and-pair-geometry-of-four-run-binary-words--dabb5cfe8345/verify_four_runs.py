"""Independent finite checks for the four-run binary-attractor theorem.

No external packages required. Usage: python verify_four_runs.py
Every fact for arbitrarily large run lengths rests on the symbolic proof,
not on finite enumeration.
"""
from itertools import product, combinations
import random


def factors_as_union_masks(word):
    """Each distinct factor is assigned the union of all occurrence intervals."""
    n = len(word)
    masks = {}
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            factor = word[start:start + length]
            occ = ((1 << length) - 1) << start
            masks[factor] = masks.get(factor, 0) | occ
    return tuple(masks.values())


def all_pair_attractors(word):
    masks = factors_as_union_masks(word)
    n = len(word)
    return set((x, y) for x, y in combinations(range(n), 2)
               if all(((1 << x) | (1 << y)) & m for m in masks))


def theorem_pairs(a, b, c, d):
    """Formula for nondegenerate parameters, all >= 2; zero-based indices."""
    assert min(a, b, c, d) >= 2
    p = a - 1
    q = a
    left = a + b - 1
    right = a + b
    r = right + c - 1
    s = right + c
    sets = []
    if a >= c and b >= d:
        sets.append((p, left))
    if c >= a and d <= b <= d + 1:
        sets.append((left, r))
    if a <= c <= a + 1 and b >= d:
        sets.append((q, right))
    if c >= a and d >= b:
        sets.append((right, s))
    return set(tuple(sorted(t)) for t in sets)


def theorem_size(a, b, c, d):
    return 3 if (a > c and d > b) or (c >= a + 2 and b >= d + 2) else 2


def canonical_three_positions(a, b, c, d):
    left = a + b - 1
    zero_mark = a - 1 if a >= c else a + b + c - 1
    one_mark = a if b >= d else a + b + c
    return {left, zero_mark, one_mark}


def verify_direct(word, marks):
    """Separate direct implementation: scan each factor, each occurrence."""
    n = len(word)
    marks = set(marks)
    for length in range(1, n + 1):
        distinct = {word[start:start + length]
                    for start in range(n - length + 1)}
        for f in distinct:
            if not any(word[start:start + length] == f and
                       any(start <= mark < start + length for mark in marks)
                       for start in range(n - length + 1)):
                return False
    return True


def run():
    phase_cases = 0
    exact_pair_cases = 0
    brute_pairs = 0
    direct_cases = 0
    # Full two-attractor census over an interval including singleton runs.
    for a, b, c, d in product(range(1, 7), repeat=4):
        word = '0' * a + '1' * b + '0' * c + '1' * d
        actual = all_pair_attractors(word)
        assert (bool(actual) == (theorem_size(a, b, c, d) == 2)), (a, b, c, d)
        phase_cases += 1
        brute_pairs += len(actual)
        if min(a, b, c, d) >= 2:
            assert actual == theorem_pairs(a, b, c, d), (a, b, c, d, actual, theorem_pairs(a, b, c, d))
            exact_pair_cases += 1
        if max(a, b, c, d) <= 3:
            assert verify_direct(word, canonical_three_positions(a, b, c, d))
            for pair in combinations(range(len(word)), 2):
                assert verify_direct(word, pair) == (pair in actual), (a,b,c,d,pair)
            direct_cases += 1

    # A second implementation checks larger cases and theorem-provided witnesses.
    rng = random.Random(2048)
    for _ in range(100):
        a, b, c, d = (rng.randrange(1, 24) for j in range(4))
        word = '0' * a + '1' * b + '0' * c + '1' * d
        assert verify_direct(word, canonical_three_positions(a, b, c, d))
        if min(a, b, c, d) >= 2:
            for pair in theorem_pairs(a, b, c, d):
                assert verify_direct(word, pair), (a,b,c,d,pair)
        direct_cases += 1
    print('FOUR_RUN_ATTRACTOR_VERIFY_OK',
          'phase_cases', phase_cases,
          'nondegenerate_exact_pair_cases', exact_pair_cases,
          'observed_pairs', brute_pairs,
          'independent_direct_instances', direct_cases)


if __name__ == '__main__':
    run()
