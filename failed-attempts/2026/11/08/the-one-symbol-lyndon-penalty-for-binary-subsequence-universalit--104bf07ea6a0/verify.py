#!/usr/bin/env python3
"""Finite independent checks for the binary Lyndon subsequence-universality theorem."""
from itertools import product


def is_lyndon(word):
    return all(word < word[i:] + word[:i] for i in range(1, len(word)))


def greedy_index(word):
    seen = set()
    result = 0
    for c in word:
        seen.add(c)
        if len(seen) == 2:
            result += 1
            seen.clear()
    return result


def by_definition(word, k):
    for bits in product('01', repeat=k):
        i = 0
        for c in word:
            if i < k and c == bits[i]:
                i += 1
        if i != k:
            return False
    return True


def expected(k):
    if k == 1:
        return ['01']
    return ['001' + '01'*(k-1), '01'*k + '1']


def verify():
    candidates = 0
    direct_comparisons = 0
    all_cases = 0
    for k in range(1, 9):
        expected_set = set(expected(k))
        for n in (2*k, 2*k+1):
            found = set()
            for bits in product('01', repeat=n):
                all_cases += 1
                w = ''.join(bits)
                if w.count('0') < k or w.count('1') < k:
                    continue
                if greedy_index(w) >= k and is_lyndon(w):
                    found.add(w)
            if n == 2*k:
                assert found == ({'01'} if k == 1 else set()), (k,n,found)
            else:
                assert found == (set(expected_set) if k >= 2 else {'001','011'}), (k,n,found)
            candidates += len(found)
        if k <= 5:
            for bits in product('01', repeat=2*k+1):
                w = ''.join(bits)
                assert (greedy_index(w) >= k) == by_definition(w, k), (k,w)
                direct_comparisons += 1
    # The binary penalty does not extend automatically to a ternary alphabet.
    witness = '012021'
    assert is_lyndon(witness)
    for target in product('012', repeat=2):
        i = 0
        for c in witness:
            if i < 2 and c == target[i]:
                i += 1
        assert i == 2, target
    for k in range(2, 101):
        for w in expected(k):
            assert len(w) == 2*k+1
            assert is_lyndon(w) and greedy_index(w) == k
    print('VERIFY_OK k=1..8 all_words=',all_cases,
          'minimal_lyndon=',candidates,
          'direct_subsequence_words=',direct_comparisons,
          'formula_witness_k=2..100 ternary_contrast=PASS')


if __name__ == '__main__':
    verify()
