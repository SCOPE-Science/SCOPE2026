#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt

def floor_sqrt_fraction(q: Fraction) -> int:
    n = isqrt(q.numerator // q.denominator)
    while Fraction((n + 1) * (n + 1), 1) <= q:
        n += 1
    while Fraction(n * n, 1) > q:
        n -= 1
    return n

count = 0
for a in range(1, 201):
    for b in range(1, 201):
        t = Fraction(a, 2 * b)
        n = floor_sqrt_fraction(t)
        eps = Fraction(2 * n * (n + 1) * b + a, 2 * n + 1)
        A2 = Fraction(2 * a * b, 1)

        lhs = A2 - eps * eps
        rhs = Fraction(
            (a - 2 * b * n * n) * (2 * b * (n + 1) * (n + 1) - a),
            (2 * n + 1) * (2 * n + 1),
        )
        assert lhs == rhs

        # Exact equality with the volume bound occurs precisely at a positive square slope.
        if lhs == 0:
            k = isqrt(t.numerator)
            assert t.denominator == 1 and k * k == t.numerator and k >= 1
        else:
            assert not (
                t.denominator == 1
                and isqrt(t.numerator) ** 2 == t.numerator
                and t.numerator >= 1
            )

        if n >= 1:
            # eps^2/A2 >= 1 - 1/(2n+1)^2.
            left = eps * eps * (2 * n + 1) ** 2
            right = A2 * ((2 * n + 1) ** 2 - 1)
            assert left >= right
            assert (left == right) == (t == n * (n + 1))

        count += 1

assert count == 40000
print("VERIFY_OK 40000 integer classes")
