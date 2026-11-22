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

# Verification of the boundary-phase minimal-nonface theorem

The standalone Python 3 program `verify.py` uses a separate recursive perfect-matching search on the full grid after fixing each proposed edge. For each \(n\in\{2,3,\ldots,18,20,25,30,40\}\), it builds all sixteen prescribed matchings, confirms that exactly the eight equal-phase configurations extend, checks that the eight opposite-phase configurations do not extend, and verifies extension after removal of **every** selected domino in those eight configurations.

To replay: `python3 verify.py`, with the script in the same directory. No third-party dependencies or external data are needed. The observed output was:

```
PHASE_CLASSIFICATION_PASS 21 strip widths
EIGHT_DISTINCT_MINIMAL_BAD_MATCHINGS_EACH_WIDTH_PASS 168
EVERY_SINGLE_DELETION_EXTENDABLE_PASS
VERIFY_OK
```

The proof of the unbounded \(n\)-parameter result is a parity argument and an explicit construction of completion tilings after one-edge deletion, not extrapolation from these computations. This is a self-review only; independent audit and external certification have not been performed.
