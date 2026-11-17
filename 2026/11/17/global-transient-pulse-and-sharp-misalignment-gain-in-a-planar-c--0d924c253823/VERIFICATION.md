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

# Verification evidence

The critical coefficient-matrix and projective-direction identities were derived symbolically from the unreduced coupled flow. The resulting exact scalar integral, norm derivative, hyperbolic-cosine identity, sharp maximum, recovery time and Haar-direction tail law are proved in `RESULT.md` for all positive \(\lambda,\beta,\gamma\), all initial unit directions, and all initial positions. The exceptional direction is handled separately.

`checker.py` runs symbolic tests, 192 numerical integrations of the original four-coordinate differential system with four observations each, exact-formula checks at available peak and recovery times, and deterministic angular quadrature tests for the closed-form gain tail. It passed in the scientific review. Reproduction requires Python with `sympy`, `numpy`, and `scipy` and the command `python checker.py`.

No automated test validates historical publication priority, and numerical ODE integrations are not infinite proofs. The result does not cover variable or unequal-magnitude Hessians, and no independent audit has been performed.
