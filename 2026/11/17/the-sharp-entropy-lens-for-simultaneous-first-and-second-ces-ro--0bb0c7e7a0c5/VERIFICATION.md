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

The supplied standard-library Python file `check_cesaro_joint_region.py` can be executed from the same directory with:

```
python check_cesaro_joint_region.py
```

Actual execution results:

```
EXACT_ALL_BINARY_WORDS_N1_TO_N15_PASSED 65534
CONTIGUOUS_BLOCK_AND_PREFIX_ESTIMATES_PASSED
ENTROPY_WIDTH_IDENTITY_PASSED
```

The first test enumerates every binary word of lengths 1 through 15 and compares the exact rational twice-Cesàro weight with the exact harmonic extremizers. The second tests prefix-erasure and scaled-interval approximations for selected sizes, and the third checks the entropy width at its maximizer. These finite tests do not establish statements for all dimensions or the Baire-category claim; the explicit analytical proof provides those. No independent audit has been performed.
