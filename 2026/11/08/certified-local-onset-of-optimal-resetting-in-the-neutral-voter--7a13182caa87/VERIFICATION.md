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

The exact-rational `certificate.py` (standard-library Python) certifies the unique root of the first reset-response coefficient in the interval \((0.8152,0.8154)\), uniform negative derivative, and strictly positive second-order coefficient at that root. The proof in `RESULT.md` explains why these three tests entail the asserted analytic local branch.

The optional `numerical_check.py` (mpmath) computes the critical fraction, magnetization, coefficient, and direct hypergeometric derivative checks. Floating-point output is illustrative and is not treated as an infinite-domain proof.

The theorem is for first absorption in the neutral voter diffusion with instantaneous Poisson resetting to the original state. There is no finite-network error estimate or global optimization assertion.
