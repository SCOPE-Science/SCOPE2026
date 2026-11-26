"""Exact finite certificate for binary-weight-three factor products.

This script checks the finite search implied by Kaneko--Stoll,
Products of integers with few nonzero digits, Theorem 2.2
(arXiv:2112.03077v1). The external theorem is not proved here.
"""
from math import isqrt

BOUND = 1 << 23
EXPECTED = (
    (7, 7, 49),
    (7, 19, 133),
    (7, 37, 259),
    (11, 35, 385),
    (13, 21, 273),
    (21, 49, 1029),
)


def by_product():
    """For every odd weight-three N < BOUND, trial-divide through sqrt(N)."""
    solutions = []
    products = 0
    candidate_divisors = 0
    for high in range(2, 23):
        for low in range(1, high):
            n = (1 << high) + (1 << low) + 1
            assert n < BOUND and n.bit_count() == 3
            products += 1
            for a in range(7, isqrt(n) + 1, 2):
                if a.bit_count() != 3:
                    continue
                candidate_divisors += 1
                if n % a == 0:
                    b = n // a
                    if b.bit_count() == 3:
                        assert a <= b and a % 2 == b % 2 == 1
                        solutions.append((a, b, n))
    return tuple(sorted(solutions)), products, candidate_divisors


def by_factors():
    """Independent factor-first enumeration, including repeated factors."""
    factors = sorted(
        1 + (1 << low) + (1 << high)
        for high in range(2, 23)
        for low in range(1, high)
    )
    solutions = []
    candidates = 0
    for index, a in enumerate(factors):
        if a * a >= BOUND:
            break
        for b in factors[index:]:
            n = a * b
            if n >= BOUND:
                break
            candidates += 1
            if n.bit_count() == 3:
                solutions.append((a, b, n))
    return tuple(sorted(solutions)), candidates


def main():
    s1, nprod, ndiv = by_product()
    s2, npairs = by_factors()
    assert nprod == 231
    assert ndiv == 5473
    assert npairs == 3672
    assert s1 == EXPECTED
    assert s2 == EXPECTED
    assert max(n for a, b, n in s1) == 1029
    print("VERIFY_OK")
    print("weight_three_products_below_2^23:", nprod)
    print("trial_divisor_checks:", ndiv)
    print("admissible_unordered_factor_pairs:", npairs)
    print("solutions:", s1)
    print("sharp_maximum_product: 1029")


if __name__ == "__main__":
    main()
