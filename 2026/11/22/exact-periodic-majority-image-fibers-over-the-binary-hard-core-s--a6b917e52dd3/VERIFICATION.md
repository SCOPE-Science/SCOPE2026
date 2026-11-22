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

# Reproducibility and verification

Run `python3 verify.py` from the extracted package using Python 3 with its standard library; no external data, packages, or network services are required. Expected final line:

`VERIFY_OK: all cyclic inputs, all outputs, and renewal counts through length 15`

This executes exhaustive enumeration of all \(2^n\) potential indexed inputs and outputs at each length \(1\le n\le15\), filters source words by cyclic avoidance of `11`, constructs actual majority outputs, and checks every fiber against the gap-product formula. A separate composition recurrence counts all admissible and singleton output profiles; the program also checks the exceptional zero-output fibers and the first eleven single-gap composition values.

Observed image counts through length fifteen: `1,3,1,3,6,9,15,19,28,38,56,81,118,171,246`.

Observed singleton-fiber counts through length fifteen: `1,3,0,2,5,8,14,10,18,17,33,44,65,86,110`.

These finite computations confirm the derived formulas on the checked lengths only. The infinite claims are supported by the constructive cyclic-gap bijection, the trace recurrence, and the formal cycle-marking generating-function identity in RESULT.md. No independent human validation has been performed.
