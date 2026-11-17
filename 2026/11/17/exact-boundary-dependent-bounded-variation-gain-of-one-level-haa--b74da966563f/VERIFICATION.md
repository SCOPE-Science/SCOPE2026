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

The exact-rational `verify.py` checks all one-jump cases for 72 even-length/block-count pairs, detects the attaining witness in each, checks 350 arbitrary rational inputs and confirms involutivity. Command: `python verify.py`. Its passing run prints:

```text
EXACT_ALL_STEPS_AND_SHARP_WITNESSES_PASS 3204 72
EXACT_GENERAL_INPUT_AND_INVOLUTION_CHECKS_PASS 350
ALL_BLOCK_HAAR_VARIATION_CHECKS_PASS
```

The all-parameter assertion is proved analytically by step decomposition and local jump counting; finite testing does not certify infinite families.
