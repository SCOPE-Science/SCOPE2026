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

# Verification of the exact first-intensity asymptotics

The complete analytic argument is in `RESULT.md`; `CHECK.py` independently integrates the Gaussian-smoothed spectrum and its first two centered moments at selected positive frequencies and parameter values. Checks compare subquadratic power corrections, the Gaussian exact case, two superquadratic exponents, the central deficit, and numerical derivatives of the tilted mean. An 95-digit error-function calculation checks the delicate exponential correction at the nonsmooth Laplace spectrum.

Executed command: `python CHECK.py`. Successful result: `ALL_STRETCHED_SPECTRAL_INTENSITY_CHECKS_PASSED`.

The numerical comparisons cover finite test values only; they do not prove the asymptotic conclusions or count all possible crossings of the white-noise intensity. Correctness also depends on the covariance/Edelman–Kostlan intensity normalization and the analytical localization and integration-by-parts arguments supplied in `RESULT.md`. This is a self-review, not an independent mathematical audit.
