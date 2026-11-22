"""Finite trace tests for zero-padded factors of mechanical binary words.

Rational rotations are used solely as reproducible finite tests; the
irrational-slope universal statements require the geometric proof.
Run: python verify.py
"""
from itertools import combinations
from fractions import Fraction
from math import comb


def subset_patterns(word_masks, support):
    patterns = set()
    for word in word_masks:
        pat = 0
        for bit, pos in enumerate(support):
            pat |= ((word >> pos) & 1) << bit
        patterns.add(pat)
    return patterns


def exists_region(p, q, support, chosen):
    # Check a required trace on three arcs using exact rational circle cells.
    # All endpoints in units 1/q; a midpoint lies in each open cell.
    endpoints = set()
    for j in support:
        endpoints.add((-j*p) % q)
        endpoints.add((p-j*p) % q)
    ordered = sorted(endpoints)
    for lo, hi in zip(ordered, ordered[1:] + [ordered[0] + q]):
        x2 = lo + hi  # coordinate in units of 1/(2q)
        trace = tuple(int(((x2 + 2*j*p) % (2*q)) < 2*p) for j in support)
        if trace == chosen:
            return True
    return False


def predicted(p, q, support, padded=True):
    n = len(support)
    if n <= 1:
        return True
    if not padded:
        if n >= 3:
            return False
        d = ((support[1]-support[0])*p) % q
        return min(d, q-d) < min(p, q-p)
    if n >= 4:
        return False
    if n == 2:
        if 2*p > q:
            return True
        d = ((support[1]-support[0])*p) % q
        return min(d, q-d) < p
    if 2*p < q:
        return False
    # The largest coordinate is positive only for full-length factors.
    return all(exists_region(p, q, support, (a,b,1))
               for a in (0,1) for b in (0,1))


def verify_case(p, q, horizon):
    assert 0 < p < q and 2*p != q and horizon < q
    full, padded = set(), set()
    for t in range(q):
        word = sum((int(((t+j)*p) % q < p) << j) for j in range(horizon))
        full.add(word)
        padded.add(word)
        for j in range(horizon-1, -1, -1):
            word &= ~(1 << j)
            padded.add(word)
    count = 0
    counts = {i:0 for i in range(5)}
    for r in range(5):
        for support in combinations(range(horizon), r):
            full_actual = len(subset_patterns(full, support)) == 2**r
            padded_actual = len(subset_patterns(padded, support)) == 2**r
            assert full_actual == predicted(p, q, support, False), (p,q,support,'fixed')
            assert padded_actual == predicted(p, q, support, True), (p,q,support,'padded')
            count += 2
            counts[r] += int(padded_actual)
    return count, counts


def main():
    parameters = [(233,610,12),(377,610,12),(5,17,10),(12,17,10),
                  (7,23,10),(16,23,10),(13,34,10),(21,34,10)]
    total=0
    for p,q,h in parameters:
        count, c = verify_case(p,q,h)
        total+=count
        print(f'{p}/{q}, horizon={h}: {count} exact comparisons; padded face counts {c}')
    print('PASS:', total, 'comparisons of independently enumerated and geometry-predicted traces')


if __name__=='__main__':
    main()
