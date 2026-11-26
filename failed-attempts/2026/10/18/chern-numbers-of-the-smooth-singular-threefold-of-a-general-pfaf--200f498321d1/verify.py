#!/usr/bin/env python3
"""Exact torus-fixed-point integration for projective skew-rank degeneracy loci.

Uses rational arithmetic only.  The optional dimension-eight calculation is a
cross-check against the classical degree-84, genus-169 Pfaffian quartic curve.
"""
from fractions import Fraction
from itertools import combinations


def cnumber_integrals(n, base):
    assert n in (8, 10) and base >= 2
    w = [base ** i for i in range(n)]
    grdim = 4 * (n - 4)
    rk = (n - 4) * (n - 5) // 2
    ambient_dim = grdim + rk - 1
    cuts = n * (n - 1) // 2 - n
    dim_s = ambient_dim - cuts
    totals = [Fraction(0) for _ in range(dim_s + 1)]
    fixed_points = 0
    for I in combinations(range(n), 4):
        J = tuple(j for j in range(n) if j not in I)
        grass_weights = [w[j] - w[i] for i in I for j in J]
        pair_set = list(combinations(J, 2))
        for R in pair_set:
            h = sum(w[j] for j in R)
            vertical = [h - sum(w[j] for j in P) for P in pair_set if P != R]
            tangent_weights = grass_weights + vertical
            assert len(tangent_weights) == ambient_dim
            assert all(tangent_weights)
            denominator = 1
            for x in tangent_weights:
                denominator *= x
            # c(T_projective_bundle)/(1+h)^cuts, truncated to degree dim_s.
            c = [1] + [0] * dim_s
            for x in tangent_weights:
                for k in range(dim_s, 0, -1):
                    c[k] += x * c[k-1]
            for _ in range(cuts):
                for k in range(1, dim_s + 1):
                    c[k] -= h * c[k-1]
            for k in range(dim_s + 1):
                totals[k] += Fraction(h ** (ambient_dim - k) * c[k], denominator)
            fixed_points += 1
    return fixed_points, totals


def main():
    expected8 = [Fraction(84), Fraction(-336)]
    expected10 = [Fraction(330), Fraction(-1650), Fraction(7920), Fraction(-31350)]
    for base in (2, 3):
        n8, a8 = cnumber_integrals(8, base)
        n10, a10 = cnumber_integrals(10, base)
        assert n8 == 70 * 6 == 420
        assert n10 == 210 * 15 == 3150
        assert a8 == expected8, (base, a8)
        assert a10 == expected10, (base, a10)
        assert 1 - a8[1] // 2 == 169
        assert a10[1] == -5 * a10[0]
        assert (-5 * a10[2]) // 24 == -1650
        assert 125 * a10[0] == 41250
    print('VERIFY_OK n10_fixed_points=3150 degree=330 c1H2=-1650 c2H=7920 c3=-31350 K3=41250 chiO=-1650')


if __name__ == '__main__':
    main()
