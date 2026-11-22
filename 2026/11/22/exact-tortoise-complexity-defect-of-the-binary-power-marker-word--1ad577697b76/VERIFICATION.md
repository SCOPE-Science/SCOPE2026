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

The universal proof is self-contained in `RESULT.md`. Verification scripts use ordinary Python 3 standard-library operations and may be run as:

```sh
python verify_direct.py
python verify_structural.py
```

Recorded outputs are supplied as `verify_direct.output.txt` and `verify_structural.output.txt`. The first independently constructs actual word windows and computes literal tortoise images, confirming all cases through length 160. The second generates admissible marker gaps and offsets without using the same window-enumeration algorithm, confirming all cases through length 320. Both programs also assert the relevant structural injectivity conditions, not just the displayed totals.

The infinite assertion is proved by disjointness of the dyadic first-image-one intervals and by exact summation of admissible offset ranges. Testing alone does not establish the theorem. Independent scientific auditing has not been performed.
