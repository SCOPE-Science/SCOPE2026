---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

All 4-seat 2-capacity count vectors reduce to four symmetry classes; exact score differences S_V−S_W=(y−x)/3 and S_U−S_V=(3y−4x)/12 give PAV winners. All branch-level greedy marginal inequalities yield its distinct transition at y/x=3/2, including ties at 1, 4/3, 3/2. Independently enumerated all 147 sorted positive integer ballot triples through 17 voters using exact fractions; of 123 below 17 none has disjoint greedy/optimal outcomes and exactly (5,5,7) of 24 at 17 does. Source verify_triangle.py independently uses aggregate and labeled-candidate scores. Infinite real-ratio rows follow from symbolic comparisons, finite exhaustion only proves 17-voter cutoff.

## originality

PASS

The general discrepancy between PAV optimization and sequential PAV is textbook/classical, so it is not claimed new. Closest 2023 primary work is axiomatic characterizations rather than this concrete three-overlap-clone family. The exact robust interval, tie-boundary outcomes, and integer cutoff 17 remain unreported in inspected primary statements and indexed published findings.

## value

PASS

The all-tie robust failure interval and sharp 17-voter cutoff give a motivated exact counterexample boundary for a natural overlapping three-type approval domain with finite capacity; usefulness does not depend on a new general impossibility theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
