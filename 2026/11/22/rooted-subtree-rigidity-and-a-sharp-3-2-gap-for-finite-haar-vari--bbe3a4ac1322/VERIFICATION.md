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

Run `python check_haar_tree_variation.py` under Python 3. The checker constructs every finite Haar rank-one projector through depth four with a common integer denominator, enumerates all coefficient masks using Gray code, and compares the exact variation seminorm with ancestor closure. It also checks the root-child \(3/2\) witness through depth nine.

Observed exact results:

```text
EXACT_MASK_EXHAUSTION_PASS depth=1 masks=2 rooted=2 nonrooted_min=None
EXACT_MASK_EXHAUSTION_PASS depth=2 masks=8 rooted=5 nonrooted_min=6/4
EXACT_MASK_EXHAUSTION_PASS depth=3 masks=128 rooted=26 nonrooted_min=12/8
EXACT_MASK_EXHAUSTION_PASS depth=4 masks=32768 rooted=677 nonrooted_min=24/16
EXACT_ISOLATED_CHILD_GAP_SHARPNESS_PASS depths_2_to_9
ALL_HAAR_TREE_VARIATION_CHECKS_PASS
```

The mathematical proof uses a dyadic block-average representation and an exact three-edge local argument for the missing-parent case, so no result for untested depths depends on finite enumeration. The source-comparison and same-model correctness checks are not independent peer review. No non-Haar or higher-dimensional case is certified.
