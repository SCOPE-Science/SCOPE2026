"""Exact rational checks for codimension-one widths of a common-axis frame.

This diagnostic confirms the finite-dimensional Gram identities and the
geometric construction of a minimizing normal; it is not a replacement
for the general analytic proof or the complexity reduction.
"""
from fractions import Fraction as F
from itertools import product


def dot(x, y):
    return sum((u * v for u, v in zip(x, y)), F(0))


def case(weights, coupling):
    a = list(map(F, weights))
    d = F(coupling)
    n = len(a)
    c = d * d / (1 + n * d * d)
    gram = [[(F(int(i == j)) + d * d) / (a[i] * a[j])
             for j in range(n)] for i in range(n)]
    inv = [[a[i] * a[j] * (F(int(i == j)) - c)
            for j in range(n)] for i in range(n)]
    check = 0
    for i in range(n):
        for j in range(n):
            assert sum(gram[i][k]*inv[k][j] for k in range(n)) == int(i == j)
            check += 1
    q = sum(x*x for x in a)
    discrepancy = min(abs(sum(e*x for e, x in zip(eps, a)))
                      for eps in product((-1, 1), repeat=n))
    W = q - c * discrepancy * discrepancy
    assert W > 0
    # The vectors are columns (e_i+d*u)/a_i in real Euclidean (n+1)-space.
    b = [[(F(int(k == i)) + (d if k == n else 0)) / a[i]
          for k in range(n+1)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            assert dot(b[i], b[j]) == gram[i][j]
            check += 1
    for eps in product((-1, 1), repeat=n):
        discrepancy_eps = abs(sum(e*x for e,x in zip(eps,a)))
        # All corners lie below the claimed maximum of the inverse quadratic.
        quad = sum(eps[i] * inv[i][j] * eps[j]
                   for i in range(n) for j in range(n))
        assert quad == q - c*discrepancy_eps*discrepancy_eps
        assert quad <= W
        check += 2
        if discrepancy_eps != discrepancy:
            continue
        coeff = [sum(inv[i][j] * eps[j] for j in range(n)) for i in range(n)]
        normal_unnormalized = [sum(coeff[i]*b[i][k] for i in range(n))
                                 for k in range(n+1)]
        assert dot(normal_unnormalized, normal_unnormalized) == W
        check += 1
        for i in range(n):
            assert dot(normal_unnormalized, b[i]) == eps[i]
            check += 1
    return check


def main():
    tests = [(2, [1, 1], F(1)),
             (3, [1, 1, 1], F(1)),
             (4, [1, 2, 3, 4], F(1)),
             (5, [1, 2, 3, 4, 9], F(1,2)),
             (6, [2, 5, 6, 11, 13, 17], F(2)),
             (7, [1, 1, 2, 2, 3, 5, 8], F(1)),
             (8, [1, 2, 2, 3, 4, 8, 13, 21], F(1,3)),
             (9, [1, 2, 3, 5, 8, 13, 21, 34, 55], F(1))]
    total = 0
    for n, weights, coupling in tests:
        total += case(weights, coupling)
        if len(weights) != n:
            raise AssertionError('test dimension')
    print('EQUIANGULAR_TERMINAL_WIDTH_RATIONAL_OK', total)


if __name__ == '__main__':
    main()
