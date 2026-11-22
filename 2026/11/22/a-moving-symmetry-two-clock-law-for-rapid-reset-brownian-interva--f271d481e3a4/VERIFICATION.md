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

The analytic proof is in RESULT.md. Reproduce the finite-parameter numerical checks with `python3 verify.py` (Python 3 standard library only). The checker evaluates exact Brownian hitting transforms, reset-renewal resolvents, rate derivatives for second moments, the independent published mean formula, and nontrivial detuning values. The executable reports 222 deterministic checks. No numerical sample, finite-rate comparison, or exponential-tail bound replaces the analytic high-rate weak-convergence and uniform-integrability proof. Independent review or validation has not been performed.
