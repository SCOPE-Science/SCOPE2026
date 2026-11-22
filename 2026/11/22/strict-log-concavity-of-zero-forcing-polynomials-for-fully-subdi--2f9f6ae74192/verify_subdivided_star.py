"""Reproduce the zero-forcing census for once-subdivided stars.

Run: python3 verify_subdivided_star.py (Python 3 standard library only).
The exact all-order proof is mathematical; finite tests are corroboration.
"""
from collections import Counter
from math import comb


def poly_product(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            result[i + j] += u * v
    return result


def expected(m):
    # Q_m(z) = (1+z)(2+z)^(m-1)(m+2z+z^2) - m - z.
    coef = [1]
    for factor in [[1, 1]] + [[2, 1]] * (m - 1) + [[m, 2, 1]]:
        coef = poly_product(coef, factor)
    coef[0] -= m
    coef[1] -= 1
    return [0] * (m - 1) + coef


def forcing(m, mask):
    n = 2 * m + 1
    adj = [0] * n
    for i in range(m):
        a, b = 2 * i + 1, 2 * i + 2
        adj[0] |= 1 << a
        adj[a] |= (1 << 0) | (1 << b)
        adj[b] |= 1 << a
    all_blue = (1 << n) - 1
    while True:
        if mask == all_blue:
            return True
        moves = 0
        for vertex in range(n):
            if (mask >> vertex) & 1:
                white_neighbors = adj[vertex] & ~mask
                if white_neighbors and white_neighbors & (white_neighbors - 1) == 0:
                    moves |= white_neighbors
        if not moves:
            return False
        mask |= moves


def census(m):
    return [sum(forcing(m, state) for state in range(1 << (2 * m + 1))
                if state.bit_count() == k) for k in range(2 * m + 2)]


def f(j, L):
    return L * (L - 1) + 4 * j


def exact_shape(m):
    # Check explicit closed coefficients using integer fractions, no numerical tolerance.
    from fractions import Fraction
    p = poly_product([1, 1], [m, 2, 1])
    for _ in range(m - 1):
        p = poly_product(p, [2, 1])
    assert len(p) == m + 3
    for j, pj in enumerate(p):
        L = m + 2 - j
        formula = (Fraction(m, (m + 2) * (m + 1) * m)
                   * Fraction(2) ** (m - 1 - j) * comb(m + 2, j)
                   * (m + j) * f(j, L))
        assert pj == formula, (m, j, pj, formula)
    q = p[:]
    q[0] -= m
    q[1] -= 1
    assert min(q) > 0
    assert all(q[j] * q[j] > q[j-1] * q[j+1]
               for j in range(1, len(q) - 1))


def symbolic_identity_check():
    # The two-variable defect identity is tested as a polynomial by finite differences.
    from math import factorial
    def expression(x, y):
        j, L = x + 1, y + 1
        return ((j + 1) * (L + 1) * f(j, L) ** 2
                - j * L * f(j - 1, L + 1) * f(j + 1, L - 1))
    def proposed(x, y):
        return (16 * x**3 + 8 * x**2 * y**2 + 16 * x**2 * y + 72 * x**2
                + x * y**4 + 12 * x * y**3 + 29 * x * y**2
                + 42 * x * y + 104 * x + y**5 + 5 * y**4
                + 17 * y**3 + 23 * y**2 + 26 * y + 48)
    for x in range(4):
        for y in range(6):
            assert expression(x, y) == proposed(x, y)
    # Both sides have bidegrees at most (3,5); polynomial interpolation makes
    # the 4x6 rational-grid equality an algebraic identity, not an extrapolation.
    print("BIVARIATE_POSITIVE_DEFECT_IDENTITY_PASS")


if __name__ == '__main__':
    symbolic_identity_check()
    tested = 0
    for m in range(2, 8):
        actual = census(m)
        model = expected(m)
        assert actual == model, (m, actual, model)
        print(f"INDEPENDENT_FORCING_SUBSET_CENSUS_PASS m={m} subsets={1 << (2*m+1)}")
        tested += 1 << (2 * m + 1)
    for m in range(2, 201):
        exact_shape(m)
    print(f"EXACT_COEFFICIENT_STRICT_LOG_CONCAVITY_PASS m=2..200; census_subsets={tested}")
    print('VERIFY_OK')
