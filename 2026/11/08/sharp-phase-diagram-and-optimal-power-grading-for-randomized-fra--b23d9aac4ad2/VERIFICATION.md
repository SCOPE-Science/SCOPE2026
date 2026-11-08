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

The theorem is analytic. Its exact identity follows from conditional Bernoulli sampling variance, the bivariate Gaussian angle law, and fractional Brownian scaling; its asymptotics follow from a uniform small-panel covariance estimate and positive power-sum asymptotics. The convergence-rate assertions apply to all integers \(n\to\infty\), not just tested grid sizes.

Run `python3 verify.py` with Python 3.9 or later; it uses no nonstandard packages. The script numerically integrates Gaussian correlation angles on panels using a midpoint rule, checks the Brownian one-panel arcsine value, and tests selected leading constants, plus the algebraic formula for the minimizer. Finite tests do not certify the infinite asymptotic statement or novelty. Other Hurst parameters, different integrands, adaptive sampling, and arbitrary partitions are outside the theorem.
