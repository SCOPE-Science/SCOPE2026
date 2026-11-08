"""Exact integer-polynomial certificate of the rational generating identity.

No numerical approximation or symbolic-library dependency.
Run: python verify_identity.py
"""


def trim(p):
    result = list(p)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result)


def add(p, q):
    result = [0] * max(len(p), len(q))
    for i, c in enumerate(p):
        result[i] += c
    for i, c in enumerate(q):
        result[i] += c
    return trim(result)


def mul(p, q):
    result = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            result[i + j] += a * b
    return trim(result)


def scale(p, n):
    return trim(tuple(n * c for c in p))


def power(p, n):
    result = (1,)
    for _ in range(n):
        result = mul(result, p)
    return result


class Rational:
    def __init__(self, numerator, denominator=(1,)):
        self.a, self.b = trim(numerator), trim(denominator)

    def __add__(self, other):
        other = other if isinstance(other, Rational) else Rational((other,))
        return Rational(add(mul(self.a, other.b), mul(other.a, self.b)),
                        mul(self.b, other.b))

    def __mul__(self, other):
        other = other if isinstance(other, Rational) else Rational((other,))
        return Rational(mul(self.a, other.a), mul(self.b, other.b))

    def equals(self, other):
        return mul(self.a, other.b) == mul(other.a, self.b)


z, z2, z3, z4 = (0, 1), (0, 0, 1), (0, 0, 0, 1), (0, 0, 0, 0, 1)
q1, q2, q3, q4 = (1, -1), (1, 0, -1), (1, 0, 0, -1), (1, 0, 0, 0, -1)


def rf(a, b=(1,)):
    return Rational(a, b)


def neg(p):
    return scale(p, -1)


def main():
    # The four support regimes: isolated constant loops, alternating
    # two-cycle, one activated outer vertex, and both outer vertices.
    loops = rf((0, 2), q1)
    alternating = rf(z2, q2)
    one_outer = rf((0, 2), power(q1, 2)) * (
        rf(z2, q2) + rf(neg(z3), q3))
    both_outer = rf(z2, power(q1, 4)) * (
        rf((1,), q2) + rf((-2,), q3) + rf((1,), q4))
    four_cases = loops + alternating + one_outer + both_outer

    target_num = (0, 2, -3, 1, -1, 0, 5, -5, 6, -7, 3)
    target_den = mul(power(q1, 5), mul((1, 1), mul((1, 0, 1), (1, 1, 1))))
    assert four_cases.equals(rf(target_num, target_den))
    print('RATIONAL_IDENTITY_OK exact integer polynomial cross-multiplication')


if __name__ == '__main__':
    main()
