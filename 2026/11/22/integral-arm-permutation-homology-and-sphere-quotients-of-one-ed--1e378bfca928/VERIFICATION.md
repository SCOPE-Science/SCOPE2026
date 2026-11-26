---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

At inclusive vertex scale two, the only cross-arm interior edges join two first-depth vertices or two last-depth vertices, since a two-step path must pass through their common neighboring pole. The two resulting full simplices meet in the pole edge, and the remaining faces are on the individual six-cycles. Each six-cycle has precisely three excluded opposite pairs and hence is an octahedral sphere. The union of the two full simplices and its intersection with each local sphere contract linearly to the pole-edge midpoint, compatibly with all symmetries. Collapsing this contractible subcomplex gives the wedge and its integral fundamental-class basis. Reversal acts by three coordinate sign flips and a transposition of the first and third axes, with determinant +1 and eigenvalues (1,-1,-1); it is a half-turn, not a reflection. For arbitrary H, subdivide to remove inversions before collapsing the contractible image of the common subcomplex in the actual orbit space. Each arm orbit leaves the quotient of one local sphere by its stabilizer, with the image of the contractible attaching subset collapsed. That stabilizer acts either trivially or by the half-turn, whose sphere quotient is a sphere (double the angular coordinate around its rotation axis). The argument uses stabilizers, not a product assumption on H, so also covers subgroups in which reversal is coupled to an arm permutation. The poles are the only vertices of degree greater than two, including h=2, giving exactly the stated automorphism group.

## originality

PASS

The absolute wedge type is an acknowledged consequence of prior Rips gluing. The supported distinct claim is the unsigned integral action including pole reversal and the homotopy classification of all genuine subgroup quotients in the one-edge Rips book. The strongest comparisons in the local index concern a two-edge Rips book (different orientation and quotient) and a directed multipath complex (different faces and acting group). Neither gives this classification.

## value

PASS

The theorem isolates a sharp symmetry distinction between overlapping six-cycle books of the same scale and absolute homotopy type. A single spine edge gives a rotation quotient rather than the collapse seen for two spine edges. The all-subgroup statement computes genuine homotopy types, including groups coupling pole reversal to arm permutations, not just ranks or rational character averages.

The dated certificate retains the supplied scientific assessment, sources and limitations.
