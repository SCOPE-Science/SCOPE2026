#!/usr/bin/env python3
# Exact consistency checks for the signature case split and source-survey transcription.
# These checks corroborate bookkeeping only; the covering-space proof is analytic.

def group_for_signature(p, q):
    assert p >= 1 and q >= 1 and p + q >= 3
    m = p + q
    if min(p, q) == 1:
        return "Z" if m == 3 else "0"
    if p == q == 2:
        return "Z^2"
    if min(p, q) == 2:
        return "Z"
    return "Z/2"

# Symmetry under swapping the positive and negative inertia indices.
for p in range(1, 9):
    for q in range(1, 9):
        if p + q >= 3:
            assert group_for_signature(p, q) == group_for_signature(q, p)

# Survey signatures transcribed from Table 1 of arXiv:2610.05189v1
# for rows marked as admitting a real Clifford-to-icosahedral switch.
survey = {
    13: (2, 1, "Z"),
    17: (1, 2, "Z"),
    19: (2, 2, "Z^2"),
    23: (1, 3, "0"),
    25: (3, 2, "Z"),
    27: (2, 2, "Z^2"),
    29: (2, 3, "Z"),
}
for n, (p, q, expected) in survey.items():
    got = group_for_signature(p, q)
    assert got == expected, (n, p, q, got, expected)

# In the (2,2) case, the quotient of R^2 has lattice generators
# (2*pi,0) and (pi,pi), represented in pi-units below.
# Their determinant is nonzero, so the deck lattice has rank two.
a = (2, 0)
b = (1, 1)
det = a[0] * b[1] - a[1] * b[0]
assert det == 2

print("VERIFY_OK")
