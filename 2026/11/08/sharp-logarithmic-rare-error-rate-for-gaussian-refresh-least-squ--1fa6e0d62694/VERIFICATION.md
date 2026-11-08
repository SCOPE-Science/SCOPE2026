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

The standalone `verify.py` is executed with Python 3 without external dependencies. It tests 3,006 deterministic and pseudorandom finite identities: Gaussian second-moment algebra, affine-SGD unrolling, the nonnegative conditional innovation variance, maxima at endpoints of constant-covariate blocks, and a discounted-additive moment envelope.

The limit is established by the five analytic proof steps in `RESULT.md`: stationary expansion; direct geometric-Gaussian tail bounds; a negative-mean stochastically dominating random walk with subexponential integrated tail; upper series control; and a matching conditional-Gaussian lower event. The use of Veraverbeke's theorem is sourced. Simulation is neither a certificate of subexponentiality nor an infinite-tail proof.

No outside independent audit, automated theorem prover or external scientific certification was performed. This document records the finite checks and mathematical limits of verification.
