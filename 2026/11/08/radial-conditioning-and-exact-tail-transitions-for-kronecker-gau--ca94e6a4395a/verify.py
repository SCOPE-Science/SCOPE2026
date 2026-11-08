"""Reproduce exact finite-dimensional moment and tail-constant checks.

Only the Python standard library is required. The analytic theorem is proved
in RESULT.md; these independent finite algebra checks are not a tail proof.
"""
from fractions import Fraction as Q
from itertools import product
from math import prod


def four(a, b, c, d):
    return int(a == b and c == d) + int(a == c and b == d) + int(a == d and b == c)


def check_moments(matrix, dimensions, sphere_mask):
    """Expand E[(x^T H x)^2] by independent fourth-order coordinate moments."""
    labels = list(product(*(range(v) for v in dimensions)))
    n = len(labels)
    total = Q(0)
    for i, ix in enumerate(labels):
        for j, jx in enumerate(labels):
            for k, kx in enumerate(labels):
                for ell, lx in enumerate(labels):
                    f = Q(1)
                    for p, dim in enumerate(dimensions):
                        f *= four(ix[p], jx[p], kx[p], lx[p])
                        if p in sphere_mask:
                            f *= Q(dim, dim + 2)
                        if f == 0:
                            break
                    if f:
                        total += matrix[i][j] * matrix[k][ell] * f
    return total


def outer(vec):
    return [[x*y for y in vec] for x in vec]


def identity(n):
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def check():
    checks = 0
    identity_4 = identity(4)
    bell = outer([Q(1, 1), Q(0), Q(0), Q(1, 1)])
    bell = [[x / 2 for x in row] for row in bell]
    for H, expected in [
        (identity_4, [Q(64), Q(32), Q(32), Q(16)]),
        (bell, [Q(6), Q(3), Q(3), Q(3, 2)]),
    ]:
        got = [check_moments(H, [2, 2], mask) for mask in [set(), {0}, {1}, {0, 1}]]
        assert got == expected, (got, expected)
        checks += 4
    cases = [
        (outer([Q(1), Q(2), Q(3), Q(4)]), [2, 2]),
        (outer([Q(-1), Q(0), Q(4), Q(3)]), [2, 2]),
        (identity(8), [2, 2, 2]),
        (outer([Q(i) for i in range(1, 9)]), [2, 2, 2]),
        (outer([Q(i*(-1)**i) for i in range(1, 9)]), [2, 2, 2]),
        (identity(6), [2, 3]),
        (outer([Q(1), Q(-2), Q(3), Q(-4), Q(5), Q(-6)]), [2, 3]),
    ]
    for H, dims in cases:
        base = check_moments(H, dims, set())
        for bits in product([False, True], repeat=len(dims)):
            mask = {i for i, b in enumerate(bits) if b}
            prediction = base * prod([Q(dims[i], dims[i] + 2) for i in mask], start=Q(1))
            assert check_moments(H, dims, mask) == prediction
            checks += 1
    # The identity example has maximally separated tail exponents.
    # The exact coefficients are r/2*(k/(c_J*rho))^(1/r) with k=1, rho=1.
    assert Q(1) == Q(2, 2)  # two Gaussian factors: power 1/2 coefficient 1
    assert Q(1, 4) == Q(1, 2*2)  # one Gaussian factor: power 1 coefficient 1/4
    checks += 2
    # In the Bell-state example the product numerical radius is 1/2,
    # not the full spectral norm 1; angular optimization matters.
    rho_bell = Q(1, 2)
    assert rho_bell < Q(1) and Q(4) * rho_bell == Q(2)
    checks += 2
    print(f"PASS: {checks} exact-rational checks; all matched.")


if __name__ == '__main__':
    check()
