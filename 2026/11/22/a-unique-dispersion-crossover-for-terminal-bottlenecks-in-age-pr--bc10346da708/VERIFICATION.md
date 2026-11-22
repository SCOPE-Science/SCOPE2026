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

Run `python3 verify.py` alongside `RESULT.md` with Python 3 and no nonstandard packages. It produces `PASS: 598 exact rational assertions` on the reviewed version.

The checker directly enumerates every parent-choice history through five birth steps for selected rational parameters and parent counts, and matches all finite-terminal one-cut and two-cut probabilities to exact product formulas. It independently multiplies the stationary truncated-lag constraints for many pairs of finite windows and verifies the claimed factorization. Rational infinite-series bounds place the dispersion threshold for several parent multiplicities between explicitly compared rational endpoints. Positive probability of two distinct renewal spacings is also checked.

The checker cannot certify the Gaussian limit, the entire infinite series, the uniqueness proof, or the asymptotic expansion for growing parent multiplicity. The result's analytical proof uses exponential strong mixing, summable covariance, finite-\(L^2\) coupling, monotonicity and a uniform expansion. There is no independent validation, formal machine proof, or externally verified priority claim.
