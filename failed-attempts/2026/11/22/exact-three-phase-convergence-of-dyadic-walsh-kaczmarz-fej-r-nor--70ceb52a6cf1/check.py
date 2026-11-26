"""Exact checks for the three-phase dyadic Walsh--Kaczmarz Fejer law.

All arithmetic is integer or Fraction. The independent fast Walsh transform
computes the L1 norms without using the closed formula under test.
"""
from fractions import Fraction


def reverse_bits(number, bits):
    result = 0
    for j in range(bits):
        result = 2 * result + ((number >> j) & 1)
    return result


def norm_from_transform(n):
    N = 1 << n
    coeff = [0] * N
    for k in range(N):
        if k == 0:
            index = 0
        else:
            m = k.bit_length() - 1
            index = (1 << m) | reverse_bits(k - (1 << m), m)
        coeff[index] = N - k
    stride = 1
    while stride < N:
        for base in range(0, N, 2 * stride):
            for j in range(stride):
                u, v = coeff[base + j], coeff[base + stride + j]
                coeff[base + j] = u + v
                coeff[base + stride + j] = u - v
        stride *= 2
    return Fraction(sum(abs(v) for v in coeff), N * N), coeff


def phase_deficit(n):
    m, r = divmod(n, 3)
    if r == 0:
        return (Fraction(5, 2) / 4**m - Fraction(7, 2) / 8**m
                + Fraction(4, 3) / 16**m)
    if r == 1:
        return (Fraction(19, 12) / 4**m - Fraction(7, 4) / 8**m
                + Fraction(1, 2) / 16**m)
    return (Fraction(1) / 4**m - Fraction(7, 8) / 8**m
            + Fraction(5, 24) / 16**m)


def first_two_value(a, b):
    # Returns 3 * (N K_N(x)) when the first two one-bits are a < b.
    return 3 * 4**a - 2**a * (2 * 4**(b-a-1) + 1)


def norm_from_sign_count(n):
    N = 1 << n
    neg = 0
    for b in range(1, n):
        for a in range(b):
            v3 = first_two_value(a, b)
            if v3 < 0:
                assert v3 % 3 == 0
                neg += (1 << (n-b-1)) * (-v3 // 3)
    return 1 + Fraction(2 * neg, N*N)


def run():
    count = 0
    for n in range(1, 13):
        direct, values = norm_from_transform(n)
        predicted = Fraction(4, 3) - phase_deficit(n)
        counted = norm_from_sign_count(n)
        assert direct == predicted == counted, (n, direct, predicted, counted)
        assert sum(values) == (1 << (2*n)), n
        count += 3
    for b in range(1, 85):
        for a in range(b):
            assert (first_two_value(a, b) < 0) == (3*a <= 2*b-3), (a, b)
            count += 1
    for n in range(1, 61):
        assert phase_deficit(n) > 0
        assert Fraction(4,3)-phase_deficit(n) <= Fraction(4,3)
        assert norm_from_sign_count(n) == Fraction(4,3)-phase_deficit(n)
        count += 3
    print('PASSED:', count, 'exact assertions; direct Walsh transforms n=1..12;')
    print('finite sign counts n=1..60; exact sign threshold b=1..84.')


if __name__ == '__main__':
    run()
