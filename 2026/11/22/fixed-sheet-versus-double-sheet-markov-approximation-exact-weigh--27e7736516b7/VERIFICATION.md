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

# Verification and reproducibility

Run `python3 verify.py` using the standard Python 3 library. Observed output: `THREE_SHEET_RATIONAL_CHECK_OK 2513`.

The script evaluates 500 integer-budget minimizations of the pointwise missing-mass lower bound, checks 499 proposed equality allocations and connected-double scalar specializations, and tests small labelled flip-path reachability for integer budgets 2 through 18. All integer counts use exact rational arithmetic. These checks detect arithmetic and small finite-state mistakes only; they cannot prove covering-space path gluing, the infinite family of budget identities or global novelty.

The proof establishes the total-variation identity, topological no-section obstruction, unrestricted componentwise triangle inequality, balanced occupancy lower bound and matching all-budget constructions using the explicitly cited connected-cover transport lemmas. The result and review distinguish the previously known two- and three-map cases from the extension to larger budgets. The finite checker neither verifies that comparison nor certifies priority.
