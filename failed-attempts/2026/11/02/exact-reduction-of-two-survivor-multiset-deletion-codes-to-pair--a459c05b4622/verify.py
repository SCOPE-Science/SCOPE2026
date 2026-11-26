#!/usr/bin/env python3
"""Independent finite checks of two-survivor multiset coding and block packing.

Requires numpy and scipy. The proof of the all-parameter theorem is symbolic;
these optimization checks are finite corroboration only.
"""

from itertools import combinations
from math import comb
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix


def compositions(total, width):
    if width == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for suffix in compositions(total - first, width - 1):
                yield (first,) + suffix


def exact_independent_cardinality(q, n):
    words = list(compositions(n, q))
    edges = [(i, j) for i in range(len(words))
             for j in range(i)
             if sum(min(x, y) for x, y in zip(words[i], words[j])) >= 2]
    if not edges:
        return len(words), 0
    row = np.repeat(np.arange(len(edges)), 2)
    col = np.asarray(edges, dtype=int).flatten()
    matrix = coo_matrix((np.ones(len(col)), (row, col)),
                        shape=(len(edges), len(words))).tocsr()
    response = milp(-np.ones(len(words)),
                    integrality=np.ones(len(words)),
                    bounds=Bounds(0, 1),
                    constraints=LinearConstraint(matrix, 0, 1),
                    options={'mip_rel_gap': 0.0, 'time_limit': 45.0})
    if response.status != 0 or response.mip_gap != 0:
        raise RuntimeError(f'Unproved code optimum q={q}, n={n}: {response.message}')
    optimum = int(round(-response.fun))
    assert abs(-response.fun - optimum) < 1e-6
    return optimum, len(edges)


def exact_block_packing(q, n):
    if n > q:
        return 0
    blocks = list(combinations(range(q), n))
    if n == 2:
        return len(blocks)
    rows = list(combinations(range(q), 2))
    pair_to_row = {p: i for i, p in enumerate(rows)}
    pairs = [(pair_to_row[p], j)
             for j, block in enumerate(blocks)
             for p in combinations(block, 2)]
    matrix = coo_matrix((np.ones(len(pairs)),
                         ([i for i, j in pairs], [j for i, j in pairs])),
                        shape=(len(rows), len(blocks))).tocsr()
    result = milp(-np.ones(len(blocks)),
                  integrality=np.ones(len(blocks)),
                  bounds=Bounds(0, 1),
                  constraints=LinearConstraint(matrix, 0, 1),
                  options={'mip_rel_gap': 0.0, 'time_limit': 45.0})
    if result.status != 0 or result.mip_gap != 0:
        raise RuntimeError(f'Unproved packing optimum q={q}, n={n}: {result.message}')
    optimum = int(round(-result.fun))
    assert abs(-result.fun - optimum) < 1e-6
    return optimum


def triple_packing_formula(q):
    if q < 3:
        return 0
    r = q % 6
    if r in (1, 3):
        return q * (q - 1) // 6
    if r in (0, 2):
        return q * (q - 2) // 6
    if r == 4:
        return (q * (q - 2) - 2) // 6
    return (q * (q - 1) - 8) // 6


def main():
    cases = [(2, 2), (3, 2), (4, 2),
             (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3),
             (3, 4), (4, 4), (5, 4), (6, 4),
             (4, 5), (5, 5), (6, 5)]
    for q, n in cases:
        observed, conflict_edges = exact_independent_cardinality(q, n)
        packing = exact_block_packing(q, n)
        expected = q + packing
        assert observed == expected, (q, n, observed, expected)
        if n == 3:
            assert packing == triple_packing_formula(q)
        print(f'q={q:2} n={n:2} code={observed:2} packing={packing:2} '
              f'conflicts={conflict_edges:5} equality=PASS')
    print(f'ALL {len(cases)} finite optimization comparisons PASSED')


if __name__ == '__main__':
    main()
