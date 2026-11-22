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

The proof uses an edge-capacity bound, a missing-to-missing edge charge, a near-one-factorization, and a derangement construction. Run `python crown_exact_check.py` with Python 3 and the `networkx` package to repeat the complete finite terminal-pair path-selection search for orders three through seven. A separate mixed-integer incidence feasibility test was used for representative shore sets, but its output is not necessary for the theorem. The finite tests provide corroboration only; the general proof is in RESULT.md.
