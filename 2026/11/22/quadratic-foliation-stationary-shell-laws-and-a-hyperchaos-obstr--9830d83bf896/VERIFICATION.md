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

Reproduce the algebra with `python checker.py` and SymPy. The checker asserts symbolic identities for the global first integral, the unit-Jacobian polynomial coordinate, both stationary coboundary formulas, divergence \(-a\) and crossing saltation determinant one.

The stationary consequences use the analytical inequalities \(|x|-x^2\le1/4\) and Cauchy–Schwarz, not finite sampling. The Floquet conclusion additionally uses the standard autonomous flow direction and the derivative of the identity coordinate; it applies only to finite, transverse crossing itineraries. The Lyapunov extension requires an integrable variational cocycle and a tempered, nonvanishing flow direction. The checker does not certify global solution uniqueness, positivity of an attractor's basin, or missing nonsmooth cocycle hypotheses.

Scientific interpretation and literature comparisons are self-reviewed only; no independent mathematical audit is claimed.
