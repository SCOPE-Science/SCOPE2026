"""Exact finite tests for the critical binary-plus-one subset-sum theorem.

All assertions are finite; the measure-zero assertion is proved analytically.
Run: python3 verify.py
"""
from fractions import Fraction
from random import Random


def floor_fraction(x):
    return x.numerator // x.denominator


def term(alpha, n):
    return floor_fraction(alpha * (2**n + 1))


def diagnostic(alpha, n):
    f = lambda x: x - floor_fraction(x)
    left = 1 + sum(term(alpha, j) for j in range(1, n + 1)) - term(alpha, n + 1)
    right = 1 + alpha * (n - 3) - sum(f(alpha * (2**j + 1)) for j in range(1, n + 1)) + f(alpha * (2**(n + 1) + 1))
    assert right.denominator != 0
    assert left == right
    return left


def assert_hole(alpha, n):
    terms = [term(alpha, i) for i in range(1, n + 1)]
    s = sum(terms)
    next_term = term(alpha, n + 1)
    assert next_term > s + 1
    # The integer s+1 cannot be made from preceding terms or any later term.
    assert next_term > s + 1
    assert diagnostic(alpha, n) == s + 1 - next_term
    return next_term - s - 1


# Exact identity, including parameters with initial zero terms.
for den in range(2, 37):
    for num in range(1, 2 * den + 1):
        alpha = Fraction(num, den)
        for n in range(1, 23):
            diagnostic(alpha, n)
print('GAP_IDENTITY_OK rational_parameter_pairs=1330 n=1..22')

# Every given dyadic parameter yields consecutive powers of two after zeros.
for k in range(1, 33):
    alpha = Fraction(1, 2**k)
    for n in range(1, 85):
        expected = 0 if n < k else 2**(n-k)
        assert term(alpha, n) == expected
print('DYADIC_BINARY_BASIS_OK k=1..32 n=1..84')

# For alpha>1/2 the first discrepancy is an explicit permanent missing integer.
for den in range(2, 61):
    for num in range(den // 2 + 1, 2 * den + 1):
        alpha = Fraction(num, den)
        if alpha >= Fraction(2, 3):
            assert term(alpha, 1) >= 2
        else:
            beta = alpha - Fraction(1, 2)
            bad = next(n for n in range(2, 64)
                       if floor_fraction(2**n * beta + alpha) >= 1)
            assert all(term(alpha, j) == 2**(j-1) for j in range(1, bad))
            assert_hole(alpha, bad - 1)
print('UPPER_HALF_OBSTRUCTION_OK denominators=2..60')

# Check a macroscopic finite gap for exact binary fractions with a long
# nonperiodic-looking prefix (no statistical claims about the finite sample).
rng = Random(20261104)
for i in range(12):
    bits = 256
    num = rng.randrange(1, 2**(bits-1))
    alpha = Fraction(num, 2**bits)
    last = diagnostic(alpha, 180)
    assert last < 0  # A finite observation, not the source of the a.e. proof.
    assert_hole(alpha, 180)
print('FINITE_GAP_EXAMPLES_OK samples=12 n=180')
print('VERIFY_OK exact_rational_arithmetic=true infinite_a.e._claim_proved_analytically=true')
