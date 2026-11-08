#!/usr/bin/env python3
"""Independent depth-first exhaustive check using the literal subsequence definition."""
from collections import Counter
from itertools import combinations

EXPECT_PREFIX_ZERO = {
    '0010001110001011000111001011100010110001101',
    '0100111001011100010110001110010111000111011',
}

def binomial_profile(block):
    single = Counter(block)
    pairs = Counter(block[i] + block[j]
                    for i, j in combinations(range(len(block)), 2))
    return (single['0'], single['1'], pairs['00'], pairs['01'],
            pairs['10'], pairs['11'])

def ending_new(word, old_squares):
    squares = set(old_squares)
    for half in range(1, len(word)//2 + 1):
        left = word[len(word)-2*half:len(word)-half]
        right = word[len(word)-half:]
        if binomial_profile(left) == binomial_profile(right):
            squares.add(left + right)
            if len(squares) > 3:
                return None
    return frozenset(squares)

counts = Counter()
longest = set()

def extend(word, squares):
    counts[len(word)] += 1
    if len(word) == 43:
        longest.add(word)
        assert len(squares) == 3
    if len(word) >= 44:
        raise AssertionError('Unexpected permitted word of length 44')
    for bit in '01':
        child = word + bit
        augmented = ending_new(child, squares)
        if augmented is not None:
            extend(child, augmented)

if __name__ == '__main__':
    # Complementation of symbols preserves 2-binomial equivalence.
    extend('0', frozenset())
    assert longest == EXPECT_PREFIX_ZERO, longest
    assert counts[43] == 2 and counts[42] == 8
    assert counts[16] == 554 and counts[40] == 32
    print('DFS_PASS')
    print('first_zero_length_43=' + repr(sorted(longest)))
    print('first_zero_length_44_count=0')
    print('states_visited=' + str(sum(counts.values())))
