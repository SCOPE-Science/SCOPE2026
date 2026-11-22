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

# Verification and reproducibility

The analytical proof of the sole accepted theorem is in RESULT.md. The accompanying `check.py` is a standalone numerical cross-check requiring Python 3, NumPy and SciPy (no external file inputs or network access). Execute `python check.py`. The recorded run returned `PASS 68 assertions`, variance `6.70464997925077`, and Poisson slope `0.81827418517348`.

The checker integrates the minCF against the Pareto density, tests the exact two-cutoff moment against its large-cutoff limit, verifies the fourth Poisson cumulant by independent piecewise integration, and compares both asymptotic variances to independent quadrature. It evaluates the oracle and likelihood-fitted statistics on reproducible samples but does not use simulations to prove convergence. The expected Gaussian mean and fourth moment agree with two-dimensional quadrature.

Exact limiting laws are proved via Hilbert-space central limit theory, Poisson point-process convergence and Pareto truncation estimates; the finite-sample code is not an infinite-dimensional certificate. A subsequent independent mathematical audit has not been performed.
