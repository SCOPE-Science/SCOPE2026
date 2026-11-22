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

# Verification scope

The complete analytic argument is in `RESULT.md` and the independent executable diagnostics are in `check.py`. Execute `python3 check.py` using the standard Python library. The checker establishes algebraic identities for rational test parameters, verifies exact antiderivative formulas to floating-point tolerance, the period recurrence, and sample signs; it is not a universal quantified certificate. The proof of nonnegativity for every positive time is the trigonometric sign-and-period argument in `RESULT.md`. The source searches and historic comparison are recorded in `AUDIT.json`.
