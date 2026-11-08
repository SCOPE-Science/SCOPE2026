#!/usr/bin/env python3
"""Exact finite transfer audit and independent prefix tests for Rudin--Shapiro runs."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product

ALPHABET = 'abcd'
PHI = {'a': 'ab', 'b': 'ac', 'c': 'db', 'd': 'dc'}
SIGN = {'a': '+', 'b': '+', 'c': '-', 'd': '-'}
BASE_PAIRS = ('ab', 'ac', 'ba', 'bd', 'ca', 'cd', 'db', 'dc')
EXPECTED_64 = ((2, 2, 2, 2),
               (2, 0, 0, 0),
               (3, 0, 1, 0),
               (1, 0, 1, 0))


def hidden_frequencies(max_length=10):
    """Exact factor frequencies of the primitive 2-uniform substitution."""
    f = {1: {a: Fraction(1, 4) for a in ALPHABET},
         2: {x: Fraction(1, 8) for x in BASE_PAIRS}}
    # Check every hidden 2-block balance equation, including zero cases.
    for u, v in product(ALPHABET, repeat=2):
        block = u + v
        internal = sum(f[1][a] for a in ALPHABET if PHI[a] == block) / 2
        crossing = sum((mass for pair, mass in f[2].items()
                        if PHI[pair[0]][1] + PHI[pair[1]][0] == block),
                       Fraction(0)) / 2
        assert f[2].get(block, 0) == internal + crossing
    for length in range(3, max_length + 1):
        output = defaultdict(Fraction)
        for parity in (0, 1):
            antecedent_length = (length + parity + 1) // 2
            assert antecedent_length < length
            for antecedent, mass in f[antecedent_length].items():
                expanded = ''.join(PHI[a] for a in antecedent)
                block = expanded[parity:parity+length]
                assert len(block) == length
                output[block] += mass / 2
        f[length] = dict(output)
        assert sum(output.values()) == 1
    return f


def binary_mass(f, pattern):
    return sum((mass for word, mass in f[len(pattern)].items()
                if ''.join(SIGN[a] for a in word) == pattern), Fraction(0))


def exact_audit():
    f = hidden_frequencies(10)
    assert binary_mass(f, '+' * 5) == 0
    assert binary_mass(f, '-' * 5) == 0
    for i in range(1, 5):
        for j in range(1, 5):
            for p in ('-' + '+' * i + '-' * j + '+',
                      '+' + '-' * i + '+' * j + '-'):
                assert binary_mass(f, p) == Fraction(EXPECTED_64[i-1][j-1], 64), (i, j, p)
    for x, y in product('+-', repeat=2):
        assert binary_mass(f, x + y) == Fraction(1, 4)
    return f


def independent_prefix_audit():
    word = 'a'
    for _ in range(18):
        word = ''.join(PHI[a] for a in word)
    binary = ''.join(SIGN[a] for a in word)
    assert len(binary) == 2**18
    # Separate digit-parity definition, independent of the hidden morphism.
    for n, symbol in enumerate(binary):
        digit_symbol = '-' if ((n & (n >> 1)).bit_count() & 1) else '+'
        assert symbol == digit_symbol, n
    pairs = []
    runs = []
    prev, runlen = binary[0], 1
    for symbol in binary[1:]:
        if symbol == prev:
            runlen += 1
        else:
            runs.append((prev, runlen))
            prev, runlen = symbol, 1
    runs.append((prev, runlen))
    assert {size for _, size in runs} == {1, 2, 3, 4}
    assert all(1 <= size <= 4 for _, size in runs)
    for i in range(len(runs)-1):
        pairs.append((runs[i][0], runs[i][1], runs[i+1][1]))
    counts = Counter(pairs)
    for first in '+-':
        for i in range(1,5):
            for j in range(1,5):
                target = Fraction(EXPECTED_64[i-1][j-1], 64)
                observed = Fraction(counts[(first, i, j)], len(binary))
                assert abs(observed-target) < Fraction(1, 200), (first, i, j, observed, target)
    return len(binary), len(runs)


if __name__ == '__main__':
    exact_audit()
    N, R = independent_prefix_audit()
    print(f'VERIFY_OK exact_block_frequencies=2..10 sign_run_pairs=32 prefix={N} runs={R}')
