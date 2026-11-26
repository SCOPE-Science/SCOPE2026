"""Finite sanity tests for reciprocal divisibility of the sixth cyclotomic polynomial.

The universal result is proved by descent in RESULT.md; these tests are not a proof.
"""
from math import isqrt, gcd


def f(n: int) -> int:
    return n * n - n + 1


def possible_larger_partners(x: int):
    value = f(x)
    for d in range(1, isqrt(value) + 1):
        if value % d == 0:
            y = value // d
            if y > x:
                yield y
            if d > x and d != y:
                yield d


def verify():
    count = 0
    checked = 0
    for x in range(2, 5001):
        assert f(x) % x == 1
        for y in possible_larger_partners(x):
            count += 1
            assert f(x) % y == 0
            assert f(y) % x != 0, (x, y)
            z = f(x) // y
            assert 1 <= z < x
            assert (z * z * f(y) - f(z)) % x == 0
            checked += 1
    for x in range(1, 201):
        for y in range(1, 201):
            assert ((f(x) % y == 0 and f(y) % x == 0) == (x == y == 1))
    # Example of the arithmetic motivation, independently by the gcd sum.
    for n in [1, 7, 13, 43, 7 * 43, 614341]:
        h = sum(n // gcd(n, i) for i in range(1, n + 1))
        direct_integral = (h % n == 0)
        factors = []
        t = n
        d = 2
        while d * d <= t:
            a = 0
            while t % d == 0:
                t //= d
                a += 1
            if a:
                factors.append((d, a))
            d += 1
        if t > 1:
            factors.append((t, 1))
        value = 1
        for p, a in factors:
            value *= (p ** (2 * a + 1) + 1) // (p + 1)
        assert value == h
        assert direct_integral == (value % n == 0)
    assert sum(f(1) % n == 0 for n in range(1, 201)) == 1
    print(f'VERIFY_OK x_range=2..5000 divisor_partner_checks={count} '
          'direct_square=1..200 test_arithmetic_inputs=6')


if __name__ == '__main__':
    verify()
