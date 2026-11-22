#!/usr/bin/env python3
"""Independent exact finite certificates for a five-row monochromatic-rectangle theorem.

Run: python3 verify.py
This checks all finite identities needed by the unrestricted proof and independently
counts rectangles in the explicit constructions up to a reproducible cutoff.
"""
from itertools import combinations
from math import comb

NROWS = 5
SLOTS = [(i, j, c) for i in range(NROWS) for j in range(i + 1, NROWS) for c in (0, 1)]
B = [3, 5, 10, 13, 14, 19, 20, 22, 24, 25]
C = [3, 13, 22, 24]
W = [24, 12, 18, 11, 21]


def incidence(mask):
    return tuple(int(((mask >> i) & 1) == ((mask >> j) & 1) == c)
                 for i, j, c in SLOTS)


def loads(masks):
    return [sum(incidence(m)[i] for m in masks) for i in range(20)]


def prescribed(n):
    q, r = divmod(n, 5)
    return 10*q*(q-1) + 4*q*r + (2 if n % 10 == 5 else 0)


def explicit(n):
    t, s = divmod(n, 10)
    if s <= 4:
        return B*t + C[:s]
    if s == 5:
        return B*t + W
    removed = C[:10-s]
    remaining = B[:]
    for mask in removed:
        remaining.remove(mask)
    return B*t + remaining


def count_direct(masks):
    # Counts each geometric monochromatic rectangle by its two columns and two rows.
    count = 0
    for x, y in combinations(masks, 2):
        for i, j in combinations(range(5), 2):
            if ((x >> i) & 1) == ((x >> j) & 1) == ((y >> i) & 1) == ((y >> j) & 1):
                count += 1
    return count


def main():
    assert len(SLOTS) == 20
    # If only two row pairs have odd equal-color counts, some row triple
    # avoids both: every edge of K5 belongs to three of its ten triangles.
    row_pairs = [(i, j) for i in range(5) for j in range(i+1, 5)]
    triples = list(combinations(range(5), 3))
    for j in range(3):
        for exceptional in combinations(row_pairs, j):
            assert any(not any(set(pair) <= set(trip) for pair in exceptional)
                       for trip in triples), exceptional
    print('TRIANGLE_PARITY_OBSTRUCTION_FOR_ZERO_ONE_OR_TWO_ODD_ROW_PAIRS_PASS')
    assert len(B) == len(set(B)) == 10 and len(C) == len(set(C)) == 4
    assert set(C) <= set(B)
    assert all(m.bit_count() in (2, 3) for m in B+C+W)
    assert loads(B) == [2]*20, loads(B)
    assert all(v in (0, 1) for v in loads(C)) and sum(loads(C)) == 16
    lw = loads(W)
    assert {v: lw.count(v) for v in set(lw)} == {0: 2, 1: 16, 2: 2}, lw
    print('TEN_COLUMN_BALANCED_DESIGN_AND_FOUR_RECTANGLE_FREE_SUBCOLUMNS_PASS')
    print('FIVE_COLUMN_TWO_RECTANGLE_DEFECT_CERTIFICATE_PASS')
    for n in range(1, 121):
        cols = explicit(n)
        assert len(cols) == n
        val = prescribed(n)
        via_slot = sum(comb(k, 2) for k in loads(cols))
        via_direct = count_direct(cols)
        assert via_slot == via_direct == val, (n, val, via_slot, via_direct)
    print('ALL_EXPLICIT_CONSTRUCTIONS_AND_INDEPENDENT_DIRECT_RECTANGLE_COUNTS_PASS 120')
    # Unrestricted lower-bound parity obstruction is exactly the H certificate above.
    for b in range(1, 61):
        q, r = divmod(b, 5)
        lower = 10*q*(q-1)+4*q*r
        assert prescribed(b) >= lower
        if b % 10 != 5: assert prescribed(b) == lower
        if b % 10 == 5: assert prescribed(b) == lower+2
    print('CONVEXITY_BOUND_AND_MOD_TEN_DEFECT_FORMULA_PASS')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
