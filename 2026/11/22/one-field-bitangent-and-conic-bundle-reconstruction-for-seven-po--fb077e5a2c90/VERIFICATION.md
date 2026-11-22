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

## Exact finite checks

`checker.py` directly enumerates all 56 exceptional classes and the 28 associated bitangent indices, and finds 126 candidate conic-bundle divisor classes by the two numerical equalities with multiplicities at most two. It checks all intersections against the 56 exceptional classes are nonnegative and compares direct Frobenius-fixed class counts with closed formulas for all 15 cycle types and for their first 21 powers. All 15 joint pairs are distinct. The independently generated `classification.csv` is the same 15-row table used in the proof.

Run:

```sh
python3 checker.py classification.csv
```

Expected leading output:

`CHECKED_56_EXCEPTIONAL_126_CONIC_CLASSES_28_BITANGENTS_15_UNIQUE_PAIRS_B10_C11`

The code validates a finite classification; it does not, without the mathematical arguments and primary geometry references in RESULT.md, independently establish every geometric correspondence or field-of-definition descent.
