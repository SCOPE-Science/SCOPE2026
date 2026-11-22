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

`python3 verify.py` returned:

```text
VERIFY_OK even n=4..100, independent exact BFS n=4..16
```

The checker constructs the displayed all-parameter witness, checks each predicted alternating parity image set and its final rank, checks the forbidden triple and exact command length, and separately searches every image-subset/rotation-run state for shorter reset words in the stated finite range. Its finite tests are not a proof beyond the tested sizes. The symbolic lower bound and image-set induction in `RESULT.md` establish the infinite even-state theorem. External independent audit has not been conducted.
