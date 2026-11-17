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

# Verification of weighted-tree centered-rectification variation sensitivity

Run `python verification/check.py` using Python 3 standard library. Its deterministic rational computations compare exact activation-column values with the proposed weighted cut formula, verify all actual test-pair inequalities, construct explicit attaining checkerboard data, and check the path/star consequences.

Observed successful output:

```text
EXACT_ALL_ACTIVATION_SETS_AND_WEIGHTED_TREE_CUTS_PASS 210 90600
EXACT_TWO_INPUT_RATIONAL_TESTS_PASS 2513
EXACT_ATTAINED_BIPARTITE_ACTIVATION_WITNESSES_PASS 180
ALL_PATH_AND_STAR_EXTREMA_PASS 28
ALL_CENTERED_RECTIFICATION_VARIATION_CHECKS_PASS
```

Sampling comprises 210 rooted random tree realizations of orders 2 through 8 with independent integer masses and weights, not an exhaustive enumeration of all labeled weighted trees. The proof in `RESULT.md` supplies the all-finite-tree quantifiers. The exceptional two-vertex case is tested explicitly. The observed calculations do not establish originality or an independent scientific audit.
