from fractions import Fraction
from math import comb


def bernoulli_numbers(nmax):
    # Exact Bernoulli numbers with B_1=-1/2, matching x/(e^x-1).
    B = [Fraction(0) for _ in range(nmax + 1)]
    B[0] = Fraction(1)
    for n in range(1, nmax + 1):
        s = sum(Fraction(comb(n + 1, k)) * B[k] for k in range(n))
        B[n] = -s / Fraction(n + 1)
    return B


B = bernoulli_numbers(100)


def zeta_neg(n):
    assert n >= 0
    return Fraction((-1) ** n) * B[n + 1] / Fraction(n + 1)


def P(a, c):
    return zeta_neg(a) * zeta_neg(c)


def R(a, c):
    return P(a, c) + Fraction((-1) ** (c + 1), c + 1) * zeta_neg(a + c + 1)


def condition(a, c):
    return a >= 1 and c >= 1 and (a + c) % 2 == 1


for n in range(0, 81):
    expected_zero = n > 0 and n % 2 == 0
    assert (zeta_neg(n) == 0) == expected_zero

checked = 0
for a in range(41):
    for c in range(41):
        detector = (P(a, c) == 0 and R(a, c) == 0)
        assert detector == condition(a, c), (a, c, P(a, c), R(a, c))
        checked += 1

print(f"VERIFY_OK detector_pairs={checked} range_a=0..40 range_c=0..40 zeta_zero_cases=0..80")
