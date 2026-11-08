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

# Verification and scope

The all-order proof uses exact additive-group algebra and has no floating-point or computational dependency. Run `python3 verify.py` in the same directory as the other files. The Python standard-library checker enumerates every characteristic-two functional-identity input pair for all common-displacement maps at field orders 4, 8, and 16; checks the distinct-rule count; and enumerates full states for representative small site lengths and supports, confirming involution and the exact fixed-state count.

Successful observed output:

```
equation_and_map_count 2 10
equation_and_map_count 3 106
equation_and_map_count 4 3826
VERIFY_OK exact_state_checks= 1686656
```

This program does not exhaust arbitrary extension degrees or site lengths, and cannot prove novelty. The universal proof is in RESULT.md. No independent scientific audit is represented or claimed here.
