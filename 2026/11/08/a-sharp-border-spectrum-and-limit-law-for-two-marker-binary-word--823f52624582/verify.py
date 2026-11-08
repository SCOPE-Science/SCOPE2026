#!/usr/bin/env python3
"""Independent finite checks for the fixed-weight-two longest-border theorem."""
from collections import Counter
from fractions import Fraction
from math import comb, floor, ceil


def longest_border_kmp(word):
    """Prefix-function calculation, independent of the gap classification."""
    pi = [0] * len(word)
    for j in range(1, len(word)):
        k = pi[j - 1]
        while k and word[k] != word[j]:
            k = pi[k - 1]
        if word[k] == word[j]:
            k += 1
        pi[j] = k
    return pi[-1]


def border_by_gaps(a, b, c):
    return a + c + 1 if b >= max(a, c) else min(a, c)


def count_by_formula(n, t):
    if n < 2 or not (0 <= t < n):
        return 0
    m = n - 2
    i = 0
    if t >= 1:
        i = max(0, min(t - 1, n - t - 1) - max(0, 2 * t - n) + 1)
    if 3 * t <= m:
        ii = 2 * ((m - t + 1) // 2)
    elif 2 * t <= m:
        ii = 2 * (m - 2 * t) + 1
    else:
        ii = 0
    return i + ii


def law_density(x):
    if not (0 <= x <= Fraction(2, 3)):
        return Fraction(0)
    return Fraction(2) if x <= Fraction(1, 3) else 4 - 6 * x


def series_multiplication(left, right, degree):
    out = [0] * (degree + 1)
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right[:degree - i + 1]):
            if b:
                out[i + j] += a * b
    return out


def geom_series(z_power, u_power, degree):
    """Sparse bivariate expansion of 1/(1-z^z_power u^u_power)."""
    result = Counter()
    for k in range(degree // z_power + 1):
        result[(k * z_power, k * u_power)] = 1
    return result


def mul2(a, b, degree):
    out = Counter()
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            if i + k <= degree:
                out[(i + k, j + l)] += x * y
    return out


def gf_coeffs(degree):
    """Coefficient extraction from the stated bivariate rational formula."""
    one = {(0, 0): 1}
    zz = geom_series(1, 0, degree)
    a = mul2(zz, geom_series(2, 1, degree), degree)
    a = mul2(a, geom_series(3, 2, degree), degree)
    a = mul2(a, {(0, 1): 1, (2, 2): 1}, degree)
    out = Counter(a)
    # First off-diagonal contribution: 2 z / ((1-z)^2(1-z^2u)).
    part = mul2(zz, zz, degree)
    part = mul2(part, geom_series(2, 1, degree), degree)
    part = mul2(part, {(1, 0): 2}, degree)
    out.update(part)
    # Second off-diagonal contribution: -2z^2 / ((1-z)(1-z^2)(1-z^3u)).
    part = mul2(zz, geom_series(2, 0, degree), degree)
    part = mul2(part, geom_series(3, 1, degree), degree)
    part = mul2(part, {(2, 0): -2}, degree)
    out.update(part)
    # Diagonal: z^2u/((1-z)(1-z^2u)) - z^3u/((1-z)(1-z^3u)).
    part = mul2(zz, geom_series(2, 1, degree), degree)
    part = mul2(part, {(2, 1): 1}, degree)
    out.update(part)
    part = mul2(zz, geom_series(3, 1, degree), degree)
    part = mul2(part, {(3, 1): -1}, degree)
    out.update(part)
    return out


def run():
    total_words = 0
    for n in range(2, 91):
        counts = Counter()
        for i in range(n):
            for j in range(i + 1, n):
                word = bytearray(b'0' * n)
                word[i] = ord('1')
                word[j] = ord('1')
                kmp = longest_border_kmp(word)
                a, b, c = i, j - i - 1, n - j - 1
                assert kmp == border_by_gaps(a, b, c), (n, i, j, kmp, a, b, c)
                counts[kmp] += 1
                total_words += 1
        assert sum(counts.values()) == comb(n, 2)
        assert max(counts) == (2 * n - 1) // 3
        assert all(counts[t] == count_by_formula(n, t) for t in range(n))
    g = gf_coeffs(35)
    assert all(g[m, t] == count_by_formula(m + 2, t)
               for m in range(36) for t in range(m + 2))
    assert all(g[m, t] == 0 for m in range(36) for t in range(m + 2, m + 7))
    for n in (101, 202, 500, 1000, 2000):
        assert sum(count_by_formula(n, t) for t in range(n)) == comb(n, 2)
        assert max(t for t in range(n) if count_by_formula(n, t)) == (2 * n - 1) // 3
    # Moment integration of the explicit density (exact rational arithmetic).
    # First segment: f=2 on [0,1/3]; second: f=4-6x on [1/3,2/3].
    from fractions import Fraction as Q
    a, b = Q(1, 3), Q(2, 3)
    def primitive_mass(x): return 4*x - 3*x*x
    def primitive_first(x): return 2*x*x - 2*x*x*x
    def primitive_second(x): return Q(4, 3)*x*x*x - Q(3, 2)*x*x*x*x
    mass = 2*a + primitive_mass(b)-primitive_mass(a)
    mean = a*a + primitive_first(b)-primitive_first(a)
    second = Q(2, 3)*a*a*a + primitive_second(b)-primitive_second(a)
    assert mass == 1
    assert mean == Q(7, 27)
    assert second == Q(5, 54)
    assert second - mean*mean == Q(37, 1458)
    # Explicit finite local limit: uniformly bounded count discrepancy.
    for n in (90, 201, 500, 1000, 2000):
        discrepancies = [abs(Q(count_by_formula(n, t)) - Q(n, 2)*law_density(Q(t, n)))
                         for t in range(n)]
        assert max(discrepancies) <= 6, (n, max(discrepancies))
    print('VERIFY_OK')
    print('Direct independent KMP words:', total_words, '(every binary word with two ones, lengths 2..90)')
    print('Bivariate rational-series coefficients: all degrees <=35, all possible borders')
    print('Exact count normalization and sharp maximum: lengths 101,202,500,1000,2000')
    print('Rational moment identities: mean 7/27, second moment 5/54, variance 37/1458')
    print('Uniform local-limit count discrepancy at selected large lengths: <=6')


if __name__ == '__main__':
    run()
