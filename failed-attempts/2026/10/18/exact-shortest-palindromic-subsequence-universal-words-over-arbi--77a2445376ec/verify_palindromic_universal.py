"""Independent finite checks of shortest palindromic subsequence-universal words.

No libraries beyond Python's standard library. Execute:
    python3 verify_palindromic_universal.py

A word is k-universal when every k-letter word occurs as an ordered
(possibly noncontiguous) subsequence. The checks below use an explicit
subsequence automaton, not the proof's arch decomposition.
"""
from itertools import product, permutations
from math import factorial


def contains_subsequence(word, target):
    pos = 0
    for c in word:
        if c == target[pos]:
            pos += 1
            if pos == len(target):
                return True
    return False


def universal(word, k, q):
    return all(contains_subsequence(word, target)
               for target in product(range(q), repeat=k))


def palindromes(q, length):
    for left in product(range(q), repeat=(length + 1) // 2):
        if length & 1:
            yield left + left[-2::-1]
        else:
            yield left + left[::-1]


def predicted_words(q, k):
    m = k // 2
    alph = range(q)
    for blocks in product(tuple(permutations(alph)), repeat=m):
        prefix = sum(blocks, ())
        suffix = prefix[::-1]
        if k % 2 == 0:
            yield prefix + suffix
        else:
            for p in permutations(alph):
                middle = p[:-1] + p[-1:] + p[-2::-1]
                yield prefix + middle + suffix


def run():
    cases = [(2, k) for k in range(1, 8)] + [(3, k) for k in range(1, 6)] \
            + [(4, k) for k in range(1, 4)] + [(5, k) for k in range(1, 3)]
    for q, k in cases:
        expected_length = q * k if k % 2 == 0 else q * k + q - 1
        # Lower bound checks start at the unconstrained q*k bound.
        for length in range(q*k, expected_length):
            assert not any(universal(w, k, q) for w in palindromes(q, length)), (q, k, length)
        by_direct = {w for w in palindromes(q, expected_length) if universal(w, k, q)}
        by_construction = set(predicted_words(q, k))
        expected_count = factorial(q) ** ((k+1)//2)
        assert by_direct == by_construction, (q, k, len(by_direct), len(by_construction))
        assert len(by_direct) == expected_count, (q, k, len(by_direct), expected_count)
        print(f"q={q},k={k}: length={expected_length}, optimum_count={expected_count}, exhaustive=PASS")
    print("ALL_CHECKS_PASS")


if __name__ == '__main__':
    run()
