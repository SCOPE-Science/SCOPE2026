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

With Python 3.10 or later and SymPy installed, run `python verify.py` from the directory holding this package. Its exact symbolic checks confirm the centered-site cubic objective, its derivative, the marginal-preserving correlation factorization and monotonicity relation. It independently computes rational Gaussian covariance Schur complements for zero, one and two readings, including coincident sites. It also evaluates several exact parameter configurations and thousands of supplementary feasible grid comparisons. The output is an automatically reproducible calculation, not independent validation or an infinite-domain certificate.

The mathematical proof of global uniqueness uses strict convexity of the cubic-gap function; the claim for all feasible joint Bernoulli laws relies on the analytic monotonicity of the scalar first-order equation. The strict optimized-risk derivative is a consequence of the exact factorization and envelope theorem, not a numerical inference. No results are claimed for adaptive selection, more readings, unequal delivery marginals, or additive observation noise.
