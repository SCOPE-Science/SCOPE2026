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

Run `python verify.py` with Python 3. The checker uses only standard-library `fractions`, `math` and `itertools`; it tests five positive exponential means and polynomial paths of every degree from zero through four, for 19,525 exact-rational cases. It calculates both risks in two independent ways: factorial moments of the pathwise estimator errors and algebraic integration of their covariance kernels. It verifies vanishing error for constant curvature, sharp equality for affine curvature, zero mean error for the endpoint estimator, and nonnegative risk. No randomness or floating-point tolerances are used in these checks.

The infinite-dimensional and non-polynomial cases are proved analytically in RESULT.md, not certified by the finite checker. Strict risk nonordering follows from the sign of the explicit kernel difference on two disjoint support regions. No stochastic-oracle errors, full-optimizer convergence experiments, or external independent validation are included.
