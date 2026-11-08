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

# Reproducibility

Run `python3 checker.py` in the same directory. It uses Python 3 standard-library integer arithmetic and enumerates all candidate directed arc sets at the theoretical maximum for alphabet sizes 2 through 5. For each feasible digraph it directly checks all length-three words and compares all minimum covers with balanced two-class codebooks. The expected success terminator is `CHECKER_OK`; the observed results are:

```
q=2: optimum_size=2, distinct_minimum_codes=1, symmetry_types=1
q=3: optimum_size=5, distinct_minimum_codes=3, symmetry_types=1
q=4: optimum_size=8, distinct_minimum_codes=3, symmetry_types=1
q=5: optimum_size=13, distinct_minimum_codes=10, symmetry_types=1
CHECKER_OK
```

This is an exact enumeration at the proven candidate optimum layer for four small alphabet sizes, not an exhaustive computational proof for all alphabet sizes or a proof that no larger arc sets exist. For the universal claim consult the disjoint-neighborhood inequality, its equality conditions, Mantel's equality case, and the even-to-odd vertex-deletion argument in `RESULT.md`.
