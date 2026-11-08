#!/usr/bin/env python3
"""Independent finite-language and recurrence checks for palindromes of M1 and M2.

Uses only the Python standard library.  All factors needed for the infinite
claim are covered by substituted adjacent-letter pairs (see RESULT.md).
"""
from functools import lru_cache

M1 = {'0': '0112', '1': '1230', '2': '2301', '3': '3023'}
M2 = {'0': '0132', '1': '2310', '2': '3201', '3': '1023'}
P_EXPECTED = {'01', '02', '03', '11', '12', '13', '21', '22', '23', '30'}
EXPECTED_COUNTS = {**{n: 2 for n in range(1, 10)}, 10: 3, 12: 3, 14: 2, 16: 2}


def iterate(morph, word, depth):
    for _ in range(depth):
        word = ''.join(morph[s] for s in word)
    return word


def binary(word):
    return ''.join(str(int(s) % 2) for s in word)


def pairs(word):
    return {word[i:i + 2] for i in range(len(word) - 1)}


def palindrome_factors(word, n):
    return {word[i:i + n] for i in range(len(word) - n + 1)
            if word[i:i + n] == word[i:i + n][::-1]}


def check():
    s4 = iterate(M1, '0', 4)
    s5 = iterate(M1, '0', 5)
    assert pairs(s4) == P_EXPECTED == pairs(s5)
    # A fixed point is partitioned into level-3 blocks of length 64.
    # Any factor of length <= 18 lies inside two consecutive blocks.
    block_words = [binary(iterate(M1, xy, 3)) for xy in sorted(P_EXPECTED)]
    spectra = {}
    for n in range(1, 19):
        factors = set().union(*(palindrome_factors(w, n) for w in block_words))
        spectra[n] = factors
        assert len(factors) == EXPECTED_COUNTS.get(n, 0), (n, factors)
    assert spectra[11] == set() and spectra[18] == set()
    assert '1010010110100101' in spectra[16]
    assert '1010101001010101' in spectra[16]
    assert sum(map(len, spectra.values())) == 28
    # Redundant source-of-letters check using the defining nested recurrences.
    @lru_cache(None)
    def m1(n):
        if n < 2:
            return n
        q, r = divmod(n, 4)
        if r == 0:
            return m1(q)
        if r == 1:
            return 1 - m1(q)
        v = m1(2 * q + 1 - m1(q))
        return v if r == 2 else 1 - v

    @lru_cache(None)
    def m2(n):
        if n < 2:
            return n
        q, r = divmod(n, 4)
        if r in (0, 1):
            v = m2(2 * q + m2(q))
            return v if r == 0 else 1 - v
        v = m2(2 * q + 1 - m2(q))
        return v if r == 2 else 1 - v

    sample1 = binary(iterate(M1, '0', 7))
    sample2 = binary(iterate(M2, '0', 7))
    for i in range(4096):
        assert int(sample1[i]) == m1(i), ('M1', i)
        assert int(sample2[i]) == m2(i), ('M2', i)
    # Every calculated short palindrome occurs in a literal fixed-point prefix.
    for n, fact_set in spectra.items():
        assert palindrome_factors(sample1, n) == fact_set, n
    psi = {'0': '01100110', '1': '10011001'}
    assert all(z == z[::-1] for z in psi.values())
    for r in range(1, 5):
        candidate = iterate(psi, '0', r)
        assert candidate == candidate[::-1]
        assert sample2.startswith(candidate)
    # Directly check the algebraic eight-fold recurrence on the same interval.
    low = (0, 1, 1, 0, 0, 1, 1, 0)
    for n in range(0, 512):
        for j in range(8):
            assert m2(8 * n + j) == m2(n) ^ low[j]
    print('VERIFY_OK')
    print('M1 adjacent-letter pairs:', ' '.join(sorted(P_EXPECTED)))
    print('M1 palindromic complexity n=1..18:',
          ' '.join(str(len(spectra[i])) for i in range(1, 19)))
    print('M1 total distinct nonempty palindromes: 28, maximum length: 16')
    print('M2 palindrome prefixes: 8, 64, 512, 4096, and 8^r for all r >= 0 by induction')
    print('Independent nested-recurrence comparisons: 8192')


if __name__ == '__main__':
    check()
