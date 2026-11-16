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

# Verification record

The standalone source file `CHECK.py` was run with Python 3 and no external modules. The observed output was:

```
THREE_BALL_EXACT_MOMENT_CHECK_OK assertions=1133
```

The checker verifies the centered difference moments in exact rational arithmetic for 343 integer triples, and verifies the noncollinear sharpness witness along 49 integer projection directions. The analytical proof supplies the unrestricted real-variable statements: the identities hold for all centered triples by symmetric-polynomial identities, the sixth-order invariant is a square of one cubic, and factor uniqueness gives the global sign. These tests are supplementary and neither exhaustive over real inputs nor independent validation. No noisy reconstruction, unequal weights or radii, or stability estimate was verified. Independent audit has not been performed.
