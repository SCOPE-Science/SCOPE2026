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

The theorem is established by the explicit five-step analytic proof in `RESULT.md`. The singular-value estimates use the exact Hilbert--Schmidt normalization, and the skew-orthogonal correction requires only the positive matrix square root on a matrix with spectral gap at least \(0.9775\). The lower witness is checked symbolically by its two block singular values and the Lipschitz bound on individual singular values.

`checker.py` executes supplementary deterministic standard-library diagnostics for seven even matrix orders and six positive block-scaling parameters, verifying explicit singular-level profiles and the dimension-sharp lower-bound witness. In the checked environment it printed `NEAR_CONFORMAL_TWO_PLANE_DIAGNOSTIC_OK 42`. The finite angular sampling does not prove global maximization; that assertion is proved separately by the elementary monotonicity of the two-level singular-value ratio. No independent audit or outside proof verification has been performed.
