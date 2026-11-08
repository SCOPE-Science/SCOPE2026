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

# Reproducible verification

Run `python check_edge_defect.py` with Python and SymPy. Its exact symbolic checks compare the weighted-complete-graph rank-one resistance formulas, every edge profile and peak difference, the factor for the exceptional four-vertex cutoff, and the sign-certificate boundary identities. It then builds six independent subdivided resistor networks with exact rational conductances, inverts grounded Laplacians and checks endpoint and midpoint resistances. The observed terminal messages are `GENERAL_SYMBOLIC_EDGE_PEAK_IDENTITIES_PASSED`, `INDEPENDENT_RATIONAL_SUBDIVISION_RESISTANCES_PASSED 6`, and `ALL_ONE_EDGE_COMPLETE_GRAPH_CHECKS_PASSED`.

The full claim for arbitrary integer dimension and positive real edge length is established by the analytic Green representation plus the symbolic identities and sign argument in RESULT.md; the six network calculations are finite corroboration, not a substitute for universal proof. The literature search is not a proof of priority and there is no independent audit.
