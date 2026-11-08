"""Independent finite allocation checks and exact order-spacing arithmetic.

Usage: python verify.py
Python 3 standard library only.
"""
from fractions import Fraction
from itertools import combinations_with_replacement, product
import random


def direct_exists(weights):
    """Search complete allocations, checking agent EF1 and center EFX literally."""
    m = len(weights)
    for assignment in product(range(4), repeat=m):
        bundles = [tuple(weights[g] for g in range(m) if assignment[g] == i)
                   for i in range(4)]
        values = [sum(bundle) for bundle in bundles]
        ef1 = True
        for i in range(4):
            for j in range(4):
                if values[i] < values[j] and not any(
                    values[i] >= values[j] - x for x in bundles[j]
                ):
                    ef1 = False
                    break
            if not ef1:
                break
        if not ef1:
            continue
        centers = [tuple(weights[g] for g in range(m) if assignment[g] // 2 == c)
                   for c in range(2)]
        if all(
            sum(centers[c]) >= sum(centers[1 - c]) - x
            for c in range(2) for x in centers[1 - c]
        ):
            return True
    return False


def criterion(values):
    a = sorted(values, reverse=True)
    if len(a) <= 3:
        return True
    if len(a) == 4:
        return a[0] <= a[1] + a[2]
    if len(a) == 5:
        return a[0] <= a[1] + a[2] + a[4]
    raise ValueError('Only at most five goods are covered')


def laplace(rates, coefficients):
    result = Fraction(1)
    for rate, coefficient in zip(rates, coefficients):
        result *= Fraction(rate, rate + coefficient)
    return result


def exact_table(distribution):
    if distribution == 'uniform':
        p4 = 1 - laplace((1, 1), (1, 1))
        p5 = 1 - laplace((1, 1, 1), (2, 1, 1))
        loss = (laplace((1, 1, 1), (2, 1, 1))
                - laplace((1, 1, 1), (3, 2, 1))) / 5
    elif distribution == 'exponential':
        p4 = 1 - laplace((4, 3), (1, 1))
        p5 = 1 - laplace((5, 4, 3), (2, 1, 1))
        loss = (laplace((5, 4, 3), (2, 1, 1))
                - laplace((5, 4, 3), (4, 3, 1))) / 5
    else:
        raise ValueError(distribution)
    gain = p5 - p4 + loss
    return {(False, False): 1 - p4 - gain,
            (False, True): gain,
            (True, False): loss,
            (True, True): p4 - loss}


def main():
    counts = {}
    for m in (1, 2, 3, 4, 5):
        count = 0
        for profile in combinations_with_replacement(range(1, 8), m):
            count += 1
            assert direct_exists(profile) == criterion(profile), (m, profile)
        counts[m] = count
    assert exact_table('uniform') == {
        (False, False): Fraction(9, 120),
        (False, True): Fraction(21, 120),
        (True, False): Fraction(1, 120),
        (True, True): Fraction(89, 120),
    }
    assert exact_table('exponential') == {
        (False, False): Fraction(41, 105),
        (False, True): Fraction(22, 105),
        (True, False): Fraction(4, 105),
        (True, True): Fraction(38, 105),
    }
    assert criterion((5, 4, 3, 2)) and not criterion((5, 4, 3, 2, 20))
    assert not criterion((12, 6, 5, 4)) and criterion((12, 6, 5, 4, 3))
    rng = random.Random(94021)
    for m in (4, 5):
        for _ in range(300):
            profile = [rng.randint(1, 60) / 3 for _ in range(m)]
            assert criterion(profile) == direct_exists(profile)
    print('PASS: exhaustive integer profiles by size:', counts)
    print('PASS: 600 independent rational-valued profiles')
    for distribution in ('uniform', 'exponential'):
        print(distribution, exact_table(distribution))
    print('PASS: both deterministic resource-transition witnesses')


if __name__ == '__main__':
    main()
