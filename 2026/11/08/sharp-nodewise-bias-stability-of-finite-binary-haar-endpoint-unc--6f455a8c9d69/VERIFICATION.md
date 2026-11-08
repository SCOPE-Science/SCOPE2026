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

# Reproducible checks and boundaries

Run `python3 verify_tree_haar.py` using Python 3's standard library only. The program builds normalized Haar kernel products directly (all global sign assignments) and independently computes ancestral-path row scores using exact rational arithmetic. It also verifies the two-scalar product recurrence, the single-defect coefficient, and the four-leaf majority-first example.

Actual program output:

```text
EXACT_FULL_HAAR_MATRIX_ROW_COMPARISONS_PASSED 39
EXACT_PRODUCT_ENVELOPE_EQUALITY_CHECKS_PASSED 240
EXACT_SINGLE_NODE_BIAS_STABILITY_COEFFICIENTS_PASSED 135
EXACT_FULL_MATRIX_SINGLE_BIAS_CASES_PASSED 11
MAJORITY_FIRST_BRANCH_COUNTEREXAMPLE_PASSED {(0, 0): Fraction(5, 2), (0, 1): Fraction(5, 2), (1, 0): Fraction(27, 10), (1, 1): Fraction(11, 10)}
ALL_NONHOMOGENEOUS_TREE_HAAR_CHECKS_PASSED
```

These exact finite tests do not exhaust all positive real probabilities or depths. The universal conclusion follows from the explicit kernel-row identity, the one-Lipschitz suffix estimate, the backward Bellman induction, and the earliest-biased-generation argument in `RESULT.md`. Independent audit has not been performed.
