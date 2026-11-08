#!/usr/bin/env python3
"""Exact finite vertex certification for one-step bounded-confidence gap bounds."""
from itertools import combinations, product
from fractions import Fraction

EXPECTED = {2: Fraction(0), 3: Fraction(1, 2), 4: Fraction(1),
            5: Fraction(5, 4), 6: Fraction(3, 2)}
EXPECTED_CELLS = {2: 1, 3: 2, 4: 8, 5: 55, 6: 549}
EXPECTED_TESTS = {2: 2, 3: 12, 4: 78, 5: 616, 6: 6150}


def update(x):
    n = len(x)
    return tuple(sum((x[j] for j in range(n) if abs(x[j] - x[i]) <= 1),
                     Fraction(0)) /
                 sum(1 for j in range(n) if abs(x[j] - x[i]) <= 1)
                 for i in range(n))


def closed_cell_bound(n):
    pairs = list(combinations(range(n), 2))
    optional = [p for p in pairs if p[1] > p[0] + 1]
    largest = Fraction(-1)
    possible_cells = 0
    tests = 0
    for mask in product((False, True), repeat=len(optional)):
        adjacent = {(i, i + 1): True for i in range(n - 1)}
        adjacent.update(dict(zip(optional, mask)))
        neighbors = [[i] for i in range(n)]
        for (i, j), contact in adjacent.items():
            if contact:
                neighbors[i].append(j)
                neighbors[j].append(i)
        feasible_at_binary_vertex = False
        # All graph-cell inequalities are integer interval sums with
        # bounds +-1, plus 0 <= g_i <= 1. Their matrix is totally
        # unimodular; therefore all vertices belong to {0,1}^{n-1}.
        for gaps in product((0, 1), repeat=n - 1):
            if any((sum(gaps[i:j]) > 1 if contact else
                    sum(gaps[i:j]) < 1)
                   for (i, j), contact in adjacent.items()):
                continue
            feasible_at_binary_vertex = True
            x = [Fraction(0)]
            for gap in gaps:
                x.append(x[-1] + gap)
            means = [sum((x[j] for j in neighbors[i]), Fraction(0)) /
                     len(neighbors[i]) for i in range(n)]
            for k in range(n - 1):
                largest = max(largest, means[k + 1] - means[k])
                tests += 1
        possible_cells += feasible_at_binary_vertex
    return largest, possible_cells, tests


def main():
    for n in range(2, 7):
        bound, cells, tests = closed_cell_bound(n)
        assert (bound, cells, tests) == (EXPECTED[n], EXPECTED_CELLS[n],
                                         EXPECTED_TESTS[n]), (n, bound, cells, tests)
        # Independent direct evaluation of every connected grid profile
        # on the mesh {0,1/3,2/3,1} for each adjacent spacing.
        for grid in product(range(4), repeat=n - 1):
            x = [Fraction(0)]
            for g in grid:
                x.append(x[-1] + Fraction(g, 3))
            means = update(x)
            assert max(means[i + 1] - means[i] for i in range(n - 1)) <= bound
        print(f'n={n}: bound={bound}, closed cells={cells}, '
              f'exact boundary comparisons={tests}, direct-grid profiles={4 ** (n - 1)}')
    for n, xs, target in ((5, (0, 1, 2, 3, 3), Fraction(5, 4)),
                           (6, (0, 0, 1, 2, 3, 3), Fraction(3, 2))):
        y = update(tuple(Fraction(x) for x in xs))
        gap = max(y[i + 1] - y[i] for i in range(n - 1))
        assert gap == target, (n, gap, y)
        print(f'sharp n={n}: x={xs}, y={y}, maximum={gap}')
    print('All exact certificates passed')


if __name__ == '__main__':
    main()
