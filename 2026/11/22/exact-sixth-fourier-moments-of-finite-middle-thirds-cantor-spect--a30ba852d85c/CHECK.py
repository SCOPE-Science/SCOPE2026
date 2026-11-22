"""Independent finite-depth tests for an exact Cantor digit collision theorem.

This script uses only Python's standard library; no external resources are needed.
"""
from collections import Counter
from math import comb


def direct_level(k):
    elements = [sum(((mask >> j) & 1) * (3 ** j) for j in range(k))
                for mask in range(1 << k)]
    frequencies = Counter({0: 1})
    for _ in range(3):
        next_frequencies = Counter()
        for t, weight in frequencies.items():
            for a in elements:
                next_frequencies[t + a] += weight
        frequencies = next_frequencies
    return sum(v * v for v in frequencies.values()), frequencies


def test():
    u, v = 1, 0
    energies = []
    for k in range(9):
        expected, histogram = direct_level(k)
        assert u == expected, (k, u, expected)
        assert sum(histogram.values()) == (8 ** k)
        support_length = (3 ** (k + 1) - 1) // 2
        assert set(histogram) == set(range(support_length)), k
        assert all(w > 0 for w in histogram.values())
        energies.append(u)
        u, v = 20 * u + 30 * v, u + 6 * v
    assert energies[:5] == [1, 20, 430, 9380, 205180]
    for k in range(7):
        assert energies[k + 2] == 26 * energies[k + 1] - 90 * energies[k]

    # Directly validate signed-digit weights and the full carry matrix.
    weights = [sum(1 for bits in range(64)
                   if sum((bits >> j) & 1 for j in range(3))
                   - sum((bits >> j) & 1 for j in range(3, 6)) == d)
               for d in range(-3, 4)]
    assert weights == [comb(6, d + 3) for d in range(-3, 4)]
    states = [-1, 0, 1]
    matrix = [[weights[3 * nxt - cur + 3]
               if -3 <= 3 * nxt - cur <= 3 else 0
               for nxt in states] for cur in states]
    assert matrix == [[6, 15, 0], [1, 20, 1], [0, 15, 6]]

    # More depths by exact integer recurrence, without exponential enumeration.
    a, b = 1, 20
    for _ in range(30):
        c = 26 * b - 90 * a
        assert c > b > 0
        a, b = b, c
    print('PASS: 9 independently enumerated levels; carry matrix; 30 recurrence steps')
    print('First 9 energies:', energies)


if __name__ == '__main__':
    test()
