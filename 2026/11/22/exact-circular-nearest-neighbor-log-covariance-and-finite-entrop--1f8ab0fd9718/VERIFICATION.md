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

The source-independent derivation decomposes normalized circular gaps into independent exponentials and their Gamma total. It computes the shared-neighbor logarithmic covariance from a bivariate survival integral, then evaluates the integral using two convergent dilogarithm series. The one-dependent central limit theorem and its variance are proved analytically in RESULT.md. Exact endpoints \(n=2\) and \(n\ge3\) are separate; matrix signs and positive Fourier modes are checked by strict inequalities, not extrapolation.

`python3 verify.py` uses Python's standard library, evaluates the constant two ways, checks analytical inequalities, and reproduces seeded Monte Carlo sample means, variances, and six covariance lags. It has passed as packaged; simulation and numerical quadrature only check the implementation, not the infinite claims. There is no finite-sample quantile certificate, independent audit, or nonuniform-null theorem.
