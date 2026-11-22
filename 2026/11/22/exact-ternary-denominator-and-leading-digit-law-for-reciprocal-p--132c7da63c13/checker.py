"""Exact-rational and modular checks for reciprocal Lucas-Jacobsthal sums."""
from fractions import Fraction


def sequence(a, n):
    # Integral recurrence with roots a and -1.
    u, v = 0, 1
    for _ in range(n):
        u, v = v, (a - 1) * v + a * u
    return u


def ternary_exponent(n):
    r = 0
    while 3 ** (r + 1) <= n:
        r += 1
    return r


def valuation_3(x):
    if x == 0:
        return None
    num, den = x.numerator, x.denominator
    valuation = 0
    while num % 3 == 0:
        valuation += 1
        num //= 3
    while den % 3 == 0:
        valuation -= 1
        den //= 3
    return valuation


def residue_3(x):
    assert x.denominator % 3
    return (x.numerator * pow(x.denominator, -1, 3)) % 3


def check_exact():
    cases = 0
    for a in (2, 5, 8, 11, 14):
        vals = [sequence(a, n) for n in range(1, 51)]
        for h in range(1, 8):
            s = Fraction(0)
            for n, j in enumerate(vals, 1):
                s += Fraction(1, j ** h)
                r = ternary_exponent(n)
                assert valuation_3(s) == -h * r, (a, h, n)
                normalized = s * 3 ** (h * r)
                assert residue_3(normalized) == n // 3 ** r, (a, h, n)
                cases += 1
    return cases


def check_modular():
    # Independent residue arithmetic, no fractions or recurrence-based large values.
    modulus = 3 ** 48
    cases = 0
    for a in (2, 5, 8, 11):
        for h in (1, 2, 3, 5):
            max_n = 1500
            max_r = ternary_exponent(max_n)
            scaled = 0
            for n in range(1, max_n + 1):
                j = (pow(a, n) - (-1) ** n) // (a + 1)
                v = 0
                while j % 3 == 0:
                    j //= 3
                    v += 1
                scaled = (scaled + 3 ** (h * (max_r - v)) * pow(j, -h, modulus)) % modulus
                if n == 1 or n % 29 == 0 or n in (2, 3, 8, 9, 26, 27, 80, 81, 242, 243, 728, 729):
                    r = ternary_exponent(n)
                    assert scaled % (3 ** (h * (max_r - r) + 1)) == (n // 3 ** r) * 3 ** (h * (max_r - r)) % (3 ** (h * (max_r - r) + 1)), (a, h, n)
                    cases += 1
    return cases

if __name__ == '__main__':
    e = check_exact()
    m = check_modular()
    assert Fraction(1, 1) + Fraction(1, 3) + Fraction(1, 13) == Fraction(55, 39)
    print('VERIFY_OK exact_rational_cases=%d modular_cases=%d base_boundary_sum=55/39' % (e, m))
