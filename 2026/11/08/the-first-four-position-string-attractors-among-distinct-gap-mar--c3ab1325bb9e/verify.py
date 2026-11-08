#!/usr/bin/env python3
"""Reproduce the complete distinct-gap attractor threshold through length 18.

Only the Python standard library is required. All positions are zero-based.
"""
from collections import Counter
from itertools import combinations, permutations

TARGET = '101000100100000001'
TARGET_GAPS = (1, 3, 2, 7)
REVERSED_GAPS = tuple(reversed(TARGET_GAPS))
TARGET_ATTRACTOR = (0, 3, 8, 13)
FORCING_FACTORS = ('101', '10000', '00010', '00001', '001000', '0001')
EXPECTED_COVERAGE = (
    tuple(range(0, 3)),
    tuple(range(9, 14)),
    tuple(range(3, 8)),
    tuple(range(13, 18)),
    tuple(range(7, 13)),
    tuple(range(3, 7)) + tuple(range(14, 18)),
)

def marker_word(gaps):
    return '1' + ''.join('0' * g + '1' for g in gaps)

def factor_coverage(word):
    """Map each distinct factor to all positions in ALL its occurrences."""
    found = {}
    for left in range(len(word)):
        positions = 0
        for right in range(left, len(word)):
            positions |= 1 << right
            factor = word[left:right + 1]
            found[factor] = found.get(factor, 0) | positions
    return found

def exact_attractor(word):
    """Exact search by cardinality; factor coverage is an exact hitting-set test."""
    masks = sorted(set(factor_coverage(word).values()), key=int.bit_count)
    # If A is a subset of B, hitting A necessarily hits B.
    essential = []
    for mask in masks:
        if not any((old & mask) == old for old in essential):
            essential.append(mask)
    for cardinality in range(1, len(word) + 1):
        for subset in combinations(range(len(word)), cardinality):
            chosen = sum(1 << p for p in subset)
            if all(mask & chosen for mask in essential):
                return cardinality, subset
    raise AssertionError('Every nonempty word has a trivial attractor')

def independently_check_attractor(word, positions):
    """Direct occurrence-by-occurrence definition, not the bitset reduction."""
    selected = set(positions)
    for factor in set(word[i:j] for i in range(len(word))
                      for j in range(i + 1, len(word) + 1)):
        if not any(word[i:i + len(factor)] == factor
                   and any(p in selected for p in range(i, i + len(factor)))
                   for i in range(len(word) - len(factor) + 1)):
            return False
    return True

def run():
    counts = Counter()
    exceptional = []
    for k in range(1, 5):
        # Five distinct positive gaps already force length at least
        # 1 + 5 + (1+2+3+4+5) = 21 > 18.
        for gaps in permutations(range(1, 18), k):
            if sum(gaps) + k + 1 > 18:
                continue
            word = marker_word(gaps)
            size, positions = exact_attractor(word)
            assert independently_check_attractor(word, positions)
            counts[k] += 1
            if size >= 4:
                exceptional.append((gaps, size))
    assert counts == Counter({1: 16, 2: 98, 3: 246, 4: 168}), counts
    assert set(exceptional) == {(TARGET_GAPS, 4), (REVERSED_GAPS, 4)}, exceptional
    assert marker_word(TARGET_GAPS) == TARGET and len(TARGET) == 18
    assert independently_check_attractor(TARGET, TARGET_ATTRACTOR)
    covered = factor_coverage(TARGET)
    assert len(covered) == 117
    assert tuple(tuple(p for p in range(18) if covered[f] >> p & 1)
                 for f in FORCING_FACTORS) == EXPECTED_COVERAGE
    # Six coverage constraints have no three-element transversal.
    masks = [covered[f] for f in FORCING_FACTORS]
    for a in combinations(range(18), 3):
        chosen = sum(1 << p for p in a)
        assert not all(mask & chosen for mask in masks)
    print('VERIFIED: 528 distinct-gap words of length at most 18')
    print('VERIFIED: exactly two four-attractor words, reversals of each other')
    print('VERIFIED: 117 factors, 4-position witness, six-factor lower obstruction')
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
