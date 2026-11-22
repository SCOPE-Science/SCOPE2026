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
# Reproduction and verification

The theorem concerns exact real-arithmetic Runge–Kutta coefficients. The proof in RESULT.md covers all admissible stage weights, all nonnegative algebraic-stability parameters, the full damping range \(0\le\rho<1\), and the uniqueness assertion. Numerical sampling is only supplementary and does not establish any all-parameter assertion.

From this directory, run `python verify.py` with an ordinary Python 3 interpreter; no third-party packages or external data are required. The standard-library script checks: (i) the order-one, order-two and both order-three identities, (ii) the positive-semidefinite matrix's explicit rank-one form, (iii) trace, determinant and rational stability function against direct linear solves, (iv) the closed-form boundary branch and interior sample inequalities, and (v) the full-damping Radau IIA endpoint. It passed 27,683 checks in the packaged execution.

The unique interior zero of the derivative is proved analytically by monotonicity. Finite rational grid checks and floating-point root approximations cannot certify uniqueness or exclude off-grid counterexamples; those facts follow instead from the explicit exhaustive family and strictly monotone derivative in RESULT.md. The computation does not validate any claim about wider classes of integrators. Independent audit is not performed.
