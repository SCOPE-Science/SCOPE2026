"""Exact independent checks for the two-read deletion graph degree law.
Run with Python 3 standard library: python3 checker.py
"""
from itertools import product
from collections import Counter, defaultdict
from fractions import Fraction


def outputs(x):
    return {x[:i] + x[i + 1:] for i in range(len(x))}


def degree_from_alternation(x):
    total = 0
    for a in range(len(x)):
        for b in range(a + 1, len(x)):
            if all(x[k] == x[k - 2] for k in range(a + 2, b + 1)) and x[a] != x[a + 1]:
                total += 1
    return total


def exact_graph_histogram(q, n):
    words = list(product(range(q), repeat=n))
    balls = [outputs(x) for x in words]
    distribution = Counter()
    for i, x in enumerate(words):
        degree = sum(len(balls[i] & balls[j]) == 2 for j in range(len(words)) if i != j)
        assert degree == degree_from_alternation(x), (q, n, x, degree)
        distribution[degree] += 1
    return distribution


def recurrence_histogram(q, n):
    # (longest alternating suffix length) -> polynomial coefficients
    state = {1: {0: q}}
    for length in range(1, n):
        nxt = defaultdict(lambda: defaultdict(int))
        for suffix, polynomial in state.items():
            for degree, count in polynomial.items():
                nxt[1][degree] += count
                if suffix == 1:
                    nxt[2][degree + 1] += (q - 1) * count
                else:
                    nxt[2][degree + 1] += (q - 2) * count
                    nxt[suffix + 1][degree + suffix] += count
        state = nxt
    return Counter({d: sum(poly.get(d, 0) for poly in state.values())
                    for d in {k for poly in state.values() for k in poly}})


def exact_moments(q, n):
    r = Fraction(1, q)
    mean = Fraction(n) - Fraction(q, q - 1) * (1 - r ** n)
    var = Fraction(0)
    for i in range(1, n + 1):
        v = Fraction(2, q - 1) + r ** (i - 1) * (Fraction(q - 3, q - 1) - 2 * (i - 1)) - r ** (2 * (i - 1))
        var += v * (1 + 2 * (1 - r ** (n - i)) / (q - 1))
    return mean, var


def histogram_moments(hist, q, n):
    assert sum(hist.values()) == q ** n
    mu = sum(Fraction(d * c, q ** n) for d, c in hist.items())
    var = sum(Fraction(c, q ** n) * (d - mu) ** 2 for d, c in hist.items())
    return mu, var


def run():
    ngraphs = 0
    for q, nmax in [(2, 9), (3, 6), (4, 5)]:
        for n in range(1, nmax + 1):
            actual = exact_graph_histogram(q, n)
            from_dp = recurrence_histogram(q, n)
            assert actual == from_dp, (q, n, actual, from_dp)
            assert histogram_moments(actual, q, n) == exact_moments(q, n), (q, n)
            ngraphs += q ** n
    for q in range(2, 8):
        for n in range(1, 24):
            hist = recurrence_histogram(q, n)
            assert histogram_moments(hist, q, n) == exact_moments(q, n), (q, n)
    print('PASS: direct graph degrees, distribution recurrence, exact moments, q=2..4; checked vertices:', ngraphs)
    print('PASS: recurrence vs rational moments q=2..7, n=1..23')


if __name__ == '__main__':
    run()
