"""Independent elementary arithmetic and finite-section checks for the stated Jacobi family.

Run: python3 checker.py. Standard-library only. Finite sections are not
proof of the infinite counting law; the analytical proof is in RESULT.md.
"""
from fractions import Fraction
from math import sqrt, isfinite


def bond(n, s):
    t = s / 2
    return (s / 2) * (n + 1) * sqrt((n + 2) * (n + 3)) / (
        (n + 1 + t) * (n + 2 + t)
    )


def eigenvalues_above_finite_section(n_dimension, s, level):
    """Sturm inertia for the real tridiagonal Jacobi finite section."""
    p = -level
    negative = int(p < 0)
    for j in range(n_dimension - 1):
        p = -level - bond(j, s) ** 2 / p
        if abs(p) < 1e-200:
            raise ArithmeticError("near-zero Sturm pivot; change level")
        negative += int(p < 0)
    return n_dimension - negative


def run_checks():
    total = 0
    for n in range(800):
        # Exact difference at the sharp candidate t = 1/4.
        x = Fraction(n)
        t = Fraction(1, 4)
        lhs = (x + 1 + t) ** 2 * (x + 2 + t) ** 2
        rhs = (x + 1) ** 2 * (x + 2) * (x + 3)
        assert lhs - rhs == Fraction(224*n*n + 688*n + 489, 256)
        assert lhs - rhs > 0
        total += 2
    for s in (0.5, 0.75, 1.0, 2.0, 5.0, 10.0):
        for n in range(500):
            assert bond(n, s) < s/2
            total += 1
    for s in (0.05, 0.2, 0.25, 0.4):
        for n in (2000, 4000, 8000):
            assert eigenvalues_above_finite_section(n, s, s) >= 1
            total += 1
    for s in (0.5, 0.75, 1.5):
        for n in (2000, 4000):
            assert eigenvalues_above_finite_section(n, s, s) == 0
            total += 1
    for n in (1000, 4000, 12000):
        c = eigenvalues_above_finite_section(n, 0.25, 0.2501)
        assert c in range(1, 15)
        total += 1
    # First-order tail, comparing the exact ratio with asymptotic statement.
    for s in (0.12, 0.25, 0.4, 0.5, 0.8):
        n = 2_000_000
        r = 2 * bond(n, s) / s
        assert isfinite(r)
        assert abs(n*(r-1) - (0.5-s)) < 0.00004
        total += 2
    return total


if __name__ == '__main__':
    print(f"PASS: {run_checks()} finite exact/inertia/asymptotic assertions")
