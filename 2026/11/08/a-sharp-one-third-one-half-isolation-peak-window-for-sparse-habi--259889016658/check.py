"""Exact finite reproducibility checks for surviving singleton-component isolation peaks.

Run with Python 3 (standard library only): python check.py
This verifies examples and finite algebraic checks, not the all-size theorem.
"""
from fractions import Fraction as F


def degree_counts(edges, n):
    degrees = [0] * n
    for u, v in edges:
        assert 0 <= u < n and 0 <= v < n and u != v
        degrees[u] += 1
        degrees[v] += 1
    assert min(degrees) >= 1
    return degrees


def expected_by_degree(degrees, q):
    return (1 - q) * sum((q ** d for d in degrees), F(0))


def first_derivative(degrees, q):
    return sum((q ** (d - 1) * (d - (d + 1) * q) for d in degrees), F(0))


def second_derivative(degrees, q):
    return sum((d * q ** (d - 2) * (d - 1 - (d + 1) * q)
                for d in degrees if d >= 2), F(-2 * degrees.count(1)))


def independent_enumeration(edges, n, q):
    neighbors = [0] * n
    for u, v in edges:
        neighbors[u] |= 1 << v
        neighbors[v] |= 1 << u
    p = 1 - q
    total = F(0)
    for subset in range(1 << n):
        occupied = subset.bit_count()
        singleton_count = sum(bool(subset & (1 << v)) and not (subset & neighbors[v])
                              for v in range(n))
        total += singleton_count * p ** occupied * q ** (n - occupied)
    return total


def partitions(number, least=1):
    if number == 0:
        yield ()
        return
    for k in range(least, number + 1):
        for tail in partitions(number - k, k):
            yield (k,) + tail


def check():
    # All realizable tree degree multisets through 18 vertices. Every
    # partition of n-2 corresponds to one tree degree multiset.
    tested = 0
    for n in range(3, 19):
        for blocks in partitions(n - 2):
            degs = [1] * (n - len(blocks)) + [a + 1 for a in blocks]
            assert sum(degs) == 2 * (n - 1)
            assert first_derivative(degs, F(1, 2)) > 0
            assert first_derivative(degs, F(2, 3)) < 0
            for q in (F(1, 2), F(7, 12), F(2, 3)):
                assert second_derivative(degs, q) < 0
            tested += 1
    # Explicit independently enumerated vertex-survival outcomes.
    edge_cases = [
        (7, [(i, i+1) for i in range(6)]),
        (8, [(0, i) for i in range(1, 8)]),
        (7, [(i, (i + 1) % 7) for i in range(7)]),
        (9, [(0, 1), (1, 2), (1, 3), (3, 4), (3, 5),
             (5, 6), (5, 7), (7, 8)]),
    ]
    for n, edges in edge_cases:
        degrees = degree_counts(edges, n)
        for q in (F(1, 4), F(1, 2), F(2, 3), F(3, 4)):
            assert independent_enumeration(edges, n, q) == expected_by_degree(degrees, q)
    # The sharp one-extra-edge violation: a chorded cycle C_8.
    chorded = [(i, (i + 1) % 8) for i in range(8)] + [(0, 4)]
    chord_degs = degree_counts(chorded, 8)
    assert sorted(chord_degs) == [2] * 6 + [3] * 2
    assert first_derivative(chord_degs, F(2, 3)) == F(8, 27)
    assert first_derivative(chord_degs, F(1)) < 0
    assert second_derivative(chord_degs, F(2, 3)) < 0
    for q in (F(1, 4), F(1, 2), F(2, 3), F(3, 4)):
        assert independent_enumeration(chorded, 8, q) == expected_by_degree(chord_degs, q)
    for n in range(3, 19):
        degs = [2] * n  # cycle C_n
        assert first_derivative(degs, F(2, 3)) == 0
        assert first_derivative(degs, F(1, 2)) > 0
    # A connected, 14-vertex non-sparse counterexample: K_13 plus one leaf.
    n = 14
    edges = [(i, j) for i in range(13) for j in range(i + 1, 13)] + [(0, 13)]
    degs = degree_counts(edges, n)
    assert sorted(degs) == [1] + [12] * 12 + [13]
    witness = ((F(1, 2), +1), (F(3, 5), -1),
               (F(9, 10), +1), (F(1), -1))
    for q, expected_sign in witness:
        assert first_derivative(degs, q) * expected_sign > 0
    for q in (F(1, 2), F(3, 5), F(9, 10)):
        assert independent_enumeration(edges, n, q) == expected_by_degree(degs, q)
    print('PASS: exact degree-sequence comparisons:', tested)
    print('PASS: 16 independent tree/cycle survival-sum comparisons')
    print('PASS: exact 14-vertex cyclic counterexample at four parameters')
    print('PASS: three independently enumerated 14-vertex survival sums')
    print('PASS: chorded-cycle sharp edge-budget boundary and four exact survival sums')
    print('LIMIT: all-size uniqueness and interval bounds require the written proof')


if __name__ == '__main__':
    check()
