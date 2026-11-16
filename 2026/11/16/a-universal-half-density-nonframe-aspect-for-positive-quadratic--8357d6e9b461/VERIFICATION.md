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

# Verification details

The infinite-dimensional result is established analytically in `RESULT.md`: a positive theta product, strict monotonicity, Poisson asymptotics, exact cancellation of every pre-Gramian row, and the published pre-Gramian non-frame criterion. The existence and uniqueness assertions refer specifically to the alternating-character equation, not the complete Gabor nonframe locus.

The standalone standard-library `CHECK.py` program numerically solves the dimensionless equation for sample parameters and tests the theta monotonicity, all tested even/odd pre-Gramian rows, and logarithmic curvature comparisons. The saved program was executed and passed 276 finite consistency assertions. Results are parameter-sample consistency checks only; they cannot establish the infinite proof or priority.

Independent mathematical validation has not been performed. Prior-literature comparisons and remaining publication-priority risks are summarized in `REVIEW.md` and `AUDIT.json`.
