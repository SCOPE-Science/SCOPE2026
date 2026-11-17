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

The analytical proof in RESULT.md applies in every finite dimension; this document reports supporting reproducibility checks only. Running `python3 checker.py` with Python 3.10+ and no third-party dependencies printed:

```
EXACT_ACTIVE_SUPPORT_CUT_COMPARISONS_PASSED 346476
EXACT_ATTAINED_SIMPLEX_PAIRS_PASSED 88
EXACT_TWO_INPUT_NONLINEAR_INEQUALITIES_PASSED 28574
ALL_COMPLETE_GRAPH_GINI_SIMPLEX_CHECKS_PASSED
```

Exact rational arithmetic is used throughout. The program directly computes the simplex projection by sorting and solving for a threshold, compares cut ratios for every active subset and proper cut in dimensions two through nine, and checks concrete attaining pairs for dimensions two through 89. The finite sample checks are not an exhaustive substitute for the universal layer-cake and cut-optimization arguments. No independent external validation has been performed.
