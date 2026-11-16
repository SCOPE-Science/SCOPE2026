#!/usr/bin/env python3
"""Exact independent tests of the signed derangement permanent at order five.

No external dependencies. All data and arithmetic are integers. This is a
finite enumeration certificate; the all-order parity theorem has a separate proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations

N = 5
TREE = {(0, j) for j in range(1, N)} | {(i, 0) for i in range(1, N)} | {(1, 2)}
EDGES = {(i, j) for i in range(N) for j in range(N) if i != j}
CHORDS = sorted(EDGES - TREE)
DERANGEMENTS = [p for p in permutations(range(N)) if all(i != p[i] for i in range(N))]
assert len(TREE) == 9 and len(CHORDS) == 11 and len(DERANGEMENTS) == 44
CHORD_BIT = {e: k for k, e in enumerate(CHORDS)}
PERM_MASKS = [sum(1 << CHORD_BIT[e] for e in ((i,p[i]) for i in range(N)) if e in CHORD_BIT)
              for p in DERANGEMENTS]
SIZE = 1 << len(CHORDS)
EXPECTED_ABS = {0:338, 2:504, 4:405, 6:260, 8:130,
                10:240, 12:90, 16:60, 22:20, 44:1}
EXPECTED_PROJECTION = {6:960, 10:360, 14:44, 18:70, 22:360,
                       26:240, 46:12, 338:1, 1710:1}


def sign_permanent_by_ryser(chord_mask):
    # Independent inclusion--exclusion over subsets of columns, with
    # zero diagonal and +1 tree edges.
    rows = []
    for i in range(N):
        row = []
        for j in range(N):
            if i == j:
                row.append(0)
            elif (i, j) in TREE:
                row.append(1)
            else:
                row.append(-1 if (chord_mask >> CHORD_BIT[(i,j)]) & 1 else 1)
        rows.append(row)
    permanent = 0
    for s in range(1, 1 << N):
        term = -1 if (N - s.bit_count()) % 2 else 1
        for row in rows:
            term *= sum(row[j] for j in range(N) if (s >> j) & 1)
        permanent += term
    return permanent


def hadamard_in_place(v):
    h = 1
    while h < len(v):
        for start in range(0, len(v), 2 * h):
            for j in range(start, start + h):
                a, b = v[j], v[j+h]
                v[j], v[j+h] = a + b, a - b
        h *= 2


def main():
    signed = []
    for s in range(SIZE):
        direct = sum(1 - 2*((s & p).bit_count() % 2) for p in PERM_MASKS)
        ryser = sign_permanent_by_ryser(s)
        assert direct == ryser, (s, direct, ryser)
        signed.append(direct)

    abshist = Counter(map(abs, signed))
    assert dict(abshist) == EXPECTED_ABS, abshist
    assert sum(abshist.values()) == SIZE
    assert sum(t*t*c for t,c in abshist.items()) == SIZE*len(DERANGEMENTS)
    assert 2 == min(abs(x) for x in signed if x)

    support = [int(t != 0) for t in signed]
    assert sum(support) == 1710
    hadamard_in_place(support)
    kernel_hist = Counter(map(abs,support))
    assert dict(kernel_hist) == EXPECTED_PROJECTION, kernel_hist
    assert sum(x*x for x in support) == SIZE*1710
    assert sum(map(abs,support)) == 27996
    assert Fraction(sum(map(abs,support)), SIZE) == Fraction(6999,512)
    # Independent direct character sums for the entire 2^11 dual group.
    admissible = [s for s in range(SIZE) if signed[s] != 0]
    for t in range(SIZE):
        direct = sum(1-2*((t & s).bit_count()%2) for s in admissible)
        assert support[t] == direct, (t, support[t], direct)

    assert 338*(1<<14) == 5537792
    assert 1710*(1<<14) == 28016640
    assert 5537792+28016640 == 1<<25
    print('DERANGEMENT5_WALSH_PROJECTOR_PASS cases=2048 rank=28016640 projection=6999/512')

if __name__ == '__main__':
    main()
