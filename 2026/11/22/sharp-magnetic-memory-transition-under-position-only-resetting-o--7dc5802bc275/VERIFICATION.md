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

The analytic covariance formula and its sign classification are proved in `RESULT.md`. The accompanying `check.py` requires NumPy and SciPy and can be invoked by running `python check.py`. It performed 436 checks: 360 independent real-matrix-exponential comparisons over positive parameter grids, 60 Laplace-quadrature comparisons for the stationary variance, 7 resonant-line threshold tests and 9 strictly positive slow-reset coefficient tests. All passed in the indicated numerical environment.

No finite numerical test establishes infinitely many sign changes; this conclusion instead follows from nonzero oscillatory asymptotics and the exact critical trigonometric amplitude. Checks do not prove literature novelty, measurement robustness, or any additional claims outside the stated linear process.
