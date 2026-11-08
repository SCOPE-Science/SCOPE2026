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

The accompanying `verify.py` uses only the Python standard library. It independently computes centered-coordinate covariances by exact rational walk weights and by a formal algebraic-resolvent expansion, checking 29 successive coefficients across multiple dimensions and rational parameters. It then computes long finite covariance sequences and compares them to the indicated pole, square-root collision and interior branch asymptotic amplitudes.

For an independent map-level numerical spot check at the original parameter \(m=2,a=1/3\), 1,200,000 Lebesgue-sampled two-dimensional initial points were advanced by the piecewise-affine map. The first six sampled covariances were close to the exact predictions. Neither finite calculation proves the infinite statements.

The complete mathematical argument is the signed branch-free formal generating-function derivation followed by singularity and residue analysis in `RESULT.md`. At fixed parameters the asymptotic error is not asserted to be uniform in a double scaling limit. No independent audit has been conducted.
