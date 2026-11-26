#!/usr/bin/env python3
"""Independent direct enumeration of edge-open packings in rook graphs.

Run: python3 verify.py. Uses only Python's standard library.
An edge set is feasible exactly when no two chosen edges have a third
edge joining an endpoint of one to an endpoint of the other.
"""
from collections import Counter
from itertools import combinations
from math import factorial


def rook_edges(rows, cols):
    vertices = [(i, j) for i in range(rows) for j in range(cols)]
    return [tuple(sorted((v, w))) for v, w in combinations(vertices, 2)
            if v[0] == w[0] or v[1] == w[1]]


def direct_coefficients(rows, cols):
    edges = rook_edges(rows, cols)
    adjacency_mask = [0] * len(edges)
    for i, j in combinations(range(len(edges)), 2):
        first = edges[i]
        second = edges[j]
        forbidden = False
        for bridge in edges:
            if bridge == first or bridge == second:
                continue
            left, right = bridge
            if ((left in first and right in second)
                    or (left in second and right in first)):
                forbidden = True
                break
        if forbidden:
            adjacency_mask[i] |= 1 << j
            adjacency_mask[j] |= 1 << i

    counts = Counter()
    def visit(remaining, size):
        if remaining == 0:
            counts[size] += 1
            return
        low_bit = remaining & -remaining
        index = low_bit.bit_length() - 1
        visit(remaining ^ low_bit, size)
        visit((remaining ^ low_bit) & ~adjacency_mask[index], size + 1)

    visit((1 << len(edges)) - 1, 0)
    return counts


def formula_coefficients(rows, cols):
    counts = Counter()
    numerator = factorial(rows) * factorial(cols)
    for horizontal in range(rows + 1):
        for vertical in range(cols + 1):
            for corners in range(min(rows, cols) // 2 + 1):
                used_rows = horizontal + 2 * vertical + 2 * corners
                used_cols = 2 * horizontal + vertical + 2 * corners
                if used_rows > rows or used_cols > cols:
                    continue
                den = (2 ** (horizontal + vertical) * factorial(horizontal)
                       * factorial(vertical) * factorial(corners)
                       * factorial(rows - used_rows)
                       * factorial(cols - used_cols))
                assert numerator % den == 0
                counts[horizontal + vertical + 2 * corners] += numerator // den
    return counts


def expected_max(rows, cols):
    m, n = sorted((rows, cols))
    return m - (m == n and m % 2 == 1)


def run():
    trials = 0
    legal_sets = 0
    for m in range(1, 7):
        for n in range(m, 7):
            direct = direct_coefficients(m, n)
            predicted = formula_coefficients(m, n)
            assert direct == predicted, (m, n, direct, predicted)
            assert max(direct) == expected_max(m, n), (m, n, direct)
            trials += 1
            legal_sets += sum(direct.values())
    # Further formula/boundary checks exercise both parity branches.
    for m in range(1, 21):
        for n in range(m, 21):
            coefficients = formula_coefficients(m, n)
            assert max(coefficients) == expected_max(m, n)
            if m == n:
                top = coefficients[max(coefficients)]
                f = factorial(m)
                if m % 2 == 0:
                    expected = f * f // factorial(m // 2)
                elif m == 1:
                    expected = 1
                else:
                    t = (m - 1) // 2
                    expected = f * f // factorial(t) + f * f // (4 * factorial(t - 1))
                assert top == expected, (m, top, expected)
    print('VERIFICATION_OK direct_rectangles=%d enumerated_valid_edge_sets=%d formula_max_rectangles=210'
          % (trials, legal_sets))
    print('Examples: P_3,3=%s; P_4,4=%s' %
          (sorted(formula_coefficients(3, 3).items()),
           sorted(formula_coefficients(4, 4).items())))


if __name__ == '__main__':
    run()
