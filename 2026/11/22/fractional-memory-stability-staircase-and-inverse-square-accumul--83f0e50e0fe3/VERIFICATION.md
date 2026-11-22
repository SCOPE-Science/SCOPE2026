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

The analytic argument reduces the stationary equations to all inverse-sine branches, computes each Jacobian trace and determinant, applies the fractional Caputo-delta spectral boundary, and obtains the exact integer count with strict inequality at equality cases. The independent standalone script `checker.py` checks direct substitutions, Jacobian identities, sample spectral boundaries and stable-branch counts (including a fractional-only stability example), and the inverse-square threshold scaling.

The scalar generating function was independently derived from the discrete Volterra weights. Published general spectral stability criteria are attributed in the references. Finite tests supplement but do not replace the quantified proof for all orders, positive parameter values and integer branches. There is no nonlinear attraction or full nonlinear basin theorem, and no independent mathematical audit has been conducted.
