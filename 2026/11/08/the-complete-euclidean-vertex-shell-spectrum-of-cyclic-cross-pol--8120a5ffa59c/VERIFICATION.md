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
# Reproducibility and limits
Run `python verify.py` with NumPy and SciPy installed. It enumerates all four signed endpoint choices at each edge of the cycle for dimensions 3 through 7, confirms the predicted maximum squared norm and multiplicity among all sums, then calculates convex hulls (dimensions 3 through 5) to compare the complete vertex radial shell distribution with the closed formula. It raises on mismatch and prints `PASS` at completion.

The computation is exhaustive only for the stated finite parameters. The infinite-dimensional statement requires the generic-support/orientation proof and transition count in `RESULT.md`. Floating-point convex hulls are corroborative only, not exact certificates. Historical priority remains provisional, and no independent scientific audit has been performed.
