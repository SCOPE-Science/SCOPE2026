"""Exact finite checks for variation norms of inverse riffle averaging.

Run: python check.py
Only Python's standard library is required.
"""
from fractions import Fraction
from itertools import product
from math import comb


def variation(values):
    return sum(abs(values[i + 1] - values[i]) for i in range(len(values) - 1))


def position_image(n, a, k, probabilities=None):
    """Direct enumeration of independent bucket labels, with rational weights."""
    if probabilities is None:
        probabilities = [Fraction(1, a)] * a
    assert sum(probabilities) == 1 and all(p > 0 for p in probabilities)
    result = [Fraction(0) for _ in range(n)]
    for labels in product(range(a), repeat=n):
        mass = Fraction(1)
        for c in labels:
            mass *= probabilities[c]
        order = sorted(range(n), key=lambda j: (labels[j], j))
        for i, j in enumerate(order):
            if j < k:
                result[i] += mass
    return result


def binary_binomial_image(n, k):
    """Independent, closed binomial-count formula for two equal buckets."""
    result = []
    for i in range(1, n + 1):
        count = 0
        for x in range(k + 1):
            for y in range(n - k + 1):
                if i <= x or x + y < i <= y + k:
                    count += comb(k, x) * comb(n - k, y)
        result.append(Fraction(count, 2 ** n))
    return result


def expectation_matrix(n, a):
    out = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    denom = a ** n
    for labels in product(range(a), repeat=n):
        order = sorted(range(n), key=lambda j: (labels[j], j))
        for i, j in enumerate(order):
            out[i][j] += Fraction(1, denom)
    return out


def multiply(A, B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def main():
    expected = {
        2: Fraction(1, 2), 3: Fraction(1, 2),
        4: Fraction(5, 8), 5: Fraction(11, 16),
        6: Fraction(29, 32), 7: Fraction(67, 64),
        8: Fraction(155, 128), 9: Fraction(357, 256),
    }
    cases = 0
    for n, value in expected.items():
        images = [binary_binomial_image(n, k) for k in range(1, n)]
        norm = max(map(variation, images))
        assert norm == value, (n, norm, value)
        for k in range(1, n):
            direct = position_image(n, 2, k)
            assert direct == images[k-1], (n, k)
            cases += 1
    print('BINARY_EXACT_N2_TO_N9_AND_INDEPENDENT_ENUMERATION_PASS', cases)
    for n in range(2, 8):
        for a in (2, 3):
            images = [position_image(n, a, k) for k in range(1, n)]
            gain = max(map(variation, images))
            assert gain <= 2*a - 1
            if a == 2:
                assert gain == expected[n]
    print('PACKET_RUN_BOUND_AND_EXACT_SMALL_DECKS_PASS')
    for n in range(2, 6):
        A = expectation_matrix(n, 2)
        B = expectation_matrix(n, 4)
        assert multiply(A, A) == B
    print('INVERSE_SHUFFLE_PRODUCT_RULE_DIRECT_MATRIX_PASS')
    for n in range(2, 6):
        probs = [Fraction(1, 3), Fraction(2, 3)]
        for k in range(1,n):
            x = position_image(n, 2, k, probs)
            assert sum(x) == k
            assert variation(x) <= 3
    print('BIASED_EXACT_MASS_AND_PACKET_BOUND_PASS')
    print('ALL_INVERSE_RIFFLE_VARIATION_CERTIFICATES_PASS')


if __name__ == '__main__':
    main()
