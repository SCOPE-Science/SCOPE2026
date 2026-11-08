"""Exact rational finite checks for the diagonal-composition shadowing theorem.

These tests illustrate its algebraic recurrences, not its infinite-dimensional proof.
Run: python check_shadowing.py
"""
from fractions import Fraction

checks = 0

def check(statement):
    global checks
    assert statement
    checks += 1

# Scalar eigenmode pulse recurrences and forced initial coefficients.
for t in (Fraction(2, 5), Fraction(3, 7), Fraction(7, 5), Fraction(11, 3)):
    for k in range(1, 29):
        a = Fraction(1, 3 ** (k + 5))
        if t < 1:
            y = -t ** (k - 1) * a
            for m in range(k, k + 14):
                xminusm = -t ** (-(m - k + 1)) * a
                check(xminusm == t ** (-m) * y)
            check(y * t ** (1 - k) == -a)
        else:
            y = t ** (-k) * a
            for m in range(k, k + 14):
                xm = t ** (m - k) * a
                check(xm == t ** m * y)
            check(t ** k * y == a)

# Sample exact rational subcritical tail bounds: |c|=5, rho=1/2, N=3.
q = Fraction(5, 8)
for total_degree in range(3, 27):
    for steps in range(0, 40):
        weight_ratio = 5 ** steps * Fraction(1, 2) ** (total_degree * steps)
        check(weight_ratio <= q ** steps)

# A mixed coordinate example has no resonance despite bounded monomial moduli.
# 5 * 3**b / 2**a cannot equal one because its numerator is divisible by five.
for a in range(0, 30):
    for b in range(0, 30):
        t = Fraction(5 * 3 ** b, 2 ** a)
        check(t != 1)

# Exact bounded-modulus selection for two-coordinate mixed dilations 1/2 and 3.
# Use the integer part of m log_2(3), checking a rational inequality rather than logs.
for m in range(1, 120):
    power = 3 ** m
    n = power.bit_length() - 1  # floor(log_2(3**m)) exactly
    t = Fraction(5 * 3 ** m, 2 ** n)
    check(Fraction(5) <= t < Fraction(10))
    check(n + m >= m)

# Stable and inverse-stable nonresonance in the sample cases.
for a in range(0, 25):
    for b in range(0, 25):
        check(Fraction(5, (2 ** a) * (3 ** b)) != 1)
        check(Fraction((2 ** a) * (3 ** b), 5) != 1)

print(f"DIAGONAL_SHADOWING_CHECK_OK {checks} exact rational assertions")
