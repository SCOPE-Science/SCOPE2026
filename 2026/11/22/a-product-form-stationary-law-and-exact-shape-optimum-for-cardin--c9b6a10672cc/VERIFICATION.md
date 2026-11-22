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

# Reproducibility

Execute `python verify.py` with Python 3's standard library. The test constructs the weak generator residual for monomials with heading-dependent coefficients in two and three dimensions and checks cancellation over exact rational arithmetic for 80 combinations. It checks force/area versus the derived active-pressure formula. Separately, it uses 319,000 stationary post-burn-in event intervals per axis-weight setting for independently drawn redirection weights 0.2 and 0.8 and checks the predicted stationary mean, vanishing cross-covariance, and positive corner mass. It also solves the fixed-volume scalar multiplier in three dimensions.

# Analytical checks not reducible to finite numerics

The proof in `RESULT.md` verifies stationarity for arbitrary differentiable heading-dependent test functions by exact integration of the transport and redraw terms, then establishes uniqueness by a uniform finite-time corner minorization. It derives the pressure force and strict fixed-volume convexity symbolically for all finite integers \(d\ge2\). The finite generator tests and simulations cannot independently establish those quantifiers, and no generalization to thermal noise, continuously distributed headings, or microscopic interactions is asserted. No independent scientific audit has been performed.
