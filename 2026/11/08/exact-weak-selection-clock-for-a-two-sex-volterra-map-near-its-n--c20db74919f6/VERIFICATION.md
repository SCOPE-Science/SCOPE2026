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

Run `python verify.py` from the directory containing this document. The program uses SymPy and SciPy and checks the following identities exactly: the conserved-coordinate drift, neutral equilibrium curve, derivative of the explicit clock, and the uniform-contraction derivative formula. It then checks representative positive and negative determinant perturbations at three scales, comparing against the inverse-function clock; these are finite numerical corroborations only.

Expected final successful marker:

`VERIFY_OK exact_slow_primitive=1 exact_balance_identity=1 exact_transverse_derivative=1 finite_slow_clocks=4 three_scale_convergence_checks=12`

Proof obligations independent of finite sampling, including the all-parameter uniform error estimate, are discharged analytically in `RESULT.md`. The numerical checker does not certify mathematical originality or long-time behavior beyond the stated theorem. No external audit was performed.
