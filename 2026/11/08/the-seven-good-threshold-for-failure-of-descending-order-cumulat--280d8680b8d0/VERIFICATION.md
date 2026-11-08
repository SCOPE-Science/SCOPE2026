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

# Exact certificate replay

Run `python3 certificates/verify_duals.py` from this directory. The verifier uses only Python standard-library exact rational arithmetic, reconstructing all 1,364 dual identities for the universal at-most-six-goods theorem and enumerating all 64 seven-good sign allocations. It checks sign-code coverage and nonnegative rational multipliers, including boundary cases. No numerical optimizer is used in this verification. A successful check prints two PASS lines.

The linear-programming reduction in RESULT.md supplies the mathematical link from these finite dual identities to all real nonincreasing input weights. The verifier checks the finite identities and example, not the literature priority question or any larger population/general-arrival conjecture. The work has not received independent external audit.
