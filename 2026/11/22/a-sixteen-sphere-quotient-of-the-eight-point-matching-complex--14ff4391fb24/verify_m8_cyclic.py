#!/usr/bin/env python3
"""Exact integral homology computation for the eight-point matching-complex
quotient under cyclic rotation. Python standard library only.

The simplices are chains of nonempty matchings, i.e. cells of the
barycentric subdivision. Quotient cells are orbits of such chains.
Boundary signs are determined by deleting positions in a chain.
Integer row-column elimination uses only pivots +1/-1, so each step
is a chain-equivalence over the integers, retaining all torsion data.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations

N = 8
EDGES = list(combinations(range(N), 2))
EDGE_IDS = {e: i for i, e in enumerate(EDGES)}


def rotate_edge(eid, t):
    u, v = EDGES[eid]
    return EDGE_IDS[tuple(sorted(((u + t) % N, (v + t) % N)))]


@lru_cache(maxsize=None)
def canonical(chain):
    return min(
        tuple(tuple(sorted(rotate_edge(e, t) for e in matching))
              for matching in chain)
        for t in range(N)
    )


def nonempty_matchings():
    by_cardinality = []
    for size in range(1, N // 2 + 1):
        matchings = []
        for choice in combinations(range(len(EDGES)), size):
            endpoints = [v for e in choice for v in EDGES[e]]
            if len(set(endpoints)) == 2 * size:
                matchings.append(choice)
        by_cardinality.append(matchings)
    return by_cardinality


def quotient_chain_complex():
    by_cardinality = nonempty_matchings()
    assert tuple(map(len, by_cardinality)) == (28, 210, 420, 105)
    cells = [set() for _ in range(4)]

    @lru_cache(maxsize=None)
    def proper_nonempty_subsets(matching):
        return tuple(s for k in range(1, len(matching))
                     for s in combinations(matching, k))

    def descend(matching, chain_above):
        chain = (matching,) + chain_above
        cells[len(chain) - 1].add(canonical(chain))
        for proper in proper_nonempty_subsets(matching):
            descend(proper, chain)

    for group in by_cardinality:
        for matching in group:
            descend(matching, ())

    cells = [sorted(group) for group in cells]
    index = [{c: i for i, c in enumerate(group)} for group in cells]
    differential = {}
    for degree in (1, 2, 3):
        columns = {}
        for j, chain in enumerate(cells[degree]):
            entries = defaultdict(int)
            for deleted in range(degree + 1):
                face = chain[:deleted] + chain[deleted + 1:]
                entries[index[degree - 1][canonical(face)]] += (-1) ** deleted
            columns[j] = {i: v for i, v in entries.items() if v}
        differential[degree] = columns
    assert tuple(map(len, cells)) == (107, 576, 804, 318)
    for degree in (2, 3):
        for col in differential[degree].values():
            image = defaultdict(int)
            for row, v in col.items():
                for lower_row, w in differential[degree - 1][row].items():
                    image[lower_row] += v * w
            assert all(v == 0 for v in image.values())
    return cells, differential


def rank_mod_prime(columns, prime):
    pivots = {}
    for initial in columns.values():
        col = {i: v % prime for i, v in initial.items() if v % prime}
        while col:
            row = min(col)
            if row not in pivots:
                inverse = pow(col[row], -1, prime)
                pivots[row] = {i: (v * inverse) % prime for i, v in col.items()
                               if (v * inverse) % prime}
                break
            factor = col[row]
            for i, v in pivots[row].items():
                result = (col.get(i, 0) - factor * v) % prime
                if result:
                    col[i] = result
                else:
                    col.pop(i, None)
    return len(pivots)


def integral_unit_contractions(input_matrices, counts):
    boundary = {k: {j: dict(col) for j, col in input_matrices[k].items()}
                for k in (1, 2, 3)}
    cofaces = {k: defaultdict(dict) for k in (1, 2, 3)}
    for k in (1, 2, 3):
        for col, rows in boundary[k].items():
            for row, v in rows.items():
                cofaces[k][row][col] = v
    live = [set(range(c)) for c in counts]
    cancellations = Counter()
    while True:
        choice = None
        for degree in (1, 2, 3):
            for col, rows in boundary[degree].items():
                for row, v in rows.items():
                    if v not in (1, -1):
                        continue
                    cost = (len(rows) - 1) * (len(cofaces[degree][row]) - 1)
                    candidate = (cost, len(rows) + len(cofaces[degree][row]),
                                 degree, row, col)
                    if choice is None or candidate < choice:
                        choice = candidate
        if choice is None:
            break
        _, _, degree, row, col = choice
        pivot = boundary[degree][col][row]
        pivot_column = dict(boundary[degree][col])
        pivot_row = dict(cofaces[degree][row])
        for other_col, coefficient in pivot_row.items():
            if other_col == col:
                continue
            multiple = coefficient // pivot
            for other_row, value in pivot_column.items():
                if other_row == row:
                    continue
                result = boundary[degree][other_col].get(other_row, 0) - multiple * value
                if result:
                    boundary[degree][other_col][other_row] = result
                    cofaces[degree][other_row][other_col] = result
                else:
                    boundary[degree][other_col].pop(other_row, None)
                    cofaces[degree][other_row].pop(other_col, None)
        for other_col in list(cofaces[degree][row]):
            boundary[degree][other_col].pop(row, None)
        cofaces[degree].pop(row, None)
        for other_row in list(boundary[degree][col]):
            cofaces[degree][other_row].pop(col, None)
        boundary[degree].pop(col)
        if degree < 3:
            for other_col in list(cofaces[degree + 1][col]):
                boundary[degree + 1][other_col].pop(col, None)
            cofaces[degree + 1].pop(col, None)
        if degree > 1:
            for other_row in list(boundary[degree - 1][row]):
                cofaces[degree - 1][other_row].pop(row, None)
            boundary[degree - 1].pop(row)
        live[degree].remove(col)
        live[degree - 1].remove(row)
        cancellations[degree] += 1
    reduced_counts = tuple(map(len, live))
    assert reduced_counts == (1, 0, 16, 0)
    assert tuple(cancellations[k] for k in (1, 2, 3)) == (106, 470, 318)
    assert all(not col for k in boundary for col in boundary[k].values())
    return reduced_counts, tuple(cancellations[k] for k in (1, 2, 3))


def main():
    cells, differential = quotient_chain_complex()
    counts = tuple(map(len, cells))
    ranks = [tuple(rank_mod_prime(differential[k], p) for k in (1, 2, 3))
             for p in (2, 3, 5, 7, 11, 101)]
    assert all(x == (106, 470, 318) for x in ranks)
    reduced, pivots = integral_unit_contractions(differential, counts)
    # The antipodal matching is fixed as a set by every rotation.
    opposite = tuple(sorted(EDGE_IDS[(i, i + 4)] for i in range(4)))
    assert all(tuple(sorted(rotate_edge(e, t) for e in opposite)) == opposite
               for t in range(8))
    print('matching_faces:', (28, 210, 420, 105))
    print('quotient_barycentric_cells:', counts)
    print('differential_ranks_mod_2_3_5_7_11_101:', ranks)
    print('integral_unit_cancellations:', pivots)
    print('remaining_chain_counts:', reduced)
    print('euler_characteristic:', sum((-1) ** i * v for i, v in enumerate(counts)))
    print('M8_ROTATION_QUOTIENT_INTEGRAL_CHECKS_OK')


if __name__ == '__main__':
    main()
