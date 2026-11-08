"""Finite corroboration of a self-contained analytic residual-length theorem.

Uses only the Python standard library. Finite checks are NOT an infinite proof.
"""
from fractions import Fraction
from itertools import product
from math import comb, log2, sqrt


def exhaustive_transform(bits):
    """Return (fair_output, residual) under exhaustive Peres recursion."""
    n = len(bits) // 2
    if n == 0:
        return (), bits
    u = tuple(bits[2 * j] ^ bits[2 * j + 1] for j in range(n))
    v = tuple(bits[2 * j + 1] for j in range(n) if u[j] == 0)
    y = tuple(bits[2 * j + 1] for j in range(n) if u[j] == 1)
    fu, ru = exhaustive_transform(u)
    fv, rv = exhaustive_transform(v)
    return fu + y + fv, ru + rv + bits[2 * n :]


def exact_means(limit):
    out = [Fraction(0), Fraction(1)]
    for m in range(2, limit + 1):
        n = m // 2
        expected = sum((Fraction(comb(n, k), 1 << n) * out[k]
                        for k in range(n + 1)), Fraction(0))
        out.append(out[n] + expected + (m % 2))
    return out


def main():
    means = exact_means(150)
    alpha = log2((1 + sqrt(5)) / 2)
    assert 0.5 < alpha < 1
    assert means[:9] == [Fraction(0), Fraction(1), Fraction(3, 2),
                         Fraction(5, 2), Fraction(19, 8),
                         Fraction(27, 8), Fraction(15, 4),
                         Fraction(19, 4), Fraction(507, 128)]
    for n in range(13):
        total = 0
        for bits in product((0, 1), repeat=n):
            fair, residual = exhaustive_transform(bits)
            assert len(fair) + len(residual) == n
            total += len(residual)
        assert Fraction(total, 1 << n) == means[n], (n, total, means[n])
    for n in range(1, 151):
        value = float(means[n])
        lower = (n ** alpha + 1) / 2
        upper = 2 * n ** alpha - 1
        assert lower <= value + 1e-10, (n, value, lower)
        assert value <= upper + 1e-10, (n, value, upper)
    print('PASS: exact recursion vs all binary words at lengths 0..12')
    print('PASS: finite 1..150 bounds (analytic proof in RESULT.md)')
    print('alpha:', alpha, 'a_150:', float(means[150]))


if __name__ == '__main__':
    main()
