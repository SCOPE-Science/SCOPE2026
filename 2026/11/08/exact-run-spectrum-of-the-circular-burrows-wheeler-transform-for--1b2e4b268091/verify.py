"""Reproduce finite checks for the binary weight-three circular BWT-run law.

Requires Python 3.9+. Only standard-library modules are used.
"""
from collections import Counter
from itertools import combinations
from math import comb


def bwt_direct(word):
    rotations = [word[i:] + word[:i] for i in range(len(word))]
    return ''.join(rotation[-1] for rotation in sorted(rotations))


def from_gaps(gaps):
    out = []
    for t in range(max(gaps), -1, -1):
        valid = [i for i in range(3) if gaps[i] >= t]
        valid.sort(key=lambda i: (gaps[(i+1) % 3],
                                  gaps[(i+2) % 3], gaps[i]), reverse=True)
        out.extend('1' if gaps[i] == t else '0' for i in valid)
    return ''.join(out)


def run_count(word):
    return 1 + sum(a != b for a, b in zip(word, word[1:]))


def theoretical_counts(n):
    assert n >= 4
    if n % 3 == 0:
        return {2: n // 3, 4: n * (n - 3),
                6: n * (n - 3) * (n - 6) // 6}
    return {2: n, 4: n * (n - 4),
            6: n * (n - 4) * (n - 5) // 6}


def classify(g):
    x, y, z = sorted(g)
    if z - x <= 1:
        return 2
    if x == y or y == z:
        return 4
    close_xy = (y == x + 1 and
                tuple(g) in {(x,z,y), (z,y,x), (y,x,z)})
    close_yz = (z == y + 1 and
                tuple(g) in {(x,y,z), (y,z,x), (z,x,y)})
    return 4 if close_xy or close_yz else 6


def check():
    triples = 0
    for s in range(1, 36):
        observed = Counter()
        for a in range(s + 1):
            for b in range(s - a + 1):
                c = s - a - b
                g = (a, b, c)
                w = '1' + '0' * a + '1' + '0' * b + '1' + '0' * c
                direct = bwt_direct(w)
                gap_result = from_gaps(g)
                assert direct == gap_result, (g, direct, gap_result)
                r = run_count(direct)
                assert r == classify(g), (g, direct, r)
                observed[r] += 1
                triples += 1
        expected = {2: 1 if s % 3 == 0 else 3,
                    4: 3 * s - (0 if s % 3 == 0 else 3)}
        expected[6] = comb(s + 2, 2) - expected[2] - expected[4]
        assert observed == Counter({k:v for k,v in expected.items() if v}), (s,observed,expected)
    print('GAP_BWT_AND_CLASSIFICATION_OK', triples)

    labeled = 0
    for n in range(4, 24):
        hist = Counter()
        for positions in combinations(range(n), 3):
            w = ''.join('1' if i in positions else '0' for i in range(n))
            hist[run_count(bwt_direct(w))] += 1
            labeled += 1
        exp = theoretical_counts(n)
        assert sum(exp.values()) == comb(n,3)
        assert hist == Counter({k:v for k,v in exp.items() if v}), (n,hist,exp)
    print('INDEPENDENT_INDEXED_WORD_CENSUS_OK', labeled)
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    check()
