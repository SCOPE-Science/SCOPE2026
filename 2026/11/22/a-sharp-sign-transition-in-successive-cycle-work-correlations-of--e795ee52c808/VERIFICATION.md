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

The proof uses a direct cycle-by-cycle solution of the linear Gaussian engine, active-force covariance integration, Isserlis' identity, and a monotone range classification. Numerical execution of `verify.py` independently tests the closed adjacent and diagonal force covariances against double integrals, 1,200 monotonicity samples, threshold witnesses, and exact finite-dimensional Gaussian-sampling estimates of two work lags. The script passed during preparation. Python 3 plus NumPy enable all tests; without NumPy, analytical and quadrature tests run and Monte Carlo is marked skipped. These checks cannot establish priority, the validity of an uninspected publication, or results outside the Gaussian full-shift assumptions.
