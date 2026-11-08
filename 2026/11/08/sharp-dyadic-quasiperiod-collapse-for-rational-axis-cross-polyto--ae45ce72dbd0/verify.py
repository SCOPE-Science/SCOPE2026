"""Exact reproducibility checks for dyadic pseudo-integral axis cross-polytopes.

Only the Python standard library is required. The verification is finite;
the general mathematical statements are proved separately.
"""
from itertools import combinations_with_replacement, product
from collections import Counter
from math import comb, gcd, lcm


def l1_counts(weights, maximum):
    """Independent coefficient recurrence for exact weighted absolute sums."""
    dp = [0] * (maximum + 1)
    dp[0] = 1
    for weight in weights:
        new = [0] * (maximum + 1)
        for j, count in enumerate(dp):
            if not count:
                continue
            new[j] += count
            for q in range(1, (maximum - j) // weight + 1):
                new[j + q * weight] += 2 * count
        dp = new
    running = 0
    result = []
    for count in dp:
        running += count
        result.append(running)
    return result


def polynomial_criterion(weights):
    c = Counter(weights)
    if any(a & (a - 1) for a in weights):
        return False
    top = max(weights).bit_length() - 1
    for j in range(1, top + 1):
        if c[1 << (j - 1)] < sum(c[1 << k] for k in range(j, top + 1)):
            return False
    return True


def has_only_unit_pole(weights):
    """Cyclotomic pole-order test, with all possible root orders tested."""
    for order in range(2, 2 * max(weights) + 1):
        denominator_poles = sum(a % order == 0 for a in weights)
        numerator_zeros = sum(
            order % 2 == 0 and a % order == order // 2
            for a in weights
        )
        if denominator_poles > numerator_zeros:
            return False
    return True


def predicted_min_period(weights):
    orders = []
    for m in range(2, max(weights) + 1):
        poles = sum(a % m == 0 for a in weights)
        zeros = sum(m % 2 == 0 and a % m == m // 2 for a in weights)
        if poles > zeros:
            orders.append(m)
    return lcm(*orders) if orders else 1


def is_quasipolynomial_period(values, dimension, period):
    for residue in range(period):
        samples = values[residue::period]
        if len(samples) < dimension + 3:
            return False
        for _ in range(dimension + 1):
            samples = [b - a for a, b in zip(samples, samples[1:])]
        if any(samples):
            return False
    return True


def brute_count(weights, dilate):
    values = [range(-dilate // a, dilate // a + 1) for a in weights]
    return sum(sum(a * abs(v) for a, v in zip(weights, point)) <= dilate
               for point in product(*values))


def check():
    assertions = 0
    cases = 0
    for dim in range(1, 6):
        for weights in combinations_with_replacement(range(1, 9), dim):
            criterion = polynomial_criterion(weights)
            poles = has_only_unit_pole(weights)
            assert criterion == poles, (weights, criterion, poles)
            assertions += 1
            values = l1_counts(weights, 45)
            differences = values[:]
            for _ in range(dim + 1):
                differences = [b - a for a, b in zip(differences, differences[1:])]
            is_polynomial_on_tested_range = all(v == 0 for v in differences)
            assert criterion == is_polynomial_on_tested_range, weights
            assertions += 1
            cases += 1
    # Exact minimum-period tests against independently generated count sequences.
    for dim in range(1, 5):
        for weights in combinations_with_replacement(range(1, 6), dim):
            D = lcm(*weights)
            values = l1_counts(weights, (dim + 3) * D)
            min_period = predicted_min_period(weights)
            assert D % min_period == 0
            assertions += 1
            for candidate in range(1, D + 1):
                if D % candidate:
                    continue
                observed = is_quasipolynomial_period(values, dim, candidate)
                assert observed == (candidate % min_period == 0), (weights, candidate, min_period)
                assertions += 1
    # Completely independent coordinate enumeration in small dimensions.
    for dim in range(1, 4):
        for weights in combinations_with_replacement(range(1, 5), dim):
            seq = l1_counts(weights, 12)
            for dilate in range(9):
                assert seq[dilate] == brute_count(weights, dilate), (weights, dilate)
                assertions += 1
    # Sharp boundary: the unique multiplicities in dimensions 2^r.
    for r in range(1, 6):
        weights = ([2 ** k for k in range(r)
                    for _ in range(2 ** (r - k - 1))] + [2 ** r])
        dim = len(weights)
        assert dim == 2 ** r and polynomial_criterion(weights)
        assertions += 1
        seq = l1_counts(weights, 70)
        for q in range(71):
            target = comb(q + dim, dim) + (comb(q, dim) if q >= dim else 0)
            assert seq[q] == target, (r, q, seq[q], target)
            assertions += 1
        # A smaller dimension with the same denominator cannot be polynomial.
        if r >= 2:
            for removed in range(dim - 1):
                assert not polynomial_criterion(weights[:removed] + weights[removed+1:])
                assertions += 1
    print(f"VERIFIED {assertions} exact assertions, {cases} weight multisets")


if __name__ == '__main__':
    check()
