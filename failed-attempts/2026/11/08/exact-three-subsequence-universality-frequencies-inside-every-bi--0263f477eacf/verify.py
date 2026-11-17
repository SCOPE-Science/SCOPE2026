#!/usr/bin/env python3
"""Finite cross-checks of exact three-subsequence-universality fiber formulas."""
from collections import Counter, defaultdict
from itertools import combinations, product

PATTERNS = tuple(''.join(s) for s in product('ab', repeat=3))

def has_subseq(w, pat):
    it = iter(w)
    return all(any(x == letter for x in it) for letter in pat)

def inversions_ab(w):
    seen_a = total = 0
    for x in w:
        if x == 'a':
            seen_a += 1
        else:
            total += seen_a
    return total

def candidate_words(A, B, C):
    D = A * B - C
    result = {}
    if C <= B:
        result['aab'] = 'b' * (B-C) + 'a' + 'b' * C + 'a' * (A-1)
    if C <= A:
        result['abb'] = 'b' * (B-1) + 'a' * C + 'b' + 'a' * (A-C)
    if D <= B:
        result['baa'] = 'a' * (A-1) + 'b' * D + 'a' + 'b' * (B-D)
    if D <= A:
        result['bba'] = 'a' * (A-D) + 'b' + 'a' * D + 'b' * (B-1)
    if C % A == 0:
        result['aba'] = 'b' * (B-C//A) + 'a' * A + 'b' * (C//A)
    if C % B == 0:
        result['bab'] = 'a' * (C//B) + 'b' * B + 'a' * (A-C//B)
    return result

def formula(A, B, C):
    D = A * B - C
    raw = sum((C <= A, C <= B, D <= A, D <= B, C % A == 0, C % B == 0))
    return raw - sum((C == 1, D == 1, C == A, D == A, C == B, D == B)) - 3*(C == 0) - 3*(D == 0)

def class_sizes_dp(A, B):
    # Independently compute Gaussian-binomial coefficient in the ab-count convention.
    d = {(0, 0): Counter({0: 1})}
    for a in range(A + 1):
        for b in range(B + 1):
            if (a,b) == (0,0):
                continue
            cnt = Counter()
            if a:
                cnt.update(d[(a-1,b)])
            if b:
                for c, v in d[(a,b-1)].items():
                    cnt[c+a] += v
            d[(a,b)] = cnt
    return d[(A,B)]

def verify():
    exact_words = 0
    exact_classes = 0
    for A in range(3,9):
        for B in range(3,9):
            total = Counter()
            bad = Counter()
            realized_bad = defaultdict(set)
            for pos in combinations(range(A+B), A):
                positions = set(pos)
                w = ''.join('a' if i in positions else 'b' for i in range(A+B))
                C = inversions_ab(w)
                total[C] += 1
                if not all(has_subseq(w, p) for p in PATTERNS):
                    bad[C] += 1
                    realized_bad[C].add(w)
                exact_words += 1
            gaussian = class_sizes_dp(A,B)
            for C in range(A*B+1):
                E = formula(A,B,C)
                candidates = candidate_words(A,B,C)
                assert 0 <= E <= 2, (A,B,C,E)
                assert E == bad[C] == len(set(candidates.values())), (A,B,C,E,bad[C],candidates)
                assert set(candidates.values()) == realized_bad[C], (A,B,C)
                assert total[C] == gaussian[C], (A,B,C,total[C],gaussian[C])
                for missing, w in candidates.items():
                    assert w.count('a') == A and w.count('b') == B
                    assert inversions_ab(w) == C
                    assert not has_subseq(w, missing)
                exact_classes += 1
            assert sum(bad.values()) == 3*(A+B)-6, (A,B,sum(bad.values()))
    # Separate unbounded symbolic-candidate comparisons over a larger finite range.
    extra = 0
    for A in range(3,17):
        for B in range(3,17):
            for C in range(A*B+1):
                assert len(set(candidate_words(A,B,C).values())) == formula(A,B,C)
                extra += 1
    print(f'VERIFY_OK: {exact_words} direct words, {exact_classes} Parikh fibers, '
          f'{extra} additional candidate-fiber comparisons')

if __name__ == '__main__':
    verify()
