---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification record

The proof establishes positivity by weight monotonicity, computes the trace by telescoping, and obtains the sharp singular-value coefficient from the exact first difference of a rational weight formula and a counting argument. No finite experiment is used to prove the ideal threshold.

The accompanying `checker.py` uses Python standard-library arithmetic to check examples of the squared weights, positive commutator entries, exact partial traces and large-index coefficients. Its beta-product moment tests concern background only. To replay the supplementary finite cases, use `python3 checker.py` in the result directory.
