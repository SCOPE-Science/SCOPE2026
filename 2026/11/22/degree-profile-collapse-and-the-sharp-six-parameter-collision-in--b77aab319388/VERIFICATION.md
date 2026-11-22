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

# Verification and evidentiary limits

Run `python3 verify_degree_collapse.py` using Python 3 and the standard library. `verification_output.txt` records the exact successful output. All graph instances are generated from the defining deleted-edge pattern. For each, triangle-freeness of candidate neighborhoods is tested directly, separately from the degree-expression calculation. All fixed-shore bipartite patterns with at most five vertices are generated (with both third-shore sizes one and two), including four-cycle cases. The canonical test uses every within-shore permutation and exchanges equally sized shores. The unique earliest fibre for two plus three defect vertices is directly checked, and the two witness families are independently enumerated for third-shore size one through seven. No external tables are assumed.

The all-order assertions are proved algebraically in `RESULT.md`, not by finite enumeration. The checker does not independently certify historical priority, and no independent mathematical audit has been performed. The full-text source comparisons and the unresolved limits are recorded in `AUDIT.json`.
