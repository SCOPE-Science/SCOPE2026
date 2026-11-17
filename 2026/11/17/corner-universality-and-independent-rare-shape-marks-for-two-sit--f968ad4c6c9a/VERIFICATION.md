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

The full proof is in `RESULT.md`. The reproducible `check.py` compares a half-plane polygon clipping computation against a separate algebraic corner-area expression on 300 random pairs in two rectangles, verifies the exact rational prefactor, and simulates 2,000,000 pairs per geometry. The checker passes with `RECTANGLE_TWO_SITE_CHECKS_OK` using NumPy.

For two rectangles of area four and thresholds equal to 2.5% of area, observed rare-event probabilities were 0.0016895 and 0.0017075, compared with leading prediction 0.0016666667. Threshold bias is expected. Conditional sample means and symmetry fractions were approximately 0.674, 0.502, 0.504, 0.507 against targets 2/3, 1/2, 1/2, 1/2.

These finite numerical experiments are diagnostic, not a proof of an asymptotic statement. No quantitative uniform error over rectangle aspect ratios is established. No independent mathematical audit is claimed.
