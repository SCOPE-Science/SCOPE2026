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

# Reproduction and boundaries

Run `python3 verify_complete_graph_maximal.py` with Python 3; no external packages or data files are required. The script was executed on the actual embedded source before delivery. Its outputs were:

```
EXACT_ACTIVE_CUT_TABLES_PASSED 50375
INDEPENDENT_EXPLICIT_ACTIVE_CUTS_PASSED 85372
EXACT_STRICT_BRANCH_WITNESSES_PASSED 299
EXACT_TWO_INPUT_RATIONAL_PAIRS_PASSED 3598
SIGNED_SEMINORM_OBSTRUCTION_CHECKS_PASSED 19
ALL_COMPLETE_GRAPH_TWO_INPUT_BV_CHECKS_PASSED
```

The proof applies to all finite graph orders and uses exact coarea and an elementary convexity argument. Neither finite tests nor rational samples certify a universal identity by themselves. The claimed maximal function on nonnegative data is the conventional centered graph-ball average; signed-input absolute values are excluded. Literature coverage was checked against the three cited primary preprints; a possible earlier equivalent result under a different functional-analytic vocabulary remains an originality risk.
