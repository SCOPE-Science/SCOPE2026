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

# Reproduction and limits

Run `python3 verification/checker.py` (Python 3.10+ and only the standard library). It checks all canonical orbit characteristic formulas for sizes one through eight by evaluating actual regular program relations, including composition, star, tests and loops. It also enumerates all labelled partial functions of each size one through five, with all possible roots. The expected type numbers are \(2,5,9,14,20\), and the success sentinel is `ALL_CHECKS_OK`. The five-world exhaustive sweep contains \(38{,}880\) pointed cases. The full all-size claim is proved algebraically in `RESULT.md`, not extrapolated from code. Independent validation and historical priority certification have not been performed.
