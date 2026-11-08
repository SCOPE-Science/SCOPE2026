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

# Verification and replay

Run `python verify_moment_controls.py` in an environment with the dependencies in `requirements.txt` (NumPy and SymPy). The independently constructed test suite used deterministic seed `20260806` and completed as follows:

- Six exact SymPy moment-order checks for the two-state upper-sharpness example, including the limiting elasticity.
- 864 network/group/moment logarithmic derivative comparisons against independent centered finite differences.
- 864 positive finite-change tests at independent control multipliers.
- 576 state-clock coefficient-distribution, covariance-Hessian, moment-reconstruction and null-vector tests.
- 144 reproducible independently generated 2–5 transient-state networks, each having a direct absorbing edge from every transient state.

The finite tests provide evidence of correct implementation, not a proof over arbitrary networks or moment orders. The complete analytic argument uses the positive-affine inverse lemma, finite positive moment expansion, global time-rescaling and exponential-sum covariance identity. There is no independent validation or external audit.
