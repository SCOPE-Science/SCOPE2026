"""Finite-graph exact checker for dimer adsorption on two bridged cliques.

The checker compares a reduced rate recursion with an independently
constructed full available-edge Markov recursion. Infinite-size claims
require the accompanying mathematical argument, not these finite checks.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations


def reduced_probability(m, n, beta):
    beta = Fraction(beta)
    @lru_cache(None)
    def value(a, b):
        internal_a = a * (a - 1) // 2
        internal_b = b * (b - 1) // 2
        total = beta + internal_a + internal_b
        numerator = beta
        if a >= 3:
            numerator += (a - 1) * (a - 2) // 2 * value(a - 2, b)
        if b >= 3:
            numerator += (b - 1) * (b - 2) // 2 * value(a, b - 2)
        return numerator / total
    return value(m, n)


def full_graph_probability_and_uncovered(m, n, beta):
    beta = Fraction(beta)
    total_vertices = m + n
    edges = [(u, v) for u, v in combinations(range(m), 2)]
    edges += [(u, v) for u, v in combinations(range(m, total_vertices), 2)]
    bridge = (0, m)
    edges += [bridge]

    @lru_cache(None)
    def solve(mask):
        eligible = [(u, v) for (u, v) in edges if (mask >> u) & 1 and (mask >> v) & 1]
        if not eligible:
            return Fraction(0), Fraction(mask.bit_count())
        total_rate = sum(beta if edge == bridge else 1 for edge in eligible)
        probability, expectation = Fraction(0), Fraction(0)
        for u, v in eligible:
            edge = (u, v)
            rate = beta if edge == bridge else 1
            child_probability, child_uncovered = solve(mask ^ (1 << u) ^ (1 << v))
            probability += rate * (int(edge == bridge) + child_probability)
            expectation += rate * child_uncovered
        return probability / total_rate, expectation / total_rate
    return solve((1 << total_vertices) - 1)


def run_tests():
    rates = (Fraction(1, 3), Fraction(1), Fraction(5, 2), Fraction(10))
    exact = parity = 0
    for m in range(2, 8):
        for n in range(2, 8):
            for beta in rates:
                direct, uncovered = full_graph_probability_and_uncovered(m, n, beta)
                reduced = reduced_probability(m, n, beta)
                assert direct == reduced, (m, n, beta, direct, reduced)
                exact += 1
                if m % 2 == n % 2 == 0:
                    assert uncovered == 2 * reduced
                elif m % 2 == n % 2 == 1:
                    assert uncovered == 2 * (1 - reduced)
                else:
                    assert uncovered == 1
                parity += 1
    benchmarks = {
        (2, 2): Fraction(1, 3),
        (2, 3): Fraction(3, 10),
        (3, 3): Fraction(2, 7),
        (4, 4): Fraction(5, 26),
    }
    for sizes, expected in benchmarks.items():
        assert reduced_probability(*sizes, 1) == expected
    for m, n in ((2, 3), (3, 5), (4, 4), (5, 6)):
        values = [reduced_probability(m, n, beta) for beta in rates]
        assert all(a < b for a, b in zip(values, values[1:]))
    print('PASS graph-vs-reduction', exact, 'exact rational comparisons')
    print('PASS uncovered-parity', parity, 'exact rational comparisons')
    print('PASS four independent unit-rate benchmarks; four positive-rate monotonicity checks')
    print('Values:', [(sizes, str(reduced_probability(*sizes, 1))) for sizes in benchmarks])


if __name__ == '__main__':
    run_tests()
