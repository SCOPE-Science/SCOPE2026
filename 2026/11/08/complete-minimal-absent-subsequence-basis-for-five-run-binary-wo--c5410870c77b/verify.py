#!/usr/bin/env python3
"""Standalone computational checks for a five-run subsequence antidictionary.

The finite tests are supplementary to the proof in RESULT.md.
Run: python3 verify.py
"""
from itertools import product
import random


def subsequence(pattern, word):
    pos = 0
    for symbol in word:
        if pos < len(pattern) and pattern[pos] == symbol:
            pos += 1
    return pos == len(pattern)


def proposed_basis(a, b, c, d, e):
    patterns = {
        '0' * (a + c + e + 1),
        '1' * (b + d + 1),
        '0' * (a + c + 1) + '1',
        '0' * (a + 1) + '1' * (d + 1),
        '1' * (b + 1) + '0' * (e + 1),
        '1' + '0' * (c + e + 1),
        '1' + '0' * (c + 1) + '1',
    }
    if b >= 2:
        patterns.add('10' + '1' * (d + 1))
    if c >= 2:
        patterns.add('0' * (a + 1) + '1' + '0' * (e + 1))
    if d >= 2:
        patterns.add('1' * (b + 1) + '01')
    if b >= 2 and c >= 2:
        patterns.add('101' + '0' * (e + 1))
    if c >= 2 and d >= 2:
        patterns.add('0' * (a + 1) + '101')
    if b >= 2 and c >= 2 and d >= 2:
        patterns.add('10101')
    return patterns


def brute_basis(word):
    """Independent enumeration of the entire distinct-subsequence downset."""
    present = {''}
    for ch in word:
        present.update({v + ch for v in present})
    missing_neighbours = set()
    for v in present:
        for j in range(len(v) + 1):
            for bit in '01':
                missing_neighbours.add(v[:j] + bit + v[j:])
    missing_neighbours.difference_update(present)
    return {
        v for v in missing_neighbours
        if all(v[:j] + v[j+1:] in present for j in range(len(v)))
    }


def main():
    exhaustive_cases = 0
    frequencies = {}
    for a, b, c, d, e in product(range(1, 5), repeat=5):
        word = '0'*a + '1'*b + '0'*c + '1'*d + '0'*e
        actual = brute_basis(word)
        claimed = proposed_basis(a, b, c, d, e)
        assert actual == claimed, (a, b, c, d, e, actual ^ claimed)
        count = 7 + (b >= 2) + (c >= 2) + (d >= 2) + (b >= 2 and c >= 2) + (c >= 2 and d >= 2) + (b >= 2 and c >= 2 and d >= 2)
        assert len(actual) == count
        frequencies[count] = frequencies.get(count, 0) + 1
        exhaustive_cases += 1

    rng = random.Random(20261104)
    deletion_checks = 0
    language_checks = 0
    for _ in range(220):
        a, b, c, d, e = (rng.randrange(1, 51) for _ in range(5))
        word = '0'*a + '1'*b + '0'*c + '1'*d + '0'*e
        basis = proposed_basis(a, b, c, d, e)
        for candidate in basis:
            assert not subsequence(candidate, word)
            for j in range(len(candidate)):
                assert subsequence(candidate[:j] + candidate[j+1:], word)
                deletion_checks += 1
        for _ in range(30):
            p = ''.join(rng.choices('01', k=rng.randrange(1, 111)))
            assert subsequence(p, word) == all(not subsequence(bad, p) for bad in basis)
            language_checks += 1

    print('EXHAUSTIVE_PARAMETER_TUPLES', exhaustive_cases)
    print('COUNT_FREQUENCIES', sorted(frequencies.items()))
    print('RANDOM_ONE_LETTER_DELETION_TESTS', deletion_checks)
    print('RANDOM_PATTERN_MEMBERSHIP_TESTS', language_checks)
    print('VERIFICATION_OK')


if __name__ == '__main__':
    main()
