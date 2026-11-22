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

# Verification and limits

The standalone `check_polygon_design.py` uses only Python standard-library math, random numbers and numerical elimination. Run `python3 check_polygon_design.py` in a directory containing this file. The verifier prints `POLYGON_SUPPORT_DESIGN_PASS` after checking 1,120 seeded random determinant identities for normal counts 3–16, balanced and midpoint singular/nonsingular tests, and transverse inverse-pole ratios. The actual replay of the packaged script completed successfully.

The numerical tests do **not** establish analytic tail behavior or global all-dimensional facts. Those follow from the exact determinant, rank-one singularity, nonvanishing gradient, compactness and coarea proof stated in `RESULT.md`. The constant is an explicitly defined geometric integral. Its positivity assumes the sampling density is positive near each sector midpoint.

The statistical assertion assumes noise independent of the random angular design, with covariance \(\sigma^2I\), and studies only the unconstrained linear inverse of support values. All other estimator classes are outside this verification.
