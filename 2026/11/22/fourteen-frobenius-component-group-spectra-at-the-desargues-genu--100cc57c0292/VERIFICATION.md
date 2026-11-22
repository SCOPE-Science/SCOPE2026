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

The included `verify_desargues.py` was executed with Python 3.13.5 and SymPy 1.14, and returned `DESARGUES_14_FROBENIUS_COMPONENT_GROUPS_OK`. It reconstructs all twenty vertices and thirty edges, tests all 240 full graph symmetries, calculates the graph critical-group Smith form, and checks the fourteen equivariant Smith presentations at two independently chosen sink vertices. The claimed infinite-family conclusion uses standard deformation and Néron monodromy theorems; the finite calculation itself verifies only exact integer presentations, not the existence of algebraic smoothing families. Independent mathematical audit is not performed.
