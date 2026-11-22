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

# Computational checks and limitations

Run with standard Python 3 from the root of the unpacked file set:

```sh
python3 checks/verify_bruteforce.py
python3 checks/verify_gap.py
```

`verify_bruteforce.py` independently constructs every binary palindrome of fixed weight eight through length 24, directly tests every prefix and equally long factor, and compares against the rational-series coefficients. All seventeen length cases passed, with sequence `1,1,2,3,5,5,8,10,13,15,20,23,28,32,39,44,52`.

`verify_gap.py` independently checks all seven gap-window comparisons against the four-condition criterion on all 4,096 gap tuples with entries 0 through 7. It also compares all 113 generating-function coefficients from lengths 8 through 120 with a separate nonnegative-integer solution enumeration. Both tests passed.

The formal-power-series identity and its all-length applicability are proved symbolically in `RESULT.md`; finite tests do not prove infinitely many cases. This verification is a self-review and does not constitute an independent audit or external mathematical certification.
