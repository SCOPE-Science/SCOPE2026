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

The analytic proof gives all parameter and observation quantifiers. Running `python3 checker.py` (Python 3 standard library) verifies exact rational signatures for all \(2\le N\le150\), forced prime-power coordinates and selected regular-grid values, as well as finite-tolerance and Farey-gap instances. The checker printed `PASS: 11025 exact assertions`. Checks of finite cases are supplementary and cannot prove the unbounded theorem. Common finite detection tolerance is restricted to \(0\le\varepsilon<1/(2N^2)\); the exact grid restriction does not extend to positive tolerance. Independent audit has not been performed.
