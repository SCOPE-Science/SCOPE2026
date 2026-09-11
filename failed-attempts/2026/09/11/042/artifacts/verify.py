#!/usr/bin/env python3
"""Replayable exact-integer verification that C1(Q) strictly exceeds the claimed 7-point set.

Curve C1: y^2 = x^5 - 2x^3 + x + 1.
Claimed set S = {inf, (0,+-1), (1,+-1), (-1,+-1)}.
Witnesses outside S: P1=(7,127) and P2=(17/16,1033/1024) (plus hyperelliptic conjugates).
Uses only stdlib exact integer arithmetic.
"""
from fractions import Fraction

def check_int_point(x, y):
    lhs = y * y
    rhs = x**5 - 2 * x**3 + x + 1
    assert lhs == rhs, f"FAIL at ({x},{y}): {lhs} != {rhs}"
    return True

def check_frac_point(a, b, p, q):
    # x = a/b, y = p/q; verify (p/q)^2 == (a/b)^5 - 2(a/b)^3 + (a/b) + 1
    # via common denominator b^5 and q^2 cross-multiplication in integers.
    x = Fraction(a, b)
    y = Fraction(p, q)
    assert y * y == x**5 - 2 * x**3 + x + 1, f"FAIL at ({a}/{b},{p}/{q})"
    # independent raw-integer cross-check: N(a,b)/b^5 == p^2/q^2
    N = a**5 - 2 * a**3 * b**2 + a * b**4 + b**5
    assert N * q * q == p * p * b**5, "raw integer cross-check failed"
    return True

def main():
    # Witness 1: (7, 127). 7^5=16807, 2*7^3=686, 16807-686+7+1=16129=127^2.
    assert 7**5 - 2 * 7**3 + 7 + 1 == 16129
    assert 127**2 == 16129
    check_int_point(7, 127)
    check_int_point(7, -127)

    # Witness 2: (17/16, 1033/1024). Numerator N=1067089=1033^2, denom 16^5=1048576=1024^2.
    a, b, p, q = 17, 16, 1033, 1024
    N = a**5 - 2 * a**3 * b**2 + a * b**4 + b**5
    assert N == 1067089 == 1033**2, N
    assert b**5 == 1048576 == 1024**2
    check_frac_point(a, b, p, q)
    check_frac_point(a, b, -p, q)

    # Distinctness: x-coordinates 7 and 17/16 are not in {0, 1, -1}; y != 0 so +- are distinct.
    assert 7 not in (0, 1, -1)
    assert Fraction(17, 16) not in (Fraction(0), Fraction(1), Fraction(-1))
    assert 127 != 0 and Fraction(1033, 1024) != 0

    # Sanity: the 6 claimed affine points are on the curve (so witnesses are genuinely extra).
    for x, y in [(0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        check_int_point(x, y)

    print("VERIFY_OK")

if __name__ == "__main__":
    main()
