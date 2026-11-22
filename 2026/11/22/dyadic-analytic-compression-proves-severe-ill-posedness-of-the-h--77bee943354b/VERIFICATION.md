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

# Verification scope

The rank construction is proved symbolically using vector-valued holomorphy, the Bernstein ellipse of parameter two, the Cauchy bounds for Chebyshev coefficients, a Hilbert–Schmidt dyadic sum and the approximation-number characterization. The explicit constant is \(128/21+\sqrt{3/2}<8\).

The associated `verify.py` passed 163 finite diagnostic checks on finite weighted Hilbert matrices, interpolation residuals in Gauss quadrature and tail traces. Its finite interpolation tests use a different polynomial approximation from the analytic series truncation in the proof. Finite numerics are neither evidence that the infinite result follows nor a proof of optimality; the infinite claim follows from the stated analytic inequalities.

No independent audit has been performed. No sharp asymptotic lower bound is certified.
