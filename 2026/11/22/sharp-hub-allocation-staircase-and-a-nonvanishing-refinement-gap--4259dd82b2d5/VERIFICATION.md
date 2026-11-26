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

The one-split asymptotic at fixed screening and fixed parent-class budget follows from the uniform balancing and pair-count bounds in `RESULT.md`. The unchanged standalone `verify_star.py` uses Python 3 with standard-library dependencies only. It covers exact-rational Green entries and finite partition costs, auxiliary fixed-budget optimizer formulas, the example with 12 leaves, and bounded refinements. The script's original terminal count is `PASS: 367 exact-rational comparisons / identities`. These finite tests corroborate individual instances and are not an asymptotic proof or evidence about historical priority.
