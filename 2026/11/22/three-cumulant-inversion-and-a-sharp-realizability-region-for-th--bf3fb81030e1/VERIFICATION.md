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

## Reproduction

Use Python 3 with SymPy and run `python check_exact.py` from this directory. The code reconstructs the stationary equations for the coupled position and two-state heading process, forms the second, fourth and sixth cumulants, cancels all common parameters in their ratio, checks the analytical monotonicity and endpoint range, and exactly inverts one rational example.

## Scope of checked assertions

The exact recurrence identities and algebraic manipulations are checked symbolically, including cancellation of the independent thermal Gaussian contribution above second order. The stationary distribution is derived in the accompanying proof by exponential pullback and beta integration. Strict uniqueness, sufficiency, and two-cumulant nonidentifiability are established by inequalities and continuity in the proof; no finite sampling or computational experiment is asserted to prove these global facts.

A full independent mathematical audit, statistical finite-sample sensitivity analysis, and a proof of novelty across all unindexed literature have not been performed.
