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

The package contains a standalone pure-Python exact rational Kirchhoff-cofactor checker. It computes the crown Laplacian independently for each graph order 3 through 7, compares the single- and pair-leaf probabilities with the closed expressions, and verifies the recurrence coefficients used in the positivity proof. Executed command: `python3 crown_leaf_check.py`. Actual result: `VERIFY_OK 51 exact assertions`. This tests finite cases only; the all-order proof is algebraic and analytic. No independent external audit was performed.
