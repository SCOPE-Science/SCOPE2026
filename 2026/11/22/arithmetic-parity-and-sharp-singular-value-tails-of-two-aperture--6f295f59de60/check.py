"""Finite corroboration for the two-aperture periodic convolution theorem.

Requires only the Python standard library. This does not certify any limit.
"""
import cmath
import math
from fractions import Fraction

PI = math.pi


def scaled_multiplier(n, a, b):
    return (2.0 / PI) * abs(math.sin(PI * n * a) * math.cos(PI * n * b))


def direct_multiplier(n, a, b):
    integral = (1.0 - cmath.exp(-2j * PI * n * a)) / (2j * PI * n)
    return abs(integral * (1 + cmath.exp(-2j * PI * n * b)))


def rational_constant(q):
    if q % 2 == 0:
        return 8.0 / (PI * PI * q) / math.tan(PI / (2 * q))
    return 8.0 / (PI * PI * q) / math.sin(PI / (2 * q))


def direct_threshold_coefficient(t, a, b):
    # Every positive frequency satisfying the threshold lies below this bound.
    bound = math.floor(2 / (PI * t)) + 2
    return 2 * t * sum(scaled_multiplier(n, a, b) > t * n
                       for n in range(1, bound + 1))


def check():
    count = 0
    a = math.sqrt(2) / 10
    pairs = [0.5, 1 / 3, 1 / 4, 1 / 5, 2 * a, math.sqrt(3) / 5]
    for b in pairs:
        assert a < b < 1 - a
        for n in range(1, 151):
            direct = direct_multiplier(n, a, b)
            symbolic = scaled_multiplier(n, a, b) / n
            assert abs(direct - symbolic) < 3e-13
            count += 1

    for q in range(2, 200):
        total = sum(abs(math.cos(PI * r / q)) for r in range(q)) / q
        assert abs(8 * total / PI**2 - rational_constant(q)) < 5e-13
        count += 1
        for p in range(1, q):
            if math.gcd(p, q) != 1:
                continue
            permutation_total = sum(abs(math.cos(PI * r * p / q)) for r in range(q)) / q
            assert abs(total - permutation_total) < 3e-13
            count += 1

    for q in range(2, 20):
        p = next(p for p in range(1, q) if math.gcd(p, q) == 1)
        for n in range(1, 250):
            cos_zero = abs(math.cos(PI * n * p / q)) < 1e-11
            assert cos_zero == (q % 2 == 0 and n % q == q // 2)
            count += 1

    generic = 16 / PI**3
    dependent = (16 * math.sqrt(2) - 8) / (3 * PI**2)
    assert rational_constant(2) < dependent < generic < rational_constant(3)
    for q in range(2, 400):
        c = rational_constant(q)
        assert rational_constant(2) - 1e-12 <= c <= rational_constant(3) + 1e-12
        if q % 2 == 0:
            assert c < generic
        else:
            assert c > generic
        count += 1

    for b, expected in [(0.5, rational_constant(2)),
                        (1/3, rational_constant(3)),
                        (1/4, rational_constant(4)),
                        (1/5, rational_constant(5)),
                        (2*a, dependent),
                        (math.sqrt(3)/5, generic)]:
        k = 300000
        mean_coefficient = 2 * sum(scaled_multiplier(n, a, b)
                                   for n in range(1, k + 1)) / k
        assert abs(mean_coefficient - expected) < 0.0015, (b,mean_coefficient,expected)
        count += 1
        for t in [0.00006, 0.00003, 0.000015]:
            got = direct_threshold_coefficient(t, a, b)
            assert abs(got - expected) < 0.006, (b,t,got,expected)
            count += 1

    print('PASS:', count, 'independent finite checks; no infinite limit inferred')
    print('rational q=2:', format(rational_constant(2), '.12f'))
    print('rational q=3:', format(rational_constant(3), '.12f'))
    print('rationally dependent b=2a:', format(dependent, '.12f'))
    print('independent:', format(generic, '.12f'))


if __name__ == '__main__':
    check()
