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

The continuous result follows from explicit stable matrix Lyapunov dynamics, conditional Gaussianity, the exactly integrated square-wave phase response, Wick identities and a positive derivative of \(F(z)=1-\tanh(z)/z\). The finite checker is not a substitute for any of these steps.

Run `python checker.py` with NumPy and SciPy installed. It independently constructs the periodic covariance as a fixed point of full matrix propagators for the two temperature regimes, uses Gaussian quadrature of conditional moments to compute mixed fourth-order observables, checks the complete-lag covariance identity at a positive lag, and verifies both sides of a critical-period example. A fresh execution passed 639 deterministic assertions.

The model is infinite-duration stationary, not a finite-time transient. The only limiting operations in the proof are the small- and large-period limits of a continuous strictly increasing explicit function. Publication-priority comparisons do not constitute independent scientific validation.
