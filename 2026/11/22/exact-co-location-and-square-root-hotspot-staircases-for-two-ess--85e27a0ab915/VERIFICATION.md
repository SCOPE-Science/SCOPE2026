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

# Verification

The analytic proof is in RESULT.md. The separate complete `check.py` is executable with the Python standard library (`python check.py`). It evaluated **60,282** assertions: exact rational square and derivative identities; exact neighboring support-score signs for rational inputs and patch counts 2 through 5; exhaustive *finite-grid* checks of two independently allocated inputs with 2–4 sites; exact small examples; and nineteen numerical checks of the square-root tie formula.

The finite mesh cannot establish global optimality for all continuous allocations or arbitrary numbers of sites. The global result follows instead from the displayed exact square identity, pairwise sign argument and analytic threshold comparisons. No independent external proof check, field validation, or numerical certification of infinite ranges is claimed.
