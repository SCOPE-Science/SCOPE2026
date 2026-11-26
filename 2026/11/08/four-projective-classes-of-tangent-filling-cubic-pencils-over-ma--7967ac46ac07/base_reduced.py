"""Exact affine-chart Jacobian test for the four plane-cubic pencils.

Run with Python 3 and SymPy. Decode the normalized generator codes in the
displayed monomial order, reading base-three digits least significant first.
"""

from itertools import combinations
from sympy import diff, expand, groebner, symbols


def main():
    x, y, z = variables = symbols('x y z')
    monomials = (x**3, y**3, z**3, x*x*y, x*x*z, x*y*y,
                 y*y*z, x*z*z, y*z*z, x*y*z)

    def decode(code):
        return sum((code // (3**i) % 3) * term
                   for i, term in enumerate(monomials))

    for pair in ((345, 3753), (345, 3757), (345, 6649), (346, 3756)):
        f, g = map(decode, pair)
        minors = [diff(f, u)*diff(g, v) - diff(f, v)*diff(g, u)
                  for u, v in combinations(variables, 2)]
        for fixed in variables:
            remaining = [v for v in variables if v != fixed]
            polynomials = [expand(p.subs(fixed, 1)) for p in (f, g, *minors)]
            basis = groebner(polynomials, *remaining, modulus=3)
            if [p.as_expr() for p in basis.polys] != [1]:
                raise AssertionError(f'Nonunit Jacobian-minor ideal: {pair}, {fixed}=1')
        print(f'{pair}: all three Jacobian-minor ideals are the unit ideal')


if __name__ == '__main__':
    main()
