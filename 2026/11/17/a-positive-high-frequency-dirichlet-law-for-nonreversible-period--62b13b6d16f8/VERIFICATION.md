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

# Verification of the analytic claim

The proof checks Floquet analyticity, the first-order vanishing, the integration-by-parts second-order identity, and the exact positive-coefficient boundary. The package checker in `checks/check_fast_switching.py` uses exact rational integration to corroborate both an equal-rate and an asymmetric nonreversible three-patch cycle; its matrix exponential tests address finite periods only. Run with `python checks/check_fast_switching.py` in an environment with `numpy` and `scipy`. The rigorous general-network conclusion follows from the paper proof, not those finite experiments. No independent mathematical audit was undertaken.
