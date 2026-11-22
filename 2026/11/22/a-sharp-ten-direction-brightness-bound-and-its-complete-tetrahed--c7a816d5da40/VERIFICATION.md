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

Run `python verify.py` with Python 3, NumPy, and SymPy. The checker reconstructs explicit tetrahedron edge vectors and checks their outward oriented face areas, in addition to using exact symbolic vector arithmetic for five rational values of the equality parameter, verifies all maximum-axis norms and the sharp ten-center Gram contact, independently checks the Cauchy expression against all sixteen subset sums on 100 randomly generated balanced configurations, and compares the exact terminal-tail law with a 250,000-direction simulation at two thresholds.

The mathematical proof, not the random experiment, establishes the universal bound, completeness of the equality family, and exact tail over a continuum of thresholds. The checker does not provide external certification or guarantee historical originality.
