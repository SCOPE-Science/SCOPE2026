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

# Reproducibility and boundaries

Run `python checker.py` with standard Python. It should print `FOREST_BRIDGE_EXACT_CHECKS_PASSED 48`. Checks cover full acyclic edge-subset enumeration for graph sizes 4 through 7 and activities one third, one, two, plus exact rational mixture identities through graph size 100. This is not an exhaustive numerical check of arbitrary graph sizes and it is not independent validation.

The all-size proof is the mutually exclusive one-bridge classification, the conditional three-state product law, exact moment subtraction, differentiation, a one-sign-change application of Descartes' rule, and a simple-root asymptotic expansion. The checker does not replace these steps. No claims are made about arbitrary edge activities, other graph families, or exhaustive prior-art discovery.
