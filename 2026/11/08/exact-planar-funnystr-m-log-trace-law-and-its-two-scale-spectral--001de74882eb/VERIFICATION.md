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

# Verification and limits

Run `python3 verify.py` using Python 3 standard library. The recorded run produced `VERIFICATION_OK checks=6020`. The checker performs exact-rational identities for the two rank-one residual expressions; checks exact inversion of the Cauchy-square CDF at nonboundary quantiles; compares analytic angular-logarithm and reciprocal angular integrals with deterministic midpoint numerical quadrature; and tests the leading high-spike mean and fixed-quantile constants.

The CDF requires only the exact standard Cauchy law of the ratio of independent standard normal variables. The angular integral is proved by analytic circle averaging, while the direct reciprocal integral follows by \(u=\tan\theta\). These infinite mathematical facts, asymptotic assertions and publication novelty are not established merely by the finite checker. The dimensional restriction, real Gaussian requirement, lack of oversampling and fixed positive lower eigenvalue in the spike limit are essential to the stated theorem.
