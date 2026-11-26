---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The exact finite-neighbor mark decomposition and Pareto integrations are proved in RESULT.md. `check.py` was run with Python 3; it reported 225 passed exact-rational or controlled-numerical assertions. It verifies several finite-size formulas but cannot establish convergence or originality by itself. The limiting Poisson theorem follows from the explicitly calculated rare multinomial cell probabilities, and the tail conclusion from conditional Poisson concentration.

The literature comparison in RESULT.md distinguishes the capped model from the soft exponential kernel, and credits the earlier extreme-weight point process, one-root marking, and soft-kernel pair generating function. It does not certify historical priority.
