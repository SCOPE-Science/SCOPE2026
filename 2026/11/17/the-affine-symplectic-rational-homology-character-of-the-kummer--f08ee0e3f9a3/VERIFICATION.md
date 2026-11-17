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

The included programs were executed on the exact sixteen-point design. `verify_integral_homology.py` exhaustively collapses the original simplicial complex, constructs the remaining signed integer triangle boundary, and verifies its Smith factors (104 unit factors and one factor 2). This proves reduced integral degree-two rank 55 and degree-one group \(\mathbb Z/2\).

`verify_character.py` enumerates all 720 symplectic linear maps and all 11520 affine maps, checks every induced block permutation, and compares the closed character formula to a separate oriented-simplex Lefschetz trace across all 808 faces and every group element. All 11520 comparisons succeeded. The resulting character frequency table and invariant dimensions are printed in `verification_output.txt`.

Finite exact verification applies only to the stated sixteen-point complex and the indicated finite group. The homotopy classification quoted as prior work is not independently re-certified here; the integral homology needed for this argument is recomputed. Neither quotient is claimed to have torsion-free integral homology or a particular fundamental group. No independent external mathematical audit has been performed.
