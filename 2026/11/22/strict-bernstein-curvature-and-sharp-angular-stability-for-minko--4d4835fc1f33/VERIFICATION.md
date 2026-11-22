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
# Verification of the area-curvature theorem

The analytic proof is in RESULT.md. The independent tests below check separate representations and representative numerical consequences but are not a certificate for the universal analytic claim.

Run `python3 verification.py` in the same directory; no additional dependencies are needed. Verified output: `ELLIPSE_MIXED_AREA_BERNSTEIN_PASS 214`.

The checks compare (i) Steiner/singular-value area versus an independently integrated support-curvature formula, (ii) both against the shoelace area of an independently parameterized smooth boundary, (iii) Laplace perimeter versus direct ellipse arc length, and (iv) strict monotonicity, concavity/chord inequalities and the circle boundary cases for explicit positive semiaxis tuples. Numerical quadrature is finite, so the proof of every-order sign and the exact optimal curvature comes from the Gaussian–Laplace calculation, not from samples. The novelty conclusion remains provisional pending independent priority review.
