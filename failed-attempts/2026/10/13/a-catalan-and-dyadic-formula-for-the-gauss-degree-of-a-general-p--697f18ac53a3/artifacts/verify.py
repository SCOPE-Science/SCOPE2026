from fractions import Fraction
from math import comb

def catalan(n):
    return comb(2*n, n) // (n + 1)

def D_product(g):
    out = Fraction(1, 1)
    for j in range(0, g - 3):
        out *= Fraction(
            comb(g + j, g - 3 - j),
            comb(2*g - 7 - 2*j, g - 3 - j)
        )
    assert out.denominator == 1
    return out.numerator

def v2(n):
    out = 0
    while n and n % 2 == 0:
        out += 1
        n //= 2
    return out

def is_power_two(n):
    return n > 0 and (n & (n - 1)) == 0

checks = 0
for g in range(3, 301):
    d1 = D_product(g)
    d2 = (2 ** (g - 3)) * catalan(g - 2)
    assert d1 == d2, (g, d1, d2)

    gauss_from_source = d1 + 2 ** (g - 3)
    gauss_closed = (2 ** (g - 3)) * (catalan(g - 2) + 1)
    assert gauss_from_source == gauss_closed

    predicted = g - 3 + (1 if is_power_two(g - 1) else 0)
    assert v2(gauss_closed) == predicted, (g, gauss_closed, v2(gauss_closed), predicted)

    if is_power_two(g - 1):
        assert catalan(g - 2) % 4 == 1

    checks += 1

# Independent recurrence replay.
for g in range(3, 200):
    lhs = Fraction(D_product(g + 1), D_product(g))
    rhs = Fraction(4 * (2*g - 3), g)
    assert lhs == rhs, (g, lhs, rhs)

print("VERIFY_OK", checks)
