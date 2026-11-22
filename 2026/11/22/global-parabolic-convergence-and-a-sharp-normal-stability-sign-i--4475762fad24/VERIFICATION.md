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

# Verification record

The standard-library script `verify.py` checks, using exact rational polynomial arithmetic, the transformed equations and full Lyapunov derivative identity for symbolic coefficients and state variables. It also recomputes the two normal-spectrum invariants and tests strict spectral instability at negative mixed coupling for finite rational witnesses. Run `python verify.py` from the extracted package.

Formal algebraic checking supplements the proof; global existence, invariant-measure rigidity, and normal-sign sharpness are proved analytically in RESULT.md and are not inferred from finite numerical trajectories. No independent mathematical audit has been performed.
