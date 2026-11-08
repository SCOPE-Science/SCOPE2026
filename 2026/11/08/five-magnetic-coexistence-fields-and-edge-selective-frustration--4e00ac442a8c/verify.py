#!/usr/bin/env python3
"""Exact finite-state check for the 3-color Chvatal-graph antiferromagnet.

Uses only the Python standard library. The two independent traversals
encode color assignments differently: ternary words versus zero-color
subsets followed by binary assignments on the complement.
"""
from collections import Counter
import csv
from pathlib import Path
from fractions import Fraction
from itertools import product

NEIGHBORS = {
    0: (1, 4, 6, 9), 1: (2, 5, 7), 2: (3, 6, 8),
    3: (4, 7, 9), 4: (5, 8), 5: (10, 11),
    6: (10, 11), 7: (8, 11), 8: (10,), 9: (10, 11),
}
EDGES = tuple(sorted((i, j) for i, js in NEIGHBORS.items() for j in js))
EXPECTED = ((4,4), (3,32), (2,124), (1,96), (1,312), (1,96),
            (2,64), (5,448), (8,320), (12,416), (16,168),
            (20,24), (24,1))
EXPECTED_DEFECT = (42,42,24,24,24,42,24,0,30,6,24,6,
                   30,42,24,24,24,6,0,0,30,30,0,6)
CROSSINGS = (Fraction(-1), Fraction(0), Fraction(1),
             Fraction(3), Fraction(4))
ACTIVE_K = (0,3,5,6,8,12)


def record(table, k, e):
    if e < table[k][0]:
        table[k] = [e, 1]
    elif e == table[k][0]:
        table[k][1] += 1


def ternary_census():
    table = [[1000, 0] for _ in range(13)]
    defect = Counter()
    num = 0
    for spins in product(range(3), repeat=12):
        k = sum(s == 0 for s in spins)
        bad = [edge for edge in EDGES if spins[edge[0]] == spins[edge[1]]]
        record(table, k, len(bad))
        if len(bad) == 1:
            defect[bad[0]] += 1
        num += 1
    return tuple(map(tuple, table)), tuple(defect[edge] for edge in EDGES), num


def subset_binary_census():
    # Each coloring corresponds bijectively to one zero-color subset S
    # and one 0/1 binary assignment on its complement.
    table = [[1000, 0] for _ in range(13)]
    defect = Counter()
    num = 0
    for zero_mask in range(1 << 12):
        k = zero_mask.bit_count()
        complement = [v for v in range(12) if not ((zero_mask >> v) & 1)]
        for two_mask in range(1 << len(complement)):
            color = [0] * 12
            for bit, v in enumerate(complement):
                color[v] = 1 + ((two_mask >> bit) & 1)
            bad_count = 0
            bad_edge = None
            for edge in EDGES:
                i, j = edge
                if color[i] == color[j]:
                    bad_count += 1
                    bad_edge = edge
            record(table, k, bad_count)
            if bad_count == 1:
                defect[bad_edge] += 1
            num += 1
    return tuple(map(tuple, table)), tuple(defect[edge] for edge in EDGES), num


def exact_ground(x, table):
    values = [Fraction(e) - x*k for k, (e, _) in enumerate(table)]
    minimum = min(values)
    indices = tuple(k for k, value in enumerate(values) if value == minimum)
    return minimum, indices, sum(table[k][1] for k in indices)


def check():
    assert len(EDGES) == 24 and len(set(EDGES)) == 24
    assert all(u < v for u, v in EDGES)
    assert all(sum(v in edge for edge in EDGES) == 4 for v in range(12))
    assert all(not ({u, v, w} <= {a for edge in EDGES for a in edge}) or
                   not ((min(u,v),max(u,v)) in EDGES and
                        (min(u,w),max(u,w)) in EDGES and
                        (min(v,w),max(v,w)) in EDGES)
               for u in range(12) for v in range(u+1,12)
               for w in range(v+1,12))
    a = ternary_census()
    b = subset_binary_census()
    assert a == b
    table, defects, num = a
    assert num == 3**12 == 531441
    assert table == EXPECTED
    assert defects == EXPECTED_DEFECT
    root = Path(__file__).resolve().parent
    with (root / 'SECTOR_COUNTS.csv').open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 13
    for k, row in enumerate(rows):
        assert int(row['favored_color_count']) == k
        assert (int(row['minimum_monochromatic_edges']),
                int(row['attaining_labeled_configurations'])) == table[k]
    with (root / 'EDGE_DEFECT_COUNTS.csv').open(newline='', encoding='utf-8') as f:
        erows = list(csv.DictReader(f))
    assert len(erows) == 24
    for edge, cnt, row in zip(EDGES, defects, erows):
        assert (int(row['edge_u']), int(row['edge_v'])) == edge
        assert int(row['zero_field_unique_monochromatic_bond_configurations']) == cnt
    assert sum(defects) == 504
    assert tuple(EDGES[i] for i, t in enumerate(defects) if t == 0) == (
        (2,3), (6,11), (7,8), (9,10))
    # Exact convex lower-hull slopes. Every sector is on a hull face.
    slopes = tuple(Fraction(table[k+1][0] - table[k][0]) for k in range(12))
    assert slopes == (-1,-1,-1,0,0,1,3,3,4,4,4,4)
    assert slopes == tuple(sorted(slopes))
    assert tuple(k for k in range(1,12) if slopes[k-1] != slopes[k]) == (3,5,6,8)
    assert tuple(sorted(set(slopes))) == CROSSINGS
    fields = (Fraction(-2), Fraction(-1), Fraction(-1,2),
              Fraction(0), Fraction(1,2), Fraction(1),
              Fraction(2), Fraction(3), Fraction(7,2),
              Fraction(4), Fraction(5))
    expected_winners = ((0,), tuple(range(4)), (3,), (3,4,5), (5,),
                        (5,6), (6,), (6,7,8), (8,),
                        tuple(range(8,13)), (12,))
    expected_counts = (4,256,96,504,96,160,64,832,320,929,1)
    for x, ks, n in zip(fields, expected_winners, expected_counts):
        e, who, count = exact_ground(x, table)
        assert who == ks and count == n, (x, e, who, count)
    # Rational strict witnesses for each of the six unique open branches.
    assert [exact_ground(x, table)[1] for x in (-2, Fraction(-1,2),
             Fraction(1,2), 2, Fraction(7,2), 5)] == [
                 (0,), (3,), (5,), (6,), (8,), (12,)]
    print('PASS: two complete, independent enumerations of', num, 'states')
    print('PASS: 13 sector minima/counts, 24 defect-edge counts, exact convex envelope')
    print('PASS: 5 coexistence fields, 6 strict field regimes, 11 rational field tests')
    print('sector table: k:e:deg')
    print(' '.join(f'{k}:{e}:{c}' for k,(e,c) in enumerate(table)))
    print('zero-defect-support edges:', [EDGES[i] for i,t in enumerate(defects) if t == 0])


if __name__ == '__main__':
    check()
