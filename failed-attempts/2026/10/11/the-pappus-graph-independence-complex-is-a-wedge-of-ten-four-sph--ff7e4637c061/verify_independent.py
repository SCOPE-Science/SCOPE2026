#!/usr/bin/env python3
"""Independent incidence-presentation homology and combinatorial checks."""
from collections import defaultdict
import json

LINES = [(0, 1, 2), (3, 4, 5), (0, 4, 6), (3, 1, 6),
         (0, 5, 7), (3, 2, 7), (1, 5, 8), (4, 2, 8), (6, 7, 8)]
N = 18

def faces_by_size():
    e = {tuple(sorted((i, 9 + j))) for j, row in enumerate(LINES) for i in row}
    assert len(e) == 27
    assert [sum(i in row for row in LINES) for i in range(9)] == [3] * 9
    faces = [[] for _ in range(10)]
    for m in range(1 << N):
        if any(m & (1 << i) and m & (1 << j) for i, j in e):
            continue
        faces[m.bit_count()].append(m)
    assert [len(x) for x in faces] == [1, 18, 126, 438, 801, 756, 348, 90, 18, 2]
    return faces

def rank_mod_p(low, high, p):
    positions = {face: i for i, face in enumerate(low)}
    pivots = {}
    for mask in high:
        col = {}
        elems = [i for i in range(N) if mask & (1 << i)]
        for parity, i in enumerate(elems):
            row = positions[mask ^ (1 << i)]
            col[row] = 1 if parity % 2 == 0 else (p - 1)
        while col:
            pivot = min(col)
            if pivot not in pivots:
                invert = pow(col[pivot], -1, p)
                pivots[pivot] = {r: (v * invert) % p for r, v in col.items()}
                break
            coeff = col[pivot]
            for r, v in pivots[pivot].items():
                value = (col.get(r, 0) - coeff * v) % p
                if value:
                    col[r] = value
                elif r in col:
                    del col[r]
    return len(pivots)

def main():
    levels = faces_by_size()
    summary = {}
    for p in (2, 3):
        # Unaugmented simplicial boundaries C_i -> C_{i-1} for i >= 1.
        ranks = [0] + [rank_mod_p(levels[k - 1], levels[k], p) for k in range(2, len(levels))] + [0]
        # ranks[k-1] = rank boundary C_{k-1} -> C_{k-2}; ranks[0]=0.
        betti = [len(levels[k]) - ranks[k - 1] - ranks[k] for k in range(1, len(levels))]
        assert betti == [1, 0, 0, 0, 10, 0, 0, 0, 0], (p, ranks, betti)
        summary[str(p)] = {'boundary_ranks_d1_to_d8': ranks[1:-1], 'betti_d0_to_d8': betti}
    print(json.dumps({'result': 'PASS', 'f_vector': [len(x) for x in levels[1:]],
                      'finite_field_checks': summary}, sort_keys=True))

if __name__ == '__main__':
    main()
