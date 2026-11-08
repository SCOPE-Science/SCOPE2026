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
# Verification

The proof in `RESULT.md` supplies the general argument. To reproduce finite checks, run `python3 artifacts/quad_bent_gabor_check.py` using Python 3.8 or newer. Only the standard library is required.

The checker tests all ambiguity coefficients exactly for both quadratic Gauss signs in binary dimensions four, six, and eight by enumerating the window and applying an integer fast Walsh transform. It compares the complete signed coefficients to the formula derived independently from quadratic Gauss sums, checks all multiplicity totals and positive-rank formulas, and verifies the real-symmetric projector rank for both signs at dimension four by exact modular Gaussian elimination. Expected final output: `QUADRATIC_BENT_REAL_GABOR_EXACT_CHECKS_OK`.

These finite verifications cannot prove a universal infinite-dimensional statement, which is established in `RESULT.md` by the Gauss-sum calculation and Weyl orthogonality. No external mathematical audit has been performed. The observable matrix space is explicitly the real symmetric space; for the complex lifting, the real skew-symmetric directions remain in the kernel. Historical priority is bounded by the named source comparison.
