"""Exact-rational diagnostics for Kalman-graded skew-chain Schatten coefficients.

Run with Python 3; uses only the Python standard library. The general
operator-theoretic theorem is proved analytically and is not certified by
these finite diagnostics.
"""
from fractions import Fraction
from math import factorial


def det_exact(M):
    A = [[Fraction(x) for x in row] for row in M]
    n = len(A)
    result = Fraction(1)
    for k in range(n):
        pivot = next((i for i in range(k, n) if A[i][k]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            A[k], A[pivot] = A[pivot], A[k]
            result = -result
        a = A[k][k]
        result *= a
        for i in range(k + 1, n):
            factor = A[i][k] / a
            for j in range(k + 1, n):
                A[i][j] -= factor * A[k][j]
            A[i][k] = 0
    return result


def gram_chain(m):
    return [[Fraction(2 * ((-1) ** (i + j)),
                       factorial(i) * factorial(j) * (i + j + 1))
             for j in range(m)] for i in range(m)]


def factorial_coefficient(m):
    out = Fraction(1)
    for k in range(m):
        out *= Fraction(factorial(2 * k) * factorial(2 * k + 1),
                        factorial(k) ** 2)
    return out


def run():
    tests = 0
    for m in range(1, 9):
        G = gram_chain(m)
        determinant = det_exact(G)
        assert determinant > 0
        # For p=1, (2/p)^m / det(G) equals the factorial product.
        assert Fraction(2 ** m, 1) / determinant == factorial_coefficient(m)
        tests += 2
    assert det_exact(gram_chain(3)) == Fraction(1, 1080)
    assert factorial_coefficient(3) == 8640
    tests += 2
    print(f'KALMAN_GRADED_EXACT_RATIONAL_OK {tests}')


if __name__ == '__main__':
    run()
