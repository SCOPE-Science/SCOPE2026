#!/usr/bin/env python3
"""Exact residue-table verification for adjacent run lengths in paperfolding words.

Python 3 standard library only. The finite symbolic calculation is a step
within the mathematical proof in RESULT.md; prefix tests are supplementary.
"""
from collections import Counter
from itertools import product

EXPECTED = ((0, 3, 1), (3, 2, 3), (1, 3, 0))


def symbol(index, instructions):
    """One-indexed generalized paperfolding sign from the valuation formula."""
    assert index >= 1
    power = (index & -index).bit_length() - 1
    odd = index >> power
    return instructions[power] * (1 if odd % 4 == 1 else -1)


def template(residue, upper_sign, instructions):
    """Length-eight local window, with its sole multiple-of-eight sign free."""
    out = []
    for j in range(8):
        n = residue + j
        if n % 8 == 0:
            out.append(upper_sign)
        else:
            power = (n & -n).bit_length() - 1
            odd = n >> power
            out.append(instructions[power] * (1 if odd % 4 == 1 else -1))
    return tuple(out)


def two_run_event(word, left, right):
    """Complete successive runs, with both exterior opposite signs."""
    length = left + right + 2
    s = word[1]
    return (word[0] == -s
            and all(x == s for x in word[1:1+left])
            and all(x == -s for x in word[1+left:1+left+right])
            and word[length-1] == s)


def exact_table(instructions):
    counts = Counter()
    for residue, upper_sign in product(range(16), (-1, 1)):
        word = template(residue, upper_sign, instructions)
        for left, right in product((1, 2, 3), repeat=2):
            if two_run_event(word, left, right):
                counts[left, right] += 1
    return tuple(tuple(counts[i, j] for j in (1, 2, 3))
                 for i in (1, 2, 3))


def direct_run_pairs(instructions, length):
    word = [symbol(i, instructions) for i in range(1, length+1)]
    lengths = []
    run_start = 0
    for i in range(1, length):
        if word[i] != word[i-1]:
            lengths.append(i - run_start)
            run_start = i
    lengths.append(length - run_start)
    assert max(lengths) <= 3
    pairs = Counter(zip(lengths, lengths[1:]))
    return tuple(tuple(pairs[i, j] for j in (1, 2, 3))
                 for i in (1, 2, 3))


def fold(instructions):
    word = []
    for bit in instructions:
        word = word + [bit] + [-x for x in reversed(word)]
    return word


def main():
    # Check every normalized choice of the first three instructions and
    # its globally sign-reversed counterpart. This is exhaustive, not random.
    for instructions in product((-1, 1), repeat=3):
        matrix = exact_table(instructions)
        assert matrix == EXPECTED, (instructions, matrix)
    # Verify the 2-adic formula against the recursive finite-fold definition.
    for depth in range(1, 8):
        for instructions in product((-1, 1), repeat=depth):
            expected_word = fold(instructions)
            actual_word = [symbol(i, instructions) for i in
                           range(1, 2**depth)]
            assert expected_word == actual_word
    # Separate direct finite-prefix sanity checks. These are not the proof
    # of the limiting-frequency assertion.
    for k in range(8):
        instructions = tuple(1 if ((j*j + 3*j + k*(j+1) + k//2) % 5) < 3
                             else -1 for j in range(19))
        counts = direct_run_pairs(instructions, 2**16)
        for i in range(3):
            for j in range(3):
                assert abs(counts[i][j]- 2**16 * EXPECTED[i][j]//32) <= 16
    assert sum(sum(row) for row in EXPECTED) == 16
    print('VERIFY_OK symbolic_cases=256 fold_cases=254 prefix_cases=8')
    for row in EXPECTED:
        print(' '.join(map(str, row)))


if __name__ == '__main__':
    main()
