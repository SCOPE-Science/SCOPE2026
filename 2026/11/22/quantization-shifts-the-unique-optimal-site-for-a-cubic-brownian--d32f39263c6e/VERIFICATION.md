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

Run `python verify.py` with the versions in `requirements.txt`. The checker reconstructs the two Gaussian-regression integrals and one Brownian Wick variance integral symbolically; it verifies the sign-bit risk, full-reading risk, both extremum equations and the strict site comparison. It then performs ten 45-digit independent scalar integrations as numerical cross-checks. On the supplied dependencies the observed terminal status was `EXACT_QUADRATURE_CHECKS_OK 27`.

All infinite-dimensional and global optimization assertions are established by the covariance identity, Gaussian regression and polynomial root-sign proof in `RESULT.md`. The numerical tests are not used to infer uniqueness, completeness or publication priority. The computations do not check arbitrary other encoders or sampling protocols; those are outside the stated claim.
