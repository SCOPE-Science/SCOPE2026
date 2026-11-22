#!/usr/bin/env python3
"""Exact integer witness for the five-label Stirling pair-erasure packing."""
import json
from collections import Counter
from pathlib import Path


def insertion_family(n):
    words = [(1, 1)]
    for k in range(2, n + 1):
        words = [w[:i] + (k, k) + w[i:]
                 for w in words for i in range(2 * k - 1)]
    return sorted(words)


def independent_family(n):
    """Enumerate unique balanced multiset words, then test nesting independently."""
    counts = [0] + [2] * n
    word, good = [], []
    def rec():
        if len(word) == 2 * n:
            for x in range(1, n + 1):
                i = word.index(x)
                j = len(word) - 1 - word[::-1].index(x)
                if any(v <= x for v in word[i+1:j]):
                    return
            good.append(tuple(word))
            return
        for x in range(1, n + 1):
            if counts[x]:
                counts[x] -= 1
                word.append(x)
                rec()
                word.pop()
                counts[x] += 1
    rec()
    return good


def erase_pair_and_standardize(word, k):
    return tuple(x - (x > k) for x in word if x != k)


def check():
    root = Path(__file__).resolve().parent
    cert = json.loads((root / 'certificate.json').read_text(encoding='utf-8'))
    assert cert['order'] == 5
    big = insertion_family(5)
    small = insertion_family(4)
    assert len(big) == 945 and len(small) == 105
    assert big == independent_family(5)
    assert small == independent_family(4)
    target_index = {w: i for i, w in enumerate(small)}
    shadows = []
    for w in big:
        images = {erase_pair_and_standardize(w, k) for k in range(1, 6)}
        assert images <= target_index.keys()
        shadows.append({target_index[z] for z in images})
    assert Counter(len(v) for v in shadows) == {1:3, 2:46, 3:248, 4:404, 5:244}
    witness = cert['lower_code_lex_indices']
    assert len(witness) == len(set(witness)) == 33
    assert all(type(i) is int and 0 <= i < 945 for i in witness)
    used = set()
    for i in witness:
        assert not (used & shadows[i])
        used |= shadows[i]
    weights = cert['upper_weights_for_order4_lex_targets']
    scale = cert['scale']
    assert type(scale) is int and scale > 0
    assert len(weights) == 105
    assert all(type(y) is int and y >= 0 for y in weights)
    assert sum(weights) == 339636 < 34 * scale
    assert all(sum(weights[j] for j in sh) >= scale for sh in shadows)
    print('VERIFY_OK: 945 sources, 105 outputs, 33 disjoint shadows,')
    print('integer dual certificate sum=339636/10000 <34; all 945 inequalities checked')

if __name__ == '__main__':
    check()
