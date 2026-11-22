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

The analytical proof derives the entropy invariants and uniform small-state asymptotics for the specified positive-state semidiscrete ODE. A standalone Python verifier is included as `verify.py`; running `python verify.py` completed 4387 finite diagnostics without errors. Its exact-rational tests cover the mean and entropy-potential identities for several integer parameters; floating-point tests cover the geometric angular solution and boundary coefficients. Finite tests do not certify the universal quantified theorem; those limits are established by the proof. The general real-power case, global-in-time interior invariance for negative parameters, and small-state hitting laws were separately reconstructed analytically. No independent audit or external formal verification has been performed.
