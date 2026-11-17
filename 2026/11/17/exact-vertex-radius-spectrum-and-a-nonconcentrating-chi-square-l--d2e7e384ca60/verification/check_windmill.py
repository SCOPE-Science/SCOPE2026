"""Finite exact-integer checks of centered clique-windmill zonotope radii.

Run: python verification/check_windmill.py
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import factorial


def direct_shells(k, m):
    """Enumerate all acyclic orientations, constructing the graph edge sums directly."""
    orders = tuple(permutations(range(k)))
    n = 1 + m * (k - 1)
    hist = Counter()
    vertices = set()
    for order_tuple in product(orders, repeat=m):
        coordinate_doubles = [0] * n
        for blade, order in enumerate(order_tuple):
            inverse = {v: i for i, v in enumerate(order)}
            def global_vertex(v):
                return 0 if v == 0 else 1 + blade * (k - 1) + v - 1
            for u in range(k):
                for v in range(u + 1, k):
                    sign = 1 if inverse[u] > inverse[v] else -1
                    coordinate_doubles[global_vertex(u)] += sign
                    coordinate_doubles[global_vertex(v)] -= sign
        vec = tuple(coordinate_doubles)
        assert sum(vec) == 0
        vertices.add(vec)
        hist[sum(a * a for a in vec)] += 1
    assert len(vertices) == factorial(k) ** m
    return hist


def predicted_shells(k, m):
    # Integer formula for four times the squared Euclidean norm.
    bs = [2 * j - (k - 1) for j in range(k)]
    constant = m * k * (k * k - 1) // 3
    hist = Counter()
    for js in product(range(k), repeat=m):
        bs_here = [bs[j] for j in js]
        q = constant + sum(bs_here) ** 2 - sum(t * t for t in bs_here)
        hist[q] += factorial(k - 1) ** m
    return hist


def moments(hist):
    total = sum(hist.values())
    mean = sum(Fraction(v * multiplicity, total) for v, multiplicity in hist.items())
    second = sum(Fraction(v * v * multiplicity, total) for v, multiplicity in hist.items())
    return mean, second - mean * mean


def main():
    cases = ((3, 2), (3, 3), (3, 4), (4, 2), (4, 3), (5, 2), (6, 2))
    checked = 0
    for k, m in cases:
        direct = direct_shells(k, m)
        formula = predicted_shells(k, m)
        assert direct == formula, (k, m, direct, formula)
        assert sum(direct.values()) == factorial(k) ** m
        variance_single = Fraction(k * k - 1, 12)
        local_norm2 = Fraction(k * (k * k - 1), 12)
        # The enumerator records 4 times squared radius.
        avg, var = moments(direct)
        assert avg == 4 * m * local_norm2
        assert var == 16 * 2 * m * (m - 1) * variance_single ** 2
        maximum = 4 * m * local_norm2 + m * (m - 1) * (k - 1) ** 2
        assert max(direct) == maximum
        assert direct[maximum] == 2 * factorial(k - 1) ** m
        checked += factorial(k) ** m
    print('CLIQUE_WINDMILL_RADII_PASS cases=%d enumerated=%d' % (len(cases), checked))


if __name__ == '__main__':
    main()
