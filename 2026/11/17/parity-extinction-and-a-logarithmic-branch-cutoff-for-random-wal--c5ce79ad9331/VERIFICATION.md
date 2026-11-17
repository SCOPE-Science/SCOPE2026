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

# Mathematical verification

The exact proof consists of (i) the tree-cut decomposition reducing edge variation norm to one-edge cut inputs, (ii) the three-coordinate recurrence for the two double-star edge orbits, (iii) the exact bridge and leaf solutions, and (iv) a direct logarithmic cutoff argument. The code `check.py` uses Python's `fractions.Fraction` to compute all selected finite checks with no numerical tolerance and no external libraries. Run `python check.py` from the extracted package directory.

Observed successful output:

```
EXACT_ALL_CUT_NORMS_AND_CLOSED_FORM_PASSED 910
EXACT_SIGNED_INPUT_STABILITY_PASSED 12320
EXACT_ODD_POWER_THRESHOLD_TESTS_PASSED 3162
ALL_BALANCED_DOUBLE_STAR_VARIATION_TESTS_PASSED
```

The 910 exact cut enumerations cover 14 branch counts and 65 powers, all tree-edge cut orbits, and equality of the maximum with the claimed formula. The 12,320 signed-input checks vary each branch count and input, but do not exhaust real inputs. Every dimension and every power is covered by the analytical argument, not by extrapolation from these finite tests. Neither priority nor independent certification is asserted.
