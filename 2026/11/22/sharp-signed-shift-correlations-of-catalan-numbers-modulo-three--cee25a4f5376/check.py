"""Exact reproducibility checks for the signed Catalan three-adic correlation theorem."""
from fractions import Fraction
from functools import lru_cache
from math import comb


def digit_sign(n):
    z = 1
    while n:
        digit = n % 3
        if digit == 2:
            return 0
        if digit == 1:
            z = -z
        n //= 3
    return z


def catalan_sign(n):
    return digit_sign((n + 1) // 3)


@lru_cache(None)
def alpha(v):
    if v == 0:
        return Fraction(1)
    q, t = divmod(v, 3)
    if t == 0:
        return alpha(q)
    if t == 1:
        return -alpha(q) / 2
    return -alpha(q + 1) / 2


def correlation(h):
    q, t = divmod(h, 3)
    return ((3 - t) * alpha(q) + t * alpha(q + 1)) / 2


def is_power_of_three(n):
    if n < 1:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1


checks = 0
for n in range(500):
    assert comb(2 * n, n) // (n + 1) % 3 == catalan_sign(n) % 3, n
    checks += 1
for r in range(3, 8):
    length = 3 ** r
    signs = [catalan_sign(n) for n in range(length + 202)]
    for h in range(1, 202):
        observed = sum(signs[n] * signs[n + h] for n in range(length))
        if h < 3 ** (r - 2):
            assert observed == correlation(h) * 2 ** r, (r, h, observed)
        checks += 1
for h in range(1, 30001):
    val = correlation(h)
    assert -Fraction(3, 4) <= val <= Fraction(3, 4), h
    if val == Fraction(3, 4):
        assert h == 1, h
    if val == -Fraction(3, 4):
        assert h >= 3 and is_power_of_three(h), h
    if h == 1 or (h >= 3 and is_power_of_three(h)):
        assert abs(val) == Fraction(3, 4), h
    checks += 1
print(f"passed {checks} exact Catalan, finite correlation and bound assertions")
