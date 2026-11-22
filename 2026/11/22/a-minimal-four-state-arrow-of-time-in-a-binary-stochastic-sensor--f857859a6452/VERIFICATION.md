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

Run `python checker.py` with Python 3, SymPy, NumPy and SciPy. Actual execution completed successfully: exact symbolic cancellation of the first three coefficients of the antisymmetric four-word probability, exact general cubic factorization, 20 independent numerical four-rate cases with small-lag convergence, 15 finite-lag reversibility checks on the two equality surfaces, and a positive backward-rate example at 0.025.

The mathematical proof of infinite-state-space quantifiers is not claimed (the model is finite-state); the all-positive-parameter and all-positive-time reversibility statements use the explicit regenerative/phase arguments in RESULT.md, not finite tests. The generic four-state generator outside the directed ring is not classified. No estimation accuracy or finite-sample power guarantee is asserted. Independent validation has not been conducted.
