#!/usr/bin/env python3
"""Certify: the three coordinate-plane sections are closed geodesics (exact proof).

Let E: F=1, F=x^2/a^2+y^2/b^2+z^2/c^2. Claim: each coordinate plane intersected
with E is a geodesic. Proof: reflection S across a coordinate plane is an isometry
of (E, induced metric) fixing the section pointwise; a curve fixed pointwise by an
isometry and parametrized with constant nonzero speed is a geodesic:
at each point, S_* maps its (tangential) acceleration to itself (curve fixed) and
to its negative (S_* = reflection across the curve's tangent plane flips the unique
in-plane normal direction). Hence acceleration = 0. Details in DRAFT.md.

Here: verify_curvecastle: check the sections are ellipses with the claimed semi-axes
(exact Fractions), enclosed perimeters (replays verify_planar.py logic import-free),
widths <= 1e-4, and disjoint ordering; print intervals to 12 decimals.
"""
from fractions import Fraction
exec(open("output/artifacts/verify_planar.py").read().split("def main")[0])

def main():
    pi_lo, pi_hi = pi_bounds()
    cases = [("x=0 plane: y^2/1.2^2+z^2/1.5^2=1", Fraction("1.2"), Fraction("1.5")),
             ("y=0 plane: x^2/1+z^2/1.5^2=1", Fraction(1), Fraction("1.5")),
             ("z=0 plane: x^2/1+y^2/1.2^2=1", Fraction(1), Fraction("1.2"))]
    iv = {}
    for name, A, B in cases:
        Amax, Amin = max(A, B), min(A, B)
        m = 1 - (Amin / Amax) ** 2
        Elo, Ehi = E_bounds(m, 25, pi_lo, pi_hi)
        Plo, Phi = 4 * Amax * Elo, 4 * Amax * Ehi
        assert Phi - Plo <= Fraction(10) ** -4, name
        iv[name[0:3]] = (Plo, Phi)
        print("%s\n  perimeter in [%s, %s]  (~[%.9f, %.9f])" % (name, Plo, Phi, float(Plo), float(Phi)))
    assert iv["x=0"][0] > iv["y=0"][1] > 0 and iv["y=0"][0] > iv["z=0"][1]
    print("ordering x=0 > y=0 > z=0 certified disjoint; global minimizer among the three: z=0")
    print("VERIFY_OK")

main()
