"""Deterministic tests for a finite-block central-binomial valuation theorem.

Run with Python 3.9+; no third-party packages are used. All integer
counts and statistical comparisons are exact (fractions, not floats).
"""
from collections import Counter
from fractions import Fraction
from math import comb


def valuation_by_integer(n, p):
    a = comb(2 * n, n)
    r = 0
    while a % p == 0:
        a //= p
        r += 1
    return r


def valuation_by_carries(n, p):
    total = carry = 0
    while n or carry:
        n, digit = divmod(n, p)
        carry = (2 * digit + carry) // p
        total += carry
    return total


def moments(p, k):
    r = Fraction(1, p)
    mean = Fraction(k, 2) - (1 - r**k) / (2 * (p - 1))
    variance = (Fraction((p + 1) * k, 4 * (p - 1))
                - Fraction(2 * p + 1, 4 * (p - 1)**2)
                + (2 * (p + 1) * r**k - r**(2 * k)) / (4 * (p - 1)**2))
    half_diff_second = sum((2 * j - 1) * r**j for j in range(1, k + 1))
    return mean, variance, variance - half_diff_second


def expected_difference_counts(p, k):
    count = {0: (p - 2) * p**(k - 1)}
    for j in range(1, k):
        count[j] = count[-j] = (p - 1) * p**(k - j - 1)
    count[k] = count[-k] = 1
    return count


def matrix_joint_counts(p, k):
    """Five-state simultaneous doubling-and-increment carry automaton."""
    m = (p - 1) // 2
    # Each edge is (destination, number_of_digits, gain_in_first, gain_in_second).
    graph = {
        'A': [('B', 1, 1, 0), ('C', m, 0, 0),
              ('D', 1, 0, 1), ('E', m - 1, 1, 1)],
        'B': [('B', 1, 1, 0), ('C', m, 0, 0), ('E', m, 1, 1)],
        'C': [('C', m + 1, 0, 0), ('E', m, 1, 1)],
        'D': [('C', m, 0, 0), ('D', 1, 0, 1), ('E', m, 1, 1)],
        'E': [('C', m, 0, 0), ('E', m + 1, 1, 1)],
    }
    counts = {('A', 0, 0): 1}
    for _ in range(k):
        nxt = Counter()
        for (state, i, j), number in counts.items():
            for state2, multiplicity, di, dj in graph[state]:
                nxt[(state2, i + di, j + dj)] += number * multiplicity
        counts = nxt
    joint = Counter()
    for (_, i, j), number in counts.items():
        joint[(i, j)] += number
    return {pair: number for pair, number in joint.items() if number > 0}


def check(p, k):
    m = p**k
    values = [valuation_by_integer(n, p) for n in range(m)]
    assert all(values[n] == valuation_by_carries(n, p) for n in range(m))
    # The endpoint n = p**k has valuation zero for odd p.
    assert valuation_by_integer(m, p) == 0
    differences = [values[(n + 1) % m] - values[n] for n in range(m)]
    assert dict(Counter(differences)) == expected_difference_counts(p, k)
    joint = dict(Counter((values[n], values[(n+1) % m]) for n in range(m)))
    assert joint == matrix_joint_counts(p, k)
    mean = Fraction(sum(values), m)
    variance = Fraction(sum(x * x for x in values), m) - mean**2
    covariance = Fraction(sum(values[n] * values[(n + 1) % m]
                              for n in range(m)), m) - mean**2
    assert (mean, variance, covariance) == moments(p, k)
    expected_sign = -1 if p == 3 and k in (1, 2) else 1
    assert (covariance > 0) - (covariance < 0) == expected_sign
    return m


def run():
    cases = ((3, 6), (5, 4), (7, 3), (11, 2), (13, 2), (17, 2))
    checked = total = 0
    for prime, kmax in cases:
        for k in range(1, kmax + 1):
            total += check(prime, k)
            checked += 1
    assert checked == 19
    print(f"PASS: {checked} (prime, exponent) cases; {total} individual indices")
    print("PASS: independent binomial-integer and Kummer-carry valuations")
    print("PASS: five-state full joint counts, exact signed differences, means, variances, covariances, and signs")


if __name__ == "__main__":
    run()
