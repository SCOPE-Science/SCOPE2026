#!/usr/bin/env python3
"""Exact finite checks for sharp ternary digit-product progressions."""
import json


def ternary_digits(n):
    assert n >= 0
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(n % 3)
        n //= 3
    return digits


def digit_product_nonzero(n):
    assert n > 0
    result = 1
    for d in ternary_digits(n):
        if d:
            result *= d
    return result


def is_prodigious(n):
    return n > 0 and n % digit_product_nonzero(n) == 0


# A residue in F is guaranteed non-prodigious for every positive integer in it:
# its 2-adic valuation is exactly 1, but its lowest three ternary digits
# contain at least two occurrences of the digit 2.
forbidden = []
for residue in range(0, 108, 2):
    low = ternary_digits(residue % 27)
    if residue % 4 == 2 and low.count(2) >= 2:
        forbidden.append(residue)
assert forbidden == [26, 50, 62, 74, 78, 98, 106]

# With step 2, one traverses all 54 even residue classes modulo 108.
# Every stretch of 14 such classes intersects F.
for start in range(0, 108, 2):
    assert any((start + 2*j) % 108 in forbidden for j in range(14))

# On odd starts, every product must be 1; the last two ternary
# digits then belong to {00,01,10,11}.
allowed_mod9 = {0, 1, 3, 4}
for start in range(9):
    assert any((start + 2*j) % 9 not in allowed_mod9 for j in range(3))

# Direct all-digit witness.  These thirteen positive terms have product <= 4.
witness = [108 + 2*j for j in range(13)]
products = [digit_product_nonzero(n) for n in witness]
assert products == [1, 2, 1, 2, 4, 1, 1, 2, 2, 2, 4, 2, 4]
assert all(is_prodigious(n) for n in witness)
assert not is_prodigious(134)

# There are infinitely many such progressions: when K>=5, adding
# 4*3^K prepends the ternary digits 11 without carrying, and is 0 mod 4.
for K in range(5, 51):
    shifted = [n + 4*3**K for n in witness]
    assert all(digit_product_nonzero(shifted[j]) == products[j] for j in range(13))
    assert all(is_prodigious(n) for n in shifted)

# Separate bounded spot-check: no run longer than 13 in a large range.
max_length, running = 0, 0
for n in range(2, 200001, 2):
    running = running + 1 if is_prodigious(n) else 0
    max_length = max(max_length, running)
assert max_length == 13

print(json.dumps({
    'forbidden_residues_mod108': forbidden,
    'forbidden_positions_in_even_step2_cycle': [r//2 for r in forbidden],
    'cyclic_gaps': [12, 6, 6, 2, 10, 4, 14],
    'max_gap_minus_one': 13,
    'odd_step2_run_max_at_most': 2,
    'sharp_witness_start': 108,
    'sharp_witness_end': 132,
    'sharp_witness_length': len(witness),
    'witness_digit_products': products,
    'shifted_witness_tests': 46,
    'independent_scan_even_limit': 200000,
    'independent_scan_max_run': max_length
}, sort_keys=True, indent=2))
