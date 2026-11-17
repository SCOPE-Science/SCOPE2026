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

The standalone `verify_split_gini.py` was executed with Python 3 using exact rational arithmetic, without external dependencies. It builds the actual row-stochastic transition matrix, checks the complete-pair Gini inequality and additional classwise losses on every nonempty proper subset for the stated test dimensions, checks equality rigidity, and repeats the operation for powers. It also checks the exact two-class eigenmode and a sample of arbitrary signed rational vectors.

Recorded execution output:

```text
EXACT_FULL_SUBSET_CLASSWISE_GINI_AND_RIGIDITY_PASSED 7618
EXACT_ALL_POWERS_EIGENMODE_ATTAINMENT_PASSED 1183
EXACT_GENERAL_RATIONAL_INPUT_CLASSWISE_DISSIPATION_PASSED 12100
ALL_SPLIT_GRAPH_GINI_CHECKS_PASSED
```

The proof of the unrestricted statement is in RESULT.md and does not extrapolate from the finite runs. No computer algebra result or external proof certificate is needed. Independent audit remains unperformed.
