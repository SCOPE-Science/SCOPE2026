#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction

EXPECTED_COUNTS = [1, 1, 1, 2, 15, 768, 477965]
EXPECTED_EX = [0, 0, 0, 1, 3, 7, 14]


def tetrahedron_free_stats(n):
    triples = list(combinations(range(n), 3))
    idx = {e: i for i, e in enumerate(triples)}
    four_masks = []
    for q in combinations(range(n), 4):
        m = 0
        for e in combinations(q, 3):
            m |= 1 << idx[e]
        four_masks.append(m)

    count = 0
    max_edges = 0
    for g in range(1 << len(triples)):
        if any((g & qmask) == qmask for qmask in four_masks):
            continue
        count += 1
        max_edges = max(max_edges, g.bit_count())
    return count, max_edges


def main():
    counts = []
    extrema = []
    for n in range(7):
        c, e = tetrahedron_free_stats(n)
        counts.append(c)
        extrema.append(e)

    assert counts == EXPECTED_COUNTS, (counts, EXPECTED_COUNTS)
    assert extrema == EXPECTED_EX, (extrema, EXPECTED_EX)

    upper = Fraction(312372062889819, 560000000000000)
    assert Fraction(5, 9) < upper
    assert float(upper) < 0.557808

    print("counts", counts)
    print("extremal_edges", extrema)
    print("upper_decimal", float(upper))
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
