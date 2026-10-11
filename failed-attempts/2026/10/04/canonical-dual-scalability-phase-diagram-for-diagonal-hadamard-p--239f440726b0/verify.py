from fractions import Fraction as F


def two_level(u, v):
    a2 = F(1) - u * v
    b2 = F(2) + u + v
    assert a2 + b2 * u == (F(1) + u) ** 2
    assert a2 + b2 * v == (F(1) + v) ** 2
    return a2, b2


for u, v in [(F(1, 4), F(1)), (F(1, 4), F(4)), (F(1, 9), F(9))]:
    a2, b2 = two_level(u, v)
    assert (a2 >= 0) == (u * v <= 1)

u, v, w = F(1), F(4), F(9)
b = ((1 + v) ** 2 - (1 + u) ** 2) / (v - u)
a = (1 + u) ** 2 - b * u
assert a + b * w - (1 + w) ** 2 == -40

print("VERIFY_OK")
