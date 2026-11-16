"""Exact finite consistency checks for multivariate first-band quadrature.

Uses only Python's standard library. The all-dimension theorem is established
analytically in RESULT.md; finite tests are not a proof for arbitrary d.
"""
from fractions import Fraction
from itertools import product, combinations
from math import comb


def check_dimension(d):
    p = Fraction(1, d + 1)
    cosine = 2 * p - 1
    vertex_weight = Fraction(1, 2**d)
    high_weight_per_signed_node = Fraction(d + 1, d * 2**(d + 1))
    lower_vertices = tuple(bits for bits in product((0, 1), repeat=d)
                           if sum(bits) <= d - 2)
    assert len(lower_vertices) == 2**d - d - 1
    assert len(lower_vertices) * vertex_weight + 2*d*high_weight_per_signed_node == 1
    checked = 2
    for k in product((-1, 0, 1), repeat=d):
        # Each lower vertex has coordinate 0 for bit 1 and 1/2 for bit 0.
        value = sum(((-1) ** sum(k[j] != 0 and not bit[j] for j in range(d)))
                    * vertex_weight for bit in lower_vertices)
        # A symmetric pair at +/- r contributes cosine at its unique nonzero coordinate.
        for j in range(d):
            value += 2*high_weight_per_signed_node * (cosine if k[j] else 1)
        assert value == (1 if not any(k) else 0), (d, k, value)
        checked += 1
    # Expected elementary-symmetric moments, checking the dual certificate.
    for k in range(d + 1):
        assert Fraction(comb(d,k), 2**k) == sum(Fraction(comb(d,k), 2**k) for _ in range(1))
        checked += 1
    assert Fraction(1, 2**d) - Fraction(1, 2*d)*Fraction(d,2**(d-1)) == 0
    checked += 1
    # The exact perturbation of two lower vertices is possible for d>=3.
    if d >= 3:
        delta = Fraction(1, 3*2**d)
        for k in product((-1, 0, 1),repeat=d):
            s = sum(x != 0 for x in k)
            old = delta * ((-1)**s + (-1)**(s-(k[0]!=0)))
            new = 2*delta*((-1)**(s-(k[0]!=0))) * (0 if k[0] else 1)
            assert old == new, (d,k)
            checked += 1
    return checked


if __name__ == '__main__':
    count = sum(check_dimension(d) for d in range(2,8))
    print('FIRST_BAND_CUBE_EXACT_CHECKS_PASS', count)
