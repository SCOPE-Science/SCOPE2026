"""Exact reproducibility checks for first-hit survival under optimal riffle guesses.

Run with Python 3 and no third-party dependencies. These finite tests supplement,
but do not replace, the generalized cycle-lemma proof.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb


def binomial_atom(a, t):
    m = t // a
    return Fraction(comb(t, m) * (a - 1) ** (t - m), a ** t)


def survivor_by_counts(a, n):
    """Enumerate words of length n by surviving count and walk height."""
    dp = {(0, 0): 1}
    checks = 0
    for t in range(1, n + 1):
        new = defaultdict(int)
        for (h, j), number in dp.items():
            new[(h + 1, j)] += number
            if h >= a - 1:
                new[(h - a + 1, j + 1)] += number
        dp = dict(new)
        for (h, j), number in dp.items():
            assert h == t - a * j >= 0
            candidate = Fraction(h + 1, t + 1) * comb(t + 1, j)
            assert candidate.denominator == 1
            assert number == candidate.numerator, (a, t, j, number, candidate)
            checks += 1
        numerator = sum(count * (a - 1) ** (t - j) for (h, j), count in dp.items())
        assert Fraction(numerator, a ** t) == binomial_atom(a, t)
        checks += 1
    return checks


def direct_shuffle(a, n):
    """Independently enumerate iid packet words for a direct a-shuffle."""
    assert n <= 12 and a ** n <= 100000
    successes = [0] * (n // 2 + 1)
    deficient = [0] * (n // 2 + 1)
    for digits in product(range(a), repeat=n):
        sizes = [0] * a
        for b in digits:
            sizes[b] += 1
        starts = [0] * a
        for b in range(1, a):
            starts[b] = starts[b - 1] + sizes[b - 1]
        seen = [0] * a
        first = n + 1
        for i, b in enumerate(digits, 1):
            seen[b] += 1
            actual = starts[b] + seen[b]
            guess = i // a + 1
            if i <= n // 2 and first == n + 1 and actual == guess:
                first = i
        for t in range(1, n // 2 + 1):
            if first > t:
                successes[t] += 1
            if sizes[0] <= t // a:
                deficient[t] += 1
    count = a ** n
    for t in range(1, n // 2 + 1):
        actual = Fraction(successes[t], count)
        reference = binomial_atom(a, t)
        bad_packet = Fraction(deficient[t], count)
        assert abs(actual - reference) <= bad_packet, (a, n, t, actual, reference)
    return n // 2


def main():
    tested = 0
    for a in (2, 3, 4, 5, 6, 7, 8):
        tested += survivor_by_counts(a, 60)
        # A new block can begin without the first-match hazard at its boundary.
        for m in range(1, 12):
            assert binomial_atom(a, a * m - 1) == binomial_atom(a, a * m)
            tested += 1
    for a, n in ((2, 12), (3, 9), (4, 8), (8, 5)):
        tested += direct_shuffle(a, n)
    print(f'PASS {tested} exact ballot, prefix, plateau and direct-shuffle assertions')


if __name__ == '__main__':
    main()
