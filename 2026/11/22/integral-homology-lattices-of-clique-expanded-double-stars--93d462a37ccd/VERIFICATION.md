---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducibility

The attached `check_double_star.py` reconstructs every independent face of seven complete uniform-fiber double-star expansions, forms all augmented simplicial boundary columns and computes ranks over \(\mathbb F_2\) and \(\mathbb F_{101}\). It also calculates signed simplicial Lefschetz numbers for hub-color and leaf-color swaps, leaf-position transpositions, and hub exchange where the sides are balanced. The attached `check_weighted.py` tests three nonuniform fiber-size assignments using the same full boundary procedure. Both were run from the same directory with Python 3, and stdout is stored in `CHECKS.txt`.

The finite tests are **not** an infinite proof, an integer Smith-normal-form certificate, or an independent audit. The all-parameter integral proof uses the exact three-piece subcomplex cover, nullhomotopic inclusions, join Künneth formula, and canonical integral relative chains. In particular, the hub-color permutation lattice is computed integrally, not inferred from a rational character. A nonequivariant wedge splitting is never used to claim an equivariant homotopy equivalence.
