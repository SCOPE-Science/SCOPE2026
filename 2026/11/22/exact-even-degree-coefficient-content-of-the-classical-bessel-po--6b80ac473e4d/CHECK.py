#!/usr/bin/env python3
"""Recompute even-degree Bessel coefficient contents by independent formulas."""
from math import comb, gcd, prod


def odd_part(z):
    while z % 2 == 0:
        z //= 2
    return z


def bessel_formula(n, k):
    return comb(n + k, 2 * k) * prod(range(1, 2 * k, 2))


def target(n):
    block = (n - 1) * n * (n + 1) * (n + 2)
    return odd_part(block) // (3 if n % 3 == 1 else 1)


def v3(z):
    t = 0
    while z % 3 == 0:
        z //= 3
        t += 1
    return t


checks = 0
p0, p1 = [1], [1, 1]
for n in range(2, 257):
    # The differential-equation recurrence gives a coefficient list independent
    # of the factorial/binomial formula used to compute row content.
    new = [0] * (n + 1)
    for k, value in enumerate(p1):
        new[k + 1] += (2 * n - 1) * value
    for k, value in enumerate(p0):
        new[k] += value
    assert len(new) == n + 1 and new[0] == 1
    checks += 1
    even_content = 0
    for k in range(n + 1):
        assert new[k] == bessel_formula(n, k), (n, k)
        checks += 1
        if k and k % 2 == 0:
            even_content = gcd(even_content, new[k])
    assert even_content == target(n), (n, even_content, target(n))
    checks += 1
    r = 1 << (n.bit_length() - 1)
    assert r % 2 == 0 and new[r] % 2 == 1, n
    checks += 1
    if n % 3 == 1:
        assert n >= 4 and v3(new[4]) == v3(new[2]) - 1
        checks += 1
    p0, p1 = p1, new
print('PASS:', checks, 'exact assertions; n=2..256, all coefficients via independent recurrence.')
