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

# Verification and scope

The standalone `verify_digit_lags.py` has been run with standard-library exact rational arithmetic. It verifies the stated density normalization, the piecewise Perron--Frobenius invariance identity at one sample from every cell of the *exhaustive finite partition* whose boundaries include all inverse images of density breakpoints, and all first-/second-lag cylinder integrations at eight rational parameters including endpoints and the interior sign-transition parameter. Results are diagnostic, not a substitute for the analytic proof over all real parameters. The proof in `RESULT.md` covers the continuum of parameters.

No numerical simulation or finite enumeration is used to conclude uniqueness, ergodicity, or infinite-time claims: the existence, uniqueness and ergodicity of the absolutely continuous invariant law are established in the cited primary paper, and the time-frequency statements follow by Birkhoff's ergodic theorem. No external or independent mathematical audit has been performed.
