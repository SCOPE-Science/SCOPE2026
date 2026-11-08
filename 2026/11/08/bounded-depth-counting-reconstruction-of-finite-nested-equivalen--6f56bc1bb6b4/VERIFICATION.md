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

# Reproduction

Run `python3 verify.py` using only Python's standard library. The deterministic seed is `17291`. Expected output:

```
DEPTH_WITNESS_OK 16 2
VERIFY_OK nested_partitions 5400 repeated_signatures 1826 levels_1_to_4 sizes_1_to_10
```

The script independently constructs colored nested-equivalence structures, computes hierarchy isomorphism types as nested multisets, computes joint counting-refinement colors through their number of levels, checks equality of colors with orbit-path classes on every instance, and checks that equal final histograms have equal canonical hierarchy type. The separate two-level witness has identical round-one histograms but different round-two histograms, and distinct canonical types.

These are bounded computational tests, not an exhaustive census and not an infinite proof. The mathematical induction in RESULT.md supplies the unbounded correctness argument. No independent review or external certification has been performed.
