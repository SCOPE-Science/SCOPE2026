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

Run `python verify.py` with Python 3 and no third-party packages. The checker separately constructs the labelled graph, tests every initial subset for induced connectedness, and runs ordinary simultaneous zero-forcing closure to convergence. This is compared coefficient by coefficient with the interval-and-gap formula.

The run returned:

```text
VERIFY_OK exhaustive_leaf_patterns=120 n=3..6 labelled_placement_comparisons=120
DEGREE_SEQUENCE_CONTRAST_PASS n=7 three_leaves min_sizes=3_and_5
KNOWN_SUNLET_SPECIALIZATION_PASS n=3..14
```

All 120 possible leaf-placement patterns for cycle orders three through six are checked; the two explicit seven-cycle contrasts are separately brute-forced. Checks of the full-sunlet minimum coefficient and total count up to cycle order fourteen are finite consistency checks. An unrestricted theorem follows from the step-by-step two-front structural proof in RESULT.md, not from these finite tests. No external or independent review has been performed.
