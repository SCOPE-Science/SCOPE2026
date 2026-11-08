"""Independent finite tests for the exact Parikh-pair distribution of maximally universal binary words.

Run: python3 checker.py
Pure Python 3 standard library, no external input.
These finite tests support but do not replace the all-parameter proof.
"""
from itertools import combinations, product
from math import comb
from collections import defaultdict


def formula(k, r):
    """Coefficients indexed by C, via truncated formal-product multiplication."""
    T = k * (k - 1) // 2
    # (used_extra_a, additional_ab_pairs) -> multiplicity, after the k arches
    d = {(0, 0): 1}
    for j in range(k, 0, -1):
        nxt = defaultdict(int)
        for (m, e), count in d.items():
            # ba arch: no additional a
            nxt[(m, e)] += count
            # a^(u+1)b arch: u additional a; its b counts as +1
            for u in range(r - m + 1):
                nxt[(m + u, e + 1 + u * j)] += count
        d = nxt
    poly = defaultdict(int)
    # the unused extra a all trail the last arch: zero ab contribution
    for (m, e), count in d.items():
        assert m <= r
        poly[T + e] += count
    return dict(poly)


def is_subseq(s, w):
    i = 0
    for x in w:
        if i < len(s) and x == s[i]:
            i += 1
    return i == len(s)


def brute(k, r):
    A = k + r
    B = k
    n = A + B
    all_targets = [''.join(t) for t in product('ab', repeat=k)]
    poly = defaultdict(int)
    for apos in combinations(range(n), A):
        word = ['b'] * n
        for i in apos:
            word[i] = 'a'
        w = ''.join(word)
        if all(is_subseq(t, w) for t in all_targets):
            before_a = c = 0
            for x in w:
                if x == 'a':
                    before_a += 1
                else:
                    c += before_a
            poly[c] += 1
    return dict(poly)


def coefficient(p, c):
    return p.get(c, 0)


def main():
    cases = words = totals = edges = symmetries = 0
    for k in range(1, 6):
        for r in range(0, 5):
            f = formula(k, r)
            b = brute(k, r)
            assert f == b, (k, r, f, b)
            cases += 1
            words += comb(2 * k + r, k)
            n = k * (k + r)
            assert sum(f.values()) == sum(comb(k, j) * comb(r + j, j)
                                           for j in range(k+1))
            totals += 1
            for c, v in f.items():
                assert f.get(n - c, 0) == v, (k, r, c)
                symmetries += 1
            if k >= 2:
                T = k * (k - 1) // 2
                expected = [1, k, comb(k, 2) + (r >= 1),
                            comb(k, 3) + (k if r >= 1 else 0)
                            + (1 if r >= 2 else 0)]
                for e, val in enumerate(expected):
                    assert coefficient(f, T + e) == val, (k, r, e, f)
                    edges += 1
    example = [coefficient(formula(4, 1), c) for c in range(6, 15)]
    assert example == [1, 4, 7, 8, 8, 8, 7, 4, 1]
    print(f'PASS: {cases} independent parameter cases, '
          f'{words} enumerated binary words, {totals} unweighted totals, '
          f'{symmetries} reciprocal coefficients, {edges} edge coefficients')
    print('PASS: k=4, r=1, C=6..14:', example)


if __name__ == '__main__':
    main()
