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

# Verification and reproducibility

The exact rational multiplier derivative, the paired-weight inequality, and the endpoint Taylor expansions are fully proved in `RESULT.md`. `check_stability.py`, using `requirements.txt`, independently simplifies the pivotal algebraic identities symbolically and verifies the boundary against high-precision quadrature. `verification_output.txt` records a successful run with 19,832 assertions. These assertions include finitely many rational parameters and are not used as a replacement for the proof over all nonnegative parameters.

The cutoff \(X\) is uniquely defined by \(X^2/(1+X)-2\log(1+X)=0\), beyond the trivial root \(0\); quoted decimals are ancillary numerical approximations, not the mathematical definition. The exact constants in the claim use this implicit definition. The boundary graph excludes equality because the second moment is constant at multiplier one, not decaying. At \(z=0\) the multiplier is identically one, also outside the open stability region.

No independent scientific audit, separate proof validation, or general nonlinear stability check has been performed.
