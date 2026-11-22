"""Exact integer and finite recurrence checks for a 5-core tuple congruence theorem.

Requires only Python 3 standard library. No finite test substitutes for the
formal-series identities proved in the accompanying mathematical argument.
"""
from math import isqrt


def sigma(n):
    return sum(d + n // d if d * d != n else d
               for d in range(1, isqrt(n) + 1) if n % d == 0)


def low_coefficients(k, degree=14):
    """Coefficients of (E(q^5)^5/E(q))^k via its log derivative."""
    a = [1]
    for n in range(1, degree + 1):
        total = sum((sigma(j) - (25 * sigma(j // 5) if j % 5 == 0 else 0))
                    * a[n - j] for j in range(1, n + 1))
        assert (k * total) % n == 0
        a.append(k * total // n)
    return a


def u5_polynomial(target, modulus):
    """Coefficients P_target(t) mod modulus for U_5(zeta^target)."""
    P = [[1], [-1], [-1], [5], [-5]]
    for n in range(5, target + 1):
        p = [0] * (n // 5 + 2)
        for offset, weight in ((1, -5), (2, -15), (3, -25), (4, -25)):
            for j, coeff in enumerate(P[n - offset]):
                p[j] += weight * coeff
        for j, coeff in enumerate(P[n - 5]):
            p[j + 1] += coeff
        P.append([c % modulus for c in p])
    return [(j, coeff) for j, coeff in enumerate(P[target]) if coeff % modulus]


def test():
    assert u5_polynomial(229, 625) == [(45, 45)]
    assert u5_polynomial(1479, 3125) == [(295, 1920)]
    # Each listed equality is in Z/modulus Z, from exact integer arithmetic.
    for k, modulus, expected in (
        (21, 625, {9: 375}),
        (146, 625, {9: 250}),
        (396, 3125, {9: 1250}),
        (1021, 3125, {9: 625}),
        (1646, 15625, {9: 9375, 14: 9375}),
        (4771, 15625, {9: 6250, 14: 12500}),
    ):
        c = low_coefficients(k)
        assert {j: c[j] % modulus for j in expected} == expected, (k, modulus)
    # Modulus-specific linear increment check, for all five residue classes:
    for i in range(5):
        c = low_coefficients(21 + 125 * i)
        assert c[9] % 625 == 125 * ((3 - i) % 5)
        c = low_coefficients(396 + 625 * i)
        assert c[9] % 3125 == 625 * ((2 - i) % 5)
        c = low_coefficients(1646 + 3125 * i)
        assert c[9] % 15625 == 3125 * ((3 - i) % 5)
        assert c[14] % 15625 == 3125 * ((3 + i) % 5)
    print('FIVE_CORE_SHARP_5ADIC_CERTIFICATE_OK', 1479, 6, 15)


if __name__ == '__main__':
    test()
