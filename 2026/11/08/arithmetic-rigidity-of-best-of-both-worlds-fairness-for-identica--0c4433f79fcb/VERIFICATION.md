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

# Verification

The universal mathematical claims follow from the proof in `RESULT.md`. The reproducible checker `verify_homogeneous_chore_rigidity.py` was executed from the packaged source under Python with SciPy and completed with:

```text
all exact rational-grid classification tests: 658
all exchange-rigidity comparisons: 2939
n+1 exceptional-profile symbolic counts checked for n=2..6
exact two-person congruence checks: 528
```

The test checks WEF1 inequalities and exchange equalities with exact rational arithmetic, and performs numerical linear programming to test convex-hull feasibility on a bounded collection of exact rational input weights. The linear-programming results are numerical corroboration and not exact certificates. The infinite conclusion comes from the detailed integer and graph argument in `RESULT.md`, not from finite test coverage.

The proof applies to every integer \(n\ge2\), \(m\ge1\) and strictly positive normalized entitlement vector under identical unit costs. It does not establish claims for non-identical chores, and no independent scientific audit has been performed.
