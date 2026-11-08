#!/usr/bin/env python3
"""Exact rational certificate for a comparison of two power-sum congruence densities."""
from fractions import Fraction
from math import gcd, isqrt


def prime(n):
    if n < 2:
        return False
    return all(n % d for d in range(2, isqrt(n) + 1))


def admissible_by_obstructions(n, Q):
    # A new obstruction p must divide n and have (p-1) dividing Q*n.
    # Testing every p dividing n by trial division is finite and exact.
    for p in range(2, n + 1):
        if n % p == 0 and prime(p) and Q % p and (Q * n) % (p - 1) == 0:
            return False
    return True


common_primes = [p for p in range(2, 101)
                 if prime(p) and 1806 % p != 0 and p % 43 != 1]
C = sum((Fraction(gcd(42, p - 1), p * (p - 1))
         for p in common_primes), Fraction(0))
assert len(common_primes) == 21
assert C < Fraction(227, 1000)

exceptional_k = [k for k in range(2, 1001, 2) if prime(43 * k + 1)]
S = sum((Fraction(gcd(42, k), k * (43 * k + 1))
         for k in exceptional_k), Fraction(0))
assert len(exceptional_k) == 109
assert S < Fraction(9, 2000)

# The omitted common-prime reciprocal sum is <= 42/100.
# The exceptional k>1000 tail is < 42/(43*1000).
common_density_lower = 1 - Fraction(227, 1000) - Fraction(42, 100)
assert common_density_lower == Fraction(353, 1000)
certified_gap = common_density_lower / 43 - Fraction(9, 2000) - Fraction(42, 43000)
assert certified_gap == Fraction(47, 17200)
assert certified_gap > Fraction(1, 400)

# Direct, independent power-sum congruence checks for small cases.
for Q in (42, 1806):
    for n in range(1, 36):
        m = Q * n
        actual = sum(pow(a, m, m) for a in range(1, m + 1)) % m
        criterion = admissible_by_obstructions(n, Q)
        assert (actual == n) == criterion, (Q, n, actual, criterion)

# Direct finite checks of the 43-obstruction decomposition.
for n in range(1, 300):
    common_ok = True
    for p in range(5, n + 1):
        if prime(p) and 1806 % p and p % 43 != 1:
            if n % (p * (p - 1) // gcd(42, p - 1)) == 0:
                common_ok = False
                break
    N42 = admissible_by_obstructions(n, 42)
    assert N42 == (common_ok and n % 43 != 0)
    exceptional_bad = False
    for k in range(2, n + 1, 2):
        p = 43 * k + 1
        if prime(p):
            b = p * k // gcd(42, k)
            if n % b == 0:
                exceptional_bad = True
                break
    assert admissible_by_obstructions(n, 1806) == (common_ok and not exceptional_bad)

print('VERIFY_OK')
print('common_primes=', len(common_primes), 'exceptional_prime_indices=', len(exceptional_k))
print('C_exact_below_227_over_1000=', C < Fraction(227, 1000))
print('S_exact_below_9_over_2000=', S < Fraction(9, 2000))
print('gap_lower_bound=', certified_gap, 'positive=', certified_gap > 0)
print('power_sum_cases=', 70, 'residue_decomposition_cases=', 299)
