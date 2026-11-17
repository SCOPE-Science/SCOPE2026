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

The analytic proof uses exact half-orbit graph formulas, beta integration, an explicit algebraic inverse, and a constant logarithmic Jacobian. A standalone, standard-library checker tests the beta recurrence, 1000 random forward/inverse compositions and 1000 random inverse/forward compositions. On the recorded execution it printed `PIECEWISE_CENTER_FOUR_MEASUREMENT_INVERSE_OK`. Separate symbolic matrix inversion verified determinant `-2/9` and inverse row absolute sums `(6,4,3,1)`; numerical quadrature of an asymmetric parameter example agreed with both area-to-time identities. Finite checks are supporting evidence, not exhaustive proof of universal statements.

The theorem assumes positive parameters, exact model normalization, an identified transverse closed orbit and physical-time durations. External independent validation has not been performed.
