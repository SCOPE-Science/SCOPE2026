#!/usr/bin/env python3
"""Exhaustive prefix search for binary words having at most three distinct 2-binomial squares."""
from collections import Counter

EXPECTED_AT_43 = (
    '0010001110001011000111001011100010110001101',
    '0100111001011100010110001110010111000111011',
    '1011000110100011101001110001101000111000100',
    '1101110001110100111000110100011101001110010',
)

def pair_signature(block):
    zeros = 0
    scattered_01 = 0
    for bit in block:
        if bit == '0':
            zeros += 1
        else:
            scattered_01 += zeros
    return zeros, scattered_01

def ending_squares(word):
    return {word[-2 * half_length:]
            for half_length in range(1, len(word) // 2 + 1)
            if pair_signature(word[-2 * half_length:-half_length])
            == pair_signature(word[-half_length:])}

def count_layers():
    current = [('', frozenset())]
    sizes = []
    for length in range(1, 45):
        following = []
        for word, squares in current:
            for bit in '01':
                child = word + bit
                collected = squares.union(ending_squares(child))
                if len(collected) <= 3:
                    following.append((child, frozenset(collected)))
        sizes.append(len(following))
        if length == 43:
            longest = tuple(sorted(word for word, _ in following))
            assert longest == EXPECTED_AT_43, longest
            assert all(len(squares) == 3 for _, squares in following)
        if length == 44:
            assert not following
        current = following
    assert sizes[14:18] == [1084, 1108, 1102, 1032]
    assert sizes[-5:] == [64, 32, 16, 4, 0]
    print('BFS_PASS')
    print('length_43_count=4; length_44_count=0')
    print('layer_counts=' + ','.join(str(v) for v in sizes))
    return sizes

if __name__ == '__main__':
    count_layers()
