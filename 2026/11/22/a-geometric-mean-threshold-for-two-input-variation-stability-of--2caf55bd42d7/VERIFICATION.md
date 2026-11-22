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

# Reproducible checks and their limits

Execute `python3 check_weighted_local_isotonic.py` with Python 3 and no external dependencies. The checker recomputes all local fits with exact rational arithmetic, compares 5,000 two-input variation inequalities for positive rational weights and sample lengths 8, 9, 11, and 14, and confirms exact equality for 30 constructed finite pairs across lengths 8, 9, 10, 13, and 20. The four local PAV branch formulas are tested separately.

Observed output:

```text
EXACT_PAV_BRANCH_CHECKS_PASS 4
EXACT_TWO_INPUT_VARIATION_INEQUALITIES_PASS 5000
EXACT_FINITE_PAIR_SHARPNESS_PASS 30
ALL_WEIGHTED_LOCAL_ISOTONIC_CHECKS_PASS
```

These are finite computational corroborations, not exhaustive analysis of all real inputs or all positive weight triples. The universal conclusion is proved in `RESULT.md` through the exact branch derivatives, a sharp induced difference-seminorm bound, and disjoint-support finite witnesses. No external proof certification or independent audit was performed.
