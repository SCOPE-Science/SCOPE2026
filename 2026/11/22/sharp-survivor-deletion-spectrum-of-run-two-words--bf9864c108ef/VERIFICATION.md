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

# Verification of filtered single-deletion sphere classification

Run `python checker.py` using only Python's standard library. The checker enumerates every allowed word and compares a direct set of all allowed one-deletion outputs against a separate run-based computation, then compares the complete degree histogram with an independent four-state transfer polynomial recurrence. The script checks all \(q=2\) sources for lengths 1–16, all \(q=3\) sources for lengths 1–10, and all \(q=4\) sources for lengths 1–8: 115,544 admitted source words in total. It verifies every stated minimum, maximum, equality count and sharp-span minimum-extremizer count in range, plus four congruence-class witness constructions for target degrees 1–17.

The proof does not rely on finite testing. The critical infinite steps are (i) the run-deletion output equivalence and receiver-filter criterion, (ii) the transfer encoding of the middle run's validity, (iii) the incidence lower bound, and (iv) equality rigidity at maximal span. This package does not assert external or independent certification and contains no proof for run caps above two or for multiple deletions.
