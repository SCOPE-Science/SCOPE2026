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

The proof reduces exact generator equations, not experimental measurements. An independent degree-two polynomial-generator construction with rational arithmetic was run as `python kmp_silent_checks.py` and returned:

`PASS: 12 exact independent generator systems, 144 exact moment equations; all moments and covariances agree.`

Parameters checked: system sizes 2, 3, 4, 5; internal rates 0, 1/3, 2; reservoir means 3 and 1. The checker constructs and inverts all first/second-degree stationary equations and tests every site and site pair. These tests do not establish the all-size theorem independently; the all-size proof is given in RESULT.md. No independent scientific audit has been performed.
