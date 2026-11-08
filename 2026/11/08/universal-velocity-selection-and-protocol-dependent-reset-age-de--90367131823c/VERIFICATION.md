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

# Reproducibility and verification

Run `python verify.py` with Python 3.10 or later in the directory containing this document and `verify.py`. The script uses only the standard library, and checks two fixed parameter triples, two large conditioned-position values, and both reset protocols. It evaluates the exact covariance formulas, their Maxwellian/zero-reset algebraic differences and positive definiteness, then independently integrates the stationary age-mixture density using composite Simpson quadrature. The results are compared with the exponential tail normalization, the selected Gaussian velocity mean and variance, and the asymptotic age mean and age variance. The checker raises an assertion on failed tolerance and prints PASS on completion.

The proof in `RESULT.md` establishes the theorem by Gaussian conditioning, precise large-age covariance asymptotics, exponential localization of the reset age, the exact reference Laplace integral, and an age moment-generating-function argument. No finite numerical calculation certifies an infinite limit. The checks do not cover simultaneous vanishing damping/reset rates, non-Gaussian kicks, or finite-duration returns. The independent audit channel has not been performed.
