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

# Reproducibility and limits

The package includes `checker.py`, a standalone Python 3 program requiring only the standard library. Run `python checker.py`. It checks the rank partition of all alternating coefficient matrices, direct sparse polynomial derivative identities over characteristics two, three and five and prime-power fields of sizes 2,3,4,5,8,9, and exact parameter wall inequalities in dimensions 5 through 8. It also verifies the degree-three and degree-four five-variable census examples.

The complete proof of the universally quantified result is in `RESULT.md`; finite checks are evidence of arithmetic consistency, not a substitute for that proof. The exact defining Jacobian ideal, smoothness of the exceptional divisor, adjunction discrepancy and Fedder obstruction are individually explained there. All code and numbers are ordinary scientific reproducibility material.

Independent mathematical audit: not performed.
