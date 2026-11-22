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

The included `checker.py` was executed with Python 3 and passed 327 exact rational assertions. It checks both radial Poisson-equation polynomials, the exposed-time moment variance, and the estimator-risk / stopped-path-information identity over a rational parameter grid. An independent symbolic differentiation confirmed that the modified-Bessel expression solves the radial Feynman–Kac equation. The analytic proof separately addresses the conditional Gaussian decomposition, the stopped likelihood, and the large-domain convergence. Numerical or finite symbolic checks alone are not treated as proofs of these infinite-dimensional probabilistic statements. No independent audit was performed.
