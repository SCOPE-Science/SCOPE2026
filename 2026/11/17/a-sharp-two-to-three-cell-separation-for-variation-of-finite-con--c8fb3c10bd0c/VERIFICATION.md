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

The exact rational standalone script `check.py` can be executed with ordinary Python 3 and no third-party packages, using `python check.py`. It constructs every path-step output explicitly, calculates the adjacent-variation ratio, and cross-checks the independent two-cell transition/prefix formula for 4083 anchored binary words. It evaluates the four three-class construction families at every size from 3 to 120, confirms the binary alternating-tail bound at every size from 4 to 300, enumerates all set partitions up to seven positions, and independently verifies exact two-class maxima at lengths three through seven. The observed successful diagnostics are:

```
EXACT_BINARY_PATH_PREFIX_IDENTITY_PASS 4083
THREE_CELL_CONSTRUCTIONS_EXACT_PASS 118
BINARY_ASYMPTOTIC_CONSTRUCTION_AND_BOUND_PASS 297
EXACT_ALL_PARTITIONS_SMALL_N_PASS [(2, '1'), (3, '1'), (4, '2'), (5, '5/2'), (6, '3'), (7, '10/3')]
ALL_PARTITION_VARIATION_CHECKS_PASS
EXACT_BINARY_ONSET_N3_TO_N7_PASS
```

The finite tests do not prove the asymptotic formulas. Their proof is contained in `RESULT.md`: exact step decomposition, misplaced-site transition bound, one-variable maximum, explicit rounded binary witnesses, four-residue ternary witnesses, finite onset and the all-length comparison inequality. The exact global three-class envelope, weighted extensions and historical uniqueness are unproved.
