#!/usr/bin/env python3
"""Exact coefficient and 5-adic lifting checks for a 5-core tuple coefficient.
Requires Python 3 standard library only. Run: python3 verify.py
"""
from fractions import Fraction

N = 39
P = 5

def sigma(m):
    return sum(d for d in range(1, m + 1) if m % d == 0)

B = [0] + [sigma(j) - (25 * sigma(j // 5) if j % 5 == 0 else 0)
           for j in range(1, N + 1)]

def v5_fraction(value):
    value = Fraction(value)
    if not value:
        return None
    numerator, denominator = abs(value.numerator), value.denominator
    level = 0
    while numerator % 5 == 0:
        numerator //= 5
        level += 1
    while denominator % 5 == 0:
        denominator //= 5
        level -= 1
    return level

def residue5_fraction(value):
    value = Fraction(value)
    assert v5_fraction(value) is not None and v5_fraction(value) >= 0
    assert value.denominator % 5 != 0
    return (value.numerator * pow(value.denominator, -1, 5)) % 5

def polynomial_coefficients():
    # R_n(X)=[z^n](E(z^5)^5/E(z))^(111+125X), n=0,...,39.
    rows = [[Fraction(1)]]
    for n in range(1, N + 1):
        sums = [Fraction(0) for _ in range(n + 1)]
        for j in range(1, n + 1):
            for degree, c in enumerate(rows[n - j]):
                sums[degree] += B[j] * c
        result = [Fraction(0) for _ in range(n + 1)]
        for degree, c in enumerate(sums):
            result[degree] += Fraction(111, n) * c
            if degree < n:
                result[degree + 1] += Fraction(125, n) * c
        rows.append(result)
    return rows[N]

def coefficient_direct(k):
    # Integer logarithmic-derivative recurrence, not polynomial interpolation.
    a = [1] + [0] * N
    for n in range(1, N + 1):
        numerator = k * sum(B[j] * a[n - j] for j in range(1, n + 1))
        assert numerator % n == 0
        a[n] = numerator // n
    return a[N]

def product_coefficients():
    # Independent Euler-product construction of one 5-core factor F(z).
    partitions = [1] + [0] * N
    for j in range(1, N + 1):
        for n in range(j, N + 1):
            partitions[n] += partitions[n - j]
    numerator = [1] + [0] * N
    for m in range(1, N // 5 + 1):
        for _ in range(5):
            for n in range(N, 5 * m - 1, -1):
                numerator[n] -= numerator[n - 5 * m]
    return [sum(numerator[j] * partitions[n - j] for j in range(n + 1))
            for n in range(N + 1)]

def multiply(a, b):
    c = [0] * (N + 1)
    for i, x in enumerate(a):
        if x:
            for j in range(N + 1 - i):
                c[i + j] += x * b[j]
    return c

def power_coefficient(f, exponent):
    total = [1] + [0] * N
    base = f[:]
    while exponent:
        if exponent & 1:
            total = multiply(total, base)
        exponent //= 2
        if exponent:
            base = multiply(base, base)
    return total[N]

def norm(i):
    numerator = coefficient_direct(111 + 125 * i)
    assert numerator % 625 == 0
    return numerator // 625

def main():
    c = polynomial_coefficients()
    assert len(c) == 40
    assert v5_fraction(c[0]) == 5
    assert v5_fraction(c[1]) == 4
    assert v5_fraction(c[2]) == 4
    assert residue5_fraction(c[1] / 625) == 3
    assert residue5_fraction(c[2] / 625) == 3
    assert all(not c[j] or v5_fraction(c[j]) >= 6 for j in range(3, 40))
    assert min(v5_fraction(x) for x in c if x) == 4
    assert all(sum(c[j] * (i ** j) for j in range(40)) == coefficient_direct(111 + 125 * i)
               for i in range(8))
    f = product_coefficients()
    for i in [0, 1, 2, 3, 4, 5, 9, 24]:
        assert power_coefficient(f, 111 + 125 * i) == coefficient_direct(111 + 125 * i)
    for i in range(20):
        assert norm(i) % 5 == (3 * i * (i + 1)) % 5
    for initial in (0, 4):
        root = initial
        for depth in range(1, 9):
            modulus = 5 ** depth
            if depth > 1:
                old_modulus = 5 ** (depth - 1)
                candidates = [root + old_modulus * j for j in range(5)]
                valid = [i for i in candidates if norm(i) % modulus == 0]
                assert len(valid) == 1
                root = valid[0]
            assert norm(root) % modulus == 0
            # All siblings at this level are nonroots by exact integer arithmetic.
    print('PASS: exact degree-39 polynomial coefficient certificate;')
    print('PASS: independent truncated Euler products for eight tuple orders;')
    print('PASS: two distinct simple 5-adic root branches through precision 5^8.')

if __name__ == '__main__':
    main()
