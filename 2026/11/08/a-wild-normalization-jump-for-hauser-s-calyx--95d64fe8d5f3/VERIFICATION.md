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

The Python checker (`verify.py`) is standalone apart from `sympy`. It confirms the equations used for the odd-characteristic normalization and the characteristic-two specialization, the square-completion leading to the \(A_3\) equation, and conductor-generator multiplication identities. Its recorded output is in `verify_output.txt`. These checks do not prove Serre normality or a historical-priority claim; those appear as separate mathematical arguments and qualified literature comparisons.
