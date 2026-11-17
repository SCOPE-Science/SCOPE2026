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

# Verification record

The theorem follows analytically from the independently verified uniform horizontal increments, the unique-crossing interval argument, the exact vertical overlap kernel, and the four finite elementary integrals in `RESULT.md`. `verification/check_crossing.py` checks all four integrals symbolically and recomputes the final constant, tests the uniform-slope identity by direct numerical quadrature, and compares direct geodesic-crossing simulations across widely different cylinder aspect ratios. A successful run prints `CYLINDER_CROSSING_CHECKS_OK`. The finite random tests are corroborative only; the exact proof does not rely on them.

The related closed flat-torus crossing theorem has been compared by mathematical implication rather than wording: the change from two periodic coordinates to one periodic and one bounded coordinate changes the conditional intersection measure. Historical priority remains provisional. No independent mathematical audit or external certification has been performed.
