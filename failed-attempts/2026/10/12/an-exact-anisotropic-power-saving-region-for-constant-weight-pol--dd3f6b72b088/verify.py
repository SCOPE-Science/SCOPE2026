from fractions import Fraction


def zeta_from_reduced(k, a, b, c, r):
    M = max(k * a + b + c, 2 * b + 2 * c)
    S = b + min(a, b) + 2 * c
    return (S - (Fraction(1, 2) + Fraction(1, 2 * r))
            - max(M - 1 - Fraction(1, 2 * r), Fraction(0))) / (2 * r)


def exponent_of_delta1(k, a, b, c, r):
    return (-(a + b) / (2 * r) - c / r
            + Fraction(r + 1, 4 * r * r)
            + max(a - b, Fraction(0)) / (2 * r)
            + max(max(k * a, b + c) + b + c
                  - (1 + Fraction(1, 2 * r)), Fraction(0)) / (2 * r))


algebra_cases = 0
for k in range(2, 8):
    values = [Fraction(i, 20) for i in range(1, 10)]
    for a in values:
        if k * a >= 1:
            continue
        for b in values:
            for c in values:
                if b + c >= 1:
                    continue
                for r in (2, 3, 5, 11, 37):
                    assert exponent_of_delta1(k, a, b, c, r) == -zeta_from_reduced(k, a, b, c, r)
                    algebra_cases += 1

diagonal_cases = 0
for k in range(2, 8):
    for i in range(1, 100):
        eta = Fraction(i, 500)
        if k * eta >= 1 or 2 * eta >= 1:
            continue
        M = max((k + 2) * eta, 4 * eta)
        S = 4 * eta
        reduced = S > Fraction(1, 2) + max(M - 1, Fraction(0))
        published = eta > Fraction(1, 8) and (k == 2 or eta < Fraction(1, 2 * (k - 2)))
        assert reduced == published
        diagonal_cases += 1

k = 2
a, b, c = Fraction(1, 20), Fraction(1, 5), Fraction(1, 5)
M = max(k * a + b + c, 2 * b + 2 * c)
S = b + min(a, b) + 2 * c
assert M == Fraction(4, 5)
assert S == Fraction(13, 20)
assert S > Fraction(1, 2) + max(M - 1, Fraction(0))
assert zeta_from_reduced(k, a, b, c, 4) == Fraction(1, 320)

print(f"VERIFY_OK algebra_cases={algebra_cases} diagonal_cases={diagonal_cases} anisotropic_example=1")
