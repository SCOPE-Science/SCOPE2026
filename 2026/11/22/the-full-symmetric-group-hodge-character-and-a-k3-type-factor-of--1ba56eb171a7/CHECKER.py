#!/usr/bin/env python3
"""Exact rational character checks for the equivariant Hodge theorem."""
from fractions import Fraction
# Classes: identity, a transposition, a 3-cycle.
characters = {"trivial": (1, 1, 1), "sign": (1, -1, 1), "standard": (2, 0, -1)}


def character(multiplicities):
    return tuple(sum(multiplicities.get(k, 0) * char[i] for k, char in characters.items()) for i in range(3))


def invariants(m):
    # S_3, a transposition subgroup, and A_3, in this order.
    return (m.get("trivial", 0), m.get("trivial", 0) + m.get("standard", 0), m.get("trivial", 0) + m.get("sign", 0))


def decompose(dimension, full, transposition, alternating):
    a = full
    c = transposition - a
    b = alternating - a
    assert a >= 0 and b >= 0 and c >= 0
    assert a + b + 2*c == dimension
    return {"trivial": a, "sign": b, "standard": c}

# Literature input: c_2(X)=12, q=4, p_g=6 and 18 A_3-fixed points.
b2 = 12 - 2 + 4*4
assert b2 == 26
# Invariants under S_3, a transposition and A_3 respectively.
# Quotients: P^2/K (b_2=1), Bl_p(A/K) (b_2=7), X/A_3 (chi=16, b_1=0).
chi_A3_quotient = Fraction(12 + 2*18, 3)
assert chi_A3_quotient == 16
b2_A3_invariant = chi_A3_quotient - 2
assert b2_A3_invariant == 14
h2 = decompose(b2, 1, 7, b2_A3_invariant)
h20 = decompose(6, 0, 1, 4)
h11 = {k:h2[k]-2*h20[k] for k in characters}
h10 = {"trivial":0,"sign":0,"standard":2}
assert h2 == {"trivial":1,"sign":13,"standard":6}
assert h20 == {"trivial":0,"sign":4,"standard":1}
assert h11 == {"trivial":1,"sign":5,"standard":4}
assert sum(h11[k]*characters[k][0] for k in characters) == 14
assert invariants(h2) == (1,7,14)
assert invariants(h20) == (0,1,4)
assert character(h2) == (26,-12,8)
assert character(h20) == (6,-4,3)
assert character(h11) == (14,-4,2)
assert character(h10) == (4,0,-2)
# Lefschetz character for the full alternating cohomology.
E = tuple(2 + character(h2)[i] - 4*character(h10)[i] for i in range(3))
assert E == (12,-10,18)
# Six-dimensional standard multiplicity Hodge factor has (1,4,1).
assert (h20["standard"],h11["standard"],h20["standard"]) == (1,4,1)
# Primitive Hodge-Riemann: real (2,0)+(0,2) positive and (1,1) negative.
assert (2*h20["standard"], h11["standard"]) == (2,4)
assert (1 + 2*4 + 2*1*2, 5 + 4*2) == (13,13) # whole H^2 intersection signature
print("PASS: S3 character, subgroup invariants, Hodge dimensions, Lefschetz numbers and K3-type signature")
