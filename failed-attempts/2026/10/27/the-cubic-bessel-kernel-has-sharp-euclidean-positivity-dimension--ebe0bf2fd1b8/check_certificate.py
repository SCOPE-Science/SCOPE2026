#!/usr/bin/env python3
"""Exact arithmetic certificate for a radial Bessel-cube moment obstruction.

Python 3 standard library only. All computations use integers and Fractions.
"""
from fractions import Fraction
from math import factorial


def three_step_moment(k):
    total = 0
    fk = factorial(k)
    for i in range(k + 1):
        for j in range(k - i + 1):
            h = k - i - j
            multinomial = fk // (factorial(i) * factorial(j) * factorial(h))
            total += multinomial * multinomial
    return total


def candidate_radial_moment(dim, k):
    poch = Fraction(1)
    for i in range(k):
        poch *= Fraction(dim + 2 * i, 2)
    return Fraction(three_step_moment(k), factorial(k)) * poch


def determinant_exact(matrix):
    # Rational Gaussian elimination, avoiding floating point.
    a = [list(map(Fraction, row)) for row in matrix]
    out = Fraction(1)
    n = len(a)
    for k in range(n):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            out = -out
        v = a[k][k]
        out *= v
        for i in range(k + 1, n):
            factor = a[i][k] / v
            for j in range(k + 1, n):
                a[i][j] -= factor * a[k][j]
            a[i][k] = Fraction(0)
    return out


def quadratic_form(coeff, moments):
    return sum(Fraction(ci * cj) * moments[i + j]
               for i, ci in enumerate(coeff) for j, cj in enumerate(coeff))


def main():
    A = [three_step_moment(k) for k in range(13)]
    assert A[:7] == [1, 3, 15, 93, 639, 4653, 35169]
    m3 = [candidate_radial_moment(3, k) for k in range(13)]
    m4 = [candidate_radial_moment(4, k) for k in range(7)]
    assert m3[:7] == [Fraction(1), Fraction(9,2), Fraction(225,8),
                      Fraction(3255,16), Fraction(201285,128),
                      Fraction(3224529,256), Fraction(105612507,1024)]
    assert m4 == [1, 6, 45, 372, 3195, 27918, 246183]

    h3 = [[m3[i + j] for j in range(7)] for i in range(7)]
    d3 = determinant_exact(h3)
    expected_d3 = Fraction(-59778222499952939497463042623250744763,
                           302231454903657293676544)
    assert d3 == expected_d3 < 0

    c3 = [34035104594901162582389214003063,
          -60360260712009095593397404197864,
          38428664823683231149593451588392,
          -11626688676825713700932703259136,
          1809597562222368116915713421568,
          -140012888060094789091172161536,
          4266143229501193191697041408]
    expected_q3 = Fraction(-512439033544299213494397684864863599452333628604779974841761, 2)
    assert quadratic_form(c3, m3) == expected_q3 < 0

    h4 = [[m4[i + j] for j in range(4)] for i in range(4)]
    assert determinant_exact(h4) == -27756
    assert quadratic_form([-1146, 747, -132, 7], m4) == -10794
    print('PASS: three-step moments, exact 7x7 3D determinant, and polynomial witness')
    print('PASS: exact 4x4 4D determinant and short polynomial witness')
    print('det H_3(7) =', d3)
    print('det H_4(4) =', determinant_exact(h4))
    print('quadratic witness 3D =', expected_q3)
    print('quadratic witness 4D = -10794')


if __name__ == '__main__':
    main()
