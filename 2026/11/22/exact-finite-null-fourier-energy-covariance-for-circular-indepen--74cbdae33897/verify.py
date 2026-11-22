"""Exact coefficient-extraction checks for finite circular Fourier independence energies.

Every Haar expectation is computed by extracting the constant term of a
Laurent polynomial in independent unit-circle coordinates. No simulation.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product


def multiply(left, right):
    output = defaultdict(int)
    for a, x in left.items():
        for b, y in right.items():
            output[tuple(i + j for i, j in zip(a, b))] += x * y
    return {a: x for a, x in output.items() if x}


def conjugate(poly):
    return {tuple(-i for i in exponent): coeff for exponent, coeff in poly.items()}


def numerator(n, p, q):
    """Laurent polynomial n^2 D_(p,q)."""
    result = defaultdict(int)
    for i, j in product(range(n), repeat=2):
        exponent = [0] * (2 * n)
        exponent[i] += p
        exponent[n + j] += q
        result[tuple(exponent)] += (n - 1 if i == j else -1)
    return {a: x for a, x in result.items() if x}


def constant(poly):
    return poly.get((0,) * len(next(iter(poly))), 0)


def actual_covariance(n, p, q, r, s):
    first = numerator(n, p, q)
    second = numerator(n, r, s)
    first_sq = multiply(first, conjugate(first))
    second_sq = multiply(second, conjugate(second))
    joint = Fraction(constant(multiply(first_sq, second_sq)), n**8)
    return joint - Fraction((n - 1)**2, n**4)


def predicted_covariance(n, p, q, r, s):
    x_match = abs(p) == abs(r)
    y_match = abs(q) == abs(s)
    if not x_match and not y_match:
        return Fraction(0)
    if x_match != y_match:
        return Fraction(n - 1, n**5)
    if p * q * r * s < 0:
        return Fraction((n - 1) * (n + 3), n**6)
    return Fraction((n - 1) * (n * (n - 1)**2 + 3), n**6)


def formula_variance(n, pmax, qmax):
    return Fraction(
        2 * pmax * qmax *
        (n * (n - 1)**2 + n + 6 + 2 * n * (pmax + qmax - 2)),
        n**2 * (n - 1),
    )


def combinatorial_variance(n, pmax, qmax):
    frequencies = [(p, signed_q) for p in range(1, pmax + 1)
                   for q in range(1, qmax + 1) for signed_q in (q, -q)]
    return sum((predicted_covariance(n, p, q, r, s) *
                Fraction(n**4, (n - 1)**2)
                for p, q in frequencies for r, s in frequencies), Fraction(0))


def main():
    cases = [
        (1, 1, 2, 3), (1, 1, 1, 3), (1, 1, 3, 1),
        (1, 1, -1, 3), (1, 1, 1, 1), (1, 1, -1, -1),
        (1, 1, 1, -1), (1, 1, -1, 1), (1, 1, 2, -2),
        (1, 2, 1, 2), (1, 2, 1, -2),
    ]
    checked = 0
    for n in (2, 3, 4):
        for p, q, r, s in cases:
            result = actual_covariance(n, p, q, r, s)
            expected = predicted_covariance(n, p, q, r, s)
            assert result == expected, (n, p, q, r, s, result, expected)
            checked += 1
        for pmax, qmax in ((1, 1), (1, 3), (2, 2), (3, 2)):
            assert combinatorial_variance(n, pmax, qmax) == formula_variance(n, pmax, qmax)
            checked += 1
    print(f"Passed {checked} exact rational assertions ({len(cases)*3} independent Laurent checks).")

if __name__ == "__main__":
    main()
