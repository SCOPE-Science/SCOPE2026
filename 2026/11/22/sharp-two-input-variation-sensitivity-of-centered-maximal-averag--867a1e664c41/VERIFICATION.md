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

Run `python3 checker.py` from the extracted package. The script uses only standard-library exact rational arithmetic for an exhaustive enumeration of the \(4\cdot3\cdot3\cdot4=144\) possible branch matrices and identifies the unique branch whose path-variation seminorm exceeds \(11/6\). It independently computes both maximal outputs for the explicit attaining signal pair and tests 10,000 additional seeded rational pairs.

Observed successful output:

```
ALL_144_MASKS_RATIONAL_EXHAUSTIVE_PASS step_maxima= ('3/2', '2', '3/2') unique_excluded= (3, 0, 0, 3)
EXPLICIT_NONNEGATIVE_ATTAINING_PAIR_PASS ('18', '26', '25', '24') ('37/2', '26', '26', '74/3')
RANDOM_10000_EXACT_RATIONAL_TWO_INPUT_TESTS_PASS
CENTERED_P4_BV_ALL_CHECKS_PASS
```

The exhaustive computation concerns only the finite branch family. Correctness for all real inputs requires the paper's separate argument showing that the sole larger-norm branch is impossible at nonconstant signals and that the piecewise-affine derivative bound integrates over line segments. The random tests are not exhaustive for input pairs. No independent mathematical audit or machine-checked formal proof is asserted.
