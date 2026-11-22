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

# Verification notes

The analytic argument first proves entry into a fixed small critical neighborhood by positive scalar comparison, then uses the exact fast-coordinate relation to obtain a quadratic slaving jet. Its coefficients and invariance cancellation are checked as identities by `checker.py`. The reciprocal recurrence has a remainder summable through \(n\le TN\); its weighted harmonic sum gives the exact second-order term. The host-coordinate law follows from the same stable filter.

Run `python checker.py` with SymPy installed. The script has no external inputs; its exact tests are algebraic, and the finite trajectory tests only corroborate the predicted bounded residual. Formal theorem verification by an independent party has not been performed.
