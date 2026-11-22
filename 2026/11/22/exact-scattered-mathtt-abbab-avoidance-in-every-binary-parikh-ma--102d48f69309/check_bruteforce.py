#!/usr/bin/env python3
"""Direct lexicographic enumeration of binary words and subsequence test."""
from itertools import combinations
from collections import Counter

PATTERN = 'abbab'

def contains_scattered(word, pattern=PATTERN):
    matched = 0
    for letter in word:
        if letter == pattern[matched]:
            matched += 1
            if matched == len(pattern):
                return True
    return False

def ab_pairs(word):
    a_seen = 0
    count = 0
    for letter in word:
        if letter == 'a':
            a_seen += 1
        else:
            count += a_seen
    return count

def predicted(A, B, C):
    assert 0 <= C <= A * B
    if C == 0:
        return 1
    return min(A, C) - (C + B - 1) // B + 1


def run():
    cases = words = 0
    for A in range(9):
        for B in range(9):
            hist = Counter()
            for apos in combinations(range(A + B), A):
                indices = set(apos)
                word = ''.join('a' if i in indices else 'b'
                               for i in range(A + B))
                if not contains_scattered(word):
                    hist[ab_pairs(word)] += 1
                words += 1
            for C in range(A * B + 1):
                observed = hist[C]
                expected = predicted(A, B, C)
                assert observed == expected, (A, B, C, observed, expected)
                cases += 1
    print('BRUTEFORCE_OK', 'words', words, 'classes', cases)

if __name__ == '__main__':
    run()
