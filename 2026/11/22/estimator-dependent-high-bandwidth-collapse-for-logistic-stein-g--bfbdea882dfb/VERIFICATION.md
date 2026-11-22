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

The analytic proof supplies the two exact likelihood-score identities, the stochastic Taylor reduction in the diverging Gaussian-precision regime, and the logistic moment computations leading to the \(\chi_1^2\) constants. Run `python checks/check_logistic.py` with NumPy and SciPy installed; the packaged script has 15 independent assertions for score roots, six quadrature identities, positivity, and three increasing-bandwidth comparisons for each estimator. Numerical experiments corroborate finite-dimensional identities but do not establish an asymptotic or exclude historical coverage. The statement concerns only the null distribution for deterministic tuning sequences.
