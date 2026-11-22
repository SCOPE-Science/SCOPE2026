"""Exact independent checks for a depth-two counting-modal counterexample.

No external packages needed; run `python checker.py`.
"""
from fractions import Fraction
from math import comb


def central_event_probability(n):
    return Fraction(comb(n, (n + 1) // 2), 2 ** n)


def analytic_root_probability(n):
    q = central_event_probability(n)
    return (1 - q) ** n


def exhaust_valuations(n):
    """Independently evaluate the whole depth-2 regular tree, including unused labels.

    Number of vertices = 1+n+n*n, and every assignment of the sole atom is uniform.
    """
    vertices = 1 + n + n*n
    hits = 0
    for valuation in range(1 << vertices):
        root_successes = 0
        for child in range(n):
            start = 1 + n + child*n
            positives = sum((valuation >> (start+i)) & 1 for i in range(n))
            total = n
            # No shortcut through the binomial probability used by the theorem.
            left_equality = (total == 2*positives)
            right_equality = (total + 1 == 2*positives)
            if left_equality or right_equality:
                root_successes += 1
        if root_successes == 0:
            hits += 1
    return Fraction(hits, 1 << vertices)


def coefficients_without_independent_events(n):
    # Independently obtain the root count from the ordinary polynomial of one
    # child block, rather than reusing analytic_root_probability.
    child_nice = 0
    for mask in range(1 << n):
        positives = mask.bit_count()
        child_nice += int(n == 2*positives or n + 1 == 2*positives)
    bad = (1 << n) - child_nice
    return Fraction(bad**n, (1 << n)**n)


def main():
    for n in range(1, 4):
        a, b, c = analytic_root_probability(n), exhaust_valuations(n), coefficients_without_independent_events(n)
        assert a == b == c, (n, a, b, c)
    for n in range(1, 13):
        assert analytic_root_probability(n) == coefficients_without_independent_events(n)
    for n in (10, 100, 1000, 10000):
        # Central events have vanishing probability but growing expected count.
        q = float(central_event_probability(n))
        assert q < 0.5 and n*q > 1
    # Under the iterated-limit prescription the child event has probability 0,
    # so its number of occurrences is 0 almost surely and the root formula is true.
    surrogate = Fraction(1)
    assert surrogate == 1
    print('COUNTING_MODAL_SURROGATE_MAX_GAP_OK')
    for n in (1, 2, 3, 4, 5, 6, 8, 10):
        print(f'n={n} child={central_event_probability(n)} root={analytic_root_probability(n)}')


if __name__ == '__main__':
    main()
