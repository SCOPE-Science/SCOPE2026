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

# Reproducibility

Run `python verify.py` after installing NumPy. The script checks 42 exact rational normal-form identities, 36 independent conditioning-matrix cases, 4,500 random candidate designs, and two rational examples, giving a total of 4,578 automatic checks plus the two examples. The computation was executed successfully in the scientific review of this theorem.

These tests verify algebraic consequences on specified rational/finite domains. They do not enumerate the continuum of nodes, noise budgets or sensor counts. The continuum claim follows from the rearrangement, concavity, Jensen and scalar strict-convexity proof in RESULT.md. The cited literature comparisons concern published claims and their scope; absolute historical priority and independent review have not been established.
