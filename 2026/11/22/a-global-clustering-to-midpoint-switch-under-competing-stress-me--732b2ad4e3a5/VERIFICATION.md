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

# Reproducibility and scope

Run `python3 verify_memory_pulses.py` with Python 3 (standard library only). This deterministic program checks the exact normalized-slope example, both transition expressions, the derivative-sign geometry, and dense grid and seeded perturbation tests. It returned `VERIFICATION_OK 327720 supplementary assertions` when executed from the package source. The executable is bundled here in full, without external data dependencies.

The universal theorem follows analytically from the strictly increasing hyperbolic-sine ratio and the strictly increasing quotient of exponential deficits. Tests sample finitely many parameters and times and cannot establish absence of other optima; the proof supplies the infinite-parameter statement. Model extensions and empirical validation have not been performed. External independent audit is not yet performed.
