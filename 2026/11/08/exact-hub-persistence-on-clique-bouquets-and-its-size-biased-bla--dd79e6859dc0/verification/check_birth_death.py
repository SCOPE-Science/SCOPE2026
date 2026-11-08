"""Exact symbolic checks for hub persistence in a bouquet of cliques.

Run: python verification/check_birth_death.py
Dependency: sympy.
"""
from math import exp
from sympy import Matrix, Rational, Symbol, diff, factor, prod, simplify


def block_transform(r, theta):
    """Return exact transform of integrated zeros for one frozen-hub blade."""
    B = Matrix.zeros(r, r)
    for z in range(1, r + 1):
        down = Rational(z * (r - z + 1), r)
        up = Rational(z * (r - z), r)
        B[z - 1, z - 1] = down + up + z * theta
        if z > 1:
            B[z - 1, z - 2] = -down
        if z < r:
            B[z - 1, z] = -up
    source = Matrix.zeros(r, 1)
    source[0, 0] = 1
    result = factor((B.inv() * source)[r - 1])
    product_down = prod(Rational(z * (r - z + 1), r) for z in range(1, r + 1))
    assert simplify(result - product_down / B.det()) == 0
    return result


def main():
    t = Symbol('t')
    expected = {
        1: 1 / (1 + t),
        2: 1 / (1 + 4 * t + 2 * t**2),
        3: 2 / (2 + 18 * t + 27 * t**2 + 9 * t**3),
    }
    for r in range(1, 7):
        f = block_transform(r, t)
        assert simplify(f.subs(t, 0) - 1) == 0
        assert simplify(-diff(f, t).subs(t, 0) - r * r) == 0
        if r in expected:
            assert simplify(f - expected[r]) == 0
        print('blade', r, 'E[integrated zero count]', r*r)
    test_blades = [[1], [2], [3], [1, 2], [2, 2], [1, 3], [3, 3], [1, 1, 2]]
    for sizes in test_blades:
        L = sum(sizes)
        value = prod(block_transform(r, Rational(1, L)) for r in sizes)
        print('sizes', sizes, 'persistence', value)
    for r in range(1, 6):
        k = 100
        p = float(block_transform(r, Rational(1, k*r)) ** k)
        assert abs(p - exp(-r)) < 0.02
        print('fixed blade', r, 'k', k, 'prob', format(p, '.12f'),
              'limit', format(exp(-r), '.12f'))
    print('SYMBOLIC CHECKS PASS')


if __name__ == '__main__':
    main()
