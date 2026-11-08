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

# Verification notes

The self-contained `verify.py` program uses Python 3's standard library. Run `python3 verify.py`. It executes 846 bounded algebraic and numerical tests of the exactly soluble \(H=1\) parent covariance case with varied gamma shape, gamma-clock parameter, correlation time, window length and observation separation. The tests check the finite-interval Gaussian covariance identity, strict gap ordering and positive floor, the universal \(L^{-1}\) correction, the \(L^{-2}\) gap contrast and the known kurtosis-floor identity.

For arbitrary \(1/2<H\leq1\), the necessary checks are analytic: the positive-definite parent covariance, the conditional Gaussian Wick formula, the exact gamma moments, exponential control of the variance remainder, and the bounded-convergence argument for the gap profile. These steps are provided in RESULT.md. No finite numerical test verifies the universal quantifiers or establishes uniqueness relative to all prior publications. Independent audit has not been performed.
