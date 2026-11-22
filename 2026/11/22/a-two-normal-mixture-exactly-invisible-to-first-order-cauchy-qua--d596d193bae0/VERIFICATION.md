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

The mathematical certificate is `certify.py`, using only Python's `fractions.Fraction` and standard library. It was executed successfully and produced the included `CERTIFICATE.txt`. It checks strict rational inequalities for Gaussian-quantile brackets, variance brackets and the Cauchy reference variance. Machin's arctangent identity, monotone alternating series and Mills-tail inequalities supply all analytic error bounds; the checker uses no floating-point numbers for mathematical assertions.

The symbolic joint-quantile covariance calculation is written in `RESULT.md` and can be verified independently from Brownian-bridge increment covariances. The checker does not purport to prove the delta method or the intermediate value theorem; these mathematical arguments are written explicitly. The printed floating-point representations in `CERTIFICATE.txt` are diagnostic renditions of rigorously compared rational intervals.

Verified scientific limits: the limiting-power conclusion concerns asymptotically normal two-sided critical values for a scalar quantile ratio and does not establish exact finite-sample calibration. The exact witness is obtained existentially by continuous root crossing, not by taking the displayed approximate mixture parameters as exact. No independent audit has been performed.
