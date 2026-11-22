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
# Verification

Run `python verify.py` using Python 3 and SymPy. The program returns `VERIFY_OK 34581` on a passing run. It symbolically checks the softmax-covariance ratio identity, the derivative factor, and the derivative of the critical-point map; it also uses exact fractions for a broad range of positive ternary distributions and an explicit rational witness.

The analytic proof in `RESULT.md` is required for all-parameter correctness. In particular, strict positivity of the critical-point map derivative, uniqueness of the optimizer, the asymptotic \(1/(12p)\) constant and the sharp angular threshold follow by exact inequalities and continuity, not finite sampling. Numerical root tests only corroborate these conclusions.

Verification is for zero-probe local estimates only. No finite-test-point rule, trained model, stochastic minibatch, or downstream convergence guarantee was validated. Independent audit has not been performed.
