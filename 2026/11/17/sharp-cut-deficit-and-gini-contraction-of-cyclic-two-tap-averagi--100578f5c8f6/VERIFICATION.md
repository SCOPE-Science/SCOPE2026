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

The independently executable exact-arithmetic file `verify_two_tap_gini.py` uses no optional third-party dependencies. From its containing directory, run `python verify_two_tap_gini.py`.

The checker verifies all nonconstant binary cuts at dimensions 2 through 12 for five rational mixing parameters; in each case it tests the exact \(r^2\) deficit and the balanced-arc sharp witness. It also verifies 58,500 rational nonbinary examples and Dobrushin disjoint-row witnesses. The analytical cut proof covers untested dimensions and all real weights, including irrational ones; the script is corroborative, not a finite surrogate for that proof.

Expected terminal markers:

```
EXACT_ALL_BINARY_CUT_DEFICITS_AND_SHARP_BISECTIONS_PASSED 40830
EXACT_NONBINARY_RATIONAL_SIGNAL_CHECKS_PASSED 58500
EXACT_DOBRUSHIN_SEPARATION_CHECKS_PASSED_N4_TO_N29
ALL_TWO_TAP_CYCLIC_GINI_CHECKS_PASSED
```
