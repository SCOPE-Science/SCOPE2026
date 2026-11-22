#!/usr/bin/env python3
"""Exact finite checks for a Farey/rotation record mean identity.

This program uses only the Python standard library. It is supplementary
finite evidence; the accompanying proof establishes every integer case.
"""
from fractions import Fraction
from math import gcd


def mu(n):
    v, p, parity = n, 2, 0
    while p * p <= v:
        if v % p == 0:
            v //= p
            if v % p == 0:
                return 0
            parity ^= 1
            while v % p == 0:
                v //= p
        p += 1
    if v > 1:
        parity ^= 1
    return -1 if parity else 1


def record_from_floors(d, x):
    return all(
        (d * x.numerator) // x.denominator
        - (j * x.numerator) // x.denominator
        - ((d - j) * x.numerator) // x.denominator == 0
        for j in range(1, d)
    )


def predicted_intervals(d):
    out = []
    for r in range(1, d):
        if gcd(r, d) == 1:
            b = pow(r, -1, d)
            a = (r * b - 1) // d
            out.append((Fraction(a, b), Fraction(r, d)))
    return sorted(out)


def measured_intervals(d):
    cuts = {Fraction(0), Fraction(1)}
    for den in range(1, d + 1):
        cuts.update(Fraction(num, den) for num in range(1, den))
    cuts = sorted(cuts)
    return [(left, right) for left, right in zip(cuts, cuts[1:])
            if record_from_floors(d, (left + right) / 2)]


def harmonic(n, power):
    return sum((Fraction(1, k ** power) for k in range(1, n + 1)), Fraction(0))


def main():
    checked_cells = 0
    direct = {1: Fraction(0)}
    for d in range(2, 56):
        found = measured_intervals(d)
        expected = predicted_intervals(d)
        assert found == expected, (d, found, expected)
        assert len(found) == sum(gcd(b, d) == 1 for b in range(1, d))
        exact = sum((right - left for left, right in found), Fraction(0))
        arithmetic = sum((Fraction(1, d * b) for b in range(1, d)
                          if gcd(b, d) == 1), Fraction(0))
        assert exact == arithmetic, (d, exact, arithmetic)
        direct[d] = direct[d - 1] + exact
        checked_cells += len(found)
    print(f"Exact Farey interval comparison: 54 denominators; {checked_cells} true cells")
    for n in range(1, 56):
        rhs = sum((Fraction(mu(k), 2 * k * k)
                   * (harmonic(n // k, 1)**2 - harmonic(n // k, 2))
                   for k in range(1, n + 1)), Fraction(0))
        assert rhs == direct[n], (n, rhs, direct[n])
    print("Exact direct-sum / Möbius-harmonic identity: N=1,...,55")
    print("P2=", direct[2], "; P3=", direct[3] - direct[2],
          "; P5=", direct[5] - direct[4],
          "; P7=", direct[7] - direct[6], sep="")
    print("All supplementary finite checks passed")


if __name__ == '__main__':
    main()
