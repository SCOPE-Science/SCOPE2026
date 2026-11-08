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

# Exact finite checks and limits

Run `python3 verify.py` with Python 3.11 or later. It uses only the Python standard library, and implements finite exact-integer bitset sumsets, semigroup-membership dynamic programming, and a separate set-based sumset enumerator. Observed successful output:

```
TWO_GAP_ALL_H_FORMULA_OK 12632
STABLE_HOLE_SET_OK 882
SHARP_THRESHOLD_PREDECESSORS_OK 294
GENUS_EXACT_SEMIGROUP_OK 294
INDEPENDENT_SET_SUM_CROSSCHECK_OK 1568
VERIFY_OK cases 294 a_min 4 a_max 150 d_values [2, 3] infinite_proof_separate True independent_audit False
```

The parameter range in the main tests is 4 through 150. This is a finite consistency check, not a proof of universal quantifiers. The symbolic proof in RESULT.md independently establishes the infinite claim. No independent mathematical audit or certification was performed.
