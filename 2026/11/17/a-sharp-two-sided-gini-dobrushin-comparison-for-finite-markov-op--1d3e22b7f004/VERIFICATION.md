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
# Verification and scope

Run `python3 check_gini_dobrushin.py` using Python 3's standard library from a directory containing the script. It uses exact rational arithmetic; it does not need scientific software or external files.

The checker calculates Gini-induced norms from **every** nonempty proper binary cut for each checked dimension, rather than sampling vectors. It verifies both strictly positive bistochastic sharpness families for \(2\le n\le11\), both symmetric four-state examples, and sharp Gini/oscillation bounds on cuts. The all-\(n\) claims follow from the inequalities and explicit parametric witnesses in RESULT.md. The finite checker is a consistency and reproducibility check, not a substitute for the universal proof or an independent audit.

Expected terminal lines include:

```
EXACT_GINI_OSCILLATION_EXTREME_CUTS_PASSED 36
EXACT_POSITIVE_BISTOCHASTIC_TWO_SIDED_SHARPNESS_PASSED 20
EXACT_SYMMETRIC_POSITIVE_SEMIDEFINITE_EXAMPLES_PASSED 2
ALL_GINI_DOBRUSHIN_COMPARISON_CHECKS_PASSED
```
