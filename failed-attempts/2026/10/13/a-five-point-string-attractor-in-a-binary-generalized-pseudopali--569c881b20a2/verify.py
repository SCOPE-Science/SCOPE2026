#!/usr/bin/env python3
"""Exact finite certificate for a generalized pseudopalindromic word's string-attractor number."""
from itertools import product

DIRECTIVE = "10111"
ANTIMORPHISMS = "EEERE"
EXPECTED_WORD = "10011010011011001011001100101100100110100110"
EXPECTED_LENGTHS = (2, 6, 12, 23, 44)
EXPECTED_LONGEST_SUFFIXES = (0, 0, 2, 3, 4)
LOWER_WITNESSES = {
    "1010": (4, 36),
    "11011": (9,),
    "00100": (30,),
    "110011": (18,),
    "0101": (15, 25),
    "001100": (20,),
}
ATTRACTOR = (9, 16, 23, 33, 39)
EXPECTED_FACTOR_COUNTS = (2, 4, 6, 10, 14, 18, 22, 25, 28)


def involution(word, operator):
    reversed_word = word[::-1]
    if operator == "R":
        return reversed_word
    assert operator == "E"
    return "".join("0" if c == "1" else "1" for c in reversed_word)


def closure(prefix, operator):
    # Inspect every possible suffix length from longest to shortest.
    for k in range(len(prefix), -1, -1):
        suffix = prefix[len(prefix) - k:]
        if suffix == involution(suffix, operator):
            missing = prefix[:len(prefix) - k]
            return prefix + involution(missing, operator), k
    raise AssertionError("Empty suffix always works")


def occurrences(word, factor):
    return tuple(i for i in range(len(word)-len(factor)+1)
                 if word[i:i+len(factor)] == factor)


def support(word, factor):
    return set(j for i in occurrences(word, factor)
               for j in range(i, i+len(factor)))


def verify():
    word = ""
    lengths, suffixes = [], []
    for digit, operator in zip(DIRECTIVE, ANTIMORPHISMS):
        word, k = closure(word + digit, operator)
        assert word == involution(word, operator)
        lengths.append(len(word))
        suffixes.append(k)
    assert word == EXPECTED_WORD
    assert tuple(lengths) == EXPECTED_LENGTHS
    assert tuple(suffixes) == EXPECTED_LONGEST_SUFFIXES

    support_sets = []
    for factor, expected_starts in LOWER_WITNESSES.items():
        assert occurrences(word, factor) == expected_starts
        support_sets.append(support(word, factor))
    base = support_sets[:4]
    assert all(base[i].isdisjoint(base[j]) for i in range(4)
               for j in range(i+1, 4))
    assert all(support_sets[4].isdisjoint(base[i]) for i in range(3))
    assert all(support_sets[5].isdisjoint(base[i]) for i in range(3))
    assert support_sets[4] & base[3] == {18}
    assert support_sets[5] & base[3] == {20, 21, 22, 23}
    assert (support_sets[4] & base[3]).isdisjoint(support_sets[5] & base[3])

    # Independent exhaustive check of all positions permitted by four
    # mutually disjoint witness supports (rather than relying on optimization).
    candidates = 0
    for points in product(*[sorted(s) for s in base]):
        candidates += 1
        assert not (any(i in support_sets[4] for i in points)
                    and any(i in support_sets[5] for i in points))
    assert candidates == 1200

    # Five-position upper certificate: maximum unmarked run is only nine.
    assert len(ATTRACTOR) == 5
    assert len(set(ATTRACTOR)) == 5
    marks = set(ATTRACTOR)
    gaps = []
    last = -1
    for p in sorted(marks):
        gaps.append(p-last-1)
        last = p
    gaps.append(len(word)-last-1)
    assert max(gaps) == 9

    counts = []
    for length in range(1, 10):
        all_factors = set()
        covered_factors = set()
        for i in range(len(word)-length+1):
            factor = word[i:i+length]
            all_factors.add(factor)
            if any(i <= p < i+length for p in marks):
                covered_factors.add(factor)
        assert all_factors == covered_factors, (length, all_factors-covered_factors)
        counts.append(len(all_factors))
    assert tuple(counts) == EXPECTED_FACTOR_COUNTS
    print("VERIFY_OK length=44 closures=5 lower_witnesses=6 "
          "four_position_candidates=1200 five_attractor=9,16,23,33,39 "
          "checked_factor_lengths=1..9 max_unmarked_run=9")


if __name__ == "__main__":
    verify()
