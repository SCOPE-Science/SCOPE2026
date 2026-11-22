"""Exact small-case verification of earliest intact blocks in uniform q-Stirling permutations.

The asymptotic point-process theorem requires an independent analytic proof;
this script verifies its finite joint-probability identity and scale numerically.
"""
from fractions import Fraction
from math import gamma, lgamma, exp


def all_words(q, n):
    words = [tuple([1] * q)]
    for label in range(2, n + 1):
        piece = (label,) * q
        words = [word[:gap] + piece + word[gap:]
                 for word in words for gap in range(len(word) + 1)]
    return words


def intact_mask(word, q, n):
    result = 0
    for i in range(1, n + 1):
        start = word.index(i)
        if word[start:start + q] == (i,) * q:
            result |= 1 << (i - 1)
    return result


def exact_joint(q, n, labels):
    labels = sorted(labels)
    probability = Fraction(1)
    present = 0
    for l in range(1, n):
        if l in labels:
            present += 1
        probability *= Fraction(q * l + 1 - (q - 1) * present, q * l + 1)
    return probability


def run():
    assertions = 0
    for q in (2, 3, 4):
        max_n = 6 if q == 2 else 5
        for n in range(1, max_n + 1):
            words = all_words(q, n)
            assert len(words) == __import__('math').prod(q * l + 1 for l in range(1, n))
            assertions += 1
            masks = [intact_mask(word, q, n) for word in words]
            for subset in range(1 << n):
                observed = Fraction(sum((mask & subset) == subset for mask in masks), len(masks))
                expected = exact_joint(q, n, [i for i in range(1, n + 1) if subset & (1 << (i - 1))])
                assert observed == expected, (q, n, subset, observed, expected)
                assertions += 1
            assert all(mask & (1 << (n - 1)) for mask in masks)
            assertions += 1

    for q in (2, 3, 4):
        alpha = (q - 1) / q
        scale_power = alpha / (alpha + 1)
        n = 10 ** 8
        scale = n ** scale_power
        for t in (1.0, 2.0):
            cutoff = int(t * scale)
            mean = sum(exp(lgamma(n - 1 + 2/q) - lgamma(n + 1/q)
                           + lgamma(i + 1/q) - lgamma(i - 1 + 2/q))
                       for i in range(1, cutoff + 1))
            limit = t ** (alpha + 1) / (alpha + 1)
            assert abs(mean - limit) < 0.08, (q, t, mean, limit)
            assertions += 1
    print(f"PASS: {assertions} exact/numerical assertions; no simulation-based infinity claim")


if __name__ == '__main__':
    run()
