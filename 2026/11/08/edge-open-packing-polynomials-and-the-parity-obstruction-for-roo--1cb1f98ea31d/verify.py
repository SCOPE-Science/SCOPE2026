"""Literal finite verification of edge-open-packing enumeration on rook graphs.

This file independently enumerates edge subsets through a pair-conflict graph,
where two rook edges conflict when a *third* rook edge joins their endpoints.
It then compares all cardinality coefficients with the factorial formula.
Finite tests are not proofs of the unrestricted result.
"""
from collections import defaultdict
from itertools import combinations
from math import factorial


def graph_edges(m, n):
    cells = [(r, c) for r in range(m) for c in range(n)]
    return [tuple((a, b)) for a, b in combinations(cells, 2)
            if a[0] == b[0] or a[1] == b[1]]


def literal_counts(m, n):
    edges = graph_edges(m, n)
    q = len(edges)
    clashes = [0] * q
    for i in range(q):
        a, b = edges[i]
        for j in range(i + 1, q):
            c, d = edges[j]
            # The explicit third-edge test does not use the classification.
            bad = any(k != i and k != j and
                      ((u in (a, b) and v in (c, d)) or
                       (v in (a, b) and u in (c, d)))
                      for k, (u, v) in enumerate(edges))
            if bad:
                clashes[i] |= 1 << j
                clashes[j] |= 1 << i

    counts = defaultdict(int)
    def visit(available, chosen):
        if not available:
            counts[chosen] += 1
            return
        first_bit = available & -available
        index = first_bit.bit_length() - 1
        visit(available ^ first_bit, chosen)
        visit((available ^ first_bit) & ~clashes[index], chosen + 1)
    visit((1 << q) - 1, 0)
    return dict(counts)


def predicted_counts(m, n):
    def falling(a, b):
        return factorial(a) // factorial(a - b)
    c = defaultdict(int)
    for h in range(m + 1):
        for v in range(n + 1):
            for l in range(min(m, n) // 2 + 1):
                row_use = h + 2 * v + 2 * l
                col_use = 2 * h + v + 2 * l
                if row_use <= m and col_use <= n:
                    numerator = falling(m, row_use) * falling(n, col_use)
                    denominator = (2 ** (h + v) * factorial(h) *
                                   factorial(v) * factorial(l))
                    assert numerator % denominator == 0
                    c[h + v + 2 * l] += numerator // denominator
    return dict(c)


def maximum_size(m, n):
    s = min(m, n)
    return s - (m == n and s % 2 == 1)


def maximum_multiplicity(m, n):
    if m > n:
        m, n = n, m
    if m == n:
        if m % 2 == 0:
            return factorial(m) ** 2 // factorial(m // 2)
        h = (m - 1) // 2
        return (factorial(m) ** 2 // factorial(h) +
                factorial(m) ** 2 // (4 * factorial(h - 1)))
    total = 0
    for h in range(m % 2, min(m, n - m) + 1, 2):
        l = (m - h) // 2
        total += (factorial(m) * factorial(n) // factorial(n - m - h)
                  // (2 ** h * factorial(h) * factorial(l)))
    return total


def check():
    comparisons = 0
    counted = 0
    for m in range(2, 7):
        for n in range(m, 7):
            direct = literal_counts(m, n)
            theory = predicted_counts(m, n)
            assert direct == theory, (m, n, direct, theory)
            assert max(direct) == maximum_size(m, n)
            assert direct[max(direct)] == maximum_multiplicity(m, n)
            comparisons += 1
            counted += sum(direct.values())
    for m in range(2, 20):
        for n in range(m, 25):
            theory = predicted_counts(m, n)
            assert max(theory) == maximum_size(m, n)
            assert theory[max(theory)] == maximum_multiplicity(m, n)
    print('VERIFY_OK literal_graph_profiles', comparisons,
          'literal_packing_sets', counted,
          'all_coefficients=PASS', 'extremal_formula=PASS',
          'additional_arithmetic_profiles=PASS')


if __name__ == '__main__':
    check()
