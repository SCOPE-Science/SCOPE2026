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

# Finite verification and mathematical scope

The standalone `verify.py` constructs the complete-graph subdivision directly from its closed neighborhoods. It independently enumerates all vertex masks for leaf counts 2 through 5, checks domination, computes the all-cardinality census as a cross-check, and compares each budget-restricted addition/deletion graph's component count against the theorem. Run `python3 verify.py` with Python 3 standard library.

Observed replay: `n 2 subsets 8 dominating 5 component_budgets 3 PASS`; `n 3 subsets 64 dominating 39 component_budgets 5 PASS`; `n 4 subsets 1024 dominating 513 component_budgets 8 PASS`; `n 5 subsets 32768 dominating 12305 component_budgets 9 PASS`; final `VERIFY_OK`. These are finite checks only; the all-integer theorem uses the rigorous domination criterion, minimal-set classification and explicit TAR paths in `RESULT.md`. No third-party or independent mathematical audit was performed.
